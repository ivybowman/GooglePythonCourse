#! /usr/bin/env python3

import os
import requests

# Set Var
# feedback_dir = '/data/feedback'
feedback_dir = 'feedback'
os.chdir(feedback_dir)
files = os.listdir()

for file in files:
    with open(file, 'r') as f:
        feedback = f.readlines()





