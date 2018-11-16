#Start the custom action server by running:
Set-Location -Path "./backend"
python -m rasa_core_sdk.endpoint --actions actions
#invoke-expression 'cmd /c start powershell -Command { python -m rasa_core_sdk.endpoint --actions ./backend/actions }'
