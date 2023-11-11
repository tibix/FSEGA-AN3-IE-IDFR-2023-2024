<?php

/*** mysql hostname ***/
$hostname = 'localhost';
/*** mysql username ***/
$username = 'root';
/*** mysql password ***/
$password = '';
/*** baza de date ***/
$db = 'student';
/*** se creaza un obiect mysqli ***/
$mysqli = new mysqli($hostname, $username, $password,$db);
/* se verifica daca s-a realizat conexiunea */
if(!mysqli_connect_errno())
{
    echo 'Connectat la baza de date: '. $db;
// $mysqli->close();
}
else
{
    echo 'Nu se poate connecta';
    exit();
}
?>