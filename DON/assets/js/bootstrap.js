$(document).on('click', '#register', function (e) {
    e.preventDefault();

    console.log($('#name').val())
    $.ajax({
        type: 'POST',
        url: 'createUser',
        data: {
            name: $('#name').val()
        },
        success: function () {
            console.log("test");
        },
        error: function () {
            console.log("fail");
        }
    });
})