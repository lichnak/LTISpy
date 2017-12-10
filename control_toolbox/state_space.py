import sympy as sp
#from sympy.mpmath import polyroots

class ss():

    def __init__(self, A, B, C, D):
        """
        TODO: check type of A, B, C, D - should do difference between symbolic and numeric?

        :param A:
        :param B:
        :param C:
        :param D:
        """
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.n = len(B)
        self.s = sp.symbols("s")

    def char_poly(self):
        """
        This function obtains characteristic polynomial of the system.

        :return: sympy polynomial
        """
        I = sp.eye(self.n)
        char_poly = (self.s * I - self.A).det()
        return sp.poly(char_poly, self.s)

    def char_poly_coeffs(self):
        """
        This function obtains coefficients of charackteristic polynomial.

        :return: list of coefficients
        """
        char_poly = self.char_poly()
        return char_poly.all_coeffs()

    def poles(self):
        char_poly = self.char_poly()
        return sp.solve(char_poly)