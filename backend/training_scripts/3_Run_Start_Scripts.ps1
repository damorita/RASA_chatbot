#Check if Action Server is Running. Start Action Server
invoke-expression 'cmd /c start powershell -Command { ./backend/training_scripts/start/Start_Action_Server.ps1 }'

#Start Chat in Terminal
#invoke-expression 'cmd /c start powershell -Command { python "./training_scripts/start/Start_Chat_Terminal.py" }'
python "./backend/training_scripts/start/Start_Chat_Terminal.py"
