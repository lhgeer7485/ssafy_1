SELECT * FROM article, user WHERE article.userid = user.id;

SELECT * FROM EMPLOYEE, DEPARTMENT WHERE EMPLOYEE.deptno = DEPARTMENT.deptno;

SELECT * FROM EMPLOYEE e, DEPARTMENT d WHERE e.deptno = d.deptno;

SELECT e.name, d.deptno, d.name FROM EMPLOYEE e, DEPARTMENT d WHERE e.deptno = d.deptno;

SELECT e.name, d.deptno, d.name FROM EMPLOYEE e INNER JOIN DEPARTMENT d ON e.deptno = d.deptno;

SELECT e1.name, e1.job, e1.deptno, e1.boss, e2.name FROM EMPLOYEE e1, EMPLOYEE e2 WHERE e1.boss = e2.empno;

SELECT e1.name, e1.job, e1.deptno, e1.boss, e2.name FROM EMPLOYEE e1 LEFT OUTER JOIN EMPLOYEE e2 ON e1.boss = e2.empno;

SELECT e1.name, e2.name, d.name 
  FROM EMPLOYEE e1, EMPLOYEE e2, DEPARTMENT d 
  WHERE e1.boss = e2.empno AND e1.deptno = d.deptno;

