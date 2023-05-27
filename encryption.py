import pyAesCrypt


def Encrypt(password, filename):
    pyAesCrypt.encryptFile(fr"{filename}", 'Enc.txt.aes', password)


def Decrypt(password, filename):
    pyAesCrypt.decryptFile("Dec.txt.aes", fr"{filename}", password)


def main():
    password = input("Input your password: ")
    file_nime = input("Input path og the file: ")
    Encrypt(password, file_nime)

if __name__ == '__main__':
    main()
