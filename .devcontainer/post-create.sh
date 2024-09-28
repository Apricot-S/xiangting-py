#!/usr/bin/env bash

set -euxo pipefail

sudo apt-get update
sudo apt-get clean
sudo rm -rf /var/lib/apt/lists/*

sudo chown vscode:vscode /workspaces
sudo chown -R vscode:vscode /workspaces/xiangting-py

chmod +x scripts/*.sh

python3 -m venv .venv # for `maturin develop`
uv sync
