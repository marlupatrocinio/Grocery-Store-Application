CREATE TABLE Product (product_id int NOT NULL auto_increment PRIMARY KEY,
product_name varchar(20) not null,
uom_id int not null,
price_per_unit double not null);

CREATE TABLE Orders (order_id int not null auto_increment PRIMARY KEY,
customer_name varchar(100) not null,
total double not null,
datetime_order datetime not null);

CREATE TABLE `GS_app`.`orders_detail` (
  `order_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  `quantity` DOUBLE NOT NULL,
  `total_price` DOUBLE NOT NULL,
  INDEX `fk_order_id_idx` (`order_id` ASC) VISIBLE,
  INDEX `fk_product_id_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `fk_order_id`
    FOREIGN KEY (`order_id`)
    REFERENCES `GS_app`.`Orders` (`order_id`)
    ON DELETE NO ACTION
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_product_id`
    FOREIGN KEY (`product_id`)
    REFERENCES `GS_app`.`Product` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE RESTRICT);

CREATE TABLE `GS_app`.`uom` (`uom_id` int not null auto_increment primary key,
`uom_name` varchar(45) not null);

ALTER TABLE `GS_app`.`Product`
ADD INDEX `fk_uom_id_idx` (`uom_id` ASC) VISIBLE;
;
ALTER TABLE `GS_app`.`Product`
ADD CONSTRAINT `fk_uom_id`
  FOREIGN KEY (`uom_id`)
  REFERENCES `GS_app`.`uom` (`uom_id`)
  ON DELETE NO ACTION
  ON UPDATE RESTRICT;

SELECT Product.product_id, Product.product_name, Product.uom_id, Product.price_per_unit, uom.uom_name 
FROM Product 
INNER JOIN uom ON Product.uom_id = uom.uom_id;

SELECT * FROM Product;