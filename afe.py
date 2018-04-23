"""Absolute free energy calculations

Example implementation using Abigail and NAMD.

"""

from htbac import EnsembleSimulation, Runner, System


def run_afe():
    system = System(prefix='systems/dov-wt')

    afe = EnsembleSimulation()
    afe.system = system
    afe.engine = 'namd'
    afe.cores = 2

    afe.numminsteps = 10
    afe.numsteps = 10

    afe.add_input_file('inputs/md2.inp', is_executable_argument=True)
    afe.add_input_file('inputs/restraint.in', is_executable_argument=False)

    afe.add_ensemble('replica', range(2))
    afe.add_ensemble('lambda_window', [0.0, 1.0])

    afe.cutoff = 12.0
    afe.switchdist = 10.0
    afe.pairlistdist = 11.5

    afe.k1 = 10
    afe.k2 = 500

    ht = Runner('local')
    ht.rabbitmq_config(hostname='two.radical-project.org', port=33146)
    ht.add_protocol(afe)
    ht.run(walltime=1000)


if __name__ == '__main__':
    run_afe()

