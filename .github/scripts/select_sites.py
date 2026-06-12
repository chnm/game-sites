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

The hugo --source dir == key; the build job derives the release tag prefix
("<key>-<tier>-") and baseURL from the selected tier/FQDN.
"""
import json
import os

# key -> (prod_fqdn, dev_fqdn)
SITES = {
    "games-hub":        ("games.rrchnm.org",       "games.dev.chnm.gmu.edu"),
    "plague-site":      ("1665plague.rrchnm.org",   "1665plague.dev.chnm.gmu.edu"),
    "shipping-site":    ("1812shipping.rrchnm.org", "1812shipping.dev.chnm.gmu.edu"),
    "illuminated-site": ("illuminated.rrchnm.org",  "illuminated.dev.chnm.gmu.edu"),
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
    matrix = [
        {"key": key, "source": key, "prod_fqdn": prod, "devl_fqdn": dev}
        for key, (prod, dev) in SITES.items()
        if key in wanted
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
