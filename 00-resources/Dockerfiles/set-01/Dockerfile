FROM fedora:latest

RUN dnf install python3-pip python3 -y; \
    dnf install ansible; \
    ansible-doc -t connection -l 

    # TODO:
    
    #!  Dockerfile
    # can grab req from ztorch for testing purposes
    # enable systemd for ansible, not currently enabled in fedora