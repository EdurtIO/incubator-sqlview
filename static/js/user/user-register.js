UserRegister = function () {

    let initValidator = function () {
        $('#userRegister').submit(function () {
            let username = $('#userRegister > #username').val();
            let password = $('#userRegister > password').val();
            let re_password = $('#userRegister > re-password').val();
            const json = {
                'username': username,
                'password': password
            }
            $.ajax({
                type: "POST",
                dataType: "json",
                url: '/user/register',
                data: json,
                success: function (data) {
                    alert(data);
                },
                error: function (data) {
                    // alert("error:" + data.responseText);
                }
            });
        });
    }

    let initEvent = function () {
        initValidator();
    }

    return {
        initEvent: initEvent
    }

}()