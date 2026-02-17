#!/usr/bin/env bash
#
# Takes a tag and downloads the "dist" artifact from the latest GitHub action
# run for that tag.
#
set -euo pipefail

readonly ARTIFACT="dist"
readonly WORKFLOW="json-store"
readonly DEST=$ARTIFACT

if [[ -e "$DEST" ]]; then
    read -p "❓ Remove existing '$DEST' directory? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf "$DEST"
    fi
fi

tag="${1:-$(git describe --abbrev=0)}"
echo "📡 Downloading '$ARTIFACT' artifact for tag '$tag' → $DEST/"

run_id=$(gh run list -w "$WORKFLOW" -b "$tag" --json databaseId --jq '.[0].databaseId')
gh run download "$run_id" -n "$ARTIFACT" -D "$DEST"
