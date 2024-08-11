import itertools

from com.patrick.private.utils.benchmark import Benchmark


class Problem59(object):
    """
    Each character on a computer is assigned a unique code and the preferred standard is
    ASCII (American Standard Code for Information Interchange).
    For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

    A modern encryption method is to take a text file, convert the bytes to ASCII,
    then XOR each byte with a given value, taken from a secret key.
    The advantage with the XOR function is that using the same encryption key on the cipher text,
    restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

    For unbreakable encryption, the key is the same length as the plain text message,
    and the key is made up of random bytes.
    The user would keep the encrypted message and the encryption key in different locations,
    and without both "halves", it is impossible to decrypt the message.

    Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
    If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
    The balance for this method is using a sufficiently long password key for security,
    but short enough to be memorable.

    Your task has been made easy, as the encryption key consists of three lower case characters.
    Using a file containing the encrypted ASCII codes, and the knowledge that the plain text
    must contain common English words, decrypt the message and find the sum of the ASCII values
    in the original text.
    """

    def __init__(self, filename: str):
        with open(filename) as f:
            self.encrypted = [int(n) for n in f.read().split(",")]

        self.key_length = 3
        print("Problem 59: Decrypt the message and find the sum of the ASCII values in the original text.")

    @Benchmark
    def attempt_1(self):
        result = 0

        char_range = [n for n in range(97, 123)]
        for key in self.generate_key(char_range=char_range):
            decrypted = self.decrypt(self.encrypted, key)
            if " the " in decrypted:
                result = sum([ord(n) for n in decrypted])
                readable_key = "".join([chr(n) for n in key])
                print(f"{result} = ({readable_key}): {decrypted}")
                break

        print("")
        print(f"Result: {result}")

    @Benchmark
    def official_solution(self):
        result = "N/A"
        print("")
        print(f"Result: {result}")

    def generate_key(self, char_range):
        yield itertools.product(char_range, repeat=self.key_length)

    def decrypt(self, encrypted, decryption_key):
        decryption_key = [int(n) for n in decryption_key] * (len(self.encrypted) // self.key_length)
        return "".join(list(chr(a ^ b) for a, b in zip(encrypted, decryption_key)))


if __name__ == '__main__':
    problem = Problem59(filename="../../../../resources/problem059.txt")

    problem.attempt_1()
    problem.official_solution()
