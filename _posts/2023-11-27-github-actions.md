---
title:  Github actions - budowanie i dostarczenie
tags:
  - github
  - actions
  - ftp
  - jekyll
  - devops
---
Poniżej znajdziecie kompletną definicję `wokflow` dla gthub actions, która pozwoli Wam zbudować serwis oparty na Jekyll, 
oraz wyśle uzyskane artefakty na serwer ftp, w tym przypadku SFTP.

Zanim zaczniemy niezbędne jest zdefiniowanie 3 sekretów w ustawieniach projektu. W moim przypadku są to `ftp_url`, `ftp_user`, `ftp_password`.
Ustawiamy je w `<projekt>/settings/secrets/actions`.

Sam workflow składać się będzie z dwóch etapów: budowania oraz deploymentu

{% highlight yaml %}
name: Deploy Jekyll with GitHub Pages dependencies preinstalled
on:
  push:
    branches: [master]

  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  # Build job
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Setup Pages
        uses: actions/configure-pages@v3
      - name: Build with Jekyll
        uses: actions/jekyll-build-pages@v1
        with:
          source: ./
          destination: ./_site
          
      - name: Remove old artifact
        run: rm -rf /home/runner/work/strona.tgz
        
      - name: Create archive with build result
        run: tar -cvzf /home/runner/work/strona.tgz ./_site
  
      - name: Upload artifact
        uses: actions/upload-artifact@v2
        with:
          name: strona
          path: /home/runner/work/strona.tgz

  deploy_ftp:
    needs: ['build']
    runs-on: ubuntu-latest
    steps:
    - name: Install lftp
      run: |
        sudo apt install lftp -y
    
    - name: Download artifacts
      uses: actions/download-artifact@v2
      with:
        name: strona

    - name: Extract and flatten
      run: tar zxvf strona.tgz --strip-components 2

    - name: ftp-action
      uses: pressidium/lftp-mirror-action@v1
      with:
        # SFTP credentials
        host: ${{ secrets.ftp_url }}
        user: ${{ secrets.ftp_user }}
        pass: ${{ secrets.ftp_pass }}
        # lftp settings
        onlyNewer: true
        settings: 'sftp:auto-confirm=yes'
        # Mirror command options
        localDir: '.'
        remoteDir: 'www/'
        reverse: true
        ignoreFile: '.git'
        options: '--verbose'

{% endhighlight %}

Powyższy kod zbuduje raz jeszcze stronę opartą na Jekyll, przygotuje artefakt oraz wykorzysta go jako źródło danych do przesłania ich na serwer ftp.
Warto zaznaczyć, że kolejne uruchomienia akcji będą skutkować aktualizacją zawartości na serwerze ftp.