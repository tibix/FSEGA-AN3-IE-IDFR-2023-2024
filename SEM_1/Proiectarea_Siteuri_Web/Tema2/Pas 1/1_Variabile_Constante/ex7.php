<html>
<head><title>Exemplu variabile PHP </title></head>
<body>
<h2> Variabile globale</h2>
<?php
$ipaddress = $_SERVER['REMOTE_ADDR'];
echo "IP Address este " . $ipaddress;
$ipaddress = getenv("REMOTE_ADDR");
echo "Your IP Address este: " . $ipaddress;
echo "<br/>";
$agent = $_SERVER['HTTP_USER_AGENT'];
echo "Browser este: " . $agent;
echo "<br/>";
$numeserver = $_SERVER['SERVER_NAME'];
echo "Nume server este: " . $numeserver;
echo "<br/>";
$scriptname = $_SERVER['SCRIPT_NAME'];
echo "Nume script este: " . $scriptname;
echo "<br/>";
echo "<br/>";
echo "<br/>";
echo "<b>Afisare variabile globale pe parte de Server</b><br/>";
print_r($_SERVER);
?>
</body>
</html>