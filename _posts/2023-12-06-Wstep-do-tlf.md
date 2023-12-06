---
title:  Wstęp do tlf
tags:
  - github
  - tlf
  - radio
  - logger
  - contesting
---
Tm krótkim wpisem chcę zacząć małą serię dotyczącą bardzodobrego, choć wyjatkowo trudnego w obsłudze (szczególnie dla początkujących) programu jakim jest `TLF`. Kolejno przedstawię sam program, sposoby jego instalacji, konfiguracji i pokażę jak go wygodnie używać.

![TLF](assets/2023-12-06-Wstep-do-tlf/tlf1.png)

Sam `tlf` jest dość starym programem, bazującym na starym dosowym programie `TR-Log`. Obecnie aplikacja wspiera pracę w największych zawodach CQWW, CQ-WPX, ARRL-DX, ARRL-FD, PACC, oraz EU SPRINT. Jednocześnie umożliwia definiowane reguł pod mniejsze mniej popularne zawody krótkofalarskie.

`TLF` umożliwnia kluczowanie CW przy pomocy biblioteki `Hamlib` albo `cwdaemon`. (Te dwa aspekty opiszę w dalszej części). Komunikacja z transcieverem odbywa się  przez bibliotekę hamlib.

`TLF` pracuje w trybie konsoli (w oknie terminala), może pracować równie dobrze bez udziału systemu Xwindow (czy też Wayland). Wygląda w stylu retro może być mylący, ale jest to naprawdę współczesny i bardzo potężny logger, mogący obsługiwać stacje multi-multi czy też tzw. big gun.

Kolejno ukażą się wpisy:
- instalacja tlf oraz cwdaemon
- podstawowa konfiguracja
- praca z tlf - podstawy
- definiowanie własnych reguł zawodów