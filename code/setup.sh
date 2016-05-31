# This software is licensed under the GNU GPL V3.
# This is the official install script for SLP!
# This will ONLY work with Termux!
# AL3X V3GAS 2016 (C)

echo "We will start the installation of SLP!"
echo "Make sure you have a stable internet connection!"
echo "Installing Python 2..."
apt install python2
echo "...done."
echo "Installing colorama..."
pip install colorama
echo "...done"
echo "Generating start file..."
python2 generate.py
echo "...done."
echo "Moving the starter file to $HOME..."
cp startSLP.sh $HOME
echo "...done."
echo "The installation has finished!"
echo "To start the console type 'bash startSLP.sh' or 'sh startSLP.sh'!"
exit
