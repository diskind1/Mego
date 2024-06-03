use NORTHWND
SELECT E.EmployeeID,
	   E.LastName + ' ' + E.FirstName,
	   SUM(OD.Quantity * OD.UnitPrice) as sikum,
	   AVG(OD.Quantity * OD.UnitPrice) as MMUZa
FROM Employees AS E INNER JOIN
	Orders AS O INNER JOIN
	[Order Details] AS OD
	ON OD.OrderID = O.OrderID
	ON O.EmployeeID = E.EmployeeID
WHERE E.City LIKE 'LONDON'
GROUP BY E.EmployeeID, E.LastName, E.FirstName
