--USE NORTHWND

--SELECT E.LastName +' '+ E.FirstName AS NAME,
--E.City

--FROM Employees AS E


SELECT *

FROM Orders AS O
WHERE YEAR (O.OrderDate) = '1996'