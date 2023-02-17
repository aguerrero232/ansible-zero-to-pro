import json
import subprocess

# get container network info
cmd = "docker inspect $(docker-compose ps -q) | grep -E '(\"com.docker.compose.service\"|HostPort|\"IPAddress\": \"[0-9.]+\")'"
output = subprocess.getoutput(cmd)
# remove commas from the output
output = output.replace(",", "")
# remove spaces and tabs from the output
output = output.replace(" ", "")
output = output.replace("\t", "")
output = output.split("\n")
data = []
service = host_port = ip_address = None
for line in output:
    if "com.docker.compose.service" in line:
        service = line.split(":")[1].replace('"', "").strip()
    elif "HostPort" in line:
        # if host port is already set, skip the line
        host_port = line.split(":")[1].replace('"', "").strip()
    elif "IPAddress" in line:
        ip_address = line.split(":")[1].replace('"', "").strip()
    if service and host_port and ip_address:
        data.append(
            {"service": service, "ssh_port": host_port, "ip_address": ip_address}
        )
        service = host_port = ip_address = None

print(json.dumps(data, indent=2))
