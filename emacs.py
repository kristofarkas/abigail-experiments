from htbac import Protocol, Runner, Simulation,	System,	AbFile
from htbac.protocols import Esmacs


# Load systems

systems = list()

# Create protocol

esm = Protocol(clone_settings=False)

# Create simulations and add them to the protocol

for step, numsteps in zip(Esmacs.steps, Esmacs.numsteps):

    sim = Simulation()
    sim.engine = 'namd_openmp_cuda'

    sim.cutoff = 10.0
    sim.switchingdist = 8.0
    sim.pairlistdist = 11.5
    sim.water_model = 'tip4'

    # This is present in step 3 only.
    sim.numsmallsteps = 20000
    sim.numsteps = numsteps

    sim.add_input_file(step, is_executable_argument=True)

    sim.add_ensemble('replica', range(25))
    sim.add_ensemble('system', systems)

    esm.append(sim)

# Create runner and assign protocol to it

ht = Runner(resource='titan_orte', comm_server=('csc190specfem.marble.ccs.ornl.gov', 30672))
ht.add_protocol(esm)

# Run
ht.run(walltime=60)
