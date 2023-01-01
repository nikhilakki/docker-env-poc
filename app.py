# Copyright (c) 2023 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pathlib import os
from bottle import route, run, json_dumps


@route("/env")
def env_load():
    return json_dumps({"env vars": os.getenv("ENV_VAR", "Not Found!")})


@route("/ping")
def ping():
    return json_dumps({"response": "pong"})


run(host="0.0.0.0", port=8080)
