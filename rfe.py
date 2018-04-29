"""Absolute free energy calculations

Example implementation using Abigail and NAMD.

"""

from htbac import Runner, System, Simulation, Protocol
from htbac.protocols import Rfe


def run_rfe():
    system = System(prefix='systems/ptp1b-l1-l2')

    rfe = Simulation()
    rfe.system = system
    rfe.engine = 'namd'
    rfe.cores = 2

    rfe.numminsteps = 10
    rfe.numsteps = 10

    rfe.add_input_file(Rfe.step0, is_executable_argument=True)

    rfe.add_ensemble('replica', range(2))
    rfe.add_ensemble('lambda-window', [0.0, 1.0])

    rfe.cutoff = 12.0
    rfe.switchdist = 10.0
    rfe.pairlistdist = 13.5

    rfe_sim = Simulation()
    rfe_sim.add_input_file(Rfe.step1, is_executable_argument=True)
    rfe_sim.numsteps = 50

    p = Protocol()
    p.append(rfe)
    p.append(rfe_sim)

    ht = Runner(comm_server=('two.radical-project.org', 33146))
    ht.add_protocol(p)
    ht.run(walltime=1000)


if __name__ == '__main__':
    run_rfe()

