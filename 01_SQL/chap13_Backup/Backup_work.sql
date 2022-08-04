-- Backup_work.sql

DROP TABLE emp PURGE;  -- emp 임시 테이블까지 완전 삭제

SELECT * FROM USER_TABLES WHERE TABLE_NAME LIKE 'E%';  -- 데이블 삭제 및 복구 확인