<html>
<head>
    <title>Exemplu variabile PHP</title>
</head>
<body>
<?php
$a = 5;
$aduna = $a + 5;

print "Rezultatul adunarii este: $aduna";
?>
<h2>Alte exemple</h2>

<?php
$nume = "Unchiul Vanea";
$nascut = 1961;
$tara = "Romania";
echo "Buna ziua, numele meu este: <b>";
echo $nume;
echo "</b>";
echo "<p/>";
echo "Sunt un personaj de roman: <br/>";
echo "<em>";
echo $tara;
echo "</em>";
echo "<p/>";
echo "Eu am<b>";
echo(2023 - $nascut);
echo "</b> de ani.";
?>
</body>
</html>

