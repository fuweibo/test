CREATE OR REPLACE FUNCTION update_modified()
RETURNS TRIGGER AS $$
BEGIN
   NEW.modified = now();
   RETURN NEW;
END;
$$ language 'plpgsql';



create table if not exists users.task (
	uuid					uuid  primary key,
	employee  		uuid,
	supervisor  	uuid,
	department 		uuid,
	manager 			uuid,
	tasktype  		varchar(255),
	dt_task				varchar(24),
	area_count   	jsonb,
	img_url  			varchar(255),
	status 				varchar(24),
	ftrialtime		timestamp,
	strialtime		timestamp,
	bk_type				varchar(24),
	code					varchar(255),
	message				varchar(255),
	error_reason	varchar(255),
	downtime			float,
	created       timestamp
);
CREATE TRIGGER update_users_task_modified BEFORE UPDATE ON users.task FOR EACH ROW EXECUTE PROCEDURE update_modified();
ALTER TABLE users.task OWNER to postgres;