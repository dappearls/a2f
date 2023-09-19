if __name__ == "__main__":
	try:
		__import__("main_enc").menu()
	except Exception as e:
		exit(str(e))
