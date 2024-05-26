import engine

import sys
from PySide6.QtWidgets import QApplication

import  veiwport_window

if __name__ == '__main__':
    app = QApplication(sys.argv)
 
    viewport = veiwport_window.my_house()
    active_engine = engine.engine_instance("data/world_sections.csv",viewport)
    active_engine.set_game_mode("explore")
    active_engine.run_engine()
    
    app.exec()


    #will close itself and modify the memory_view varible "exit_case"
    #switch this output
        #active_engine.set_game_mode("combat")
        #active_engine.run_engine()
    
    #this will output something apon close, aka smth saying we have left that world file, loop back to switch
        #veiwport = veiwport_window.halo_3()
        #active_engine = engine.engine_instance("data/cutscene.csv",veiwport)
        #active_engine.run_engine()
    
    #switch the output from loop
        #veiwport = veiwport_window.my_house()
        #active_engine = engine.engine_instance("data/world_sections.csv",viewport)
        #active_engine.set_game_mode("explore")
        #active_engine.run_engine()
    





    #veiwport can be set to the window required for each engine instance, as in

        #veiwport = veiwport_window.bradeon_sanderson()

    #and used in the engine from there as
     
        #active_engine.set_mode("dialog")




    #each veiwport template will have a set layout for its assets, and interaction and "end commands"
    #VVWAD files divided by veiwport type specilized for easy loading onto the veiwport template
    #master VVWAD file will contain references to each "end command" for loading of next engine instance


    #engine.py will contain every class. No file other than scripting will contain engine
    #this allows any required data to be passed to any other class, if circularity is unavoidable



    #TO DO:

    #Finish render engine, convert to a widget, add "flash" style sprites and interaction (idk how yet lol)

                            #interaction types:
                                               #begin combat trigger
                                               #loot triggers
                                               #cutscene triggers
                                               #UI interaction (load out managment)
                                               #dialog interaction + cutscene interaction
    
                            #do not need to build these actual classes yet, but code in the "end commands for them"
                                               

    #Finish VVADmap file 

    #a map editing interface will be made to easily add 2d sprits, geometry and backrounds to sections and write to a VVADmap file

    #someone figure how to do UI on the explore state

    #build a character class, replicating what we come up with for UI + character creation veiwport for engine and game 

    #use character class to build a combat veiwport, class, and VVADcombat file template 
                            #build off shoot class for equipment and armourment idk

    #add a "dialoge" viewport template, class and VVADdial file template for the world 

    #add a cutscene viewport template, class, and VVADcut file template

    #what the fuck is quests? 

    #make a function VVADworld with multiple VVADmap, VVADcombat, VVADdial and VVADcut files 

    #Polish that game, document engine, release :)))))))))))))) 







