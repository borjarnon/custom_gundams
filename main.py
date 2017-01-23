#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random
import tweepy
import time
#import constants

with open('prefixes.json', encoding='utf-8', mode='r') as prefixes_file:
    prefixes = json.load(prefixes_file)
with open('suffixes.json', encoding='utf-8', mode='r') as suffixes_file:
    suffixes = json.load(suffixes_file)
with open('gundams.json', encoding='utf-8', mode='r') as gundams_file:
    gundams = json.load(gundams_file)

random.seed()

#while True:
rand_prefix = random.randint(0, len(prefixes["list"]) - 1)
prefix = prefixes["list"][rand_prefix]
rand_suffix = random.randint(0, len(suffixes["list"]) - 1)
suffix = suffixes["list"][rand_suffix]
rand_gundam = random.randint(0, len(gundams["list"]) - 1)
gundam = gundams["list"][rand_gundam]

rand = random.randint(1, 5)
if rand == 5:
    print(prefix + ' ' + gundam + ' ' + suffix)
elif rand == 3 or rand == 4:
    print(prefix + ' ' + gundam)
elif rand == 1 or rand == 2:
    print(gundam + ' ' + suffix)
