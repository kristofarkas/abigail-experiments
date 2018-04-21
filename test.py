from radical.htbac import Runner, BaseSimulation, EnsembleSimulation, System


resource = 'titan_orte'
engine = 'namd_openmp_cuda'
rabbit_mq = dict(hostname='two.radical-project.org', port=33146)
run_conf = dict(walltime=30, queue='debug')


def test_single_simulation():

    system = System(prefix='nilotinib-e255k')

    sim = BaseSimulation()
    sim.system = system
    sim.config = 'simple.conf'
    sim.engine = engine

    ht = Runner(resource=resource)
    ht.rabbitmq_config(**rabbit_mq)
    ht.add_protocol(sim)

    ht.run(**run_conf)


def test_replica_simulation():

    system = System(prefix='nilotinib-e255k')

    sim = EnsembleSimulation()
    sim.system = system
    sim.config = 'simple.conf'
    sim.engine = engine
    sim.add_ensemble('replica', range(2))

    ht = Runner(resource=resource)
    ht.rabbitmq_config(**rabbit_mq)
    ht.add_protocol(sim)

    ht.run(**run_conf)


def test_replica_systems_simulation():

    s1 = System(prefix='nilotinib-e255k')
    s2 = System(prefix='nilotinib-e255b')

    sim = EnsembleSimulation()
    sim.config = 'simple.conf'
    sim.engine = engine

    sim.add_ensemble('system', [s1, s2])
    sim.add_ensemble('replica', range(2))

    ht = Runner(resource=resource)
    ht.rabbitmq_config(**rabbit_mq)
    ht.add_protocol(sim)

    ht.run(**run_conf)


def test_configurable_simulation():
    s1 = System(prefix='nilotinib-e255k')

    sim = BaseSimulation()
    sim.system = s1
    sim.config = 'configurable.conf'
    sim.engine = engine

    sim.numsteps = 1000
    sim.cutoff = 10.0
    sim.water_model = 'tip4'

    ht = Runner(resource=resource)
    ht.rabbitmq_config(**rabbit_mq)
    ht.add_protocol(sim)

    ht.run(**run_conf)


if __name__ == '__main__':
    test_replica_systems_simulation()
