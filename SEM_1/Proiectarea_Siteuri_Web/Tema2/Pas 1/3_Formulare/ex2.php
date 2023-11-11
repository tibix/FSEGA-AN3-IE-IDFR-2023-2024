<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Exemplu de Radio Buttons in PHP</title>
    </style>
</head>
<body>
<div class="container my-5">
    <form action="" method="post" class="mb-3">
        <label>
            <b> Alegeti una din Universitatile de mai jos:</b>
        </label>
        <br/>
        <label>
            <input type="radio" name="radio" value="UBB">UBB
            <span class="select"></span>
        </label>
        <br/>
        <label>
            <input type="radio" name="radio" value="UTCN">UTCN
            <span class="select"></span>
        </label>
        <br/>
        <label>
            <input type="radio" name="radio" value="USAMV">USAMV
            <span class="select"></span>
        </label>
        <br/>
        <input type="submit" name="submit" value="Valori">
    </form>
    <?php
    if (isset($_POST['submit'])) {
        if (!empty($_POST['radio'])) {
            echo ' ' . $_POST['radio'];
        } else {
            echo 'Alegeti valoare.';
        }
    }
    ?>
</div>
</body>
</html>