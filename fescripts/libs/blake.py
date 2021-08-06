from fescripts.libs.cryptopals_lib import *

class Blake(object):
	def __init__(self, version=512):
		self.round_constant1 = [0x243F6A88, 0x85A308D3, 0x13198A2E, 0x03707344,
								0xA4093822, 0x299F31D0, 0x082EFA98, 0xEC4E6C89,
								0x452821E6, 0x38D01377, 0xBE5466CF, 0x34E90C6C,
								0xC0AC29B7, 0xC97C50DD, 0x3F84D5B5, 0xB5470917,]


		self.round_constant2 = [0x243F6A8885A308D3, 0x13198A2E03707344, 0xA4093822299F31D0, 0x082EFA98EC4E6C89,
								0x452821E638D01377, 0xBE5466CF34E90C6C, 0xC0AC29B7C97C50DD, 0x3F84D5B5B5470917,
								0x9216D5D98979FB1B, 0xD1310BA698DFB5AC, 0x2FFD72DBD01ADFB7, 0xB8E1AFED6A267E96,
								0xBA7C9045F12C7F99, 0x24A19947B3916CF7, 0x0801F2E2858EFC16, 0x636920D871574E69,]

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
		self.salt = [0x00, 0x00, 0x00, 0x00]
		self.xor_block = True
		self.current_length = 0
		self.__select_version(version)

	def __select_version(self, version):
		if version == 224:
			self.buffers = [0xC1059ED8, 0x367CD507, 0x3070DD17, 0xF70E5939,
							0xFFC00B31, 0x68581511, 0x64F98FA7, 0xBEFA4FA4,]

			self.round_constants = self.round_constant1
			self.rotations = [16,12,8,7]
			self.blocksize = 32
			self.rounds = 14
			self.padding_end = 0x00
			self.output_size = 7

		elif version == 256:
			self.buffers = [0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A,
							0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19,]

			self.round_constants = self.round_constant1
			self.rotations = [16,12,8,7]
			self.blocksize = 32
			self.rounds = 14
			self.padding_end = 0x01
			self.output_size = 8
			        
		elif version == 384:
			self.buffers = [0xCBBB9D5DC1059ED8, 0x629A292A367CD507, 0x9159015A3070DD17, 0x152FECD8F70E5939,
							0x67332667FFC00B31, 0x8EB44A8768581511, 0xDB0C2E0D64F98FA7, 0x47B5481DBEFA4FA4,]

			self.round_constants = self.round_constant2
			self.output_size = 6
			self.rotations = [32,25,16,11]
			self.blocksize = 64
			self.rounds = 16
			self.padding_end = 0x00
			self.output_size = 6

		elif version == 512:
			self.buffers = [0x6A09E667F3BCC908, 0xBB67AE8584CAA73B, 0x3C6EF372FE94F82B, 0xA54FF53A5F1D36F1,
							0x510E527FADE682D1, 0x9B05688C2B3E6C1F, 0x1F83D9ABFB41BD6B, 0x5BE0CD19137E2179,]
			self.round_constants = self.round_constant2
			self.rotations = [32,25,16,11]
			self.blocksize = 64
			self.rounds = 16
			self.padding_end = 0x01
			self.output_size = 8

		else:
			raise ValueError("Invalid Blake Version {}".format(self.version))
		
	def _set_message(self, message):
		#Convert to bytes if not already
		byte_message = bytearray(message)

		#Append 0x80 to the end of the message
		byte_message.append(0x80)

		#Get Length shifted by 8 and limit to int
		self.final_length = len(message) << 3
		input_length_data = asint(self.final_length, self.blocksize * 2)

		#Pad the data to a multable of 64 bytes when the 8 byte input_length_data is added 
		while len(byte_message) % (self.blocksize * 2) != ((self.blocksize * 2) - ((self.blocksize * 2) // 8)):
			byte_message.append(0x00)

		#Make the last byte of the padding end with a 1 or a 0 depending on the hash version
		byte_message[-1] |= self.padding_end

		#Append the length data to the message
		byte_message += int_to_bytes_length(input_length_data, (self.blocksize * 2) // 8 )

		return byte_message

	def _chacha_quarter_round(self, a, b, c, d, message, round_num, index):
		#Calculate indexes from Permuation table and round_index and offset
		message_index  = self.permutations[round_num][index]
		constant_index = self.permutations[round_num][index+1]

		#Modified first part to include message and round xor
		a = asint((a + b) + (message[message_index] ^ self.round_constants[constant_index]), self.blocksize)
		d = asint(d ^ a, self.blocksize)
		d = asint(shift_rotate_right(d, self.rotations[0], self.blocksize), self.blocksize)

		c = asint(c + d, self.blocksize)
		b = asint(b ^ c, self.blocksize)
		b = asint(shift_rotate_right(b, self.rotations[1], self.blocksize), self.blocksize)

		#Modified first part to include message and round xor
		a = asint((a + b) + (message[constant_index] ^ self.round_constants[message_index]), self.blocksize)
		d = asint(d ^ a, self.blocksize)
		d = asint(shift_rotate_right(d, self.rotations[2], self.blocksize), self.blocksize)

		c = asint(d + c, self.blocksize)
		b = asint(b ^ c, self.blocksize)
		b = asint(shift_rotate_right(b, self.rotations[3], self.blocksize), self.blocksize)

		return [a,b,c,d]


	def _compress_chunk(self, chunk):
		#Start the compress function

		#Create the start of the temp chunks
		temp_chunk = bytes_to_intarray(chunk, (self.blocksize //8), byte_order="big")
		#print(f"message: {[hex(x) for x in temp_chunk]}")

		#Start setting up the temp buffers
		temp_buffers = self.buffers[:] + self.round_constants[:8]

		for x in range(4):
			temp_buffers[8+x] ^= self.salt[x]

		#Do not xor currentlength when it is the last block and there is more than one block
		if self.xor_block:
			temp_buffers[12] ^= asint(self.current_length, self.blocksize)
			temp_buffers[13] ^= asint(self.current_length, self.blocksize)
			temp_buffers[14] ^= (self.current_length >> self.blocksize)
			temp_buffers[15] ^= (self.current_length >> self.blocksize)

		'''
		Resulting temp_buffers looks like this
		|IV             |IV             |IV              |IV              |
		|IV             |IV             |IV              |IV              |
		|Const ^ Salt   |Const ^ Salt   |Const ^ Salt    |Const ^ Salt    |
		|Const ^ len[0] |Const ^ len[0] |Const ^ len[1]  |Const ^ len[1]  |
		'''
		#print([hex(x) for x in temp_buffers[12:]], not self.xor_block, hex(self.current_length))

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
			#print(f"After Round {index} {temp_buffers}")

		#Update Buffers
		for x in range(8):
			#print(self.buffers[x], temp_buffers[x], temp_buffers[x+8], self.salt[x % 4])
			self.buffers[x] ^= (temp_buffers[x] ^ temp_buffers[x+8] ^ self.salt[x % 4])

		#print(self.buffers)

	def hash(self, message):
		#Setup message with padding and length data
		byte_message = self._set_message(message)

		#Opperate on each of the chunks
		blocks = to_blocks(byte_message, (self.blocksize * 2))
		#print(blocks)

		for index, chunk in enumerate(blocks):

			#Fix Edge Case for padding goes into the next block
			if index == len(blocks) - 1:
				#Calculate the last block size without padding
				mod_num = (self.final_length >> 3) % (self.blocksize * 2)
				#print(mod_num, (self.blocksize * 2) - ((self.blocksize * 2) // 8)-1, (self.blocksize * 2))

				#If adding the padding would make a new block the last block
				# If mod_num is inbetween 55-64 then 
				if (mod_num > (self.blocksize * 2) - ((self.blocksize * 2) // 8) - 1 and mod_num <= (self.blocksize * 2)):
					self.current_length = self.final_length - ((self.blocksize * 2) // 8)
					self.xor_block = False
				elif mod_num == 0:
					self.xor_block = False
				else:
					self.current_length = self.final_length 
				

			#Fix Edge Case for padding goes into the next block
			elif (self.current_length + (len(chunk) << 3)) >= self.final_length:
				self.current_length = self.final_length

			else:
				#Update the current_length
				self.current_length += (len(chunk) << 3)

			#print(self.current_length, self.final_length)
			#Compress the message Chunk
			self._compress_chunk(chunk)

		#Convert Intagers to Byte string
		output = b""
		for x in self.buffers[:self.output_size]:
			output += (x).to_bytes((self.blocksize // 8), byteorder='big')

		return output
		
	def hash_digest(self, message):
		return self.hash(message).hex()