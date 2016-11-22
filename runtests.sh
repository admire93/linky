#!/usr/bin/env bash
set -e

if [[ "$GIT_AUTHOR_DATE" ]]; then
  project_root="$PWD"
elif env | grep '^GIT_PREFIX='; then
  project_root="$PWD"
else
  project_root="$(dirname "$0")"
fi

if [[ "$VIRTUAL_ENV" = "" ]]; then
  echo 'You seem not in any virtual environment.  Stopped.' >> /dev/stderr
  exit 1
fi

pytest -vv -n 16

if [[ "$(which ag)" != "" ]]; then
  ag 'TODO|FIXME' linky
elif [[ "$(which ack)" != "" ]]; then
  ack 'TODO|FIXME' linky
elif [[ "$(which rg)" != "" ]]; then
  rg 'TODO|FIXME' linky
fi

exit 0

# vim: set filetype=sh ts=2 sw=2 sts=2:
