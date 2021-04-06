def shifr_pswrd(password):
    password = password.replace('a','Θ').replace('b', 'Ξ').replace('c', 'Σ').replace('d', 'Ψ').replace('e', 'β').replace('f', 'γ').replace('g', 'ζ').replace('h', 'λ').replace('i', 'ξ').replace('j', 'Π').replace('k', 'Τ').replace('l', 'ƒ').replace('m', '÷').replace('n', '×').replace('o', '¼').replace('p', '¾').replace('q', '½').replace('r', '±').replace('s', '°').replace('t', '™').replace('u', '®').replace('v', '©').replace('w', '§').replace('x', '¶').replace('y', '€').replace('z', '£').replace('0', '¿').replace('1', '‰').replace('2', '≠').replace('3', '≅').replace('4', '≈').replace('5', '≤').replace('6', '≥').replace('7', '∠').replace('8', '⊥').replace('9', '@')
    return password

def deshifr_pswrd(password):
    password = password.replace('Θ', 'a').replace('Ξ', 'b').replace('Σ', 'c').replace('Ψ', 'd').replace('β', 'e').replace('γ', 'f').replace('ζ', 'g').replace('λ', 'h').replace('ξ', 'i').replace('Π', 'j').replace('Τ', 'k').replace('ƒ', 'l').replace('÷', 'm').replace('×', 'n').replace('¼', 'o').replace('¾', 'p').replace('½', 'q').replace('±', 'r').replace('°', 's').replace('™', 't').replace('®', 'u').replace('©', 'v').replace('§', 'w').replace('¶', 'x').replace('€', 'y').replace('£', 'z').replace('¿', '0').replace('‰', '1').replace('≠', '2').replace('≅', '3').replace('≈', '4').replace('≤', '5').replace('≥', '6').replace('∠', '7').replace('⊥', '8').replace('@', '9')
    return password
	
def hide_password(password):
    hidden_password = str('*'*len(password))
    return hidden_password