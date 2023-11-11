<?php
require_once "ShoppingCart.php"; ?>
<html>
<HEAD>
    <TITLE>Creare cos cumparaturi </TITLE>
    <link href="style.css" type="text/css" rel="stylesheet"/>
</HEAD>
<body>
<div id="product-grid">
    <div class="txt-heading">
        <div class="txt-headinglabel">Products</div>
    </div>
    <?php
    $shoppingCart = new ShoppingCart();
    $query = "SELECT * FROM tbl_product";
    $product_array = $shoppingCart->getAllProduct($query);
    if (!empty($product_array)) {
        foreach ($product_array as $key => $value) {
            ?>
            <div class="product-item">
                <form method="post" action="cos.php?action=add&code=<?php
                echo $product_array[$key]["code"]; ?>">
                    <div class="product-image">
                        <img src="<?php echo $product_array[$key]["image"]; ?>">
                    </div>
                    <div>
                        <strong><?php echo $product_array[$key]["name"];
                            ?></strong>
                    </div>
                    <div class="product-price"><?php echo
                            "$" . $product_array[$key]["price"]; ?></div>
                    <div>
                        <input type="text" name="quantity" value="1" size="2"/>
                        <input type="submit" value="Add to cart"
                               class="btnAddAction"/>
                    </div>
                </form>
            </div>
            <?php
        }
    }
    ?>
</div>
</body>
</html>