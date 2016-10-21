#!/bin/sh
./kill.sh
./clean-env.sh ./zookld zook-exstack.conf &	
exec gdb -p $(pgrep zookd-exstack)
