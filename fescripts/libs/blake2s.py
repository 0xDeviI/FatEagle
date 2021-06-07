from fescripts.libs.cryptopals_lib import *

class Blake2(object):
	def __init__(self, version=256, key=None, salt=None, personalization=None):
		self.permutations = [
			[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15],
			[14,10, 4, 8, 9,15,13, 6, 1,12, 0, 2,11, 7, 5, 3],
			[11, 8,12, 0, 5, 2,15,13,10,14, 3, 6, 7, 1, 9, 4],
			[ 7, 9, 3, 1,13,12,11,14, 2, 6, 5,10, 4, 0,15, 8],
			[ 9, 0, 5, 7, 2, 4,10,15,14, 1,11,12, 6, 8, 3,13],
			[ 2,12, 6,10, 0,11, 8, 3, 4,13, 7, 5,15,14, 1, 9],
			[12, 5, 1,15,14,13, 4,10, 0, 7, 6, 3, 9, 2, 8,11],
			[13,11, 7,14,12, 1, 3, 9, 5, 0,15, 4, 8, 6, 2,10],
			[ 6,15,14, 9,11, 3, 0, 8,12, 2,13, 7, 1, 4,10, 5],
			[10, 2, 8, 4, 7, 6, 1, 5,15,11, 9,14, 3,12,13, 0],
			[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15],
			[14,10, 4, 8, 9,15,13, 6, 1,12, 0, 2,11, 7, 5, 3],
			[11, 8,12, 0, 5, 2,15,13,10,14, 3, 6, 7, 1, 9, 4],
			[ 7, 9, 3, 1,13,12,11,14, 2, 6, 5,10, 4, 0,15, 8],
			[ 9, 0, 5, 7, 2, 4,10,15,14, 1,11,12, 6, 8, 3,13],
			[ 2,12, 6,10, 0,11, 8, 3, 4,13, 7, 5,15,14, 1, 9],
			[12, 5, 1,15,14,13, 4,10, 0, 7, 6, 3, 9, 2, 8,11],
			[13,11, 7,14,12, 1, 3, 9, 5, 0,15, 4, 8, 6, 2,10],
			[ 6,15,14, 9,11, 3, 0, 8,12, 2,13, 7, 1, 4,10, 5],
			[10, 2, 8, 4, 7, 6, 1, 5,15,11, 9,14, 3,12,13, 0],
		]

		self.current_length = 0
		self.xor_block = False

		self.__select_version(version)

		#Copy the Buffers in to the IV array
		self.iv = self.buffers[:]

		#Deal with key, salt and personalization if required
		if key != None:
			self.key = bytearray(key[:self.blocksize // 2])
			self.buffers[0] ^= (0x01010000) | (len(self.key) << 8) | ((self.blocksize // 8) * self.output_size)

		else:
			self.key = key
			self.buffers[0] ^= (0x01010000) | ((self.blocksize // 8) * self.output_size)

		if salt != None:
			self.salt = int(salt[:self.blocksize // 8])
			self.buffers[4] ^= asint(self.salt, self.blocksize)
			self.buffers[5] ^= asint((self.salt >> self.blocksize), self.blocksize)

		if personalization != None:
			self.personalization = int(personalization[:self.blocksize // 8])
			self.buffers[6] ^= asint(self.personalization, self.blocksize)
			self.buffers[7] ^= asint((self.personalization >> self.blocksize), self.blocksize)


	def __select_version(self, version):
		#Blake 2s
		if version <= 256:
			self.buffers = [0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A,
							0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19,]

			self.rotations = [16,12,8,7]
			self.blocksize = 32
			self.rounds = 10
			self.output_size = version // self.blocksize

		#Blake2b
		else:
			self.buffers = [0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1,
							0x510e527fade682d1, 0x9b05688c2b3e6c1f, 0x1f83d9abfb41bd6b, 0x5be0cd19137e2179,]
			self.rotations = [32,24,16,63]
			self.blocksize = 64
			self.rounds = 12
			self.output_size = version // self.blocksize

		#raise ValueError("Invalid Blake2 Version {}".format(self.version))
		
	def _set_message(self, message):
		#Convert to bytes if not already
		byte_message = bytearray(message)

		#Set Final Length
		self.final_length = len(message)

		#Pad the data to a multable of the block size
		while len(byte_message) == 0 or len(byte_message) % (self.blocksize * 2) != 0:
			byte_message.append(0x00)

		return byte_message

	def _chacha_quarter_round(self, a, b, c, d, message, round_num, index):
		#Calculate indexes from Permuation table and round_index and offset
		message_index  = self.permutations[round_num][index]
		constant_index = self.permutations[round_num][index+1]

		#Modified first part to include message and round xor
		a = asint((a + b) + message[message_index], self.blocksize)
		d = asint(d ^ a, self.blocksize)
		d = asint(shift_rotate_right(d, self.rotations[0], self.blocksize), self.blocksize)

		c = asint(c + d, self.blocksize)
		b = asint(b ^ c, self.blocksize)
		b = asint(shift_rotate_right(b, self.rotations[1], self.blocksize), self.blocksize)

		#Modified first part to include message and round xor
		a = asint((a + b) + message[constant_index], self.blocksize)
		d = asint(d ^ a, self.blocksize)
		d = asint(shift_rotate_right(d, self.rotations[2], self.blocksize), self.blocksize)

		c = asint(d + c, self.blocksize)
		b = asint(b ^ c, self.blocksize)
		b = asint(shift_rotate_right(b, self.rotations[3], self.blocksize), self.blocksize)

		return [a,b,c,d]


	def _compress_chunk(self, chunk):
		#Start the compress function

		#Create the start of the temp chunks
		temp_chunk = bytes_to_intarray(chunk, (self.blocksize //8), byte_order="little")
		#print(f"message: {[hex(x) for x in temp_chunk]}")

		#Start setting up the temp buffers
		temp_buffers = self.buffers[:] + self.iv[:]

		temp_buffers[12] ^= asint(self.current_length, self.blocksize)
		temp_buffers[13] ^= asint(self.current_length >> self.blocksize, self.blocksize)

		#Do not xor currentlength when it is the last block and there is more than one block
		if self.xor_block:
			temp_buffers[14] ^= (2 **(self.blocksize) -1)

		'''
		Resulting temp_buffers looks like this
		|IV             |IV             |IV              |IV              |
		|IV             |IV             |IV              |IV              |
		|Const ^ Salt   |Const ^ Salt   |Const ^ Salt    |Const ^ Salt    |
		|Const ^ len[0] |Const ^ len[0] |Const ^ len[1]  |Const ^ len[1]  |
		'''
		#print([hex(x) for x in temp_buffers], self.xor_block, hex(self.current_length))

		#Do ChaCha rounds with modifications
		for index in range(self.rounds):
			#Do Each Column
			temp_buffers[0], temp_buffers[4], temp_buffers[8],  temp_buffers[12] = self._chacha_quarter_round(temp_buffers[0], temp_buffers[4], temp_buffers[8],  temp_buffers[12], temp_chunk, index, 0)
			temp_buffers[1], temp_buffers[5], temp_buffers[9],  temp_buffers[13] = self._chacha_quarter_round(temp_buffers[1], temp_buffers[5], temp_buffers[9],  temp_buffers[13], temp_chunk, index, 2)
			temp_buffers[2], temp_buffers[6], temp_buffers[10], temp_buffers[14] = self._chacha_quarter_round(temp_buffers[2], temp_buffers[6], temp_buffers[10], temp_buffers[14], temp_chunk, index, 4)
			temp_buffers[3], temp_buffers[7], temp_buffers[11], temp_buffers[15] = self._chacha_quarter_round(temp_buffers[3], temp_buffers[7], temp_buffers[11], temp_buffers[15], temp_chunk, index, 6)
				
			#Do Each Diagonal
			temp_buffers[0], temp_buffers[5], temp_buffers[10], temp_buffers[15] = self._chacha_quarter_round(temp_buffers[0], temp_buffers[5], temp_buffers[10], temp_buffers[15], temp_chunk, index, 8)
			temp_buffers[1], temp_buffers[6], temp_buffers[11], temp_buffers[12] = self._chacha_quarter_round(temp_buffers[1], temp_buffers[6], temp_buffers[11], temp_buffers[12], temp_chunk, index, 10)
			temp_buffers[2], temp_buffers[7], temp_buffers[8],  temp_buffers[13] = self._chacha_quarter_round(temp_buffers[2], temp_buffers[7], temp_buffers[8],  temp_buffers[13], temp_chunk, index, 12)
			temp_buffers[3], temp_buffers[4], temp_buffers[9],  temp_buffers[14] = self._chacha_quarter_round(temp_buffers[3], temp_buffers[4], temp_buffers[9],  temp_buffers[14], temp_chunk, index, 14)

		#print([hex(x) for x in temp_buffers])

		#Update Buffers
		for x in range(8):
			self.buffers[x] ^= temp_buffers[x] ^ temp_buffers[x+8]

		#print([hex(x) for x in self.buffers])

	def hash(self, message):
		#If has a key then set the first block to the key and add padding to the blocksize
		if self.key != None:
			padded_key = self.key[:]

			for x in range((self.blocksize * 2) - len(padded_key)):
				padded_key.append(0x00)

			message = padded_key + message

		#Setup message with padding and length data
		byte_message = self._set_message(message)

		#Opperate on each of the chunks
		blocks = to_blocks(byte_message, (self.blocksize * 2))


		for index, chunk in enumerate(blocks):

			#Update the current_length
			self.current_length += (len(chunk))

			#Fix Edge Case for padding goes into the next block
			if index == len(blocks) - 1:
				#Last Block
				self.xor_block = True
				self.current_length = self.final_length

			#Compress the message Chunk
			self._compress_chunk(chunk)

		#Convert Intagers to Byte string
		output = b""
		for x in self.buffers[:self.output_size]:
			output += (x).to_bytes((self.blocksize // 8), byteorder='little')

		return output
		
	def hash_digest(self, message):
		return self.hash(message).hex()