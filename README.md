Bosconian - Star Destroyer for MEGA65
=====================================

Bosconian is a classic arcade video game that was first released in 1981 by Namco. Developed during the golden age of arcade gaming, Bosconian stands out as an innovative and engaging space shooter that left a lasting impact on the gaming industry.

Bosconian is known for its unique gameplay mechanics that set it apart from other space shooters of its time. In Bosconian, players assume the role of a starship pilot navigating through space in a top-down perspective. The goal is to clear a series of enemy bases, each packed with hostile ships, mines, and defensive installations. Unlike many other shooters, Bosconian's levels are not linear but rather open-ended, allowing players to explore and engage enemies on their terms.

The player's ship is equipped with both forward-firing lasers and torpedoes that can be launched backward. The dual firing options add a strategic layer to the gameplay, as players must carefully manage their ammunition and choose the right weapon for the situation. To advance through the levels, players must destroy specific enemy formations, destroy the enemy bases' core reactors, and avoid or eliminate the threats that come their way.

This core is based on the
[MiSTer](https://github.com/https://github.com/MiSTer-devel/Arcade-Bosconian_MiSTer)
Galaga core which
itself is based on the work of [many others](AUTHORS).

[Muse aka sho3string](https://github.com/sho3string)
ported the core to the MEGA65 in 2023.

The core uses the [MiSTer2MEGA65](https://github.com/sy2002/MiSTer2MEGA65)
framework and [QNICE-FPGA](https://github.com/sy2002/QNICE-FPGA) for
FAT32 support (loading ROMs, mounting disks) and for the
on-screen-menu.

How to install the Bosconian core on your MEGA65
---------------------------------------------

1. **Download ROM**: Download the Galaga ROM ZIP file (do not unzip!) from
  [this link](https://wowroms.com/en/roms/mame-0.37b5/bosconian/118286.html)
  or search the web for "mame galaga midway set 1".

2. **Download the Python script**: Download the provided Python script that
   prepares the ROMs such that the Galaga core is able to use it from
   [Link](https://github.com/sho3string/BosconianMEGA65/blob/master/bosconian_rom_installer.py).

3. **Run the Python script**: Execute the Python script to create a folder
   with the ROMs. 
   Use the command `python bosconian_rom_installer.py <path to the zip file> <output_folder>`.

   ROM files within the zip arhive are automatically evaluated for the correct SHA256 checksums.

5. **Copy the ROMs to your MEGA65 SD card**: Copy the generated folder with
   the ROMs to your MEGA65 SD card. You can use either the bottom SD card tray
   of the MEGA65 or the tray at the backside of the computer (the latter has
   precedence over the first).
   The ROMs need to be in the folder `arcade/bosconian`.
   
   Copy the boscfg provided in 'arcade/galaga`.

   The script supports the following versions of Bosconian. 

   bosco             Bosconian - Star Destroyer (version 5)              (Namco, 1981)
   boscomd           Bosconian - Star Destroyer (Midway, new version)    (Namco (Midway license), 1981)
   

7. **Setting up dip switches**

There are two dip switch banks of 8 switches on Bosconian boards which differ slightly between Namco and Midway versions.
   
   Namco 
   [Link](http://www.arcaderestoration.com/gamedips/991/All/Bosconian.aspx)

   Midway
   Whilst I couldn't easily find DIP switch settings documented via the web, you can check the MAME driver ( boscomd )
   for a description of each switch.
   
   We have provided menu items in the core to select between Namco & Midway dip configuration settings.
   It is important to select the correct one after copying the files to /arcade/bosconian.

   To do this, go to Game Setup after pressing the 'HELP' key, set your software version then set the individual
   dip switches for that version in the dip section. Use the link above to understand what each switch is for.

   Once done, press the reset switch on the MEGA65 to load the new settings.
    
