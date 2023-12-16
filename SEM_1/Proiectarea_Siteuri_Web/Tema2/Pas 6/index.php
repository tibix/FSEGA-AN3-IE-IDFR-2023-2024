<?php
session_start();

// Includeți funcții și conectați-vă la baza de date folosind PDO MySQL
include 'conectare.php';
$pdo = pdo_connect_mysql();

// home este pgina start
$page = isset($_GET['page']) && file_exists($_GET['page'] . '.php') ? $_GET['page'] : 'home';

// Includeți și afișați pagina solicitată
include $page . '.php';

?>

