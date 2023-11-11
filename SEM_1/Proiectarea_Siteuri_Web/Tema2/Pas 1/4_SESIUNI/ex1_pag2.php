<html>
<head><title>Exemplu de sesiune</title></head>
<body>
<?php
session_start();
$_SESSION['Nume2'] = "Pop";
$_SESSION['Prenume2'] = "Ioan";
$_SESSION['Varsta'] = 39;
?>
<a href="ex1_pag3.php">pagina spre care se trimit variabilele de sesi-une</a>
</body>
</html>