#!/usr/bin/env python3
# encoding: utf-8
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from jabberbot.mucbot import MUCBot

print ("Leyendo configuracion...")
jid = 'jeff@jabberes.org' #edita esto por una cuenta de jabber
pwd = "pasword here" #Edita esto por tu password
muc_room = 'shl@conf.jabberes.org' #edita esto por el servidor y la sala
muc_nick = 'jabberstom' #Esto no lo edites el nombre es lindo xd

print ("Configuracion aceptada....")
bot = MUCBot(jid, pwd, muc_room, muc_nick)
print ("conectando...")
bot.connect()
print ("El bot esta conectado y listo para usar.. Seria preferible correr el bot en background")
bot.process(block=True)
