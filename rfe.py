"""Absolute free energy calculations

Example implementation using Abigail and NAMD.

"""

import numpy as np

from htbac import Runner, System, Simulation, Protocol
from htbac.protocols import Rfe


def run_rfe():
    system = System(prefix='systems/ptp1b-l1-l2')

    rfe = Simulation()
    rfe.system = system
    rfe.engine = 'namd_mpi'
    rfe.cores = 128

    rfe.numminsteps = 10000
    rfe.numsteps = 1000000

    rfe.add_input_file(Rfe.step0, is_executable_argument=True)

    rfe.add_ensemble('replica', range(5))
    rfe.add_ensemble('lambda-window', np.linspace(0, 1, 65))

    rfe.cutoff = 12.0
    rfe.switchdist = 10.0
    rfe.pairlistdist = 13.5

    rfe_sim = Simulation()
    rfe_sim.add_input_file(Rfe.step1, is_executable_argument=True)
    rfe_sim.numsteps = 2000000

    p = Protocol()
    p.append(rfe)
    p.append(rfe_sim)

    ht = Runner('bw_aprun', comm_server=('two.radical-project.org', 33162))
    ht.add_protocol(p)
    ht.run(walltime=480, queue='high')


if __name__ == '__main__':
    run_rfe()
