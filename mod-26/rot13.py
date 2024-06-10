def upper(input: str) -> str:
    upper_str = ""
    for char in input:
        upper_str = upper_str + chr(ord(char) - 32)
    return upper_str


def rot13(input: str) -> str:
    rotated = ""
    for char in input:
        rotated = rotated + chr((((ord(char) - 97) + 13) % 26) + 97)
    return rotated


print(upper("hello"))
input = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}"
print(rot13(input))
