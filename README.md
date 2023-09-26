Bosconian - Star Destroyer for MEGA65
=====================================

Bosconian is a classic arcade video game that was first released in 1981 by Namco. Developed during the golden age of arcade gaming, Bosconian stands out as an innovative and engaging space shooter that left a lasting impact on the gaming industry.

Bosconian is known for its unique gameplay mechanics that set it apart from other space shooters of its time. In Bosconian, players assume the role of a starship pilot navigating through space in a top-down perspective. The goal is to clear a series of enemy bases, each packed with hostile ships, mines, and defensive installations. Unlike many other shooters, Bosconian's levels are not linear but rather open-ended, allowing players to explore and engage enemies on their terms.

The player's ship is equipped with both forward-firing lasers and torpedoes that can be launched backward. The dual firing options add a strategic layer to the gameplay, as players must carefully manage their ammunition and choose the right weapon for the situation. To advance through the levels, players must destroy specific enemy formations, destroy the enemy bases' core reactors, and avoid or eliminate the threats that come their way.

This core is based on the
[MiSTer](https://github.com/https://github.com/MiSTer-devel/Arcade-Bosconian_MiSTer)
Bosconianm core which
itself is based on the work of [many others](AUTHORS).

[Muse aka sho3string](https://github.com/sho3string)
ported the core to the MEGA65 in 2023.

The core uses the [MiSTer2MEGA65](https://github.com/sy2002/MiSTer2MEGA65)
framework and [QNICE-FPGA](https://github.com/sy2002/QNICE-FPGA) for
FAT32 support (loading ROMs, mounting disks) and for the
on-screen-menu.

How to install the Bosconian core on your MEGA65
---------------------------------------------

1. **Download ROM**: Download the Bosconian MAME ROM ZIP file (do not unzip!) from the internet.
   Search for bosco.zip or boscomd.zip. Some roms are not merged correctly so you may have
   to search until you find one that works with the Python script below.
 
3. **Download the Python script**: Download the provided Python script that
   prepares the ROMs such that the Bosconian core is able to use it from
   [Link](https://github.com/sho3string/BosconianMEGA65/blob/master/bosconian_rom_installer.py).

4. **Run the Python script**: Execute the Python script to create a folder
   with the ROMs. 
   Use the command `python bosconian_rom_installer.py <path to the zip file> <output_folder>`.

   ROM files within the zip arhive are automatically evaluated for the correct SHA256 checksums.

5. **Copy the ROMs to your MEGA65 SD card**: Copy the generated folder with
   the ROMs to your MEGA65 SD card. You can use either the bottom SD card tray
   of the MEGA65 or the tray at the backside of the computer (the latter has
   precedence over the first).
   The ROMs need to be in the folder `arcade/bosconian`.
   
   Copy the boscfg provided in 'arcade/bosconian`.

   The script supports the following versions of Bosconian. 

   bosco             Bosconian - Star Destroyer (version 5)              (Namco, 1981)  
   boscomd           Bosconian - Star Destroyer (Midway, new version)    (Namco (Midway license), 1981)  

   I may add other versions of Bosconian to the install script later or you can do your own.
   

7. **Setting up dip switches**

   We have provided menu items in the core to select between Namco & Midway dip configuration settings.
   It is important to select the correct one after copying the files to /arcade/bosconian.

   To do this, go to Game Setup after pressing the 'HELP' key, set your software version then set the individual
   dip switches for that version in the dip section. 

   Once done, press the reset switch on the MEGA65 to load the new settings.

8. **Customising your game**

  There are two dip switch banks of 8 switches on Bosconian boards which differ slightly between Namco and Midway versions.

  Each switch facitates the ability to customise your game. For example, increasing or reducing the game difficulty.
     
     1. Namco [Link](http://www.arcaderestoration.com/gamedips/991/All/Bosconian.aspx)  
  
  Sample dip switch positions for Namco
  
  <img src="https://github.com/sho3string/BosconianMEGA65/assets/36328867/68739970-5544-4906-b97f-815071f5dd9c" width="219" height="304">  
  
     2. Midway  
     Whilst I couldn't find DIP switch documentation via the web, you can check the MAME driver ( boscomd )
     for a description of each switch. See below for a sample.
  
  Sample dip switch positions for Midway
  
  <img src="https://github.com/sho3string/BosconianMEGA65/assets/36328867/d4d07215-5fa9-43ca-b668-631a7a0163a4" width="219" height="304">  
  
  The above DIP configurations are the defaults used in the MEGA65 Core, so there is no need to configure these for the first time to start playing
   
   
    
