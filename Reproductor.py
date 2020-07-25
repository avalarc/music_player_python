from tkinter import *
from tkinter import filedialog
import pygame
import os

# Definiendo la clase Repriductor Musical
class ReproductorMusical:
    
    def __init__(self,container):
        self.container = container
        # Titulo de la ventana
        self.container.title("Music Player")
        # Tamaño
        self.container.geometry("1000x350")
         # Bloquear le cambio de tamaño
        self.container.resizable(width=False, height=False)
        # Ruta de las canciones
        self.directorio = StringVar()
        # Iniciar Pygame
        pygame.init()
        # Iniciar Pygame Mixer
        pygame.mixer.init()
        #Formatos aceptados
        self.aceptados = ['mp3','wav']
        
        self.estado = StringVar()
        self.cancion = StringVar()

        #Seleccionar ruta de carpeta contenedoras de canciones
        rutaContenedora = LabelFrame(self.container,text="Seleccione la ruta de sus canciones...",font=("fonatica",12,"bold"),bg="black",fg="white",bd=5,relief=FLAT)
        labeldirectorio = Label(rutaContenedora,textvariable=self.directorio,width=70,font=("fonatica",10,"bold"),bg="black",fg="white").grid(row=0,column=0,padx=10,pady=5)
        rutaContenedora.place(x=0,y=0,width=950,height=60)
        print("directorio:")
        print(self.directorio)
        
        botonBuscarContenedor = LabelFrame(self.container,text="",font=("fonatica",12,"bold"),bg="black",fg="white",bd=5,relief=FLAT)
        botonBuscarContenedor.place(x=950,y=0,width=50,height=60)
        ruta = Button(botonBuscarContenedor,text="...",command=self.seleccionarRuta,width=6,height=1,font=("fonatica",12),fg="black",bg="grey").grid(row=0,column=0,padx=0,pady=0)
        
        # PLaylist
        contenedorCanciones = LabelFrame(self.container,text="Playlist",font=("fonatica",15,"bold"),bg="black",fg="white",bd=5,relief=FLAT)
        contenedorCanciones.place(x=0,y=50,width=1000,height=200)
        # Scrollbar de la playlist
        scrol_y = Scrollbar(contenedorCanciones,orient=VERTICAL)
        # Insertando listbox de la Playlist
        self.listaCanciones = Listbox(contenedorCanciones,yscrollcommand=scrol_y.set,selectbackground="black",selectmode=SINGLE,font=("fonatica",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=FLAT)
        # Agregando el Scrollbar al listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.listaCanciones.yview)
        self.listaCanciones.pack(fill=BOTH)

        # Frame para el titulo de la cancion
        contenedorCancion = LabelFrame(self.container,text="Título",font=("fonatica",10,"bold"),bg="grey",fg="white",bd=5,relief=FLAT)
        contenedorCancion.place(x=0,y=250,width=600,height=100)
        # Se inserta mensaje del estado en el label del titulo de la cancion
        titulo = Label(contenedorCancion,textvariable=self.cancion,width=60,font=("fonatica",10,"bold"),bg="grey",fg="white").grid(row=0,column=0,padx=10,pady=5)
        # Etiqueta para identificar el estado de ejecucion de la cancion
        estadoCancion = Label(contenedorCancion,textvariable=self.estado,font=("fonatica",8,"bold"),bg="grey",fg="white").grid(row=0,column=1,padx=10,pady=5)

        # Contenedor de botones
        contenedorBotones = LabelFrame(self.container,text="Control Panel",font=("fonatica",15,"bold"),bg="grey",fg="white",bd=5,relief=FLAT)
        contenedorBotones.place(x=600,y=250,width=400,height=100)
        # Boton de play
        playBtn = Button(contenedorBotones,text=">",command=self.ReproducirCancion,width=6,height=1,font=("fonatica",12),fg="black",bg="grey").grid(row=0,column=0,padx=10,pady=5)
        # Boton de Pause
        pausaOnBtn = Button(contenedorBotones,text="||",command=self.pausarCancion,width=8,height=1,font=("fonatica",12),fg="black",bg="grey").grid(row=0,column=1,padx=10,pady=5)
        # Boton de Stop
        stopBtn = Button(contenedorBotones,text="[]",command=self.detenerCancion,width=6,height=1,font=("fonatica",12),fg="black",bg="grey").grid(row=0,column=2,padx=10,pady=5)
        
        
    # Definiendo las funciones para la ejecucion de las canciones
    def ReproducirCancion(self):
        # Mostrando el titulo de la canción
        self.cancion.set(self.listaCanciones.get(ACTIVE))
        print(self.estado.get())
        if self.estado.get() == "||":
            self.desPausar()
        else:    
            # Mostrando el estado de la ejecucion
            self.estado.set(">>..")
            # Cargando la cancion seleccionada
            pygame.mixer.music.load(self.listaCanciones.get(ACTIVE))
            # Ejecutando la cancion seleccionada
            pygame.mixer.music.play()
    
    def pausarCancion(self):
        # Mostrando el estado de la ejecucion
        self.estado.set("||")
        # Pausando la cancion
        pygame.mixer.music.pause()
    
    def detenerCancion(self):
        # Mostrando el estado de la ejecucion
        self.estado.set("[]")
        # Deteniendo cancion
        pygame.mixer.music.stop()
    
    def desPausar(self):
        # Mostrando el estado de la ejecucion
        self.estado.set(">>..")
        # Ejecutando cancion despues de pausada
        pygame.mixer.music.unpause()
    
    def seleccionarRuta(self):
        directorio = filedialog.askdirectory()
        self.directorio.set(directorio)
        # Seleccionando directorio de las canciones
        os.chdir(directorio)
        # Obteniendo cancioness
        canciones = os.listdir()
        # Borrando la lista cargada previamente
        self.listaCanciones.delete(0,END)
        # Insertando canciones en el playlist
        for track in canciones:
            if track.split('.')[-1] in self.aceptados:
                self.listaCanciones.insert(END,track)


       
        
# Creating TK Container
container = Tk()
# Passing container to ReproductorMusical Class
ReproductorMusical(container)
# container Window Looping
container.mainloop()
