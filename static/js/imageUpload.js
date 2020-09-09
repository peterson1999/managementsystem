$(document).ready(function () {
  if (window.File && window.FileList && window.FileReader) {
    $("#imageInput").on("change", function (e) {
      var files = e.target.files,
        filesLength = files.length;
      if (filesLength > 3) {
        $(".imgValidation").css("display", "block");
      } else {
        $(".imgValidation").css("display", "none");
        for (var i = 0; i < filesLength; i++) {
          var f = files[i];
          var fileReader = new FileReader();
          fileReader.onload = function (e) {
            var file = e.target;
            $(
              '<span class="imgContainer">' +
                '<img class="imgThumbnail" src="' +
                e.target.result +
                '" title="' +
                file.name +
                '"/>' +
                "</span>"
            ).insertAfter("#imageInput");
          };
          fileReader.readAsDataURL(f);
        }
      }
    });
  } else {
    alert("File not supported.");
  }
});
