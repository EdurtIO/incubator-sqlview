UserRegister = function () {

    let initValidator = function () {
        $('#userRegister').submit(function (e) {
            e.preventDefault();
            let username = $('#userRegister > #username').val();
            let password = $('#userRegister > #password').val();
            let re_password = $('#userRegister > #re-password').val();
            const json = {
                'username': username,
                'password': password,
                're-password': re_password
            }
            $.ajax({
                type: "POST",
                dataType: "json",
                url: '/api/v1/user/register',
                data: json,
                success: function (data) {
                    console.log(data)
                    if (data.status != 'SUCCESS') {
                        alert(data.message)
                        return false
                    } else {

                    }
                },
                error: function (data) {
                    console.log("error:" + data.responseText);
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