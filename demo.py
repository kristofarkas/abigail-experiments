# Import HTBAC modules

from htbac import Protocol, Simulation, System

# Import built in simulation protocol configurations
# like relative free energy calculations, or esmacs

from htbac.protocols import Rfe, Afe, Esmacs

# Step 0: load system files.

system = System(prefix='systems/ptp1b-l1-l2')

# Step 1: create the container protocol

p = Protocol()

# Step 2: create a simulation that minimizes and equilibrate the system

s0 = Simulation(name='minimizer')
s0.system = system

