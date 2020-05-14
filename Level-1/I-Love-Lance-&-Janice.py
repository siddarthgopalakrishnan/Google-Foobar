def answer(s):
	return ''.join([chr(ord('z') - ord(chari) + ord('a')) if ord('a') <= ord(chari) <= ord('z') else chari for chari in s])