
### To install the pycryptodome library ####
# sudo apt install python3-pip
# sudo pip3 install pycryptodomex

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from progress.spinner import MoonSpinner
import sys

# The name of the source file
SOURCE_FILE_NAME = None

# The AES block size must always be 16 bytes
BLOCK_SIZE = 16

# Encryption key (for AES must be 16, 24, or 32 bytes!)
ENCRYPTION_KEY = b'Sixteen byte key'

# The destination file name
DEST_FILE_NAME = "aes_encrypted_file.bin"

# Make sure the arguments were specified
if len(sys.argv) < 2:
	print("USAGE: " + sys.argv[1] + " <SOURCE FILE NAME>")
	exit(1)

# Get the source file name
SOURCE_FILE_NAME = sys.argv[1]

# The key (must be 16 bytes)
key = ENCRYPTION_KEY

# Set up the AES encryption class
encCipher = AES.new(key, AES.MODE_ECB)

# The source file
sourceFile = open(SOURCE_FILE_NAME, "rb")

# The destination file
destFile = open(DEST_FILE_NAME, "wb")

# The counter for the bar


# Read a block of plaintext
plainBytes = sourceFile.read(16)


# Create a progress bar
spinner = MoonSpinner('Encrypting ' + SOURCE_FILE_NAME + ' to create output file ' + DEST_FILE_NAME + "...")

# Go through the source file
while plainBytes:
	
	# Anything left to encrypt?	
	if plainBytes:
		
		# Should we pad?
		if len(plainBytes) < 16:
		
			# Pad it!
			plainBytes = pad(plainBytes, BLOCK_SIZE)
	
		# Encrypt!
		cipherBytes = encCipher.encrypt(plainBytes)
	
		# Save the contents
		destFile.write(cipherBytes)
	
	# Read a block of plaintext
	plainBytes = sourceFile.read(16)
	
	# Update the progress bar
	spinner.next()
# Close the files
sourceFile.close()
destFile.close()
