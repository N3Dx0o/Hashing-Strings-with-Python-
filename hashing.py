import hashlib 

class hashingtxt:
	def hashtext(slef,text,hash_type):

		text = text.encode("utf-8")
		hash_hash = hashlib.new(hash_type)
		hash_hash.update(text)
		return hash_hash.hexdigest()
