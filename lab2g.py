#!/usr/bin/env python3

# Author: Seamus James Dujua
# Author ID: sjdujua
# Date Created: 2025/01/19

import sys

if len(sys.argv) > 1:

	timer = int(sys.argv[1])

else: 
	timer = 3

while timer > 0:
	print(timer)
	timer -= 1

print('blast off!')
