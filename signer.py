import os, random, struct, re
import sys
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA 
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA512
from base64 import b64encode, b64decode 

##################################################
# Loads the RSA key object from the location
# @param keyPath - the path of the key
# @return - the RSA key object with the loaded key
##################################################
def loadKey(keyPath):
	
	# The RSA key
	key = None
	
	# Open the key file
	with open(keyPath, 'r') as keyFile:
		
		# Read the key file
		keyFileContent = keyFile.read()
		
		# Decode the key
		decodedKey = b64decode(keyFileContent)
		
		# Load the key
		key = RSA.importKey(decodedKey)

	# Return the key
	return key	
		

##################################################
# Signs the string using an RSA private key
# @param sigKey - the signature key
# @param string - the string
##################################################
def digSig(sigKey, string):
	
	# TODO: return the signature of the file

	# First, lets compute the SHA-512 hash of the data
	dataHash = SHA512.new(string).hexdigest()

	# Lets generate the signature by encrypting our hash with the private key
	dataSig = sigKey.sign(dataHash, '')

	# Return the signature of the file
	return dataSig

##########################################################
# Returns the file signature
# @param fileName - the name of the file
# @param privKey - the private key to sign the file with
# @return fileSig - the file signature
##########################################################
def getFileSig(fileName, privKey):
	
	# TODO:
	# 1. Open the file
	with open(fileName, 'r') as keyFile:
		
		# 2. Read the contents
		keyFileContent = keyFile.read()

		# 3. Compute the SHA-512 hash of the contents
		dataHash = SHA512.new(keyFileContent.encode('utf-8')).hexdigest()

		# 4. Sign the hash computed in 4. using the digSig() function
		# you implemented.
		fileSig = privKey.sign(dataHash.encode('utf-8'), '')
		
	# 5. Return the signed hash; this is your digital signature
	return fileSig

	
###########################################################
# Verifies the signature of the file
# @param fileName - the name of the file
# @param pubKey - the public key to use for verification
# @param signature - the signature of the file to verify
##########################################################
def verifyFileSig(fileName, pubKey, signature):
	
	# TODO:
	# 1. Read the contents of the input file (fileName)
	with open(fileName, 'r') as keyFile:
		keyFileContent = keyFile.read()

		# 2. Compute the SHA-512 hash of the contents
		dataHash = SHA512.new(keyFileContent.encode('utf-8')).hexdigest()

		# 3. Use the verifySig function you implemented in
		# order to verify the file signature
		isVer = verifySig(dataHash, signature, pubKey)

	# 4. Return the result of the verification i.e.,
	# True if matches and False if it does not match
	return isVer
	
	

############################################
# Saves the digital signature to a file
# @param fileName - the name of the file
# @param signature - the signature to save
############################################
def saveSig(fileName, signature):

	# TODO: 
	# Signature is a tuple with a single value.
	# Get the first value of the tuple, convert it
	# to a string, and save it to the file (i.e., indicated
	# by fileName)
	
	# Convert the signature into a string
	tupleToStr = ''.join(str(signature) for v in signature)

	try: 
		# Open the file to write to
		with open(fileName, 'w') as sigFile:
			sigFile.write(tupleToStr)
			sigFile.close()
	except:
		print 'Error writing to the target file.'
		exit(1)	

###########################################
# Loads the signature and converts it into
# a tuple
# @param fileName - the file containing the
# signature
# @return - the signature
###########################################
def loadSig(fileName):
	
	# TODO: Load the signature from the specified file.
	# Open the file, read the signature string, convert it
	# into an integer, and then put the integer into a single
	# element tuple
	with open(fileName, 'r') as keyFile:
		#reads the file
		keyFileContent = keyFile.read()

		#remove unwanted characters 
		result = re.sub('[^0-9]','', keyFileContent)

		#convert to int
		keyInt = int(result)

		#convert to tuple
		keyTuple = (keyInt,)

		#print tuple to verify
		print keyTuple
		return keyTuple


	
#################################################
# Verifies the signature
# @param theHash - the hash 
# @param sig - the signature to check against
# @param veriKey - the verification key
# @return - True if the signature matched and
# false otherwise
#################################################
def verifySig(theHash, sig, veriKey):
	
	# TODO: Verify the hash against the provided
	# signature using the verify() function of the
	# key and return the result

	# Now, verify the signature against the hash. I.e., the verify function
	# will decrypt the digital signature using the public key and then compare
	# the decrypted result to the dataHash

	if veriKey.verify(theHash, sig) == True:
		print 'Signatures match!'
		return True
	else:
		print 'Signatures DO NOT MATCH!'
		return False			



# The main function
def main():
	
	# Make sure that all the arguments have been provided
	if len(sys.argv) < 5:
		print("USAGE: " + sys.argv[0] + " <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME>")
		exit(-1)
	
	# The key file
	keyFileName = sys.argv[1]
	
	# Signature file name
	sigFileName = sys.argv[2]
	
	# The input file name
	inputFileName = sys.argv[3]
	
	# The mode i.e., sign or verify
	mode = sys.argv[4]

	# TODO: Load the key using the loadKey() function provided.
	key = loadKey(keyFileName)
	
	# We are signing
	if mode == "sign":
		
		# TODO: 1. Get the file signature
		#       2. Save the signature to the file
		inputFileSig = getFileSig(inputFileName, key)
		print 'Here is the digital signature(signed hash):\n', inputFileSig

		saveSig(sigFileName, inputFileSig)
		print "Signature saved to file", sigFileName

	# We are verifying the signature
	elif mode == "verify":
		
		# TODO Use the verifyFileSig() function to check if the
		# signature signature in the signature file matches the
		# signature of the input file
		sigFileSig = loadSig(sigFileName)

		isVerified = verifyFileSig(inputFileName, key, sigFileSig)
		
	else:
		print "Invalid mode", mode	

### Call the main function ####
if __name__ == "__main__":
	main()
