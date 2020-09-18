var current = 0;
function next() {
    if (current < 3)
        current++;
    var i = 0;
    $('.progressBar li').each(function (i) {
        if (i == current) {
            $(this).addClass("active");
            return false;
        }
        i++;
    });
    i = 0;
    $('.tab-register').each(function (i) {
        if (i == current) {
            $(this).removeClass("d-none");
        }
        else {
            $(this).addClass("d-none");
        }
        i++;
    });
    window.scrollTo(0, 0);
}

function prev() {
    if (current > 0)
        current--;
    var i = 0;
    $('.progressBar li').each(function (i) {

        if (i <= current) {
            $(this).addClass("active");
        }
        else {
            $(this).removeClass("active");
        }
        i++;
    });
    i = 0;
    $('.tab-register').each(function (i) {
        if (i == current) {
            $(this).removeClass("d-none");
        }
        else {
            $(this).addClass("d-none");
        }
        i++;
    });
    window.scrollTo(0, 0);
}