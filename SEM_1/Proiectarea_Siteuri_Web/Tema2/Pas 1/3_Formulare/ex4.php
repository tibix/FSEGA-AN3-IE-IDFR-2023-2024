<html>
<head>
    <title>un formular cu select</title>
</head>
<body>
<form action="ex4_raspuns.php" method="POST">
    <p><strong>Name:</strong><br>
        <input type="text" name="user"></p>
    <p><strong>Adresa:</strong><br>
        <textarea name="adresa" rows="5" cols="40"></textarea></p>
    <p><strong>Selectati un produs:</strong></p>
    <select name="produs[]" multiple>
        <option value="casetofon">Casetofon</option>
        <option value="CD">CD</option>
        <option value="video">Video</option>
    </select>
    <p><input type="submit" value="send"></p>
</form>
</body>
</html>