# Copyright (c) 2023 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from pathlib import os
from bottle import route, run, json_dumps
import boto3

s3 = boto3.resource('s3')


@route("/env")
def env_load():
    return json_dumps({"env vars": os.getenv("ENV_VAR", "Not Found!")})

@route("/buckets")
def get_bucket_list():
    buckets = [bucket.name for bucket in s3.buckets.all()]
    return json_dumps({"response": dict(bucket_list=buckets)})


@route("/ping")
def ping():
    return json_dumps({"response": "pong"})


run(host="0.0.0.0", port=8080)
