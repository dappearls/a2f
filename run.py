if __name__ == "__main__":
	try:
		__import__("enc_simple").DAP()
	except Exception as e:
		exit(str(e))
