#!/usr/bin/env bash
# Copyright 2017 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -ex

# Enter the gRPC repo root
cd $(dirname $0)/../../..

source tools/internal_ci/helper_scripts/prepare_build_linux_rc

export DOCKERFILE_DIR=tools/dockerfile/test/cxx_debian11_x64
export DOCKER_RUN_SCRIPT=tools/internal_ci/linux/grpc_bloat_diff_in_docker.sh
# The check_on_pr.py needs access to the key to post status on github PRs,
# so we mount the keystore dir to the docker container.
export EXTRA_DOCKER_ARGS="-v ${KOKORO_KEYSTORE_DIR}:/kokoro_keystore -e KOKORO_KEYSTORE_DIR=/kokoro_keystore"
exec tools/run_tests/dockerize/build_and_run_docker.sh
