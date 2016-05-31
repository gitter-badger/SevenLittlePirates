# This software is licensed under the GNU GPL V3.
# This is the official script to generate the starter
# for the BAV3 Console. It is an integral part
# of the setup process for Bave. The starter file was made
# so that a use can start the console easily!
# AL3X V3GAS 2016 (C)

print ("Generating the starter file...")
print ("This could take some time so please be patient...")
file = open('start.sh', 'w')
file = open('start.sh', 'a')
file.write('# This software is licensed under the GNU GPL V3.\n')
file.write('# This is the official starter script for BAV3.\n')
file.write('# AL3X V3GAS 2016 (C).\n')
file.write('\n')
file.write('echo "Starting the BAV3 Console..."\n')
file.write('python2 bave/code/bave.py\n')
file.write('echo "Exiting the BAV3 Console..."\n')
file.write('echo "...done."\n')
file.close()
print ("The file was generated successfully!")
print ("To start the console type 'sh start.sh' or type 'bash start.sh'!")
