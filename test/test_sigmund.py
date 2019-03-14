import unittest
import sys

sys.path.append('../.')

import sputtering.sigmund as sigmund

class TestSigmund(unittest.TestCase):
	def test_total_yield_high_energy(self):
		alpha_apos = 1
		nuclear_cross_section = 1
		surface_binding_energy = 1
		ref_value = 0.042

		calculated_value = sigmund.total_yield_high_energy(alpha_apos, nuclear_cross_section, surface_binding_energy)

		self.assertEqual(ref_value, calculated_value)

if __name__ == '__main__':
	unittest.main()