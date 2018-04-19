from radical.htbac import Runner
from radical.htbac.simulation import Simulation
from radical.htbac.system import System

system = System(prefix='nilotinib-e255k')

sim = Simulation()
sim.system = system
sim.config = 'esmacs-stage-0.conf'
sim.numsteps = 100
sim.cutoff = 10.0
sim.water_model = 'tip4'
sim.engine = 'namd_openmp_cuda'

ht = Runner(resource='titan_orte')
ht.rabbitmq_config()
ht.add_protocol(sim)

ht.run(walltime=30, queue='debug')




