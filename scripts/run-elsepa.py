from elsepa.generate_input import (generate_elscata_input, Settings)
from elsepa import units
import numpy as np


energies = np.array([
    10, 20, 30, 40, 50, 60, 70, 80, 90,
    100, 200, 300, 400, 500, 600, 700, 800, 900,
    1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000,
    10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000,
    100000]) * units.eV


if __name__ == "__main__":
    s = Settings(IZ=12, MNUCL=3, MELEC=4, MUFFIN=1, IELEC=-1,
                 MEXCH=1, MCPOL=2, IHEF=0, MABS=0, EV=energies)
    print(generate_elscata_input(s))

