#Set-Location -Path "C:\"

$ErrorActionPreference= 'silentlycontinue'
$WarningPreference= 'silentlycontinue'

$var = (Test-NetConnection -ComputerName localhost -Port 5005)
if($var.TcpTestSucceeded -ne $true) {invoke-expression "cmd /c start powershell -Command { & python -m rasa_core.run --enable_api --endpoints '.\backend\endpoints.yml' -d '.\backend\models\dialogue' -u '.\backend\models\nlu\default\current' -o out.log 
}"}
