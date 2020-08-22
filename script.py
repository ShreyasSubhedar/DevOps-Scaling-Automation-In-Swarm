'''
POC: - Auto Scaling feature in Docker swarm using Docker SDK

Author : ShreyasXO
Date : 12/1/2020  
'''

import docker

# To talk to a Docker daemon, you first need to instantiate a client.
client = docker.from_env()

