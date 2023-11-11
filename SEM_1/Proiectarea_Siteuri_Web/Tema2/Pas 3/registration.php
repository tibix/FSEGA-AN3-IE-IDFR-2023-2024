<?php
include_once 'include/class.user.php';
$user = new User();
// Verific daca user este login sau nu
if (isset($_REQUEST['submit'])) {
    extract($_REQUEST);
    $register = $user->reg_user($fullname, $uname, $upass, $uemail);
    if ($register) {
// Inregistrare Success
        echo 'Registration successful <a href="login.php">Click here</a> pt login';
    } else {
// Inregistrare esec
        echo "Inregistrare esec. Email sau Username exita";
    }
}
?>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1"/>
Register
<style><!--
    #container {
        width: 400px;
        margin: 0 auto;
    }

    --></style>
<script type="text/javascript" language="javascript">
    function submitreg() {
        var form = document.reg;
        if (form.name.value == "") {
            alert(" Introdu name.");
            return false;
        } else if (form.uname.value == "") {
            alert(" Introdu username.");
            return false;
        } else if (form.upass.value == "") {
            alert(" Introdu password.");
            return false;
        } else if (form.uemail.value == "") {
            alert("Introdu email.");
            return false;
        }
    }
</script>
<div id="container">
    <h1>Inregistrare nou utilizator</h1>
    <form action="" method="post" name="reg">
        <table>
            <tbody>
            <tr>
                <th>Nume complet:</th>
                <td><input type="text" name="fullname" required=""/></td>
            </tr>
            <tr>
                <th>Nume utilizator:</th>
                <td><input type="text" name="uname" required=""/></td>
            </tr>
            <tr>
                <th>Email:</th>
                <td><input type="text" name="uemail" required=""/></td>
            </tr>
            <tr>
                <th>Password:</th>
                <td><input type="password" name="upass" required=""/></td>
            </tr>
            <tr>
                <td></td>
                <td><input onclick="return(submitreg());" type="submit" name="submit"
                           value="Register"/></td>
            </tr>
            <tr>
                <td></td>
                <td><a href="login.php">Deja inregistrat! Click Here!</a></td>
            </tr>
            </tbody>
        </table>
    </form>
</div>
<?php
include_once 'include/class.user.php';
$user = new User();
// Verific daca user este login sau nu
if (isset($_REQUEST['submit'])) {
    extract($_REQUEST);
    $register = $user->reg_user($fullname, $uname, $upass, $uemail);
    if ($register) {
// Inregistrare Success
        echo 'Registration successful <a href="login.php">Click here</a> pt login';
    } else {
// Inregistrare esec
        echo "Inregistrare esec. Email sau Username exita";
    }
}
?>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1"/>
Register
<style><!--
    #container {
        width: 400px;
        margin: 0 auto;
    }

    --></style>
<script type="text/javascript" language="javascript">
    function submitreg() {
        var form = document.reg;
        if (form.name.value == "") {
            alert(" Introdu name.");
            return false;
        } else if (form.uname.value == "") {
            alert(" Introdu username.");
            return false;
        } else if (form.upass.value == "") {
            alert(" Introdu password.");
            return false;
        } else if (form.uemail.value == "") {
            alert("Introdu email.");
            return false;
        }
    }
</script>
<div id="container">
    <h1>Inregistrare nou utilizator</h1>
    <form action="" method="post" name="reg">
        <table>
            <tbody>
            <tr>
                <th>Nume complet:</th>
                <td><input type="text" name="fullname" required=""/></td>
            </tr>
            <tr>
                <th>Nume utilizator:</th>
                <td><input type="text" name="uname" required=""/></td>
            </tr>
            <tr>
                <th>Email:</th>
                <td><input type="text" name="uemail" required=""/></td>
            </tr>
            <tr>
                <th>Password:</th>
                <td><input type="password" name="upass" required=""/></td>
            </tr>
            <tr>
                <td></td>
                <td><input onclick="return(submitreg());" type="submit" name="submit"
                           value="Register"/></td>
            </tr>
            <tr>
                <td></td>
                <td><a href="login.php">Deja inregistrat! Click Here!</a></td>
            </tr>
            </tbody>
        </table>
    </form>
</div>
