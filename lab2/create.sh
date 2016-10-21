sudo kill $(pgrep zook)
sudo make clean 
sudo make
sudo make setup
sudo ./zookld zook.conf &
