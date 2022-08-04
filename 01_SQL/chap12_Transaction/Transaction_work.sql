-- Transaction_work.sql

/*
트랜잭션: DB에서 작업 수행 단위
COMMIT or COMMIT WORK: 트랜잭션 DB에 반영
SAVEPOINT 레이블명: 트랜잭션을 저장하는 역한
ROLLBACK TO 레미블명; 트랜잭션 취소 역할
*/
DROP TABLE dept_test;
CREATE TABLE dept_test
AS
SELECT * FROM dept;
SELECT * FROM dept;
DELETE FROM dept_test WHERE deptno = 40;

SAVEPOINT c0;
COMMIT;  -- DB 반영; 커밋 이전 명령문 복원 불가
ROLLBACK TO c0;

DELETE FROM dept_test WHERE deptno = 30;
SAVEPOINT c1;

DELETE FROM dept_test WHERE deptno = 20;
SAVEPOINT c2;

DELETE FROM dept_test WHERE deptno = 10;

SELECT * FROM dept_test;  -- 모든 레코드 삭제 상태

ROLLBACK TO c2;  -- 1개 deptno=10 복원

ROLLBACK;  -- COMMIT 이후 모든 명형어: 3개 복원