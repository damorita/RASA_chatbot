#Check if Action Server is Running. Start Action Server
$ErrorActionPreference= 'silentlycontinue'
$WarningPreference= 'silentlycontinue'

#Set-Location -Path "C:\"
$var = (Test-NetConnection -ComputerName localhost -Port 5055)
if($var.TcpTestSucceeded -ne $true) {invoke-expression 'cmd /c start powershell -Command { python -m rasa_core_sdk.endpoint --actions actions }'}
