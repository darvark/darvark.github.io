---
title:  Dyplomy i Certyfikaty
tags:
  - ham
  - contest
  - radio
images:
  - _assets/wpx19-ssb.png
  - _assets/wpx19-ssb-cat.png
  - _assets/wpx20-ssb.png
  - _assets/wpx20-ssb.png
  - _assets/wpx21-ssb.png
  - _assets/wpx21-ssb-cat.png
  - _assets/wpx22-ssb.png
  - _assets/wpx22-ssb-cat.png
  - _assets/wpx22-cw.png
  - _assets/wpx22-cw-cat.png
  - _assets/wpx23-ssb.png
  - _assets/wpx23-ssb-cat.png
  - _assets/cqww21-ssb.png
  - _assets/cqww22-cw.png
  - _assets/cqww22-ssb.png
  - _assets/spdx20.pdf
  - _assets/spdx21.pdf
  - _assets/spdx23.pdf
  
---

Dyplomy oraz certyfikaty z zawodów krótkofalarskich.
Kliknij na zdięcie aby otworzyć w powiększeniu.

<div class="card-columns">
    {% for img in page.images %}
    <div class="card" data-toggle="modal" data-target="#exampleModal" data-img="{{ img }}">
        <img class="card-img-top" src="{{ img }}" />
    </div>
    {% endfor %}
</div>

<div class="modal fade" id="exampleModal">
  <div class="modal-dialog modal-lg modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-body">
        <img class="modal-img w-100" />
      </div>
    </div>
  </div>
</div>

<script type="text/javascript">
  $(document).ready(function() {
    $('#exampleModal').on('show.bs.modal', function (event) {
      var button = $(event.relatedTarget)
      var img = button.data('img')
      var modal = $(this)
      modal.find('.modal-img').attr('src', img)
    })
  })
</script>



