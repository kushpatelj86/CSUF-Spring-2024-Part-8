from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP
from progress.spinner import MoonSpinner
import sys

# The name of the source file
SOURCE_FILE_NAME = None

# The destination file name
DEST_FILE_NAME = "rsa_encrypted_file.bin"

# The name of the public key file
PUBLIC_KEY_FILE_NAME = "public-key.pem"

# Make sure the arguments were specified
if len(sys.argv) < 2:
	print("USAGE: " + sys.argv[1] + " <SOURCE FILE NAME>")
	exit(1)

# Get the source file name
SOURCE_FILE_NAME = sys.argv[1]

# Open the source file
file_out = open(DEST_FILE_NAME, "wb")

# Load the key
recipient_key = RSA.import_key(open(PUBLIC_KEY_FILE_NAME).read())

# The source file name
sourceFile = open(SOURCE_FILE_NAME, "rb")

# Encrypt the session key with the public RSA key
cipher_rsa = PKCS1_OAEP.new(recipient_key, hashAlgo=None, mgfunc=None, randfunc=None)

# Read the plaintext bytes
plainBytes = sourceFile.read(2006)

# Create a progress bar
spinner = MoonSpinner('Encrypting ' + SOURCE_FILE_NAME + ' to create output file ' + DEST_FILE_NAME + "...")

# Keep reading and encrypting
while plainBytes:
	

	# Read the plaintext bytes
	if plainBytes:
	
		# Encrypt!
		cipherBytes = cipher_rsa.encrypt(plainBytes)
		
		# Save the bytes
		file_out.write(cipherBytes)
	
	# Read the plaintext bytes
	plainBytes = sourceFile.read(2006)
	
	# Work the progress bar
	spinner.next()

print("")
print("Done!")

# Close the source file
sourceFile.close()
file_out.close()

