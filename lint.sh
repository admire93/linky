#!/usr/bin/env bash
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

mkdir -p .git/hooks
if [[ -f .git/hooks/pre-commit ]]; then
  ln -s "$project_root/lint.sh" .git/hooks/pre-commit
fi

flake8 --exclude '.venv,docs,.tox' "$project_root"
import-order --exclude=.tox --exclude=docs --exclude=.venv linky .

exit 0

# vim: set filetype=sh ts=2 sw=2 sts=2:
