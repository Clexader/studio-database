'''SELECT id, Groom_Name from orders
where Photographer_id = 2
GROUP BY id, Groom_Name'''

'''SELECT ph.Name, ph.studio, ph.Phone, ph.Email, ph.Description, COUNT(*) AS 'Total events'
FROM orders o 
join photographers ph
	on o.Photographer_id = ph.id
GROUP BY Photographer_id;'''
