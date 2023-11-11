<?php
session_start(); ?>
<html>
<head><title>Exemplu de sesiune</title></head>
<?php
$_SESSION['Nume'] = "Ionescu";
$_SESSION['Prenume'] = "Laura";
?>
<a href="ex1_pag2.php">pagina spre care se trimit variabilele de sesi-une</a>
</html>