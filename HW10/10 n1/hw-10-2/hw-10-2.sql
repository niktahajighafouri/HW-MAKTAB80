CREATE TABLE employee
(employeeID int, 
 employeeName varchar,
 department varchar, salary bigint);
 
INSERT INTO employee
(employeeID,employeename,department,salary)
VALUES
(1001,'akbar','mali',10000),
(1002,'asqar','edari',700),
(1003,'zohre','edari',2000),
(1004,'zahra','mali',600),
(1005,'ali','mali',900);

SELECT * FROM employee
WHERE employeename='ali';

SELECT * FROM employee
WHERE salary<1000;

SELECT DISTINCT department, AVG(salary) AS average_salary FROM employee
GROUP BY department;

BACKUP DATABASE company
TO DISK = 'C:\my_db_backup.bak';

RESTORE DATABASE my_db
FROM DISK = 'C:\my_db_backup.bak';