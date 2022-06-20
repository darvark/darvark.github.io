---
layout: post
title:  "Instalacja dockera na Fedora Server 35"
date:   2022-04-19
author: Marcin SP6MI
---

Instalacja **docker** na Fedora Server 35 nie jest czymś wyjątkowo skomplikowanym. WYkonanie kilku dość prostych kroków umożliwi Ci korzystanie z dockera na Twoim serwerze.

Na wstępie musimy aktywować i dodać kilka dodatkowyc serwerów do konfiguracji **dnf**.

Pamiętaj, że poniższe operacje musisz wykonywać jako root - bez znaczenia przy użyjesz do tego `sudo` czy `su -`.

Na wstępie upewnijmy się, że poprzednie instalacje zostały w pełni usunięte

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
# Instalowanie dodatkowych pluginów dnf
dnf install dnf-plugins-core

# Dodanie oficjalnego repozytorium dockera
dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

# Aktywacja repozytorium dockera
# docker-ce-test repository is optional
dnf config-manager --set-enabled docker-ce-nightly
dnf config-manager --set-enabled docker-ce-test

# Instalacja dockera
dnf install docker-ce docker-ce-cli containerd.io
{% endhighlight %}

Teraz możemy uruchomić usługę dockera i uruchomić testowy obraz

{% highlight bash %}
# Uruchomie usługi
systemctl start docker

# Uruchomienie testowego obrazu image
docker run hello-world
{% endhighlight %}

Aby móc korzystać z dockera jako zwykły użytkownik należy dodać danego użytkownika do grupy `docker`.

{% highlight bash %}
usermod -a -G docker $USER
{% endhighlight %}
