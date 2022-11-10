#!/bin/bash -eu

cd "$(dirname "$0")"

command=$1
source_paths=${@:2}

python -m libcst.tool codemod --no-format "$command" $source_paths
