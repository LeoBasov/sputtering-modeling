"""This is the base module containing the Zalm Total Yield Formula and all associated functions

Unless otherwise specified the following units are usded in this module:

Length  : [Å]
Enerngy : [eV]
Mass  : [amu]

"""

import math

def total_yield_high_energy(atomic_number_incident_particle, atomic_number_target, surface_binding_energy, reduced_energy):
	"""Sigmunds total yield formula for reduced energy > 1

	Parameters
	----------
	atomic_number_incident_particle : double
		Atomic number of the incident particle [-]

	atomic_number_target : double
		Atomic number of the target [-]

	surface_binding_energy : double
		Surface binding energy of unit [eV].

		It is a tabular value specific for the target.

	reduced_energy : double
		reduced incident energy [-]

	Returns
	-------
	double
    	The return value is the total yield per incident particle.

    	Ther yield is normaly provided in unit [atoms/incident ion]

	"""
	numerator_1 = math.pow(atomic_number_incident_particle*atomic_number_target,5/6)
	numerator_2 = 0.5*math.log(1.0 + reduced_energy)
	denumerator_1 = 3.0*surface_binding_energy
	denumerator_2 = reduced_energy + 0.14*math.pow(reduced_energy, 0.42)
	factor_1 = numerator_1/denumerator_1
	factor_2 = numerator_2/denumerator_2

	return factor_1*factor_2

__author__ = "Leo Basov"
__copyright__ = "Copyright (C) 2019, Leo Basov"
__license__ = "GPLv3"