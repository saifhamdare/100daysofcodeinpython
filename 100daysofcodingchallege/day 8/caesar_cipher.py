alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print('''
                                                                                                                                       
  ,ad8888ba,                                                             ,ad8888ba,  88             88                                 
 d8"'    `"8b                                                           d8"'    `"8b ""             88                                 
d8'                                                                    d8'                          88                                 
88            ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,    88            88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
88            ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8    88            88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
Y8,           ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88            Y8,           88 88       d8 88       88 8PP""""""" 88          
 Y8a.    .a8P 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88             Y8a.    .a8P 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
  `"Y8888Y"'  `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88              `"Y8888Y"'  88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                                                                                        88                                             
                                                                                        88                                             

''')

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(plain_text,shift_amount,cipher_direction):
  end_text=""
  if cipher_direction=="decode":
    shift_amount*= -1
  for char in plain_text:
    if char in alphabet:
      position=alphabet.index(char)
      new_position=position+shift_amount
      end_text+=alphabet[new_position]
    else:
      end_text+=char
  print(f"the {cipher_direction}d text is {end_text}")
should_continue=True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift%25
  caesar(plain_text=text,shift_amount=shift,cipher_direction=direction)
  result=input("Type 'yes'to continue and 'no' to exit\n")
  if result=="no":
    should_continue=False
    print("Goodbye")

