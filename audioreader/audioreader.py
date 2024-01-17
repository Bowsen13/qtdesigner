from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QFile, QIODevice, QUrl, QTime


class Audioreader:
    
    main   = None
    player = None
    audio_output   = None
    send_to_player = False
    duration = 0
    can_stop = False
    tamere   = None
    
    def __init__(self, instance_mainwindow, inst_audio_output, inst_player):
        # classes instances
        
        Audioreader.main = instance_mainwindow
        Audioreader.audio_output = inst_audio_output
        Audioreader.player = inst_player
        
        main         = Audioreader.main
        audio_output = Audioreader.audio_output
        player       = Audioreader.player
        

        # setup
        audio_output.setVolume(Audioreader.main.verslider_audio_volume.value())
        player.setAudioOutput(Audioreader.audio_output)
        Audioreader.set_pbs_enabled(False)
        
        # event system and actions
        main.actionOpen.triggered.connect(Audioreader.open_audio)
        main.pb_play .clicked.connect(Audioreader.play_audio)
        main.pb_pause.clicked.connect(Audioreader.pause_audio)
        main.pb_stop .clicked.connect(Audioreader.stop_audio)
        main.pb_mute .clicked.connect(Audioreader.mute_audio)
        main.verslider_audio_volume  .sliderMoved .connect(Audioreader.volume_slider_changed)
        main.horslider_audio_duration.sliderMoved .connect(Audioreader.on_slider_change)
        main.horslider_audio_duration.valueChanged.connect(Audioreader.on_slider_value_changed)
        
        player.positionChanged.connect(Audioreader.position_changed)
        player.durationChanged.connect(Audioreader.duration_changed)
        player.mediaStatusChanged.connect(Audioreader.status_changed)

    # functions
    
    def open_audio():
        # objectif : ouvre un fichier audio dans la source du Qmedia; set enable btns
        fileName, _ = QFileDialog.getOpenFileName(Audioreader.main, 'nom de ma fenetre')
        print(f'filename = {fileName}')
        print(f'_ = {_}')
        if fileName !='':
            Audioreader.player.setSource(QUrl.fromLocalFile(fileName))
            Audioreader.set_pbs_enabled(True)
         
    def play_audio():
        player = Audioreader.player
        if player.position != player.duration :
            print('play')
            player.play()
            
    def pause_audio():
        print('pause audio')
        Audioreader.player.pause()
            
    def stop_audio():
        print('stop audio')
        Audioreader.player.stop()
            
    def mute_audio():
        audio_output = Audioreader.audio_output
        if audio_output.isMuted() == False :
            audio_output.setMuted(True)
        else:
            audio_output.setMuted(False)
      
    def position_changed(position):
        # objectif   : met le slider sur le slide a la position relative de l'avancement du fichier audio,
        #              change les labels en temps reel
        # parametres : self = Audioreader(); position = position du media
        # order      : needs to be called after setting self.duration ?
        
        slider = Audioreader.main.horslider_audio_duration
        
        if (slider.maximum() != Audioreader.player.duration()):
            slider.setMaximum(Audioreader.player.duration())
        
        slider.setValue(position)
        Audioreader.set_labels_media_slider(position) # remettre juste position
         
    def duration_changed(duration):
        # objectif   : converti la taille de duree du slider en fonction de la duree max de l'audio
        # parametres : self -> Audioreader
        Audioreader.main.horslider_audio_duration.setRange(0, duration)
        Audioreader.duration = duration
        Audioreader.set_labels_media_slider(Audioreader.player.position())
        print('duration have changed')
        Audioreader.set_pbs_enabled(True)
    
    def volume_slider_changed(position):
        Audioreader.audio_output.setVolume(position / 100)
    
    def on_slider_change(position):
        # objectif : if the slider moved, set the media's pos relative to the slider's pos;
        #            enable or not the stop button
        Audioreader.player.setPosition(position)
    
    def on_slider_value_changed(value):
        # objective  : if we are at the max value, set stop btn false
        # parameters : self = Audioreader; value = slider's value
        pb_stop = Audioreader.main.pb_stop
        if value == Audioreader.main.horslider_audio_duration.maximum():
            pb_stop.setEnabled(False)            
    
    def set_labels_media_slider(position):
        # objective  : doit set quand : le media est lance              #uncheck
        #                             le media est en cour de lecture #check
        # parameters : self = AudioReader(); position = self.player.position, the media's position
        duration = Audioreader.duration
        
        seconds = (position / 1000)    % 60
        minutes = (position / 60000)   % 60
        hours   = (position / 2600000) % 24
                
        # penser aux priorites operatoire
        seconds_left = ((duration - position) / 1000)    % 60
        minutes_left = ((duration - position) / 60000)   % 60
        hours_left   = ((duration - position) / 2600000) % 24
        
        time      = QTime(hours, minutes, seconds)
        time_left = QTime(hours_left, minutes_left, seconds_left)
        
        Audioreader.main.label_tps_actu.setText(time.toString())
        Audioreader.main.label_tps_left.setText(f'- {time_left.toString()}')
    
    def set_pbs_enabled(bool):
        # objective  : set pb state accordingly to the bool
        # parameters : self = AudioReader(); bool = boolean for setEnabled
        Audioreader.main.pb_stop.setEnabled(bool)
        Audioreader.main.pb_play.setEnabled(bool)
        Audioreader.main.pb_pause.setEnabled(bool)
    
    def status_changed(status):
        # objective  : if the media's status changed, set pb_stop's enable state
        # parameters : self = Audioreader; status = media's status
        pb_stop = Audioreader.main.pb_stop
        
        if   status == Audioreader.player.MediaStatus(2) or status == Audioreader.player.MediaStatus(6):
            pb_stop.setEnabled(False)
            
        elif status != Audioreader.player.MediaStatus(2) and status != Audioreader.player.MediaStatus(6):
            pb_stop.setEnabled(True)
    
    def set_source(file_name):
        player = Audioreader.player
        player.setSource(file_name)
        
        if file_name !='':
            player.setSource(file_name)
            Audioreader.set_pbs_enabled(True)
     
    def cartouche_clicked():
        print('cartouche clicked depuis  audioreader')
        print(f'duration : ')
        

                
    
       