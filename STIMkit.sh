#!/bin/bash

cd ..

yes | rm -r STIMkit

git clone https://github.com/sirseb2002/STIMkit/

cp -r ~/STIMkit/Flatworld/* ~/.minecraft/games/com.mojang/minecraftWorlds

$SHELL
