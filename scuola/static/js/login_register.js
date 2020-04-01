$("index.temp.html").ready(function () {
    $('#register').on('click', function() {
    $.ajax({
        type: "GET",
        url: "register",
        data: {
            name : $("#name").val(),
            surname : $('#surname').val(),
            email : $('#email').val(),
            pwd : $('#password').val(),
            pwd2 : $('#repeat_password').val(),
            csrfmiddlewaretoken : "{{ csrf_token }}"
        },
        success: function (response) {
            console.log(response);
            
            if(response['name'] == 0){
                $("#errorName").text("Please enter your name");
                $("#errorName").css('color', 'red');
                $("#name").removeClass('is-valid');
                $("#name").addClass('is-invalid');
            }
            else{
                $("#errorName").text("");
                $("#name").addClass('is-valid');
                $("#name").removeClass('is-invalid');
            }
            if(response['surname'] == 0){
                $("#errorSurname").text("Please enter your surname");
                $("#errorSurname").css('color', 'red');
                $("#surname").removeClass('is-valid');
                $("#surname").addClass('is-invalid');
            }
            else{
                $("#errorSurname").text("");
                $("#surname").addClass('is-valid');
                $("#surname").removeClass('is-invalid');
            }
            if(response['mail'] == 0){
                $("#errorUsername").text("Please enter valid e-mail or already registerd");
                $("#errorUsername").css('color', 'red');
                $("#email").removeClass('is-valid');
                $("#email").addClass('is-invalid');
            }
            else{
                $("#errorUsername").text("e-mail is valid");
                $("#errorUsername").css('color', 'green');
                $("#email").addClass('is-valid');
                $("#email").removeClass('is-invalid');
            }
            if(response['password'] != 0){
                $("#errorPassword").text("Passwords are matched!");
                $("#errorPassword").css('color', 'green');
                $("#password, #repeat_password").removeClass('is-invalid');
                $("#password, #repeat_password").addClass('is-valid');
            }
            else{
                $("#errorPassword").text("Please check your passwords!");
                $("#errorPassword").css('color', 'red');
                $("#password, #repeat_password").addClass('is-invalid');
                $("#password, #repeat_password").removeClass('is-valid');
            }
            if(response['success'] != 0){
                alert(response['success']);
                window.history.back();
            }
            else{
                console.log("retry");
            }
        },
        error: function (response){
            console.log("error");
            console.error(response);
        }
    });
	});
});