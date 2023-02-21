import json
import subprocess
import docker

from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.errors import AnsibleParserError
import os

client = docker.from_env()
# TODO grab from the os environment
#  ansible is not able to access
#  ! compose_project_name = os.environ[\"COMPOSE_PROJECT_NAME\"] KeyError: 'COMPOSE_PROJECT_NAME'
# compose_project_name = os.environ['COMPOSE_PROJECT_NAME']

compose_project_name = "ubuntu_ssh" 
network_name = f"{compose_project_name}_default"

class NetworkHelper:
    def __init__(self, network):
        used_attrs = []

        self.name = network.name
        self.id = network.id
        self.containers = network.containers
        self.attrs = {a: network.attrs[a] for a in network.attrs }
        #  if a in used_attrs
    def __str__(self):
        return f"name: {self.name}, id: {self.id}"

    def __repr__(self):
        return self.__str__()    

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id

    def get_attrs(self, ):
        return self.attrs

class ContainerHelper:
    def __init__(self, container):
        used_labels = [
            "com.docker.compose.project",
            "com.docker.compose.service",
            "org.opencontainers.image.ref.name",
            "org.opencontainers.image.version",
        ]

        self.name = container.name
        self.id = container.id
        self.labels = {k: container.labels[k] for k in container.labels if k in used_labels}

    def __str__(self) -> str:
        return f"name: {self.name}, id: {self.id}"

    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, other) -> bool:
        return self.name == other.name and self.id == other.id
    
    def get_labels(self):
        return self.labels


def main():
    n = list(filter(lambda network: network.name == network_name, client.networks.list()))[0]

    network = NetworkHelper(n)
    cl = client.containers.list()

    containers = [
        ContainerHelper(c)
        for c in cl
        if c.labels["com.docker.compose.project"] == compose_project_name
    ]

    print(network)
    
    [print(container) for container in containers]




if __name__ == "__main__":
    main()


# # get container network info
# # TODO create an inventory module class
# cmd = "docker inspect $(docker-compose ps -q) | grep -E '(\"com.docker.compose.service\"|HostPort|\"IPAddress\": \"[0-9.]+\")'"
# output = subprocess.getoutput(cmd)

# output = output.replace(",", "")
# output = output.replace(" ", "")
# output = output.replace("\t", "")
# output = output.split("\n")

# data = []
# service = ssh_port = ip_address = None
# for line in output:
#     if "com.docker.compose.service" in line:
#         service = line.split(":")[1].replace('"', "").strip()
#     elif "HostPort" in line:
#         if ssh_port is None:
#             ssh_port = line.split(":")[1].replace('"', "").strip()
#     elif "IPAddress" in line:
#         ip_address = line.split(":")[1].replace('"', "").strip()

#     if service and ssh_port and ip_address:
#         data.append(
#             {"service": service, "ssh_port": ssh_port, "ip_address": ip_address}
#         )
#         service = ssh_port = ip_address = None

# data = list(filter(lambda x: x["service"] != "controller", data))


# for i, v in enumerate(data):
#     if v['service'] == "controller":
#         # remove service: controller
#         data.pop(i)

# # write to docker-network.json
# # check out new style dynamic inventory
# f = open("docker-network.json", "w")
# f.write(json.dumps(data, indent=2))
# f.close()
