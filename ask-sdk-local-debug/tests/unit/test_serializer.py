# -*- coding: utf-8 -*-
#
# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the
# License.
#
import unittest

from ask_sdk_local_debug.util.serializer import Serializer


class TestSerializer(unittest.TestCase):

    def test_singleton_serializer(self):
        with self.assertRaises(TypeError) as exc:
            _test_serializer = Serializer()
        self.assertIn("Singletons must be accessed through get_instance()",
                      str(exc.exception),
                      "Serializer Singleton class didn't throw exception for "
                      "Constructor instantiation.")

    def test_singleton_serializer_instances(self):
        test_serializer_1 = Serializer.get_instance()
        test_serializer_2 = Serializer.get_instance()

        self.assertIsInstance(test_serializer_1, Serializer)
        self.assertIsInstance(test_serializer_2, Serializer)
        self.assertIs(test_serializer_1, test_serializer_2,
                      "Serializer get_instance() did not return the same "
                      "singleton instance.")
