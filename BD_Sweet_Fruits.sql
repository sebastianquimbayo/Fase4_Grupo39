use sweet_fruits;

create table empleado(
id_empleado int(10) primary key,
primer_nombre_empleado varchar(50) not null,
segundo_nombre_empleado varchar(50),
primer_apellido_empleado varchar(50) not null,
segundo_apellido_empleado varchar(50),
telefono_empleado long not null,
correo_electronico_empleado varchar(50) not null
)engine=innodb;

insert into empleado (id_empleado, primer_nombre_empleado, segundo_nombre_empleado, primer_apellido_empleado, 
segundo_apellido_empleado, telefono_empleado, correo_electronico_empleado)
values ("0093421584", "Lina", "Mariana", "Quimbayo", "Rodriguez", "3112345688", "linamq@gmail.com"),
("1123431284", "Maria", "Paula", "Quimbayo", "Rodriguez", "2113452311", "mariapq@gmail.com");

create table cliente(
id_cliente int(10) primary key,
primer_nombre_cliente varchar(50) not null,
segundo_nombre_cliente varchar(50),
primer_apellido_cliente varchar(50) not null,
segundo_apellido_cliente varchar(50),
telefono_cliente long not null,
correo_electronico_cliente varchar(50) not null
)engine=innodb;

insert into cliente (id_cliente, primer_nombre_cliente, segundo_nombre_cliente, primer_apellido_cliente, 
segundo_apellido_cliente, telefono_cliente, correo_electronico_cliente)
values ("0012345688", "Manuel", "Sebastian", "Quimbayo", "Barbosa", "3114583977", "sebas@gmail.com"),
("1112131415", "Odilia", "Isabel", "Barbosa", null, "3112112333", "isa@gmail.com");

create table venta(
id_venta int(5) primary key,
id_empleado int(10) not null,
id_cliente int(10) not null,
valor_total_venta double not null,
fecha_venta date not null,
foreign key (id_empleado) references empleado (id_empleado),
foreign key (id_cliente) references cliente (id_cliente)
)engine=innodb;

insert into venta (id_venta, id_empleado, id_cliente, valor_total_venta, fecha_venta)
values ("1", "0093421584", "0012345688", "10000.00", "2024-03-24"),
("2", "0093421584", "0012345688", "10000.00", "2024-03-24");

create table venta_producto(
id_venta_producto int(10) primary key,
id_venta int(10) not null,
id_producto int(10) not null,
foreign key (id_venta) references venta (id_venta),
foreign key (id_producto) references producto (id_producto)
)engine= innodb;

insert into venta_producto(id_venta_producto, id_venta, id_producto)
values("1", "1", "1"),
("2", "2", "2");

create table producto(
id_producto int(10) primary key,
nombre_producto varchar(50) not null,
categoria_producto varchar(50) not null,
valor_producto double not null,
cantidad_producto int (10) not null,
id_recurso int(5) not null,
foreign key (id_recurso) references recurso (id_recurso)
)engine=innodb;

insert into producto (id_producto, nombre_producto, categoria_producto, valor_producto, cantidad_producto, id_recurso)
values ("1", "Fresa Deshidratada", "fruta deshidratada", "10000.00", "10", "1"),
("2", "Mango Deshidratada", "fruta deshidratada", "10000.00", "10", "2");
insert into producto (id_producto, nombre_producto, categoria_producto, valor_producto, cantidad_producto, id_recurso)
values ("3", "Arándano Deshidratado", "Fruta deshidratada", "10000.00", "10", "1");

create table recurso(
id_recurso int(5) primary key,
nombre_recurso varchar(50) not null,
cantidad_recurso int(10) not null,
id_proveedor int(10) not null,
CONSTRAINT recurso_proveedor foreign key (id_proveedor) references proveedor (id_proveedor)
)engine=innodb;

CREATE INDEX idx_proveedor_id ON proveedor (id_proveedor);
insert into recurso (id_recurso, nombre_recurso, cantidad_recurso, id_proveedor)
values ("1", "Fresas", "500", "1"),
("2", "Mangos", "100", "2");

create table proveedor(
id_proveedor int(10) not null,
nombre_proveedor varchar(50) not null,
telefono_proveedor long not null,
correo_electronico_proveedor varchar(50) not null
)engine=innodb;

insert into proveedor (id_proveedor, nombre_proveedor, telefono_proveedor, correo_electronico_proveedor)
values ("1", "Fresas", "1211345678", "fresas@gmail.com"),
("2", "Mango", "2231231211", "mango@gmail.com");

