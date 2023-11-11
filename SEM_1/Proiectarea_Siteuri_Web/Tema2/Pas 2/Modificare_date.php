<?php // connectare bazadedate
include("Conectare.php");
//Modificare datelor
// se preia id din pagina vizualizare
if (!empty($_POST['id'])) {
    if (isset($_POST['submit'])) { // verificam daca id-ul din URL este unul valid
        if (is_numeric($_POST['id'])) { // preluam variabilele din URL/form
            $id = $_POST['id'];
            $nume = htmlentities($_POST['nume'], ENT_QUOTES);
            $prenume = htmlentities($_POST['prenume'], ENT_QUOTES);
            $an = htmlentities($_POST['an'], ENT_QUOTES);
            $grupa = htmlentities($_POST['grupa'], ENT_QUOTES);
            // verificam daca numele, prenumele, an si grupa nu sunt goale
            if ($nume == '' || $prenume == '' || $an == '' || grupa == '') { // daca sunt goale afisam mesaj de eroare
                echo "<div> ERROR: Completati campurile obligatorii!</div>";
            } else { // daca nu sunt erori se face update
                if ($stmt = $mysqli->prepare("UPDATE datepers SET nume=?,prenume=?,an=?, grupa=? WHERE idstudent='" . $id . "'")) {
                    $stmt->bind_param("ssss", $nume, $prenume, $an, $grupa);
                    $stmt->execute();
                    $stmt->close();
                }// mesaj de eroare in caz ca nu se poate face update
                else {
                    echo "ERROR: nu se poate executa update.";
                }
            }
        } // daca variabila 'id' nu este valida, afisam mesaj de eroare
        else {
            echo "id incorect!";
        }
    }
} ?>
<html>
<head>
    <title> <?php if ($_GET['id'] != '') {
            echo "Modificare inregistrare";
        } ?></title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head>
<body>
<h1>
    <?php if ($_GET['id'] != '') {
        echo "Modificare Inregistrare";
    } ?></h1>
<?php if ($error != '') {
    echo "<div style='padding:4px; border:1px solid red; color:red'>" . $error . "</div>";
} ?>
<form action="" method="post">
    <div>
        <?php if ($_GET['id'] != '') { ?>
        <input type="hidden" name="id" value="<?php echo $_GET['id']; ?>"/>
        <p>ID: <?php echo $_GET['id'];
            if ($result = $mysqli->query("SELECT * FROM datepers where idstudent='" . $_GET['id'] . "'")){
            if ($result->num_rows > 0){
            $row = $result->fetch_object(); ?>
        </p><strong>Nume: </strong>
        <input type="text" name="nume" value="<?php echo $row->nume; ?>"/><br/>
        <strong>Prenume: </strong>
        <input type="text" name="prenume" value="<?php echo $row->prenume; ?>"/><br/>
        <strong>An: </strong>
        <input type="text" name="an" value="<?php echo $row->an; ?>"/><br/>
        <strong>Grupa: </strong>
        <input type="text" name="grupa" value="<?php echo $row->grupa;
        }
        }
        } ?>"/>
        <br/>
        <input type="submit" name="submit" value="Submit"/>
        <a href="Vizualizare_date.php">Index</a>
    </div>
</form>
</body>
</html>
