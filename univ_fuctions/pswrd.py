def shifr_pswrd(password):
    password = password.replace('a','Θ').replace('b', 'Ξ').replace('c', 'Σ').replace('d', 'Ψ').replace('e', 'β').replace('f', 'γ').replace('g', 'ζ').replace('h', 'λ').replace('i', 'ξ').replace('j', 'Π').replace('k', 'Τ').replace('l', 'ƒ').replace('m', '÷').replace('n', '×').replace('o', '¼').replace('p', '¾').replace('q', '½').replace('r', '±').replace('s', '°').replace('t', '™').replace('u', '®').replace('v', '©').replace('w', '§').replace('x', '¶').replace('y', '€').replace('z', '£').replace('0', 'a').replace('1', 'b').replace('2', 'c').replace('3', 'd').replace('4', 'e').replace('5', 'f').replace('6', 'g').replace('7', 'h').replace('8', 'i').replace('9', 'j')
    return password

def deshifr_pswrd(password):
    password = password.replace('Θ', 'a').replace('Ξ', 'b').replace('Σ', 'c').replace('Ψ', 'd').replace('β', 'e').replace('γ', 'f').replace('ζ', 'g').replace('λ', 'h').replace('ξ', 'i').replace('Π', 'j').replace('Τ', 'k').replace('ƒ', 'l').replace('÷', 'm').replace('×', 'n').replace('¼', 'o').replace('¾', 'p').replace('½', 'q').replace('±', 'r').replace('°', 's').replace('™', 't').replace('®', 'u').replace('©', 'v').replace('§', 'w').replace('¶', 'x').replace('€', 'y').replace('£', 'z').replace('a', '0').replace('b', '1').replace('c', '2').replace('d', '3').replace('e', '4').replace('f', '5').replace('g', '6').replace('h', '7').replace('i', '8').replace('j', '9')
    return password
	
def hide_password(password):
    hidden_password = str('*'*len(password))
    return hidden_password