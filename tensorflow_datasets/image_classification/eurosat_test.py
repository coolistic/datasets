# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
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

"""Tests for Eurosat data loading."""

import six
from tensorflow_datasets import testing
from tensorflow_datasets.image_classification import eurosat


class EurosatTest(testing.DatasetBuilderTestCase):
  # TODO(mnn): Re-enable Py3 test (b/129964829)
  # None implies testing all BUILDER_CONFIGS, while [] implies no tests.
  BUILDER_CONFIG_NAMES_TO_TEST = None if six.PY2 else []


  DATASET_CLASS = eurosat.Eurosat
  SPLITS = {
      "train": 3,
  }


if __name__ == "__main__":
  testing.test_main()
