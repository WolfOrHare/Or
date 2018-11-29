/*
 *
 * login-register modal
 * Autor: Creative Tim
 * Web-autor: creative.tim
 * Web script: #
 * 
 */
function showRegisterForm() {
    $('.loginBox').fadeOut('fast', function () {
        $('.registerBox').fadeIn('fast');
        $('.login-footer').fadeOut('fast', function () {
            $('.register-footer').fadeIn('fast');
        });
        $('.modal-title').html('注册');
    });
    $('.error').removeClass('alert alert-danger').html('');

}

function showLoginForm() {
    $('#loginModal .registerBox').fadeOut('fast', function () {
        $('.loginBox').fadeIn('fast');
        $('.register-footer').fadeOut('fast', function () {
            $('.login-footer').fadeIn('fast');
        });

        $('.modal-title').html('登录');
    });
    $('.error').removeClass('alert alert-danger').html('');
}

function openLoginModal() {
    showLoginForm();
    setTimeout(function () {
        $('#loginModal').modal('show');
    }, 230);

}

function openRegisterModal() {
    showRegisterForm();
    setTimeout(function () {
        $('#loginModal').modal('show');
    }, 230);

}

function loginAjax() {
    $('email').reset;
    email = $('#email').val();
    password = $('#password').val();
    // console.log(email + '---->' + password)
    $.post("/login_check/", {
            'email': email,
            'password': password,
        }, function (data) {
            if (data.msg === 'ok') {
                //登录成功
                location.href = '/index/' //跳转到成功页面
            } else if (data.msg === 'fail_user') {
                loginshakeModal();
            } else if (data.msg === 'fail_verify') {
                //验证码错误
                $('#errorMsg').show().text('亲！验证码错误！')
            }
        }
    );
}

function registerAjax() {
    $('reg_email').reset;
    reg_email = $('#reg_email').val();
    reg_password = $('#reg_password').val();
    exa_password = $('#password_confirmation').val();
    // console.log(reg_email + '---->' + reg_password + '---->' + exa_password)


    $.post("/register/", {
            'reg_email': reg_email,
            'reg_password': reg_password,
            'exa_password': exa_password,
        }, function (data) {
            if (data.msg === 'reg_ok') {
                //注册成功，跳转到主页,??????这里需要做优化，应该跳转到个人页面，完善个人信息？？？？？？？？？？？？？？？？？？
                location.href = '/index/' //跳转到成功页面
            } else if (data.msg === 'exa_fail_user') {
                //验证用户
                user_reg_shakeModal();
            } else if (data.msg === 'exa_fail_reg') {
                //验证密码输入是否一致
                pwd_reg_shakeModal();
            } else if (data.msg === 'exa_password') {
                pwd_null_shakeModal();
            } else if (data.msg === 'exa_fail_verify') {
                //验证码错误
                $('#errorMsg').show().text('')
            }
        }
    );
}
//提示并产生震动效果
function loginshakeModal() {

    $('#loginModal .modal-dialog').addClass('shake');
    $('.error').addClass('alert alert-danger').html("请输入正确的用户/密码！");
    $('input[type="password"]').val('');
    setTimeout(function () {
        $('#loginModal .modal-dialog').removeClass('shake');
    }, 1000);
}

function user_reg_shakeModal() {

    $('#loginModal .modal-dialog').addClass('shake');
    $('.error').addClass('alert alert-danger').html("email已经被使用!");
    $('input[type="password"]').val('');
    setTimeout(function () {
        $('#loginModal .modal-dialog').removeClass('shake');
    }, 1000);
}

function pwd_reg_shakeModal() {

    $('#loginModal .modal-dialog').addClass('shake');
    $('.error').addClass('alert alert-danger').html("密码验证失败!");
    $('input[type="password"]').val('');
    setTimeout(function () {
        $('#loginModal .modal-dialog').removeClass('shake');
    }, 1000);
}
function pwd_null_shakeModal() {

    $('#loginModal .modal-dialog').addClass('shake');
    $('.error').addClass('alert alert-danger').html("不允许注册！用户名或密码不允许为空！");
    $('input[type="password"]').val('');
    setTimeout(function () {
        $('#loginModal .modal-dialog').removeClass('shake');
    }, 1000);
}


   