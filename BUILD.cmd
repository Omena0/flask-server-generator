echo off
echo #############################
echo ### Building GENERATOR.py ###
echo #############################
pyinstaller --noconfirm --i NONE --specpath spec --onefile code/generator.py
echo #######################
echo ### Build complete! ###
echo #######################
timeout /t 3