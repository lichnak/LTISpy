import sympy as sp


class tf():

    def __init__(self, n, d):
        """
        This class represents transfer function
        TODO: arguments should be list or iterables

        :param n: list of nominator coefficients
        :param d: list of denominator coefficients
        """
        self.s = sp.symbols("s")
        self.n_coeffs = n
        self.d_coeffs = d
        self.n_poly = sp.Poly.from_list(self.n_coeffs, self.s)
        self.d_poly = sp.Poly.from_list(self.d_coeffs, self.s)

    def poles(self):
        return sp.solve(self.d_poly)

    def zeros(self):
        return sp.solve(self.n_poly)