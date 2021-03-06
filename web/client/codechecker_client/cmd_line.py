# -------------------------------------------------------------------------
#                     The CodeChecker Infrastructure
#   This file is distributed under the University of Illinois Open Source
#   License. See LICENSE.TXT for details.
# -------------------------------------------------------------------------
"""
Command line module.
"""


import json


class CmdLineOutputEncoder(json.JSONEncoder):
    # pylint: disable=method-hidden
    def default(self, o):
        d = {}
        d.update(o.__dict__)
        return d
