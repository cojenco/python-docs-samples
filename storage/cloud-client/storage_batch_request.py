#!/usr/bin/env python

# Copyright 2021 Google LLC
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

"""Sample that uses a batch request.
This sample is used on this page:
    (todo: cathyo@ add page link)
For more information, see README.md.
"""

# [START storage_batch_request]

from google.cloud import storage


def batch_request(bucket_name, prefix=None):
    """Sets the public access prevention status to inherited, so that the bucket inherits its setting from its parent project."""
    # The ID of your GCS bucket
    # bucket_name = "my-bucket"
    # The prefix of the object paths
    # prefix = "folder-prefix/"

    client = storage.Client()
    bucket = client.bucket(bucket_name)

    # Accumulate in a list the objects with a given prefix
    blobs_to_patch = [blob for blob in bucket.list_blobs(prefix=prefix)]

    # Use a batch context manager to edit metadata in the list of blobs
    with client.batch():
        for blob in blobs_to_patch:
            metadata = {"your-metadata-key": "your-metadata-value"}
            blob.metadata = metadata
            blob.patch()

    print(f"Batch request edited metadata for all objects with the given prefix in {bucket.name}.")


# [END storage_batch_request]

if __name__ == "__main__":
    batch_request(bucket_name=sys.argv[1])
