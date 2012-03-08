"""
Taller BigGames 

Autores: 
    Sergio Galan Nieto. http://sergio.eclectico.net 
    Victor Diaz Barrales. http://www.victordiazbarrales.com

Este codigo tiene licencia GPL asi que ya sabes, si lo modificas tienes que compartir tus conocimientos
 con nostros! :)  
"""

import cherrypy
import simplejson
import string
import os
import json;
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))



class Server:

  def __init__(self):
    self.indexText = None
    self.order="none" 
    self.code="none"
    self.video="none"
    
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
    #remote = cherrypy.request.headerMap.get("Remote-Addr", "") 
    tmpl = env.get_template("index.html")
    return tmpl.render(directories=dir)  
  
  #la accion que enviamos al ordenador que controla la pantalla 
  @cherrypy.expose
  def getAction(self):
	cherrypy.response.headers['Content-Type'] = 'text/event-stream; charset=utf-8 \n\n'
  	tmp_order = self.order;
  	self.order = "none"
  	if (tmp_order=="change"):
  		return self.returnFolder()
  	else:
	  	return "data:"+  tmp_order + "\n\n"
  

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
  
  #control: List team foldersgetTeams 
  @cherrypy.expose		
  def getTeams(self):
  	dirs={}
  	for dirname, dirnames, filenames in os.walk('./static/presentation/contenidos/'):
  		b=dirname.split("/")
		if(len(b) >= 6 ):
  			group=b[4]
  			folder=b[5]
  			if(group in dirs):
  				dirs[group].append(folder)
  			else:
  				dirs[group]=[]
  				dirs[group].append(folder)	
  	return json.dumps(dirs)	  
  	
  #control: list folders for each time		
  @cherrypy.expose
  def getFolder(self,team):
	dirs=[]
  	for dirname, dirnames, filenames in os.walk('./static/presentation/contenidos/'+team):
  		dirs.append(dirname)
  	return json.dumps(dirs)

  #control: set current folder on screen
  @cherrypy.expose
  def changeSlides(self,team,folder): 
  	self.current_path=path
  	self.order="change"
  	
  	
  def returnFolder(self):
  	print "returnFOLDER------------------"  
  	n_slides=0
  	for dirname, dirnames, filenames in os.walk('./static/presentation/contenidos/'+self.current_path):
  		n_slides+=1
	cherrypy.response.headers['Content-Type']= 'text/event-stream; charset=utf-8 \n\n'
	msg="event: change\n"
	msg+= 'data: {"path": "'+self.current_path+'", "slides":"'+str(n_slides) +'"} \n\n'
	print msg
	
	return msg
  
  #codigo recibido de los clientes 
  @cherrypy.expose
  def setCode(self, **code): 
    print "hola que tal!!"
    self.code = code['code'] 

    return "OK"
  
 
  
  #codigo para setear al servidor 
  @cherrypy.expose
  def getCode(self):
    cherrypy.response.headers['Content-Type']= 'text/event-stream; charset=utf-8 \n\n'
    tmp_order = self.code; 
    print self.code
    
    self.code = "none"
    return "data:"+  tmp_order +"\n\n"
  
 
 
  #codigo recibido de los clientes 
  @cherrypy.expose
  def setVideo(self, **video): 
    print "hola que tal!!"
    self.video = video['video'] 

    return "OK"
 

 
  #codigo para setear al servidor 
  @cherrypy.expose
  def getVideo(self):
    cherrypy.response.headers['Content-Type']= 'text/event-stream; charset=utf-8 \n\n'
    tmp_order = self.video; 
    print self.video
   
    self.video = "none"
    return "data:"+  tmp_order +"\n\n"
 

#codigo recibido de los clientes 
@cherrypy.expose
def savePNG(self, **img): 
    print "hola que tal!!"
    self.img = img['img'] 
    return "OK"




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


