# This software is licensed under the GNU GPL V3.
# This is the official script to generate the starter
# for the SLP Console. It is an integral part
# of the setup process for SLP. The starter file was made
# so that a use can start the console easily!
# AL3X V3GAS 2016 (C)

print ("Generating the starter file...")
print ("This could take some time so please be patient...")
file = open('startSLP.sh', 'w')
file = open('startSLP.sh', 'a')
file.write('# This software is licensed under the GNU GPL V3.\n')
file.write('# This is the official starter script for SLP.\n')
file.write('# AL3X V3GAS 2016 (C).\n')
file.write('\n')
file.write('echo "Starting the SLP Console..."\n')
file.write('python2 bave/code/SevenLittlePirates.py\n')
file.write('echo "Exiting the SLP Console..."\n')
file.write('echo "...done."\n')
file.close()
print ("The file was generated successfully!")
print ("To start the console type 'sh startSLP.sh' or type 'bash startSLP.sh'!")
