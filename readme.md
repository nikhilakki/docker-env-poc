<!--
 Copyright (c) 2023 Nikhil Akki
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
-->

## Docker Env POC

A POC for passing an Env variable to a docker container and reading it in the application.

- A simple Python web app containerized using Docker
- Endpints -
  - `/ping` # returns pong
  - `/env` # returns ENV_VAR value passed during docker run

### How to run?

```bash
# Step 0 - Display CLI options
./docker-helper.sh
# o/p - CLI options, choose from build | run | run-env | clean
# Step 1 - Build docker container image
./docker-helper.sh build
# Step 2 - Run docker container without setting ENV_VAR
./docker-helper.sh run
# Step 3 - Run docker container with value passed in ENV_VAR; it is picked up from 2nd arg (value in "")
./docker-helper.sh run-env "this-is-coming-from-env-var"

```
> Finally open http://0.0.0.0:8080/env

##### Author

- [Nikhil Akki](nikhilakki.in)

> License - MIT