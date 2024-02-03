#Caesar Ciphar

alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
          'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
          'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   

    
def ceaser(text, shift_amount):

    # encode
    
    if direction=='encode':

        cipher_text=''

        for i in text:

            position=alphabets.index(i)
            new_position=position+shift_amount
            new_position1=alphabets[new_position]
            cipher_text=cipher_text+new_position1

        print('The encoded text is: ', cipher_text)
              
        
        
    # decode  
    
    elif direction=='decode':


        plain_text=''

        for i in text:

            position=alphabets.index(i)
            new_position=position-shift_amount
            new_position2=alphabets[new_position]
            plain_text=plain_text+new_position2

        print('The decoded text is: ', plain_text)



direction=input('Type encode to encrypt, type decode to decrypt: ')
text=input('enter text: ').lower()
shift=int(input('enter shift number: '))

ceaser(text=text, shift_amount=shift) 