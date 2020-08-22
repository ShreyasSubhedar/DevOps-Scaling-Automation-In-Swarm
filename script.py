'''
POC: - Auto Scaling feature in Docker swarm using Docker SDK

Author : ShreyasXO
Date : 12/1/2020  
'''

import docker
import os
import psutil
import time

# The default replica size is 3
# If the overall resource utlization goes upto 60 %
# and remains for it upto long enough
# then add the replica by 2
# everytime do it itraltively

threhold_value=60
intial_replica_count = 3
# To talk to a Docker daemon, you first need to instantiate a client.
client = docker.from_env()

# leaving the machine if already into swarm cluster
client.swarm.leave(force=True)

# initialzing swarm
# adding default initialization
# as per the documentation

# token = client.swarm.init() will also work
token = client.swarm.init(advertise_addr='eth0',
                          listen_addr='0.0.0.0:5000',
                          force_new_cluster=False,
                          default_addr_pool=['10.20.0.0/16'],
                          subnet_size=24,
                          snapshot_interval=5000,
                          log_entries_for_slow_followers=1200)

# creating serice
# image = code editor
# name = name of service
# hosts = mappings in dictionary
service_editor = client.services.create(image="shreyasxo/code-editor:PHP",
                                        name="Editor",
                                        hosts={"8080": "8080"})

# Logic : 
# psutil.cpu_percent gives float value of overall cpu utilization
# if the value goes higher than the threshold value
# we are adding the replica set by 2
# if the cpu utilisation decrease to 60 or less then we are
#  lowering the replica by 2  
while 1 :
    if psutil.cpu_percent() >= threhold_value:
        intial_replica_count = intial_replica_count + 2 
        service_editor.scale(intial_replica_count)
    elif psutil.cpu_percent()<threhold_value:
        intial_replica_count = intial_replica_count - 2
        if intial_replica_count <=0:
            intial_replica_count =3 
        service_editor.scale(intial_replica_count)
    time.sleep(10)



'''
TODO: Adding logic to make more work
'''