import unittest
import sys

sys.path.append('../.')

import sputtering.sigmund as sigmund

class TestSigmund(unittest.TestCase):
	def test_total_yield_high_energy_1(self):
		alpha_apos = 1
		nuclear_cross_section = 1
		surface_binding_energy = 1
		ref_value = 0.042

		calculated_value = sigmund.total_yield_high_energy(alpha_apos, nuclear_cross_section, surface_binding_energy)

		self.assertEqual(ref_value, calculated_value)

	def test_total_yield_high_energy_2(self):
		alpha_apos = 13.5
		nuclear_cross_section = 1
		surface_binding_energy = 1
		ref_value = 0.042*alpha_apos

		calculated_value = sigmund.total_yield_high_energy(alpha_apos, nuclear_cross_section, surface_binding_energy)

		self.assertEqual(ref_value, calculated_value)

	def test_total_yield_high_energy_3(self):
		alpha_apos = 1
		nuclear_cross_section = 58.123
		surface_binding_energy = 1
		ref_value = 0.042*nuclear_cross_section

		calculated_value = sigmund.total_yield_high_energy(alpha_apos, nuclear_cross_section, surface_binding_energy)

		self.assertEqual(ref_value, calculated_value)

	def test_total_yield_high_energy_4(self):
		alpha_apos = 1
		nuclear_cross_section = 1
		surface_binding_energy = 985.135
		ref_value = 0.042/surface_binding_energy

		calculated_value = sigmund.total_yield_high_energy(alpha_apos, nuclear_cross_section, surface_binding_energy)

		self.assertEqual(ref_value, calculated_value)

if __name__ == '__main__':
	unittest.main()