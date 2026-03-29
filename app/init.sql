SET NAMES utf8mb4; 
USE shop_db;

DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price VARCHAR(50) NOT NULL,
    image_url VARCHAR(255) NOT NULL 
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; 

INSERT INTO products (name, price, image_url) VALUES 
('Yuwwka Plushie', '100.000.000đ', 'images/yukka.png'),
('Bàn Phím Aula F75 Xanh nhạt', '3.500.000đ', 'images/f75.jpg'),
('Chuột Gaming Shark Attack X6', '7.000.000đ', 'images/sharkx6.jpg');