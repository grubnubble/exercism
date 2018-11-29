from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        gcd = self._gcd(int(numer), int(denom))
        numer = numer/gcd
        denom = denom/gcd
        self.numer = numer if denom > 0 else -numer
        self.denom = self._abs(denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __truediv__(self, other):
        if other.numer * self.denom == 0:
            return NaN
        else:
            numer = self.numer * other.denom
            denom = other.numer * self.denom
            return Rational(numer, denom)

    def __abs__(self):
        abs_numer = self._abs(self.numer)
        abs_denom = self._abs(self.denom)
        return Rational(abs_numer, abs_denom)

    def __pow__(self, power):
        numer = self.numer ** power
        denom = self.denom ** power
        return Rational(numer, denom)

    def __rpow__(self, base):
        return self._root(base ** self.numer, self.denom)

    def _abs(self, number):
        return number if number > 0 else -number

    def _gcd(self, numer, denom):
        numer = self._abs(numer)
        denom = self._abs(denom)
        if numer % denom == 0:
            return denom

        gcd = 1
        for x in range(2, denom):
            if numer % x == 0 and denom % x == 0:
                gcd = x
        return gcd

    def _root(self, p, q):
        power = q ** (-1)
        return p ** power
