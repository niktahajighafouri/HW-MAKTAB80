CREATE TABLE transfer
(transfer_id int,
transfer_method text DEFAULT 'By post' PRIMARY KEY);

ALTER TABLE orders
ADD transfermethod text;

ALTER TABLE orders
ADD FOREIGN KEY (transfermethod) REFERENCES transfer(transfer_method);
