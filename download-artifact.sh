#!/usr/bin/env bash
#
# Takes a tag and downloads the "dist" artifact from the latest GitHub action
# run for that tag.
#
set -euo pipefail

readonly OWNER="brainsik"
readonly REPO="json-store"
readonly ARTIFACT_NAME="dist"
readonly API_URL="https://api.github.com"

pecho() {
    echo -e "➜ $1"
}

error() {
    echo -e "💥 $1" >&2
    exit 1
}

check_dependencies() {
    local missing=()
    for cmd in curl jq unzip; do
        if ! command -v "$cmd" &>/dev/null; then
            missing+=("$cmd")
        fi
    done

    if [[ ${#missing[@]} -gt 0 ]]; then
        echo "These packages need to be installed: ${missing[*]}"
        exit 1
    fi
}

gh_request() {
    local endpoint="$1"
    local url="${API_URL}${endpoint}"

    local response
    response=$(curl -s -w "\n%{http_code}" \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer ${GITHUB_TOKEN}" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        "$url")

    local body http_code
    body=$(echo "$response" | sed '$d')
    http_code=$(echo "$response" | tail -n1)

    if [[ $http_code -ne 200 ]]; then
        error "API request failed: $endpoint\n$body"
    fi
    echo "$body"
}

get_latest_runid() {
    local sha="$1"
    pecho "Finding workflow runs for commit $sha" >&2

    local response
    response=$(gh_request "/repos/${OWNER}/${REPO}/actions/runs?head_sha=${sha}&status=completed")

    local run_id
    run_id=$(echo "$response" | jq -r '.workflow_runs[0].id // empty')

    if [[ -z "$run_id" ]]; then
        error "Couldn't find action run ID in response:\n$response"
    fi
    echo "$run_id"
}

get_artifact_id() {
    local run_id="$1"
    pecho "Fetching artifacts for run #$run_id" >&2

    local response
    response=$(gh_request "/repos/${OWNER}/${REPO}/actions/runs/${run_id}/artifacts")

    local artifact_id
    artifact_id=$(echo "$response" | jq -r ".artifacts[] | select(.name == \"${ARTIFACT_NAME}\") | .id // empty")

    if [ -z "$artifact_id" ]; then
        error "Artifact '${ARTIFACT_NAME}' not found in run #$run_id:\n$response"
    fi
    echo "$artifact_id"
}

# Download artifact
download_artifact() {
    local artifact_id="$1"
    local output_file="$2"

    pecho "Downloading artifact #$artifact_id" >&2

    local url="${API_URL}/repos/${OWNER}/${REPO}/actions/artifacts/${artifact_id}/zip"

    local http_code
    http_code=$(curl -L -s -w "%{http_code}" -o "$output_file" \
        -H "Accept: application/vnd.github+json" \
        -H "Authorization: Bearer ${GITHUB_TOKEN}" \
        -H "X-GitHub-Api-Version: 2022-11-28" \
        "$url")

    if [[ "$http_code" != "200" ]]; then
        local output_file_contents
        output_file_contents=$(cat $output_file)

        rm -f $output_file
        error "Download failed with status $http_code:\n$output_file_contents"
    fi

    if [[ ! -f "$output_file" ]] || [[ ! -s "$output_file" ]]; then
        error "Downloaded file — $output_file — is missing or empty"
    fi
}

extract_artifact() {
    local zip_file="$1"
    local output_dir="$2"

}

# ----

tag="${1:-}"
if [[ -z "$tag" ]]; then
    echo "Usage: $0 <tag>"
    exit 1
fi

if [[ -z "${GITHUB_TOKEN:-}" ]]; then
    echo "GITHUB_TOKEN environment variable is not set." >&2
    exit 1
fi

check_dependencies

zip_file="dist-${tag}.zip"
cleanup() {
    rm -f "$zip_file"
}
trap cleanup EXIT

# Download the artifact
sha=$(git show-ref --dereference "$tag" | tail -n1 | cut -f1 -d ' ')
run_id=$(get_latest_runid "$sha")
artifact_id=$(get_artifact_id "$run_id")
download_artifact "$artifact_id" "$zip_file"

# Unzip
output_dir="dist"
pecho "Extracting to $output_dir/" >&2
if ! unzip -q -o "$zip_file" -d "$output_dir"; then
    error "Extraction failed"
fi

echo "🎉"
