drop procedure if exists addTwoNum;

DELIMITER //
Create Procedure addTwoNum(in a int,in b int,out ans int)
BEGIN
set ans=a+b;
END //


call addTwoNum(20,30,@ans);
select @ans;