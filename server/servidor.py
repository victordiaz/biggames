"""
Taller BigGames 

Autores: 
    Sergio Galan Nieto. http://sergio.eclectico.net 
    Victor Diaz Barrales. http://www.victordiazbarrales.com

Este codigo tiene licencia GPL asi que ya sabes, si lo modificas tienes que enviarnos los cambios! :) 
"""

import cherrypy
import simplejson
import string

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))



class Server:

  def __init__(self):
    self.indexText = None
    self.order="none"
    cherrypy.config["tools.encode.on"] = True
    cherrypy.config["tools.encode.encoding"] = "utf-8"

  #metodo que carga archivos estaticos 
 # @cherrypy.expose
 # def index(self):
 #   if not self.indexText: 
 #     indexFileName = os.path.join(os.path.dirname(__file__),"static")
 #     indexFile = open(indexFileName)
 #     self.indexText = indexFile.read()
 #     remote = cherrypy.request.headerMap.get("Remote-Addr", "") 
 #     print cherrypy.request.headerMap['user-agent']
 #     print remote

  #  return self.indexText


  #show directories in the index 
  @cherrypy.expose 
  def index(self):
    dir = os.listdir(os.getcwd() + '/static')
    remote = cherrypy.request.headerMap.get("Remote-Addr", "") 
    return tmpl.render(directories=dir)  
  
  #la accion que enviamos al ordenador que controla la pantalla 
  @cherrypy.expose
  def getAction(self):
	cherrypy.response.headers['Content-Type']= 'text/event-stream; charset=utf-8 \n\n'
  	print "qq"  
  	tmp_order = self.order;
  	self.order = "none"
  	return "data:"+  tmp_order +"\n\n"
  
  #lo que recibe del control remoto 
  @cherrypy.expose		
  def setOrder(self, mAction = None):
    if mAction:
    	self.order = mAction;
    	return "OK"    
    else:
      if mAction is None:
        # No name was specified
        return 'No1'
      else:
        return 'No2'

  
 



#------------------- main -- 

import os.path


if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    tutconf = os.path.join(os.path.dirname(__file__), 'biggames.conf')
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print tutconf
    cherrypy.quickstart(Server(), config=tutconf ) 


   
else:
    # This branch is for the test suite; you can ignore it.
    cherrypy.tree.mount(Server(), config=tutconf)


