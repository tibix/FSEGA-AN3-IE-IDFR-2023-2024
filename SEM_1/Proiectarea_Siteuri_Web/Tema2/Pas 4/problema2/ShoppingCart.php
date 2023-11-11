<?php
require_once "DBController.php";
class ShoppingCart extends DBController
{
    function getAllProduct()
    {
        $query = "SELECT * FROM tbl_product";

        $productResult = $this->getDBResult($query);
        return $productResult;
    }
    function getMemberCartItem($member_id)
    {
        $query = "SELECT tbl_product.*, tbl_cart.id as cart_id,tbl_cart.quantity FROM tbl_product, tbl_cart WHERE tbl_product.id = tbl_cart.product_id AND tbl_cart.member_id = ?";
        $params = array(
            array(
                "param_type" => "i",
                "param_value" => $member_id
            )
        );

        $cartResult = $this->getDBResult($query, $params);
        return $cartResult;
    }
    function getProductByCode($product_code)
    {
        $query = "SELECT * FROM tbl_product WHERE code=?";

        $params = array(
            array(
                "param_type" => "s",
                "param_value" => $product_code
            )
        );

        $productResult = $this->getDBResult($query, $params);
        return $productResult;
    }
    function getCartItemByProduct($product_id, $member_id)
    {
        $query = "SELECT * FROM tbl_cart WHERE product_id = ? AND member_id = ?";

        $params = array(
            array(
                "param_type" => "i",
                "param_value" => $product_id
            ),
            array(
                "param_type" => "i",
                "param_value" => $member_id
            )
        );