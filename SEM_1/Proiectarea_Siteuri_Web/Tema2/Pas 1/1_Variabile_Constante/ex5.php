<?php $an = date("Y"); ?>
    An urmator:
<?php echo($an + 1); ?>
    <br/>
<?php $an = 2021;
echo "An: <b>$an</b> <br/>";
$an = ($an + 1);
echo "An: <b>$an</b>"; ?>
    <br/>
<?php /* Conversie EUR la DKK */
$rate = 7.5;
$euro = 100;
echo "Pentru <b>$euro</b> EUR, se primeste";
$moneda = ($euro * $rate); // înmulţire!
echo "<b>$moneda</b> DKK."; ?>
    <br/>
<?php /* Conversie DKK la EUR */
$rate = 7.5;
$moneda = 100;
echo "Pentru <b>$moneda</b> EUR, se primeste";
$euro = ($moneda / $rate); // împărţire!
echo "<b>$euro</b> DKK."; ?>
    <br/>
<?php /* Conversie DKK la EUR */
$rate = 7.5;
$moneda = 100;
echo "Pentru <b>$moneda</b> EUR, se primeste";
$euro = ($moneda / $rate); // împărţire!
$rotunjire = round($euro);
echo "<b>$rotunjire</b> DKK."; ?>
    <br/>
<?php $x = 2;
$y = 5;
$rezultat = ((1 + (2 - $x)) * ($y / 2));
echo "Rezultatul este: <b>$rezultat</b>";
?>
    <br/>
<?php $x = 7;
echo " 'x' este: <b>$x</b>";
echo "<p/>";
$x++;
echo "'x' este: <b>$x</b>";
?>
    <br/>
<?php
$x = 1;
$y = 2;
$rezultat = ($x > $y);
echo "Rezultatul este: <b>$rezultat</b>";
?>