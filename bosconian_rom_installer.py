#!/usr/bin/env python3
import os
import sys
import zipfile
import tempfile
import shutil
import hashlib

# Bosconian Namco version 5

NAMCO_V5_FILES = [
    "bos3_1.3n", "bos1_2.3m", "bos1_3.3l", "bos1_4b.3k",    #cpu
    "bos1_5c.3j","bos3_6.3h",                               #sub
    "bos1_7.3e",                                            #sub2
    "bos1_14.5d",                                           #gfx1
    "bos1_13.5e",                                           #gfx2
    "bos1-4.2r",                                            #gfx3
    "bos1-5.4m",                                            #proms ( lookup table )
    "50xx.bin", "51xx.bin","52xx.bin","54xx.bin",           #mcu
    "bos1_9.5n","bos1_10.5m","bos1_11.5k"                   #speech roms

]



NAMCO_V5_CHK = {
    "bos3_1.3n": "f1d4625a9921214bccf4d074d6d83b3de085ee84360e6c346304e1f211dab9b9", 
    "bos1_2.3m": "43933d38b56f0bcafbd4601a498496ebd2e4af552a2bc9c0ecba032adb00f3d9",
    "bos1_3.3l": "57947357a93f06cd9c5ee72dd63ea59d390aea2a56ac9c1c9e023fae7889e53f",
    "bos1_4b.3k": "42316af8dffdf7b4c2284bdcb315a9a719bc99e5acec8dcf715d8b78cd391dfa",
    "bos1_5c.3j": "106db3b75260c17787f7439e995ae672aca6ff3b9d015c9c64e8d9e317d8967b",
    "bos3_6.3h": "1f833dd97a1eed810ef246a9d2c7613bb8f2285a43cd10736a1504e7e1f6536f",
    "bos1_7.3e": "314a1fcf733843982a21ab76e3ad7b193f5c04d82fe29c3ec56834f786f57e09",
    "bos1_14.5d": "e90c9332d7897bfc5348bb1cf8c74560b378630517d3b16f51a01469389e3fb7",
    "bos1_13.5e": "de1ad4510a5788127190f532d9184a8ee30f973a0c3db77410dc561cc715602a",
    "bos1-4.2r": "2979246f2393c76975840169819852644be55b6a7da7443bad4ee72979dd2115",
    "bos1-5.4m": "34de768158dcb008573a2d2a86d887e5d322c6942662866e75fbb48043e76546",
    "50xx.bin": "8b0963bbb7049a1a5725c4948f22680272ee7808020f918f7cd1599297bdca1b",
    "51xx.bin": "bd1c1fddde888550611fdb4ae29bc06d8ac2d2c6a2771ebbff243ec109caf26e",
    "52xx.bin": "08e2adc65c137938147b6831665844427287eb7fab078b0860a1b1fb4a5319ff",
    "54xx.bin": "85c8570b91342ab729bd775c500a3e7245d655a0bab2fed6356e37ea388848e8",
    "bos1_9.5n": "4f5c0e99298e736dee33f4329747c2b7b7818d6eef7c3664dd1d959db856f4ac",
    "bos1_10.5m": "7e403198005e1c18434b439446eec185f6ea76a4afaa628e6358badd126ce897",
    "bos1_11.5k": "8bd968440c7b603a7c18a85f2b3935d5e6d54d7752ef6c2c4b60516fdd34c10c"
}



# Bosconian Midway 

MIDWAY_FILES = [
    "3n", "3m", "3l", "3k",                                 #cpu
    "3j","3h",                                              #sub
    "2900.3e",                                              #sub2
    "5300.5d",                                              #gfx1
    "5200.5e",                                              #gfx2
    "prom.2d",                                              #gfx3
    "bosco.4m",                                             #proms ( lookup table )
    "50xx.bin", "51xx.bin","52xx.bin","54xx.bin",           #mcu
    "4900.5n","5000.5m","5100.5l"                   #speech roms
]



MIDWAY_CHK = {
    
    "3n": "7d575054809da370fea79ed036b8f6c3c768cbbacb1a445df05026a46fe92040", 
    "3m": "7bcb4dbf0d85bfd1da7d92df465243602dd07c8d43999e2ef563598b206b8920",
    "3l": "20fc077c447bf8d075ec4674383e9a85017e41d13d4a8cdd5f142a82e2ea7fac",
    "3k": "17155e35e7d1db41d780376b566a8b4100dae8ae02bccb41c292fedd052c1499",
    "3j": "fbbc2f83080a022b907c9502a8316c89119057303a722cbafaa47e1198781581",
    "3h": "4d16f7f8a49b3c4e7007b3d6c6d864dd04d12f227689f30c76824c080656f0e2",
    "2900.3e": "314a1fcf733843982a21ab76e3ad7b193f5c04d82fe29c3ec56834f786f57e09",
    "5300.5d": "e90c9332d7897bfc5348bb1cf8c74560b378630517d3b16f51a01469389e3fb7",
    "5200.5e": "de1ad4510a5788127190f532d9184a8ee30f973a0c3db77410dc561cc715602a",
    "prom.2d": "2979246f2393c76975840169819852644be55b6a7da7443bad4ee72979dd2115",
    "bosco.4m": "34de768158dcb008573a2d2a86d887e5d322c6942662866e75fbb48043e76546",
    "50xx.bin": "8b0963bbb7049a1a5725c4948f22680272ee7808020f918f7cd1599297bdca1b",
    "51xx.bin": "bd1c1fddde888550611fdb4ae29bc06d8ac2d2c6a2771ebbff243ec109caf26e",
    "52xx.bin": "08e2adc65c137938147b6831665844427287eb7fab078b0860a1b1fb4a5319ff",
    "54xx.bin": "85c8570b91342ab729bd775c500a3e7245d655a0bab2fed6356e37ea388848e8",
    "4900.5n": "4f5c0e99298e736dee33f4329747c2b7b7818d6eef7c3664dd1d959db856f4ac",
    "5000.5m": "7e403198005e1c18434b439446eec185f6ea76a4afaa628e6358badd126ce897",
    "5100.5l": "8bd968440c7b603a7c18a85f2b3935d5e6d54d7752ef6c2c4b60516fdd34c10c"
}



def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def verify_checksums(temp_path,EXPECTED_CHKSM,EXPECTED_FILES):
    for file in EXPECTED_FILES:
        file_path = os.path.join(temp_path, file)
        calculated_checksum = calculate_sha256(file_path)
        expected_checksum = EXPECTED_CHKSM[file]
        if calculated_checksum != expected_checksum:
            print(f"Error: Checksum mismatch for {file}")
            print(f"Expected: {expected_checksum}")
            print(f"Calculated: {calculated_checksum}")
            sys.exit(1)

def main():

    # set pointer to particular version of Bosconian.
    EXPECTED_FILES = ""
    EXPECTED_CHKSM = {}
    
    print("Bosconian for MEGA65: ROM Installer")
    print("================================\n")
    if len(sys.argv) != 3:
        print("The Bosconian core expects the files generated by this script located in the folder /arcade/Bosconian on your SD card.")
        print("This script supports the following versions of Bosconian.\n")
        print("bosco             Bosconian - Star Destroyer (version 5)            (Namco, 1981)")
        print("boscomd           Bosconian - Star Destroyer (Midway, new version)  (Namco (Midway license), 1981)")
        print("For example, To run Midway version 5\n")
        print("Download this ZIP file from : https://wowroms.com/en/roms/mame-0.139u1/Bosconian-midway-set-1/3707.html")
        print("Or search the web for: mame Bosconian midway version 5\n")
        print("Usage: script.py <path to the zip file> <output_folder>")
        sys.exit(1)
      

    if len(sys.argv) > 1:
        argument_value = sys.argv[1]
        fileName = os.path.split(argument_value)[1]
        if fileName == "boscomd.zip":             # Bosconian NAMCO version 5
            EXPECTED_FILES=MIDWAY_FILES
            EXPECTED_CHKSM=MIDWAY_CHK
        elif fileName == "bosco.zip":     # Bosconian Midway
            EXPECTED_FILES=NAMCO_V5_FILES
            EXPECTED_CHKSM=NAMCO_V5_CHK
        
        else:
            print ("No match found for",sys.argv[1],"\n")
            print ("Suitable roms are bosco.zip boscocmd.zip\n")
            return
    

    rom_zip_path = sys.argv[1]
    output_folder = sys.argv[2]

    if not os.path.exists(output_folder):
        print(f"Creating output folder: {output_folder}")
        os.makedirs(output_folder)

    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Extracting files to temporary directory: {temp_dir}")
        try:
            with zipfile.ZipFile(rom_zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
                missing_files = [f for f in EXPECTED_FILES if not os.path.isfile(os.path.join(temp_dir, f))]
                if missing_files:
                    print(f"Error: Missing files in the provided zip file: {', '.join(missing_files)}")
                    sys.exit(1)

                print("Verifying checksums...")
                verify_checksums(temp_dir,EXPECTED_CHKSM,EXPECTED_FILES)

                
                # rom1
                print("Merging files and copying to output folder...")
                with open(os.path.join(output_folder, "rom1.rom"), "wb") as rom1:
                    for part in [EXPECTED_FILES[0], EXPECTED_FILES[1], EXPECTED_FILES[2], EXPECTED_FILES[3]]: 
                        print(f"Appending {part} to rom1.rom")
                        with open(os.path.join(temp_dir, part), "rb") as f:
                            rom1.write(f.read())
                            
                # rom2
                with open(os.path.join(output_folder, "rom2.rom"), "wb") as rom2:
                    for part in [EXPECTED_FILES[4],EXPECTED_FILES[5]]: 
                        print(f"Appending {part} to rom2.rom")
                        with open(os.path.join(temp_dir, part), "rb") as f:
                            rom2.write(f.read())           
                            
                 # rom3
                with open(os.path.join(output_folder, "rom3.rom"), "wb") as rom3:
                    for part in [EXPECTED_FILES[6]]: 
                        print(f"Copying {part} to rom3.rom")
                        with open(os.path.join(temp_dir, part), "rb") as f:
                            rom3.write(f.read())
                            
                with open(os.path.join(output_folder, "gfx1.rom"), "wb") as gfx1:
                    for part in [EXPECTED_FILES[7]]:
                        print(f"Copying {part} to gfx1.rom")
                        with open(os.path.join(temp_dir, part), "rb") as f:
                            gfx1.write(f.read())
                    

                with open(os.path.join(output_folder, "gfx2.rom"), "wb") as gfx2:
                    for part in [EXPECTED_FILES[8],EXPECTED_FILES[8]]:
                        print(f"Appending {part} to gfx2.rom")
                        with open(os.path.join(temp_dir, part), "rb") as f:
                            gfx2.write(f.read())
                  
                
                with open(os.path.join(output_folder, "gfx3.rom"), "wb") as gfx3:
                    for part in [EXPECTED_FILES[9]]:
                        print(f"Copying {part} to gfx3.rom")
                        with open(os.path.join(temp_dir, part), "rb") as f:
                            gfx3.write(f.read())
                #prom           
                with open(os.path.join(output_folder, "bos1-5.4m"), "wb") as prom:
                    for part in [EXPECTED_FILES[10]]:
                        print(f"Copying {part} to bos1-5.4m")
                        with open(os.path.join(temp_dir, part), "rb") as f:
                            prom.write(f.read())
                
                #digitized speech
                with open(os.path.join(output_folder, "bos1_9.5n"), "wb") as sp:
                    for part in [EXPECTED_FILES[15]]:
                        print(f"Copying {part} to bos1_9.5n")
                        with open(os.path.join(temp_dir, part), "rb") as f:
                            sp.write(f.read())
                            
                with open(os.path.join(output_folder, "bos1_10.5m"), "wb") as sp:
                    for part in [EXPECTED_FILES[16]]:
                        print(f"Copying {part} to bos1_10.5m")
                        with open(os.path.join(temp_dir, part), "rb") as f:
                            sp.write(f.read())
               
                with open(os.path.join(output_folder, "bos1_11.5k"), "wb") as sp:
                    for part in [EXPECTED_FILES[17]]:
                        print(f"Copying {part} to bos1_11.5k")
                        with open(os.path.join(temp_dir, part), "rb") as f:
                            sp.write(f.read())
                            
                #50xx-52xx    
                for filename in [EXPECTED_FILES[11],EXPECTED_FILES[12], EXPECTED_FILES[13],EXPECTED_FILES[14]]:
                    print(f"Copying {filename} to output folder")
                    shutil.copy(os.path.join(temp_dir, filename), output_folder)
                
                
                print("Files extracted and merged successfully.")
                print("Cleaning up temporary files...")
                

        except FileNotFoundError:
            print(f"Error: ZIP file not found: {rom_zip_path}")
            sys.exit(1)
        except zipfile.BadZipFile:
            print(f"Error: Invalid or corrupted ZIP file: {rom_zip_path}")
            sys.exit(1)

if __name__ == "__main__":
    main()
