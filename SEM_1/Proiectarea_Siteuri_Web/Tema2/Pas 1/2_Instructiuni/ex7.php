<html>
<head>
    <title> Instructiunea repetitive imbricate</title>
</head>
<body>
<form action="" method="POST">
    A: <input type="text" name="a"/>
    <input type="submit" name="submit"/>
</form>
<?php
if (isset($_POST['submit'])) {
    $n = trim($_POST['a']);
    echo "<table border=\"1\">";
    for ($i = 1; $i <= $n; $i++) {
        echo "<tr> ";
        for ($j = 1; $j <= $n; $j++) {
            echo "<td>";
            echo($i * $j);
            echo "</td> ";
        }
        echo "</tr> ";
    }
    echo "</table>";
} ?></body>
</html>