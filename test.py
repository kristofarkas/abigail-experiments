from htbac import Runner, BaseSimulation, EnsembleSimulation, System, Protocol


resource = 'local'
engine = 'namd'
rabbit_mq = dict(hostname='two.radical-project.org', port=33146)
run_conf = dict(walltime=1000)


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
    s2 = System(prefix='nilotinib-e255v')

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

    sim.add_placeholder('numsteps', 1000)
    sim.add_placeholder('cutoff', 10.0)
    sim.add_placeholder('switchingdist', 8.0)
    sim.add_placeholder('pairlistdist', 11.5)
    sim.add_placeholder('water_model', 'tip4')

    ht = Runner(resource=resource)
    ht.rabbitmq_config(**rabbit_mq)
    ht.add_protocol(sim)

    ht.run(**run_conf)

def test_full_simulation():
    s1 = System(prefix='nilotinib-e255k')
    s2 = System(prefix='nilotinib-e255v')

    sim = EnsembleSimulation()
    sim.config = 'configurable.conf'
    sim.engine = engine
    sim.cores = 2

    sim.add_ensemble('system', [s1, s2])
    sim.add_ensemble('replica', range(2))

    sim.add_placeholder('numsteps', 10)
    sim.add_placeholder('cutoff', 10.0)
    sim.add_placeholder('switchingdist', 8.0)
    sim.add_placeholder('pairlistdist', 11.5)
    sim.add_placeholder('water_model', 'tip4')

    ht = Runner(resource=resource)
    ht.rabbitmq_config(**rabbit_mq)
    ht.add_protocol(sim)

    ht.run(**run_conf)

def test_protocol():
    
    s1 = System(prefix='nilotinib-e255k')
    s2 = System(prefix='nilotinib-e255v')


    sim1 = EnsembleSimulation()
    sim1.config = 'protocol_1.conf'
    sim1.engine = engine
    sim1.cores = 2

    sim1.add_ensemble('system', [s1, s2])
    sim1.add_ensemble('replica', range(2))

    sim1.add_placeholder('numsteps', 10)
    sim1.add_placeholder('cutoff', 10.0)
    sim1.add_placeholder('switchingdist', 8.0)
    sim1.add_placeholder('pairlistdist', 11.5)
    sim1.add_placeholder('water_model', 'tip4')

    sim2 = EnsembleSimulation()
    sim2.config = 'protocol_2.conf'
    sim2.engine = engine
    sim2.cores = 2

    sim2.add_placeholder('numsteps', 10)
    sim2.add_placeholder('cutoff', 10.0)
    sim2.add_placeholder('switchingdist', 8.0)
    sim2.add_placeholder('pairlistdist', 11.5)
    sim2.add_placeholder('water_model', 'tip4')

    p = Protocol()
    p.add_simulation(sim1)
    p.add_simulation(sim2)
    
    ht = Runner(resource=resource)
    ht.rabbitmq_config(**rabbit_mq)
    ht.add_protocol(p)

    ht.run(**run_conf)

if __name__ == '__main__':
    test_protocol()
