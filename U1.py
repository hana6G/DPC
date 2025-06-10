def reverse_sentence(sentence):
    words = sentence.split()
    #words[::-1]
    reversed = words[::-1]
    return ''.join(reversed)
    print(reversed)
    
    
sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)

sentence2 = "Pooh"
reverse_sentence(sentence2)