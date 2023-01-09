CREATE TABLE employee2(
emp_id int PRIMARY KEY,
emp_name varchar,
manager_id int);

INSERT INTO employee2
(emp_id,emp_name,manager_id)
VALUES
(1001,'n1',null),
(1002,'n2',1010),
(1003,'n3',1005),
(1004,'n4',1001),
(1005,'n5',1005),
(1006,'n6',1010),
(1007,'n7',1001),
(1008,'n8',1010),
(1009,'n9',1001),
(1010,'n10',1007);

SELECT * FROM employee2;