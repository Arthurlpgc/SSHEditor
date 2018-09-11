FROM ubuntu
RUN apt-get -y update
RUN apt-get -y install software-properties-common python-software-properties
RUN add-apt-repository main
RUN add-apt-repository universe
RUN add-apt-repository restricted
RUN add-apt-repository multiverse
RUN apt-get -y update
RUN apt-get -y install linux-headers-generic build-essential
RUN apt-get -y install zlib1g-dev libssl-dev libreadline-gplv2-dev
RUN apt-get -y install curl unzip
RUN apt-get -y install software-properties-common
RUN apt-get -y install gnupg2
RUN apt-get -y install nano
RUN apt-get -y install vim
RUN apt-get -y install aptitude
RUN apt-get -y install git
RUN apt-get -y install whois
RUN apt-get -y install dos2unix
RUN apt-get -y install openssh-server
RUN mkdir -p /var/run/sshd
RUN echo 'root:root' |chpasswd
COPY sshd_config /etc/ssh/
EXPOSE 22
RUN mkdir /test_dir
RUN touch /test_dir/test1.cpp
RUN mkdir /test_dir/test2
RUN touch /test_dir/test2.cpp
RUN touch /test_dir/test2/testc.cpp
RUN touch '/test_dir/test c.cpp'
CMD    /usr/sbin/sshd -D