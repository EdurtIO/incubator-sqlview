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
                type: 'POST',
                url: '/api/v1/user/register',
                headers: {
                    'Content-Type': 'application/json'
                },
                data: JSON.stringify(json),
                success: function (data) {
                    if (data.status != 'SUCCESS') {
                        Qmsg.error(data.message);
                    } else {
                        Qmsg.success('Register Success! please login it!')
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