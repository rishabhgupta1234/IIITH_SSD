select distinct Fname,Minit,Lname,ssn,dno,temp1.cp from Employee as emp,
(
select mgr_ssn,temp.cp from department as dept,
(select count(*) as cp,super_ssn from employee group by super_ssn) as temp where temp.super_ssn=dept.mgr_ssn) as temp1
 where temp1.mgr_ssn=emp.ssn order by temp1.cp;