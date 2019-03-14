import unittest
import sys
import math

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

	def test_total_yield_low_energy_factor_1(self):
		alpha_apos = 1
		surface_binding_energy = 1
		atomic_mass_incident_particle = 1
		atomic_mass_target = 1
		ref_value = 3.0/(math.pi*math.pi*4)

		calculated_value = sigmund.total_yield_low_energy_factor(alpha_apos, surface_binding_energy, atomic_mass_incident_particle, atomic_mass_target)

		self.assertEqual(ref_value, calculated_value)

	def test_total_yield_low_energy_1(self):
		alpha_apos = 1
		surface_binding_energy = 1
		atomic_mass_incident_particle = 1
		atomic_mass_target = 1
		incident_energy = 1
		ref_value = 3.0/(math.pi*math.pi*4)

		calculated_value = sigmund.total_yield_low_energy(alpha_apos, surface_binding_energy, atomic_mass_incident_particle, atomic_mass_target, incident_energy)

		self.assertEqual(ref_value, calculated_value)

	def test_total_yield_low_energy_2(self):
		alpha_apos = 1
		surface_binding_energy = 1
		atomic_mass_incident_particle = 1
		atomic_mass_target = 1
		incident_energy = 10
		ref_value = incident_energy*3.0/(math.pi*math.pi*4)

		calculated_value = sigmund.total_yield_low_energy(alpha_apos, surface_binding_energy, atomic_mass_incident_particle, atomic_mass_target, incident_energy)

		self.assertEqual(ref_value, calculated_value)

	def test_lindhard_screening_length_1(self):
		atomic_number_incident_particle = 1
		atomic_number_target = 1
		ref_value = 0.468/math.sqrt(2)

		calculated_value = sigmund.lindhard_screening_length(atomic_number_incident_particle, atomic_number_target)

		self.assertEqual(ref_value, calculated_value)

	def test_alpha_apos_1(self):
		atomic_mass_incident_particle = 1
		atomic_mass_target = 1
		ref_value = 0.15 + 0.13

		calculated_value = sigmund.alpha_apos(atomic_mass_incident_particle, atomic_mass_target)

		self.assertEqual(ref_value, calculated_value)

	def test_alpha_apos_2(self):
		atomic_mass_incident_particle = 2
		atomic_mass_target = 12
		ref_value = 0.15 + 0.13*6

		calculated_value = sigmund.alpha_apos(atomic_mass_incident_particle, atomic_mass_target)

		self.assertEqual(ref_value, calculated_value)

if __name__ == '__main__':
	unittest.main()