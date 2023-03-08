drop table glaze;
drop table glaze_properties;
drop table glaze_recipe;

create table glaze
(
	id						numeric(10,0),
	glaze_name		char(40),
	description		text,
	comment				text
);

create table glaze_properties
(
	glaze_id	numeric(10,0),
	prop_name	char(40),
	prop_val	char(40)
);

create table glaze_recipe
(
	glaze_id	numeric(10,0),
	ingr_type	char(40),
	ingr_name	char(40),
	ingr_val	char(40)
);

insert into glaze (id,glaze_name,description,comment) values (1,"Jojo's Glaze","A wonderful mix of sugar and spice","Please, do not use this glaze. But if you do, please let Jojo know.");
insert into glaze (id,glaze_name,description,comment) values (2,"Pursuit of Frobenius","The fruits of happiness are with your grasp","Use my glaze! Please! But don't tell me if you do!");

insert into glaze_properties (glaze_id,prop_name,prop_val) values (1,"cone","013");
insert into glaze_properties (glaze_id,prop_name,prop_val) values (2,"cone","4");

insert into glaze_properties (glaze_id,prop_name,prop_val) values (1,"color","Yellow");
insert into glaze_properties (glaze_id,prop_name,prop_val) values (1,"color","Green");
insert into glaze_properties (glaze_id,prop_name,prop_val) values (2,"color","Gray");

insert into glaze_properties (glaze_id,prop_name,prop_val) values (1,"value","Dark");
insert into glaze_properties (glaze_id,prop_name,prop_val) values (2,"value","Medium");

insert into glaze_properties (glaze_id,prop_name,prop_val) values (1,"surface","Gloss");
insert into glaze_properties (glaze_id,prop_name,prop_val) values (2,"surface","Crater");

insert into glaze_properties (glaze_id,prop_name,prop_val) values (1,"firing","Reduction");
insert into glaze_properties (glaze_id,prop_name,prop_val) values (2,"firing","Wood");

insert into glaze_properties (glaze_id,prop_name,prop_val) values (1,"oxide","Zinc");
insert into glaze_properties (glaze_id,prop_name,prop_val) values (2,"oxide","Lead");

insert into glaze_properties (glaze_id,prop_name,prop_val) values (1,"hazard","Food Safe");
insert into glaze_properties (glaze_id,prop_name,prop_val) values (2,"hazard","Maybe");

insert into glaze_properties (glaze_id,prop_name,prop_val) values (1,"thermal","44");
insert into glaze_properties (glaze_id,prop_name,prop_val) values (2,"thermal","26");

insert into glaze_properties (glaze_id,prop_name,prop_val) values (1,"si2al","4:1");
insert into glaze_properties (glaze_id,prop_name,prop_val) values (2,"si2al","1:3.2");

insert into glaze_properties (glaze_id,prop_name,prop_val) values (1,"image1","graphics/jojo1.jpg");
insert into glaze_properties (glaze_id,prop_name,prop_val) values (2,"image1","graphics/jojo1.jpg");

insert into glaze_properties (glaze_id,prop_name,prop_val) values (1,"image2","graphics/jojo2.jpg");
insert into glaze_properties (glaze_id,prop_name,prop_val) values (2,"image2","graphics/jojo2.jpg");

insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (1,"base","Bromide","33");
insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (1,"base","Nipherium","33");
insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (2,"base","Iridium","40");
insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (2,"base","Giordanium","40");

insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (1,"analysis","SiO2","33");
insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (1,"analysis","LiO2","33");
insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (2,"analysis","Al2O3","40");
insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (2,"analysis","Cr2O3","40");

insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (1,"colorant","Dried Bacteria","33");
insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (1,"colorant","Dried Mucus","33");
insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (2,"colorant","Wood Ash","20");
insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (2,"colorant","Wood Bark","20");

insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (1,"molecular","Na2O","33");
insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (1,"molecular","BaO","33");
insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (2,"molecular","K2O","20");
insert into glaze_recipe (glaze_id,ingr_type,ingr_name,ingr_val) values (2,"molecular","Li2O","20");
