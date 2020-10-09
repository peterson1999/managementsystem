var current = 0;
$(document).ready(function () {
    $('#registerForm').validate({
        highlight: function (element) {
            $(element).addClass("formError");
            $('#' + element.id + '-error').addClass("formError");
            console.log(element.value);
        },
        unhighlight: function (element) {
            $(element).removeClass("formError");
            $('#' + element.id + '-error').removeClass("formError");
        },
        rules: {
            fName: "required",
            lName: "required",
            email: {
                required: true,
                email: true
            },
            password: {
                required: true,
                minlength: 6
            },
            confPassword: {
                required: true,
                minlength: 6,
                equalTo: "#password"
            },
            address: "required",
            city: "required",
            province: "required",
            zip: {
                required: true,
                number: true,
            },
            birthdate: "required",
            marStatus: "required",
            height: {
                required: true,
                min: 20 + Number.MIN_VALUE,
                max: 1000,
                number: true,
            },
            weight: {
                required: true,
                min: 1 + Number.MIN_VALUE,
                max: 300,
                number: true,
            },
            elemGrade: {
                min: 0,
                max: 100,
                number: true,
            },
            jhsGrade: {
                min: 0,
                max: 100,
                number: true,
            },
            shsGrade: {
                min: 0,
                max: 100,
                number: true,
            },
            collegeLvl: {
                min: 0,
                max: 5,
                digits: true,
            },
            postgradLvl: {
                min: 0,
                max: 5,
                digits: true,
            },
        },
        messages: {
            fName: "Please enter your first name.",
            lName: "Please enter your last name.",
            email: {
                required: "Please enter your email.",
            },
            password: {
                required: "Please enter your password.",
            },
            confPassword: {
                required: "Please enter your password again.",
                equalTo: "Your password must match with the password entered above."
            },
            address: "Please enter your address.",
            zip: {
                required: "Required.",
                number: "Please enter a valid ZIP Code."
            },
            height: {
                min: "Minimum height is at least {0} cm.",
                max: "Maximum height is {0} cm."
            },
            weight: {
                min: "Minimum weight is at least {0} kg.",
                max: "Maximum weight is {0} kg."
            }
        }
    })
});
function formValidate() {
    if ($('#registerForm').valid()) {
        next();
    }
    else {
        window.scrollTo(0, 0);
    }
}
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