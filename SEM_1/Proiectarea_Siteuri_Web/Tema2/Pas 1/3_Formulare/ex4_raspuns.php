<html>
<head>
    <title>un formular cu select</title>
</head>
<body>
<?php
echo "<p>Bine ati venit<b>$_POST[user]</b></p>";
echo "<p>Adresa introdusa este:<br><b>$_POST[adresa]<b></p>";
echo "<p>Produsele alese:<br>";
if (!empty($_POST['produs'])) //testam existenta variabilei $_POST[produs]
{
    echo "<ul>";
    foreach ($_POST['produs'] as $value) {
        echo "<li>$value";
    }
    echo "</ul>";
} ?>
</body>
</html>