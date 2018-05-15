# Import HTBAC modules

from htbac import Simulation, System, AbFile, Runner

# Step 0: load system files.

coord = AbFile('systems/nilotinib-e255k-complex.inpcrd', tag='coordinate')
top = AbFile('systems/nilotinib-e255k-complex.top', tag='topology')
system = System(name='nilotinib-e255k', files=[top, coord])

# Step 1: create a simulation

sim = Simulation()

sim.engine = 'openmm'
sim.system = system

sim.numsteps = 1000

ht = Runner(resource='titan_orte', comm_server=('csc190specfem.marble.ccs.ornl.gov', 30672))
ht.add_protocol(sim)
ht.run(walltime=30, queue='debug')
