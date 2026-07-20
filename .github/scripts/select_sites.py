#!/usr/bin/env python3
"""Decide which game-sites to build/release/deploy for this run.

Single source of truth for the per-site catalog. Reads the trigger context
from the environment and writes a GitHub Actions job matrix to $GITHUB_OUTPUT:

    matrix  JSON array of {key, source, prod_fqdn, devl_fqdn}, one per site to build
    any     "true" if the matrix is non-empty, else "false"

Selection rules:
    workflow_dispatch  -> the `sites` input (comma-separated keys, or "all")
    push, themes/**    -> every site (shared theme affects all)
    push, otherwise    -> only the sites whose own dir changed

On the prod tier (push to main, detected via REF), any selected site whose
catalog entry has prod_ready=False is dropped before the matrix is emitted, so
a site can keep shipping to *.dev.chnm.gmu.edu while it's still being readied
for production. Dev/preview builds are never filtered. This holds even for a
themes/** change or a workflow_dispatch sites=all run -- prod_ready is the one
switch that lets a site reach production.

The hugo --source dir == key; the build job derives the release tag prefix
("<key>-<tier>-") and baseURL from the selected tier/FQDN.
"""
import json
import os

# Per-site catalog. prod_ready gates the prod tier only: set it False to keep a
# site on dev until it's cleared for production (see Selection rules above).
SITES = {
    "games-hub": {
        "prod_fqdn":  "games.rrchnm.org",
        "devl_fqdn":  "games.dev.chnm.gmu.edu",
        "prod_ready": True,
    },
    "plague-site": {
        "prod_fqdn":  "1665plague.rrchnm.org",
        "devl_fqdn":  "1665plague.dev.chnm.gmu.edu",
        "prod_ready": True,
    },
    "shipping-site": {
        "prod_fqdn":  "1812shipping.rrchnm.org",
        "devl_fqdn":  "1812shipping.dev.chnm.gmu.edu",
        "prod_ready": True,
    },
    "illuminated-site": {
        "prod_fqdn":  "illuminated.rrchnm.org",
        "devl_fqdn":  "illuminated.dev.chnm.gmu.edu",
        "prod_ready": False,
    },
}


def selected_keys():
    if os.environ.get("EVENT_NAME") == "workflow_dispatch":
        want = os.environ.get("DISPATCH_SITES", "all").strip()
        if want and want != "all":
            return [s.strip() for s in want.split(",") if s.strip()]
        return list(SITES)

    # dorny/paths-filter `changes` output: JSON array of filter names that matched.
    changed = json.loads(os.environ.get("CHANGED", "[]"))
    if "themes" in changed:
        return list(SITES)
    return [k for k in SITES if k in changed]


def main():
    wanted = set(selected_keys())
    # Tier is branch-based, mirroring the build-release / deploy jobs: main -> prod.
    is_prod = os.environ.get("REF") == "refs/heads/main"
    matrix = [
        {
            "key": key,
            "source": key,
            "prod_fqdn": cfg["prod_fqdn"],
            "devl_fqdn": cfg["devl_fqdn"],
        }
        for key, cfg in SITES.items()
        if key in wanted and (cfg["prod_ready"] or not is_prod)
    ]

    # $GITHUB_OUTPUT is the current (post-`::set-output::`) env-file API and is
    # not deprecated. The plain `key=value` form only works for SINGLE-LINE
    # values — a newline would corrupt the file and need the `key<<EOF`/`EOF`
    # heredoc form instead. Safe here: json.dumps() (no indent) keeps the array
    # on one line, and `any` is just true/false.
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"matrix={json.dumps(matrix)}\n")
            f.write(f"any={'true' if matrix else 'false'}\n")

    print(json.dumps(matrix, indent=2))


if __name__ == "__main__":
    main()
