<?php
// Cantitățile de produse de afișat pe fiecare pagină
$num_products_on_each_page = 4;
// Pagina curentă, în adresa URL, va apărea ca index.php? Page = products & p = 1, index.php? Page =
products & p = 2, etc ..
$current_page = isset($_GET['p']) && is_numeric($_GET['p']) ? (int)$_GET['p'] : 1;
// Selectproduse ordonate dupa data adaugarii
$stmt = $pdo->prepare('SELECT * FROM products ORDER BY date_added DESC LIMIT ?,?');
// bindValue ne va permite să folosim întreg în instrucțiunea SQL, trebuie să folosim pentru LIMIT
$stmt->bindValue(1, ($current_page - 1) * $num_products_on_each_page, PDO::PARAM_INT);
$stmt->bindValue(2, $num_products_on_each_page, PDO::PARAM_INT);
$stmt->execute();
// Preluează produsele din baza de date și returnează rezultatul ca matrice
$products = $stmt->fetchAll(PDO::FETCH_ASSOC);
// Preluam numar total al produselor
$total_products = $pdo->query('SELECT * FROM products')->rowCount();
?>
<?=template_header('Produse')?>
<div class="products content-wrapper">
    <h1>Produse</h1>
    <p><?php echo $total_products?> Produse</p>
    <div class="products-wrapper">
        <?php foreach ($products as $product): ?>
            <a href="index.php?page=product&id=<?php echo $product['id']?>" class="product">
                <img src="imgs/<?php echo $product['img']?>" width="200" height="200" alt="<?php echo
                $product['name']?>">
                <span class="name"><?php echo $product['name']?></span>
                <span class="price">
 &dollar;<?php echo $product['price']?>
                    <?php if ($product['rrp'] > 0): ?>
                        <span class="rrp">&dollar;<?php echo $product['rrp']?></span>
                    <?php endif; ?>
 </span>
            </a>
        <?php endforeach; ?>
    </div>
    <div class="buttons">
        <?php if ($current_page > 1): ?>
            <a href="index.php?page=products&p=<?php echo $current_page-1?>">Prev</a>
        <?php endif; ?>
        <?php if ($total_products > ($current_page * $num_products_on_each_page) -
            $num_products_on_each_page + count($products)): ?>
            <a href="index.php?page=products&p=<?php echo $current_page+1?>">Next</a>
        <?php endif; ?>
    </div>
</div>
<?=template_footer()?>