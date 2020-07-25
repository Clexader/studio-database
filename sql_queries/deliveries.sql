use studio_app_2;
select
	o.id as 'ID',
    o.Groom_Name as 'Name',
    o.Phone_Number as 'phone',
    o.Event_Date,
    p.Name,
    p.Banners,
    p.Frames,
    p.Photos,
    p.Albums,
    DATE_ADD(o.Event_Date, INTERVAL 20 day) as "deadline"
from orders o
join packages p
	on o.Package_id = p.id