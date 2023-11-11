<html>
<head><title>Exemplu de sesiune</title></head>
<body>
<?php
session_start();
echo $_SESSION['Nume'] . " ";
echo $_SESSION['Prenume'] . "<br />";
echo $_SESSION['Nume2'] . ' ';
echo $_SESSION['Prenume2'] . " ";
echo $_SESSION['Varsta'];
unset($_SESSION['Nume']);
unset($_SESSION['Prenume']);
unset($_SESSION['Nume2']);
unset($_SESSION['Prenume2']);
unset($_SESSION['Varsta']);
session_destroy();
?>
</body>
</html>