# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
Exception hierarchy for this package.
"""


class DbusClientError(Exception):
    """
    Top-level error.
    """
    pass


class DbusClientGenerationError(DbusClientError):
    """
    Exception during generation of classes.
    """
    pass


class DbusClientRuntimeError(DbusClientError):
    """
    Exception raised during execution of generated classes.
    """
    pass
