cp main.py google
ln -s google baidu
ln -s google wiki
ln -s google translate
chmod +x google
chmod +x baidu
chmod +x wiki
chmod +x translate
sudo mv ./google /usr/local/bin/
sudo mv ./baidu /usr/local/bin/
sudo mv ./wiki /usr/local/bin/
sudo mv ./translate /usr/local/bin/

