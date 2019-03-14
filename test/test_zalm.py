import unittest
import sys
import math

sys.path.append('../.')

import sputtering.zalm as zalm

class TestZalm(unittest.TestCase):
	def test_total_yield_high_energy_1(self):
		atomic_number_incident_particle = 1
		atomic_number_target = 1
		surface_binding_energy = 1
		reduced_energy = 1
		ref_value = (1/3)*0.5*math.log(2)/1.14

		calculated_value = zalm.total_yield_high_energy(atomic_number_incident_particle, atomic_number_target, surface_binding_energy, reduced_energy)

		self.assertAlmostEqual(ref_value, calculated_value, 4)

if __name__ == '__main__':
	unittest.main()