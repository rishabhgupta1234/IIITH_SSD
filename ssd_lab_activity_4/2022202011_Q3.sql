use customer_db;

drop procedure if exists getAccount;
DELIMITER //
Create Procedure getAccount()
BEGIN
select CUST_NAME,GRADE from customer where RECEIVE_AMT+OPENING_AMT>10000;
END //

call getAccount();
