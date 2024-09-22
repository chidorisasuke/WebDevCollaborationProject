USE db_projectsi;

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    country VARCHAR(50)
);

CREATE TABLE orders(
	order_id INT AUTO_INCREMENT PRIMARY KEY,
	customer_id INT NOT NULL,
	order_date DATE NOT NULL,
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers (customer_name, email, country)
VALUES 
('Gading', 'gading123@gmail.com', 'Indonesia'),
('William', 'william123@gmail.com', 'Indonesia'),
('Robert', 'robert123@gmail.com', 'Turkey'),
('Yahya', 'yahya123@gmail.com', 'AS'),
('Arwi', 'arwi123@gmail.com', 'Korea');

INSERT INTO orders (customer_id, order_date)
VALUES
(1, '2024-08-22'),
(2, '2024-08-21'),
(3, '2024-09-2'),
(4, '2024-09-16'),
(5, '2024-09-22');

SELECT * FROM customers;
SELECT * FROM orders;

SHOW TABLES;

DROP TABLE customers;
DROP TABLE orders;