#Set-Location -Path ".\backend\training_scripts\build"
python ./backend/training_scripts/Build_Domain_File.py
python ./backend/training_scripts/Build_NLU_File.py
python ./backend/training_scripts/Build_Stories_File.py

