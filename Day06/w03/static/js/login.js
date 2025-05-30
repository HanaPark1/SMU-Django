if ('{{ msg }}' == 1) {
    alert("환영합니다. 로그인 성공하였습니다.");
    location.href = "/";
} else if ('{{ msg }}' == -1) {
    alert("패스워드를 다시 확인해 주세요.");
} else {
    alert("아이디를 다시 확인해 주세요.");
}