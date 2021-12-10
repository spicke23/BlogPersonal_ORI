insert into operario (idoperario, opernombre, operapellido, operedad, opercorreo) values
(1, 'juan', 'orellana', 28, 'juan@gmail.com'),
(2, 'pedro', 'orellana', 28, 'juan@gmail.com'),
(3, 'diego', 'orellana', 28, 'juan@gmail.com'),
(4, 'rodrigo', 'orellana', 28, 'juan@gmail.com'),
(5, 'patricio', 'orellana', 28, 'juan@gmail.com');


insert into categoria (idcategoria, catnombre, catdescripcion) values(1,'Redes','Problemas de comunicacion'),
(2,'Software','Aplicaion no funciona'),(3,'Hardware','mouse malo'),(4,'Otros','Varios');

insert into soporte (idsoporte, operario_idoperario, usuario_idusuario, fecha_soporte, evaluacion, categoria_idcategoria) 
values(5,2,1, '2021-02-06', 4, 2),
      (6,3,2, '2021-11-06', 1, 1),
      (7,4,3, '2021-07-06', 6, 1),
      (8,4,2, '2021-06-06', 10, 1);
#query1
/* Seleccione las 3 operaciones con mejor evaluación */
SELECT * FROM soporte
ORDER BY evaluacion DESC
LIMIT 3;
#query2
/* Seleccione las 3 operaciones con peor evaluacion */
SELECT * FROM soporte
ORDER BY evaluacion ASC
LIMIT 3;

#query3
select operario_idoperario, count(*) from soporte 
group by operario_idoperario;

select operario_idoperario,count(idsoporte) from soporte group by  operario_idoperario order by count(idsoporte) desc
limit 1;

select max(operario.opernombre) from (
select count(s.idsoporte),o.opernombre from operario as o inner join soporte as s
on o.idoperario=s.operario_idoperario
group by o.opernombre) as operario;

#---------------------

#query4
select usuario_idusuario, count(idsoporte) from soporte group by usuario_idusuario order by count(idsoporte) asc
limit 2;
 
select min(usu.nombre) from (
select count(s.id),u.nombre from usuario as u inner join soporte as s
on u.id=s.id_usu
group by u.nombre) as usu;

#query5
update usuario set useredad = useredad + 10 where idusuario in( select idusuario from usuario order by idusuario limit 3);

update usuario set useredad=useredad+10 where idusuario in (select idusuario from (select idusuario from usuario  limit 3) as usu);

#query6
ALTER TABLE usuario
rename COLUMN usercorreo to email;

#query7
select * from operario where operedad > 20;

select * from soporte;





