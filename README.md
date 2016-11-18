"Mucho que aprender todavia tiene"

“La guerra no lo hace a uno más grandioso”. : 
![alt text](http://es.seaicons.com/wp-content/uploads/2015/09/Master-Joda-icon.png "Logo Title Text 1")


### Installation
---
Jabberstom requiere algunas dependencias instaladas de este modo.
```bash
# Jabberstom requiere python3+ para funcionar
$ cd jabberstom
$ sudo apt install python-pip
$ pip install -r requeriments.txt
```
### Configuracion
---
```bash
$ cd jabberstom
$ nano jabberstom.py
```
```py
jid = 'jeff@jabberes.org' #edita esto por una cuenta de jabber
pwd = "pasword here" #Edita esto por tu password
muc_room = 'shl@conf.jabberes.org' #edita esto por el servidor y la sala
muc_nick = 'jabberstom' #Esto no lo edites el nombre es lindo xd
```
```bash
Guardamos y ejecutamos.
$ python3 jabberstom.py
```
Es preferible que corras el bot en background con lo que prefieras yo uso nohup. de este modo
```bash
$ cd jabberstom
$ nohup jabberstom.py &
```

### Comandos
---
Jabberstom cuenta con los siguientes comandos.

|Comando    |Descripcion         |Modo de uso  |
|-----------|:-------------------|:------------|
|!help | ver todos los comandos y ayuda para el bot.|!abrazo Jeff
|!besar | Besa a un user|!besar Jeff y !besar Jeff pie (lo besas en el piexD)
|!chiste| chistes random.|!chiste
|!chuck| muestra chiste de Chuck Norris de http://icndb.com|!chuck
|!goku | Por el poder de goku <nickname>!' |!goku user
|!m | Tu madre es tan... |!m Jeff
|!pokemon | encuentra un salvaje pokemon! | xD
|!regla | Puedes editar las reglas obviamente |!regla: ves todas las reglas !regla r1: ves la regla 1
|!slap | Pegale a un user. | !slap Jeff
| !version | Version del bot

### Desarrollador, Soporte y Contacto
---
> Pentsec@cock.li

> IRC: Server: irc.stormbit.net | Canal: #Linux | Puerto: 6697 (SSL)
---
License
----
GPLV3

**Free Software, Hell Yeah!**
