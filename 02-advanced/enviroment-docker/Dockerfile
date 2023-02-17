# Dockerfile for Ubuntu with SSH and sudo installed and enabled for user test
# The user needs to be test and the password is test as well.

# run the container
# docker run -d -p 2222:22 --name <name-of-container> <name-of-image>

# ssh into the container
# ssh test@<container-ip>  -p 22
# * get the container ip
#   docker inspect <name-of-container> | grep IPAddress


FROM ubuntu:latest

RUN apt update && apt install  openssh-server sudo -y
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 test 

# user and password are test:test, you can change it if you want
RUN  echo 'test:test' | chpasswd
RUN service ssh start

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]
