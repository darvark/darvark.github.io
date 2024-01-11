---
title:  Instalacja TLF
tags:
  - github
  - tlf
  - radio
  - logger
  - contesting
---

Generalnie podstawowa instalacja TLF jest opisana w pliku README, ale postaram się tutaj streścić dostępne opcje.

1. **Instalacja przez menadżer pakietów
  Większość dystrybucji linuksa, które bazują na menadżerach pakietów posiada w swojej bazie gotowe paczki wraz z zależnościami, które gwarantują działające środowisko TLF wraz z aplikacjami pomocniczymi (cwdaemon, xplanet). Wystarczy wykonać polecenie:

- dla Fedora
  {% highlight bash %}
  sudo dnf install tlf
  {% endhighlight %}

- dla rodziny Debiana
  {% highlight bash %}
  sudo apt install tlf
  {% endhighlight %}

- dla rodziny ArchLinux
  {% highlight bash %}
  sudo pacman -S tlf
  {% endhighlight %}

Instalacja taka dużo ułatwia, ale nie zawsze dostarcza najnowszą wersję oprogramowania.

2. **Instalcja ze źródeł
Zanim przystąpimy do budowania prosto ze źródeł tlf musimy upewnić się, że mamy zainstalowane wymagane oprogramowanie. Tym wymaganym oprogramowaniem jest w zasadzie tylko bibliotek Hamlib - oraz jej pakiety developerskie (najczęściej z sufixem -dev albo -devel). Pakiety `sox, xplanet, cwdaemon, libcw` są pakietami opcjonalnymi, bez których TLF również będzie działać - chociaż w mocno ograniczony sposób. Pakiety te mogą być zainstalowane przez dostarczony z dystrybucją mendżer pakietów. 

{% highlight bash %}
sudo apt install autoconf libglib2.0-dev libhamlib-dev libncurses5-dev libtinfo-dev libxmlrpc-core-c3-dev
{% endhighlight %}

Aby zdobyć najnowszą wersję kody TLF wystarczy wykonać polecenie:

{% highlight bash %}
git clone https://github.com/Tlf/tlf.git
{% endhighlight %}

Pierwszym poleceniem jakie wykonamy będąc w folderze z kodem tlf jest `autoreconf -i`, a następnie `./configure`. Skrypt configure może przyjąć nastepujące dodatkowe parametry:

- --prefix=/usr - definiuje miejsce instalacji tlf - domyślnie `/usr/local/bin`
- --datadir=/usr/share - definiuje miejsce instalacji plików danych do tlf oraz przykładowych reguł zawodów - domyślnie `/usr/local/share/tlf`
- --enable-fldigi-xmlrpc - włącza obsługę komunikacji z aplikacją flrig
- --enable-pythn-plugins - włącza obsługę pluginów python

Kolejnym krokiem jest kompilacja źródeł oprogramowania poleceniem `make` oraz filanie instalacja poprzez `sudo make install`.

Po tych krokach powinniśmy być w stanie uruchomić tlf, a system wskazać lokalizację binarki (można to sprawdzić poleceniem `which tlf`)


To jak skonfigurować apliakcję do pracy w zaowdach i jak wygląda obsługa (klawiszologia) w następnych wpisach...
