#!/bin/bash

#         "HostPort": "2222"
# "com.docker.compose.service": "controller",
#         "HostPort": "2222"
#     "IPAddress": "172.23.0.2",
#         "HostPort": "2223"
# "com.docker.compose.service": "target1",
#         "HostPort": "2223"
#     "IPAddress": "172.23.0.5",
#         "HostPort": "2224"
# "com.docker.compose.service": "target2",
#         "HostPort": "2224"
#     "IPAddress": "172.23.0.3",
#         "HostPort": "2225"
# "com.docker.compose.service": "target3",
#         "HostPort": "2225"
#     "IPAddress": "172.23.0.4",
#         "HostPort": "2226"
# "com.docker.compose.service": "target4",
#         "HostPort": "2226"
#     "IPAddress": "172.23.0.6",

# docker inspect $(docker-compose ps -q) | grep -E "(\"com.docker.compose.service\"|HostPort|\"IPAddress\": \"[0-9.]+\")"

# print the container service name host port and ip address in a json format using the above grep output
# example: 
# [
#   {
#     "service": "controller",
#     "host_port": "2222",
#     "ip_address": "127.0.0.1"
#   },
#   {
#     "service": "target1",
#     "host_port": "2223",
#     "ip_address": "127.0.0.1"
#   },  
# ]

python gcn.py > docker-network.json
