
select distinct Fname,Minit,Lname,Ssn,Dno,Dname
from Employee as emp1,
(
select Dname,Mgr_ssn
from 
(select Super_ssn
 from employee as emp,(select distinct Essn from  Works_on where hours<40) as work1
 where emp.ssn=work1.Essn) as temp,department as dept where dept.Mgr_ssn=temp.Super_ssn) as temp1 where temp1.mgr_ssn=emp1.Ssn;
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
