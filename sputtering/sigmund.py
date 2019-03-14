"""This is the base module containing the Sigmund Total Yield Formula and all associated functions

"""

import math

E_SQUARED = 14.4
"""double: Squared elemenatal charge. Provided in [eV Å].

"""

def total_yield_high_energy(alpha_apos, nuclear_cross_section, surface_binding_energy):
	"""Sigmunds total yield formula for E > 1 keV

	This function calculates the total yield for incidend energies > 1 keV.

	Parameters
	----------
	alpha_apos : double
		Parameter calculated by function...

	nuclear_cross_section : double
		Nuclear cross section as calculated by the Thomas-Fermi nuclear cross-section formula for high energy (ε >1).

	surface_binding_energy : double
		Surface binding energy of unit [eV].

		It is a tabular value specific for the target.

	Returns
	-------
	double
    	The return value is the total yield per incident particle.

    	Ther yield is normaly provided in unit [atoms/incident ion]

	"""
	return 0.042*alpha_apos*nuclear_cross_section/surface_binding_energy

def total_yield_low_energy_factor(alpha_apos, surface_binding_energy, atomic_mass_incident_particle, atomic_mass_target):
	"""Returns a factor for Sigmunds total yield formula for E < 1 keV and E > 10*surface_binding_energy

	This function calculates the factor total yield for incidend energies (E) > 1 keV and E > 10*surface_binding_energy.
	The fator needs to be multiplied with the energy of the incident particle to calculate the total yield.

	Parameters
	----------
	alpha_apos : double
		Parameter calculated by function...

	surface_binding_energy : double
		Surface binding energy is a tabular value specific for the target.

	atomic_mass_incident_particle : double
		Atomic pass of the incident particle provided in [amu]

	atomic_mass_target : double
		Atomic pass of the target provided in [amu]


	Returns
	-------
	double
    	The return value a factor for the total yield

	"""
	factor_1 = 3.0/(math.pi*math.pi)
	factor_2 = alpha_apos/surface_binding_energy
	factor_3 = atomic_mass_incident_particle*atomic_mass_target/math.pow(atomic_mass_incident_particle + atomic_mass_target, 2)

	return factor_1*factor_2*factor_3

def total_yield_low_energy(alpha_apos, surface_binding_energy, atomic_mass_incident_particle, atomic_mass_target, incident_energy):
	"""Sigmunds total yield formula for E < 1 keV and E > 10*surface_binding_energy

	This function calculates the total yield for incidend energies (E) > 1 keV and E > 10*surface_binding_energy.

	Parameters
	----------
	alpha_apos : double
		Parameter calculated by function...

	surface_binding_energy : double
		Surface binding energy is a tabular value specific for the target.

	atomic_mass_incident_particle : double
		Atomic pass of the incident particle provided in [amu]

	atomic_mass_target : double
		Atomic pass of the target provided in [amu]

	incident_energy : double
		Energy for for the incident particle provided in [eV]

	Returns
	-------
	double
    	The return value is the total yield per incident particle.

    	Ther yield is normaly provided in unit [atoms/incident ion]

	"""
	return total_yield_low_energy_factor(alpha_apos, surface_binding_energy, atomic_mass_incident_particle, atomic_mass_target)*incident_energy

def a_i(atomic_number_incident_particle, atomic_number_target):
	"""Sigmunds paramter for use in calculation of reduced energy

	Parameters
	----------
	atomic_number_incident_particle : double
		Atomic number of the incident particle [-]

	atomic_number_target : double
		Atomic number of the target [-]

	Returns
	-------
	double
    	Ther return value is in unit [Å]

	"""
	z_1 = math.pow(atomic_number_incident_particle, 2.0/3.0)
	z_2 = math.pow(atomic_number_target, 2.0/3.0)

	return 0.468/math.sqrt(z_1 + z_2)

__author__ = "Leo Basov"
__copyright__ = "Copyright (C) 2019, Leo Basov"
__license__ = "GPLv3"