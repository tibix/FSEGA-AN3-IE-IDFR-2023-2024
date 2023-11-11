<?php

session_start();
if (isset($_POST['Inregistrare'])) {
    $_SESSION['nume'][] = $_POST['nume'];
    $_SESSION['prenume'][] = $_POST['prenume'];
    $_SESSION['nota1'][] = $_POST['nota1'];
    $_SESSION['nota2'][] = $_POST['nota2'];
}
?>
<html>
<head>
    <title>Situatie elevi</title>
</head>
<body>
<div id="Layer3" style="position:absolute; left:119; top:205; width:881; height:739; z-index:2"
     align="center">
    <table width="665" border="0" cellpadding="5" cellspacing="0">
        <caption valign="top">
            <table width="660" bgcolor="#FFFF00" cellpadding=0 cellspacing=0 border=0>
                <tr>
                    <td align="center" height="15">
                        <font size="5" color="#0000FF">
                            <b>DATE ELEVI </b> </font>
                    </td>
                </tr>
            </table>
        </caption>
        <table cellpadding=5 cellspacing=0 border=0 width="75%">
            <form method="post" action="">
                <tr>
                    <td><font face="Courier" size="2">
                            <b>Nume:</b></font>
                    </td>
                    <td>
                        <input name="nume" size=20 maxlength=50>
                    </td>
                </tr>
                <tr>
                    <td>
                        <b>Prenume:</b>
                    </td>
                    <td>
                        <input name="prenume" size=20 maxlength=50>
                    </td>
                </tr>
                <tr>
                    <td>
                        <b>Nota la matematica:</b>
                    </td>
                    <td>
                        <input name="nota1" size=20 maxlength=2>
                    </td>
                </tr>
                <tr>
                    <td>
                        <b>Nota romana:</b>
                    </td>
                    <td>
                        <input name="nota2" size=20 maxlength=20>
                    </td>
                </tr>
                <tr>
                    <td width="142">
                        <input type="submit" name="Inregistrare" value="Inregistrare">
                    </td>
                </tr>
            </form>
        </table>
        <?php
        if (isset($_POST['Inregistrare'])){
        $nr_elevi = count($_SESSION['nume']); ?>
        <table cellpadding=5 cellspacing=0 border=0 width="75%">
            <tr>
                <th>Nume</th>
                <th>Prenume</th>
                <th>Nota matematica</th>
                <th>Nota romana</th>
                <th>Media</th>
            </tr>
            <?php
            for ($i = 0;
            $i < $nr_elevi;
            $i++){ ?>
            <tr>
                <td> <?php print $_SESSION['nume'][$i]; ?> </td>
                <td> <?php print $_SESSION['prenume'][$i]; ?> </td>
                <td> <?php print $_SESSION['nota1'][$i]; ?> </td>
                <td> <?php print $_SESSION['nota2'][$i]; ?> </td>
                <?php
                $nr1 = (int)($_SESSION['nota1'][$i]);
                $nr2 = (int)($_SESSION['nota2'][$i]);
                $media = (($nr1 + $nr2) / 2);
                ?>
                <td><?php print $media;
                    }
                    } ?></td>
            </tr>
        </table>
</body>
</html>