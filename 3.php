<!DOCTYPE html>
<html>
<head>
	<meta charset = "utf-8">
  <style media="screen">
    article{color : red; font-size : 50px}
  </style>
</head>
<body>
<article>
  <script type="text/javascript">
      password = prompt("비밀번호");
      if(password == 10){
        document.write("통과되셨습니다.");
      }
      else{
        document.write("잘 못 누르셨습니다.당신은 지금 112에 신고 되었습니다.");
        document.write("당신은 지금 1급기밀 보안문서의 비밀번호를 틀렸습니다.");
      }
  </script>
</article>
</body>
</html>
