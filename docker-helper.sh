# Copyright (c) 2023 Nikhil Akki
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

#!/bin/sh
cmd=$1
env=$2
case "$cmd" in
    "build") docker build . -t pyenv-poc ;;
    "run") 
        docker run --rm -p 8080:8080 pyenv-poc ;;
    "run-env") 
        echo $env && docker run --rm -e ENV_VAR=$env -p 8080:8080 pyenv-poc ;;
    "run-env-file") 
        echo $env && docker run --rm --env-file .env -p 8080:8080 pyenv-poc ;;
    "clean")
        echo "Cleaning docker build..." && docker rmi -f pyenv-poc ;;
    *)
        echo "CLI options, choose from build | run | run-env | clean" ;;              
esac
