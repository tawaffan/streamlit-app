$('#upload').click(function () {
    var formData = new FormData($('#upload-gambar-1')[0])
    $.ajax({
        type: 'POST',
        url: './ImageRecognition',
        data: formData,
        processData: false,
        contentType: false
    }).then((data) => {
        console.log(data);
    })
});

function fileSelected(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#gambar1').attr('src', e.target.result).width(150).height(200);
        }
        reader.readAsDataURL(input.files[0]);
    }
}