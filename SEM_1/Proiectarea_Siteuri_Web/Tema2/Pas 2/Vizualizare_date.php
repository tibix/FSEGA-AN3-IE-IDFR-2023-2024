<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
    <title>Vizualizare Inregistrari</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head>
<body>
<h1>Inregistrarile din tabela datepers</h1>
<p><b>Toate inregistrarile din datepers</b</p>
<?php
// connectare bazadedate
include("conectaremi.php");
// se preiau inregistrarile din baza de date
if ($result = $mysqli->query("SELECT * FROM datepers ORDER BY idstudent "))
{ // Afisare inregistrari pe ecran
    if ($result->num_rows > 0)
    {
// afisarea inregistrarilor intr-o table
        echo "<table border='1' cellpadding='10'>";
// antetul tabelului
        echo "<tr><th>ID</th><th>Nume</th><th>Prenume</th><th>an</th><th>grupa</th><th></th><th></th></t
r>";
        while ($row = $result->fetch_object())
        {
// definirea unei linii pt fiecare inregistrare
            echo "<tr>";
            echo "<td>" . $row->idstudent . "</td>";
            echo "<td>" . $row->nume . "</td>";
            echo "<td>" . $row->prenume . "</td>";
            echo "<td>" . $row->an . "</td>";
            echo "<td>" . $row->grupa . "</td>";
            echo "<td><a href='modificamysqli.php?id=" . $row->idstudent .
                "'>Modificare</a></td>";
            echo "<td><a href='stergemsqli.php?id=" . $row->idstudent .
                "'>Stergere</a></td>";
            echo "</tr>";
        }
        echo "</table>";
    }
// daca nu sunt inregistrari se afiseaza un rezultat de eroare
    else
    {
        echo "Nu sunt inregistrari in tabela!";
    }
}
// eroare in caz de insucces in interogare
else
{ echo "Error: " . $mysqli->error(); }
// se inchide
$mysqli->close();
?>
<a href="Inserare_date.php">Adaugarea unei noi inregistrari</a>
</body>
</html>