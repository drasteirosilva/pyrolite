import unittest
from pyrolite.mineral.lattice import strain_coefficient
from pyrolite.geochem import get_ionic_radii


class TestStrainCoefficient(unittest.TestCase):
    def setUp(self):
        self.r0 = get_ionic_radii("Ca", charge=2, coordination=8)  # angstroms
        self.D0 = 4.1
        self.E = 120 * 10 ** 9  # Pa
        self.Tk = 1200.0  #  kelvin

    def test_default(self):
        for rx in [
            get_ionic_radii("Sr", charge=2, coordination=8),
            get_ionic_radii("Mn", charge=2, coordination=8),
            get_ionic_radii("Mg", charge=2, coordination=8),
            get_ionic_radii("Ba", charge=2, coordination=8),
        ]:
            D_j = self.D0 * strain_coefficient(self.r0, rx, self.E, T=self.Tk)
            self.assertTrue(D_j > 0.)
            self.assertTrue(D_j < self.D0)

if __name__ == "__main__":
    unittest.main()