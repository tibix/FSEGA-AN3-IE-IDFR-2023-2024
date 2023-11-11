<html>
<head>
    <title> Schimbarea tipului variabilelor prin casting</title>
</head>
<body>
<?php
$test = 9.8; //declarare cu atribuire
$casting = (double)$test;
echo gettype($casting);//double
echo " ";
echo "este $casting <br>";//afiseaza:9.8
$casting = (string)$test;
echo gettype($casting);//string

echo " ";
echo "este $casting <br>";//afiseaza:9.8
$casting = (integer)$test;
echo gettype($casting);//integer
echo " ";
echo "este $casting <br>";//afiseaza:9
$casting = (double)$test;
echo gettype($casting);//double
echo " ";
echo "este $casting <br>";//afiseaza:9
$casting = (boolean)$test;
echo gettype($casting);//boolean
echo " ";
echo "este $casting <br>";//1
echo "<hr>";
echo "Tipul variabilei originale este:";
echo gettype($test);//double
echo " ";
echo "Valoarea variabilei initiale este: $test";//neschimbata 9.8
?>
</body>
</html>