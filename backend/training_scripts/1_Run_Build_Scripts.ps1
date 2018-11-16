#Set-Location -Path ".\backend\training_scripts\build"
python .\backend\training_scripts\build\Build_Domain_File.py
python .\backend\training_scripts\build\Build_NLU_File.py
python .\backend\training_scripts\build\Build_Stories_File.py

