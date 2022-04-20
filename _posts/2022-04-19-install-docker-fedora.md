---
layout: post
title:  "Install docker on Fedora Server 35"
date:   2022-04-19
author: Marcin SP6MI
---

Installing **docker** on Fedora Server 35 is no a rocket science1. Just few simple steps and you can start using latest docker on your server.

First we have to enable and add some additional servers to our **dnf** configuration.

Please remeber that those operations must be excuted as root - (sudo or su -)

At first please ensure that all previous installations were removed

{% highlight bash %}
dnf remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine
{% endhighlight %}

{% highlight bash %}
# install additional dnf plugin
dnf install dnf-plugins-core

# add official docker repository_url
dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

# enable docker repositories
# docker-ce-test repository is optional
dnf config-manager --set-enabled docker-ce-nightly
dnf config-manager --set-enabled docker-ce-test

# install docker
dnf install docker-ce docker-ce-cli containerd.io
{% endhighlight %}

Now we can start docker service and run test docker image

{% highlight bash %}
# enable service
systemctl start docker

# run test image
docker run hello-world
{ %endhighlight %}

To be able to use docker as non-root user you have to add user account to docker group.

{% highlight bash %}
usermod -a -G docker $USER
{ %endhighlight %}

Soon I'll publish more instruction how to play with docker and kubernetes on you won home lab.
