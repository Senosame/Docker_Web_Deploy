USE shop_db;

DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price VARCHAR(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO products (name, price) VALUES 
('USB Rubber Ducky', '1.200.000đ'),
('Wifi Pineapple', '3.500.000đ'),
('HackRF One', '7.000.000đ');