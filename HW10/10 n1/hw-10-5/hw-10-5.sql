CREATE TABLE staff
(staff_id int UNIQUE NOT NULL,
 staff_name varchar,
 manager_id int);
 
 INSERT INTO staff
 (staff_id,staff_name,manager_id)
 VALUES
 (1001,'akbari',NULL),
 (1002,'ahmadi',1001),
 (1003,'asghari',1001),
 (1004,'akrami',1003);
 
 SELECT * FROM staff;
 
 SELECT A.staff_name AS employee,C.staff_name AS manager
 FROM staff A,staff C
 WHERE A.manager_id=C.staff_id;
 
