<html>
<body>
<?php 
	echo "Hello";
	$command = escapeshellcmd('./test.py');
	$output = shell_exec($command);
	echo $output;

?>
</body>
</html>