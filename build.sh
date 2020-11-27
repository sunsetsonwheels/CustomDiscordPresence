#!/bin/sh
pyinstaller cdrp.spec
rm -r final
mkdir final
cp dist/cdrp final
cp cdrpcfg-template.json final
cp README.md final
cd final
zip CustomDiscordPresence-Auto.zip cdrp cdrpcfg-template.json README.md

