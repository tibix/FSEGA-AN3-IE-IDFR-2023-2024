<html>
<head>
    <title> Instructiunea switch...case. </title>
</head>
<body>
<form action="" method="POST">
    Nr: <input type="text" name="nr"/>
    <input type="submit" name="submit"/>
</form>
<?php
if (isset($_POST['submit'])) {
    switch (trim($_POST['nr'])) {
        case 1:
            echo "Luni";
            break;
        case 2:
            echo "Marti";
            break;
        case 3:
            echo "Miercuri";
            break;
        case 4:
            echo "Joi";
            break;
        case 5:
            echo "Vineri";
            break;
        case 6:
            echo "Sambata";
            break;
        case 7:
            echo "Duminica";
            break;
        default:
            echo "Nu este numar echivalent cu 0 zi din saptamana";
    }
} ?>
</body>
</html>