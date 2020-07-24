from tkinter import *
import pygame
import os

# Defining MusicPlayer Class
class ReproductorMusical:
    
    def __init__(self,container):
        self.container = container
        # Titulo de la ventana
        self.container.title("Music Player")
        # Tamaño
        self.container.geometry("1000x600")
         # Bloquear le cambio de tamaño
        self.container.resizable(width=False, height=False)
        # Iniciar Pygame
        pygame.init()
        # Iniciar Pygame Mixer
        pygame.mixer.init()
        
        self.estado = StringVar()
        self.cancion = StringVar()

        # Frame para el titulo de la cancion
        contenedorCancion = LabelFrame(self.container,text="Título",font=("fonatica",10,"bold"),bg="grey",fg="white",bd=5,relief=FLAT)
        contenedorCancion.place(x=0,y=500,width=600,height=100)
        # Se inserta mensaje del estado en el label del titulo de la cancion
        titulo = Label(contenedorCancion,textvariable=self.cancion,width=30,font=("fonatica",15,"bold"),bg="grey",fg="white").grid(row=0,column=0,padx=10,pady=5)
        # Etiqueta para identificar el estado de ejecucion de la cancion
        estadoCancion = Label(contenedorCancion,textvariable=self.estado,font=("fonatica",15,"bold"),bg="grey",fg="white").grid(row=0,column=1,padx=10,pady=5)

        # Contenedor de botones
        contenedorBotones = LabelFrame(self.container,text="Control Panel",font=("fonatica",15,"bold"),bg="grey",fg="white",bd=5,relief=FLAT)
        contenedorBotones.place(x=600,y=500,width=400,height=100)
        # Boton de play
        playBtn = Button(contenedorBotones,text="Play",command=self.ReproducirCancion,width=6,height=1,font=("fonatica",12),fg="black",bg="grey").grid(row=0,column=0,padx=10,pady=5)
        # Boton de Pause
        pausaOnBtn = Button(contenedorBotones,text="Pause On",command=self.pausarCancion,width=8,height=1,font=("fonatica",12),fg="black",bg="grey").grid(row=0,column=1,padx=10,pady=5)
        # Boton de UnPause
        pausaOffBtn = Button(contenedorBotones,text="Pause Off",command=self.unpause,width=10,height=1,font=("fonatica",12),fg="black",bg="grey").grid(row=0,column=2,padx=10,pady=5)
        # Boton de Stop
        stopBtn = Button(contenedorBotones,text="Stop",command=self.stop,width=6,height=1,font=("fonatica",12),fg="black",bg="grey").grid(row=0,column=3,padx=10,pady=5)
        
        # PLaylist
        contenedorCanciones = LabelFrame(self.container,text="Playlist",font=("fonatica",15,"bold"),bg="black",fg="white",bd=5,relief=FLAT)
        contenedorCanciones.place(x=0,y=0,width=1000,height=500)
        # Scrollbar de la playlist
        scrol_y = Scrollbar(contenedorCanciones,orient=VERTICAL)
        # Insertando listbox de la Playlist
        self.playlist = Listbox(contenedorCanciones,yscrollcommand=scrol_y.set,selectbackground="black",selectmode=SINGLE,font=("fonatica",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Seleccionando directorio de las canciones
        os.chdir(r'C:\Users\alejo\Music')
        # Obteniendo canciones
        songtracks = os.listdir()
        # Insertando canciones en el playlist
        for track in songtracks:
            self.playlist.insert(END,track)
        
    # Definiendo las funciones para la ejecucion de las canciones
    def ReproducirCancion(self):
        # Displaying Selected Song title
        self.cancion.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.estado.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()
    
    def pausarCancion(self):
        # Displaying Status
        self.estado.set("-Paused")
        # Paused Song
        pygame.mixer.music.pause()

       
        
# Creating TK Container
container = Tk()
# Passing container to MusicPlayer Class
ReproductorMusical(container)
# container Window Looping
container.mainloop()
