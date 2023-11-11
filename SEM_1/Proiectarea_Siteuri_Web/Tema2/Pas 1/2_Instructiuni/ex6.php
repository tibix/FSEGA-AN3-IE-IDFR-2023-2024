<html>
<head>
    <title>Calculul lui n! </title>
</head>
<body>
<form action="" method="POST">
    A: <input type="text" name="a"/>
    <input type="submit" name="submit"/>
</form>
<?php
//Determinarea factorialului
if (isset($_POST['submit'])) {
    $n = trim($_POST['a']);
//Calculul factorialul lui n
    $i = 1;
    $fact = 1;
    do {
        $fact = $fact * $i;
        $i++;
    } while ($i <= $n);
    echo "Rezultatul lui n! este: $fact";
} ?>
</body>
</html>