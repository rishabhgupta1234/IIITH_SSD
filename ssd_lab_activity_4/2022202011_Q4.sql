
use customer_db;
drop table if exists res;
drop procedure if exists Myprocedure;

Create table res(cname varchar(255),ccity varchar(255),ccountry varchar(255),grade int);
DELIMITER //

Create Procedure Myprocedure()
BEGIN
DECLARE DONE int DEFAULT FALSE;
DECLARE cname varchar(255);
DECLARE ccity varchar(255);
DECLARE ccountry varchar(255);
DECLARE cgrade int;

DECLARE mycursor CURSOR
for select CUST_NAME,CUST_CITY,CUST_COUNTRY,GRADE from customer where AGENT_CODE like 'A00%';


declare continue handler for not found set DONE=TRUE;
OPEN mycursor;

LABEL:loop
fetch mycursor INTO 
cname,
ccity,
ccountry,
cgrade ;

if DONE then leave LABEL;
end if;
insert into res values(cname,ccity,ccountry,cgrade);
end LOOP;


close mycursor;


END //

call Myprocedure();




