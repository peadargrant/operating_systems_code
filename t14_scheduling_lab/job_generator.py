#!/usr/bin/env python3
# Job generator script for job scheduling lab
# Peadar Grant

from argparse import ArgumentParser
from random import randint
import json

# command line arg parsing (better than sys.argv directly!)
parser = ArgumentParser(description="job generator for job scheduling lab", epilog="Peadar Grant")
parser.add_argument('--equal', help='force equal time', action='store_true', default=False)
parser.add_argument('njobs', help="number of jobs", type=int)
parser.add_argument('max_arrival_time', help="max arrival time", type=int)
parser.add_argument('max_run_time', help="max run time", type=int)
args = parser.parse_args()

jobs = []
while len(jobs) < args.njobs:
    job = {}
    job['name'] = "J%s" % len(jobs)
    job['arrival'] =  randint(0, args.max_arrival_time)
    job['duration'] = args.max_run_time if args.equal else randint(0, args.max_run_time)
    jobs.append(job)

print(json.dumps(jobs))
    
