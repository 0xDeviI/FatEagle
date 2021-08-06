from fescripts.libs.cryptopals_lib import *

class MD2(object):
	def __init__(self):
		self.block_size = 16
		self.buffer_size = 48
		self.round_count = 18
		self.buffer = bytearray([0 for _ in range(self.buffer_size)])

		self.sbox = [41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6,
					19, 98, 167, 5, 243, 192, 199, 115, 140, 152, 147, 43, 217, 188,
					76, 130, 202, 30, 155, 87, 60, 253, 212, 224, 22, 103, 66, 111, 24,
					138, 23, 229, 18, 190, 78, 196, 214, 218, 158, 222, 73, 160, 251,
					245, 142, 187, 47, 238, 122, 169, 104, 121, 145, 21, 178, 7, 63,
					148, 194, 16, 137, 11, 34, 95, 33, 128, 127, 93, 154, 90, 144, 50,
					39, 53, 62, 204, 231, 191, 247, 151, 3, 255, 25, 48, 179, 72, 165,
					181, 209, 215, 94, 146, 42, 172, 86, 170, 198, 79, 184, 56, 210,
					150, 164, 125, 182, 118, 252, 107, 226, 156, 116, 4, 241, 69, 157,
					112, 89, 100, 113, 135, 32, 134, 91, 207, 101, 230, 45, 168, 2, 27,
					96, 37, 173, 174, 176, 185, 246, 28, 70, 97, 105, 52, 64, 126, 15,
					85, 71, 163, 35, 221, 81, 175, 58, 195, 92, 249, 206, 186, 197,
					234, 38, 44, 83, 13, 110, 133, 40, 132, 9, 211, 223, 205, 244, 65,
					129, 77, 82, 106, 220, 55, 200, 108, 193, 171, 250, 36, 225, 123,
					8, 12, 189, 177, 74, 120, 136, 149, 139, 227, 99, 232, 109, 233,
					203, 213, 254, 59, 0, 29, 57, 242, 239, 183, 14, 102, 88, 208, 228,
					166, 119, 114, 248, 235, 117, 75, 10, 49, 68, 80, 180, 143, 237,
					31, 26, 219, 153, 141, 51, 159, 17, 131, 20]

	def _set_message(self, message):
		#Convert to bytes if not already
		byte_message = bytearray(message)

		#Get Padding Number
		padding_number = self.block_size - (len(message) % self.block_size)

		#Add the padding number to pad the input to the next block
		for _ in range(padding_number):
			byte_message.append(padding_number)

		#Append Checksum
		checksum_byte = 0
		checksum = bytearray(0 for _ in range(self.block_size))

		# For each Block
		for block_num, block in enumerate(to_blocks(byte_message, self.block_size)):

			# Calculate checksum of block using each byte of the block
			for byte_num, byte in enumerate(block):
				checksum_byte = self.sbox[byte ^ checksum_byte]
				checksum[byte_num] = checksum_byte

		byte_message += checksum

		return byte_message

	def _hash_message_chunk(self, chunk):
		for bit_index, bit in enumerate(chunk):
			self.buffer[self.block_size + bit_index] = bit
			self.buffer[2 * self.block_size + bit_index] = self.buffer[self.block_size + bit_index] ^ self.buffer[bit_index]

		#print(self.buffer)

		# Rounds of encryption over the entire array. Current byte XOR'd with the previous (substituted) byte.
		hash_byte = 0
		for round_num in range(self.round_count):
			for bit_index in range(self.buffer_size):
				#print(self.buffer)
				hash_byte = self.buffer[bit_index] ^ self.sbox[hash_byte]
				self.buffer[bit_index] = hash_byte

			hash_byte = (hash_byte + round_num) % len(self.sbox)


	def hash(self, message):
		#Setup message with padding and length data
		byte_message = self._set_message(message)

		#Opperate on each of the 64 byte chunks
		for chunk in to_blocks(byte_message, self.block_size):
			self._hash_message_chunk(chunk)

		#Convert Intagers to Byte string
		return self.buffer[:16]
		
	def hash_digest(self, message):
		return self.hash(message).hex()