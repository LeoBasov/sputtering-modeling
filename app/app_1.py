import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append('../.')

import sputtering.sigmund as sigmund
import sputtering.zalm as zalm

def main():
	M1 = 12
	M2 = 99
	Z1 = 2
	Z2 = 45
	Ub = 6.82
	E = [i for i in range(1000, 11000, 100)]
	E_show = [i for i in range(1, 11, 1)]

	E_show = np.arange(1, 11, 0.1)

	sig = []
	zal = []

	alpha_apos = sigmund.alpha_apos(M1, M2)
	lindhard_screening_length = sigmund.lindhard_screening_length(Z1, Z2)
	nuclear_cross_section_factor = sigmund.nuclear_cross_section_factor(lindhard_screening_length, Z1, Z2, M1, M2)
	reduced_energy_factor = sigmund.reduced_energy_factor(lindhard_screening_length, Z1, Z2, M1, M2)

	for energy in E:
		reduced_energy = reduced_energy_factor*energy
		thomas_fermi_screening = sigmund.thomas_fermi_screening(reduced_energy)
		nuclear_cross_section = nuclear_cross_section_factor*thomas_fermi_screening

		sig.append(sigmund.total_yield_high_energy(alpha_apos, nuclear_cross_section, Ub))
		zal.append(zalm.total_yield_high_energy(Z1, Z2, Ub, reduced_energy))

	line1, = plt.plot(E_show, sig, label='Sigmund')
	line2, = plt.plot(E_show, zal, label='Zalm')
	plt.ylabel('Yield')
	plt.xlabel('Incident Energy [keV]')
	plt.figlegend()
	plt.show()

if __name__ == '__main__':
	main()