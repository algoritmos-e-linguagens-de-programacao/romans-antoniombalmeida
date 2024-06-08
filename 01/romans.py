def int_to_roman(num):
    
    num_milhar = num // 1000
    num_centena = (num % 1000) // 100
    num_dezena = (num % 100) // 10
    num_unidade = num % 10
    
    milhar = [" ", "M", "MM", "MMM"]
    centena = [" ", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    dezena = [" ", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    unidade = [" ", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    
    romans = milhar[num_milhar] + centena[num_centena] + dezena[num_dezena] + unidade[num_unidade]
    
    return romans
    
def roman_to_int(s):
    valores_romanos = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    i = 0
    total = 0

    for roman in reversed(s):
        valor_total = valores_romanos[roman]
    
        if valor_total >= i:
            total += valor_total
        else:
            total -= valor_total

        i = valor_total
    
    return total
