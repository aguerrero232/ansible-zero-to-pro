FROM fedora:latest

# RUN dnf -y update

RUN dnf -y install ansible; \
    dnf -y install python3-pip; \
    ansible-doc -t connection -l

# RUN dnf clean all

# RUN python3 --version;\
#     pip --version;\
#     ansible --version