#!/usr/bin/env bash

set -euxo pipefail

# Set up colorful debug output
PS4='+${BASH_SOURCE[0]}:$LINENO: '
if [[ -t 1 ]] && type -t tput >/dev/null; then
  if (( "$(tput colors)" == 256 )); then
    PS4='$(tput setaf 10)'$PS4'$(tput sgr0)'
  else
    PS4='$(tput setaf 2)'$PS4'$(tput sgr0)'
  fi
fi

sudo apt-get update
sudo apt-get clean
sudo rm -rf /var/lib/apt/lists/*

sudo chown vscode:vscode /workspaces
sudo chown -R vscode:vscode /workspaces/xiangting-py

chmod +x scripts/*.sh

python3 -m venv .venv # for `maturin develop`
uv sync
