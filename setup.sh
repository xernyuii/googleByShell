cp main.py ./google
ln -s google baidu
ln -s google wiki
sudo chmod +x google
sudo chmod +x baidu
sudo chmod +x wiki
sudo mv ./google /usr/local/bin/google
sudo mv ./baidu /usr/local/bin/baidu
sudo mv ./wiki /usr/local/bin/wiki

