"""This is the base module containing the Sigmund Total Yield Formula and all associated functions

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
		Surface binding energy is a tabular value specific for the sputtered medium.

	Returns
    -------
    double
    	The return value is the total yield per incident particle.

    	Ther yield is normaly provided in unit [atoms/incident ion]

	"""
	return 0.042*alpha_apos*nuclear_cross_section/surface_binding_energy

__author__ = "Leo Basov"
__copyright__ = "Copyright (C) 2019, Leo Basov"
__license__ = "GPLv3"