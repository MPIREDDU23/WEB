#!/opt/homebrew/bin/python3

class CUtente:
    def __init__(self, attr_pubb, attr_priv):
        self.attr_pubbl = attr_pubb
        self._attr_priv = attr_priv

    @_attr_priv.setter
    def attr_priv(self, attr):
        self._attr_priv = attr    