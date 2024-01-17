to make run work :
    -change in mainwindow_ui.py the QPushButton for Une_cartouche
    -replace : import.ressources_rc by :
        import ressources.ressources_rc
        from fileexplorer.fileexplorer import File_explorer
        from cartouches.unecartouche import Une_cartouche

to convert .py to .exe:
open auto-py-to-exe :
    - set script location to your script location 
      (eg : D:\Documents\Python\project1\qtdesigner\run.py)
    - on directory
    - window based
    - add additional files : ressources, from our project's folder
    - advanced : --name : put the name of the folder/file.exe
    - settings : set the output directory (where the builded folder will be)
