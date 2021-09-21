#!/usr/bin/env python

# Copyright 2021 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
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

import sys

# [START storage_configure_retries]
from google.cloud import storage
from google.cloud.storage.retry import DEFAULT_RETRY


def configure_retries(bucket_name, blob_name):
    """Configures retries with customizations."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Customize Retry with a deadline of 500 seconds instead of the default 120 seconds.
    # Customize Retry with a wait time multiplier per iteration of 3.0 instead of the default 2.0.
    modified_retry = DEFAULT_RETRY.with_deadline(500)
    modified_retry = modified_retry.with_delay(maximum=60, multiplier=3)

    # blob.delete() uses DEFAULT_RETRY_IF_GENERATION_SPECIFIED by default.
    # Override with modified_retry so that the function retries even if the generation number is not specified.
    print("The following library method is customized to be retried according to the following configurations:")
    print(modified_retry.__str__())

    blob.delete(retry=modified_retry)
    print("Blob {} deleted with a customized retry strategy.".format(blob_name))

# [END storage_configure_retries]


if __name__ == "__main__":
    configure_retries(bucket_name=sys.argv[1], blob_name=sys.argv[2])
