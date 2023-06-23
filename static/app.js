$(function() {
  $('#submit').click(function() {
    var $btn = $(this);
    var form_data = new FormData($('#uploadForm')[0]);
    $.ajax({
      type: 'POST',
      url: '/predict',
      data: form_data,
      contentType: false,
      processData: false,
      beforeSend: function() {
        $btn.prop('disabled', true);
        $btn.html(
          `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...`
        );
      },
      complete: function() {
        $btn.removeAttr('disabled');
        $btn.html('Submit');
      },
      dataType: 'json'
    }).done(function(res, textStatus, jqXHR) {
      $('#hasil').show();
      $('#hasil').html(res.data.join(' '));
    }).fail(function(data) {
      console.error(data);
    });
  });

  $('#submit-digit').click(function() {
    var $btn = $(this);
    var form_data = new FormData($('#uploadFormDigit')[0]);
    $.ajax({
      type: 'POST',
      url: '/predict_digit',
      data: form_data,
      contentType: false,
      processData: false,
      beforeSend: function() {
        $btn.prop('disabled', true);
        $btn.html(
          `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...`
        );
      },
      complete: function() {
        $btn.removeAttr('disabled');
        $btn.html('Submit');
      },
      dataType: 'json'
    }).done(function(res, textStatus, jqXHR) {
      $('#hasildigit').show();
      $('#hasildigit').html(res.data.join(' '));
    }).fail(function(data) {
      console.error(data);
    });
  });
});

function gambar1Selected(input) {
  if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
          $('#gambar1').attr('src', e.target.result);
      }
      reader.readAsDataURL(input.files[0]);
  }
}

function gambar2Selected(input) {
  if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
          $('#gambar2').attr('src', e.target.result);
      }
      reader.readAsDataURL(input.files[0]);
  }
}