# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################
"""
The arg spec for the vyos_lldp_global module
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type


class Lldp_globalArgs(object):  # pylint: disable=R0903
    """The arg spec for the vyos_lldp_global module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "options": {
                "address": {"type": "str"},
                "enable": {"type": "bool"},
                "legacy_protocols": {
                    "choices": ["cdp", "edp", "fdp", "sonmp"],
                    "type": "list",
                },
                "snmp": {"type": "str"},
            },
            "type": "dict",
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "deleted",
                "rendered",
                "parsed",
                "gathered",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
