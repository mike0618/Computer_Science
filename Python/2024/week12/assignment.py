from string import printable


class Assignments:
    def __init__(self) -> None:
        print("Week 12 Assignments\nAuthor: Mike Zubko\nDate: 11/16/24\n")
        self.initials("Zubko Mikhail Vladimirovich")
        self.product_code("037-00901-0027")
        self.hash_tag_gen()
        self.LEN = len(printable)
        encrypted = self.caesar_cipher()
        print(f"Encrypted: {encrypted}")
        print(f"Decrypted: {self.caesar_cipher(encrypted)}")
        encrypted = self.xor_cipher()
        print(f"Encrypted: {encrypted}")
        print(f"Decrypted: {self.xor_cipher(encrypted)}")

    def initials(self, full_name: str):
        """
        Print initials from the full name (lastname, name, middlename, patronym, etc.)
        """
        print("Print Initials\n")
        if not full_name:
            return False
        lst = full_name.split()
        print(lst)
        print(lst[0][0])
        [print(word[0], end="") for word in lst]
        print()

    def product_code(self, item: str):
        """
        Parse item code of format: ###-#####-####
        """
        print("\nProduct Code Parsing\n")
        if not item:
            return False
        lst = item.split("-")
        if len(lst) < 3:
            return False
        print(f"Country Code: {lst[0]}\nProduct Code: {lst[1]}\nBatch Number: {lst[2]}")

    def hash_tag_gen(self):
        """
        Create a hashtag from the sentence
        """
        print("\nMike's Hashtag Generator\n")
        print(
            "#"
            + input("Enter a sentence to generate a hashtag: ")
            .title()
            .replace(" ", "")[:140]
        )

    def caesar_cipher(self, text=""):
        print("\nCaesar Cipher\n")
        shift = input("Charecter shift: ").strip()
        if not shift or not shift.isdigit():
            return ""
        shift = int(shift)
        if not text:  # perform encryption, otherwise decryption
            shift *= -1  # inverse shift for encryption
            text = input("Enter plaintext: ").strip()
        if not text:  # check input
            return ""
        result = ""
        for ch in text:
            if ch not in printable:
                result += ch
            i = (printable.index(ch) + shift) % self.LEN
            result += printable[i]
        return result

    def xor_cipher(self, text=""):
        print("\nXOR Cipher\n")
        key = input("Enter key: ").strip()
        if not key or not key.isdigit():
            return ""
        key = int(key)
        if not text:  # perform encryption, otherwise decryption
            text = input("Enter plaintext: ").strip()
        if not text:  # check input
            return ""
        result = ""
        for ch in text:
            result += chr(ord(ch) ^ key)
        return result


if __name__ == "__main__":
    Assignments()
