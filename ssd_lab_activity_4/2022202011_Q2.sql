use customer_db;

drop procedure if exists getName;
DELIMITER //
Create Procedure getName(in city varchar(255))
BEGIN
select CUST_NAME from customer where WORKING_AREA=city;
END //

call getName("Bangalore");
