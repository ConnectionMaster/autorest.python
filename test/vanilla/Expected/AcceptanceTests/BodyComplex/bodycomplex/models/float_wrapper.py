# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FloatWrapper(Model):
    """FloatWrapper.

    :param field1:
    :type field1: float
    :param field2:
    :type field2: float
    """

    _attribute_map = {
        'field1': {'key': 'field1', 'type': 'float'},
        'field2': {'key': 'field2', 'type': 'float'},
    }

    def __init__(self, field1=None, field2=None):
        super(FloatWrapper, self).__init__()
        self.field1 = field1
        self.field2 = field2