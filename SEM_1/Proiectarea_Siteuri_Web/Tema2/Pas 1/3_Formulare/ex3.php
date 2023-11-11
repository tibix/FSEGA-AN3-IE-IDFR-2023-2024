<!doctype html>
<html lang="ro">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Selectare multiplă în PHP</title>
</head>
<body>
<div class="container my-5">
    <form action="" method="post" class="mb-3">
        <p><b>Alege una/mai multe din opțiunile următoare</b></p>
        <p>
            <select name="Fructe[]" multiple>
                <option value="Mar">Mar</option>
                <option value="Banana">Banana</option>
                <option value="Ananas">Ananas</option>
                <option value="Zemeura">Zmeura</option>
                <option value="Capsuni">Capsuni</option>
            </select>
        </p>
        <p>
            <input type="submit" name="submit" value="Alege opțiuni">
        </p>
    </form>
    <p>
        <?php
        echo "Rezultat selectie </br>";
        if (isset($_POST['submit'])) {
            if (!empty($_POST['Fructe'])) {
                foreach ($_POST['Fructe'] as $selected) {
                    echo ' ' . $selected;
                }
            } else {
                echo 'Sa se selecteze o valuare.';
            }
        }
        ?>
    </p></div>
</body>
</html>