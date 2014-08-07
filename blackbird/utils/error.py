# -*- coding: utf-8 -*-

from exceptions import Execption


class BlackbirdError(Execption):
    """
    blackbird error.
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
