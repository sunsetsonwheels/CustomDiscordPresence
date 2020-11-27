pyinstaller cdrp.spec
Remove-Item –path "./final" –recurse
New-Item -Path . -Name "final" -ItemType directory 
Copy-Item "dist/cdrp.*" -Destination "final"
Copy-Item "cdrpcfg-template.json" -Destination "final"
Copy-Item "README.md" -Destination "final"
Compress-Archive -Path "final\*" -DestinationPath "final\CustomDiscordPresence-Auto.zip"