<!DOCTYPE html>
<html>
<head>
	<meta charset = "utf-8">
</head>
<body>
	<?php
  	$id = $_GET["id"];
		$password = $_GET["password"];
		if($id == "전민규"){
			if($password == "1111"){
				echo "당신은 주인님이 맞습니다.";
			}
			else{
				echo "당신은 주인님이 아닙니다.";
			}
		 }
		else{
			echo "당신은 주인님이 아닙니다.";
		 }
	 ?>
</body>
</html>
