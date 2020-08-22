'''
POC: - Auto Scaling feature in Docker swarm using Docker SDK

Author : ShreyasXO
Date : 12/1/2020  
'''

import docker

# To talk to a Docker daemon, you first need to instantiate a client.
client = docker.from_env()

# leaving the machine if already into swarm cluster
client.swarm.leave(force=True)

# initialzing swarm
token = client.swarm.init()

# creating serice
service_editor = client.services.create(image="shreyasxo/code-editor:PHP",
                                        name="Editor",
                                        hosts={"8080": "8080"})
