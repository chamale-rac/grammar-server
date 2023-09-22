AZ = '(A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z)'
az = '(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z)'
digit = '(0|1|2|3|4|5|6|7|8|9)'

# (( x)+ \|)*( x)+
valid_characters = f'(( ({AZ}|{az}|{digit}))+|( \ϵ))'
body = f'({valid_characters} \|)*{valid_characters}'
left = f'{AZ} ->'
regex_str = f'{left}{body}'
