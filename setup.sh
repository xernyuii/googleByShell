cp main.py google
ln -s google baidu
ln -s google wiki
ln -s google translate
chmod +x google
chmod +x baidu
chmod +x wiki
chmod +x translate
mv ./google /usr/local/bin/
mv ./baidu /usr/local/bin/
mv ./wiki /usr/local/bin/
mv ./translate /usr/local/bin/
