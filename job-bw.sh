#!/bin/bash

export RADICAL_PILOT_DBURL='mongodb://htbac:htbac@ds251287.mlab.com:51287/htbac-inspire-1'
export SAGA_PTY_SSH_TIMEOUT=2000
export RADICAL_PILOT_PROFILE=True
export RADICAL_ENMD_PROFILE=True
export RADICAL_ENMD_PROFILING=1
export RP_ENABLE_OLD_DEFINES=True

export RADICAL_ENTK_VERBOSE='DEBUG'
export RADICAL_SAGA_VERBOSE='DEBUG'
export RADICAL_PILOT_VERBOSE='DEBUG'

export GLOBUS_LOCATION=/Library/Globus

python test.py
