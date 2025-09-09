#!/usr/bin/env bash
set -euo pipefail

# -------- Config to avoid /mnt/c issues ----------
export BUNDLE_PATH="${HOME}/bundle"
export TMPDIR="/tmp"
BUILD_DIR="${JEKYLL_DEST:-${HOME}/jekyll_build}"
mkdir -p "${BUILD_DIR}"

# Write .bundle/config so future runs stick to Linux home
bundle config set --local path "${BUNDLE_PATH}" >/dev/null

# -------- Feature flags (optional) ---------------
# export FORCE_HAWKINS=1     # force hawkins even if buggy combo detected
# export DISABLE_HAWKINS=1  # never use hawkins

# -------- Detect gems/versions under bundler ----
have_hawkins=$(
  set +e
  bundle exec ruby -e 'begin; gem "hawkins"; require "hawkins"; puts "yes"; rescue LoadError; puts "no"; end' 2>/dev/null
)
webrick_ver=$(
  set +e
  bundle exec ruby -e 'begin; require "webrick"; puts WEBrick::VERSION; rescue; puts "0.0.0"; end' 2>/dev/null
)

# Compare versions (returns 0 if $1 >= $2)
ver_ge () {
  # usage: ver_ge 1.8.1 1.8.0
  [ "$(printf '%s\n' "$2" "$1" | sort -V | head -n1)" = "$2" ]
}

use_hawkins="no"
if [ "${DISABLE_HAWKINS:-}" = "1" ]; then
  use_hawkins="no"
elif [ "${FORCE_HAWKINS:-}" = "1" ]; then
  use_hawkins="yes"
elif [ "$have_hawkins" = "yes" ]; then
  # Skip hawkins when WEBrick >= 1.8.0 (known servlet crash with Jekyll 3.9.x)
  if ver_ge "${webrick_ver}" "1.8.0"; then
    use_hawkins="no"
    echo "[run_server] Detected WEBrick ${webrick_ver} (>=1.8.0). Skipping Hawkins liveserve to avoid servlet crash."
  else
    use_hawkins="yes"
  fi
fi

# -------- Run server -----------------------------
if [ "$use_hawkins" = "yes" ]; then
  echo "[run_server] Using Hawkins liveserve (WEBrick ${webrick_ver})."
  exec bundle exec jekyll liveserve \
    --force_polling \
    --destination "${BUILD_DIR}"
else
  echo "[run_server] Using plain 'jekyll serve' (WEBrick ${webrick_ver})."
  exec bundle exec jekyll serve \
    --livereload \
    --force_polling \
    --destination "${BUILD_DIR}"
fi
