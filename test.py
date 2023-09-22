# ((( x)+ \|)* x)

# [A-Z] -> (( [A-Z]|[a-z]|[0-9])+|( \ϵ))

# (( [A-Z]|[a-z]|[0-9])+|( \ϵ))
# (( [A-Z]|[a-z]|[0-9]|(\ϵ))


# x ->(( x)+|((( x)+ \|)* x))

# x ->((( [A-Z]|[a-z]|[0-9])+|( \ϵ))|(((( [A-Z]|[a-z]|[0-9])+|( \ϵ)) \|)* (( [A-Z]|[a-z]|[0-9]|(\ϵ))))

AZ = '[A-Z]'
az = '[a-z]'
digit = '[0-9]'
epsilon_C = '\ϵ'
s = ' '
or_C = '\|'
arrow = '->'

any_or_epsilon = f'({s}({AZ}|{az}|{digit}))+|({s}{epsilon_C})'

left = f'{AZ}{s}{arrow}{s}'
any_or_epsilon_with_or = f'({any_or_epsilon}{s}{or_C})'
body = f'({any_or_epsilon}|({any_or_epsilon_with_or}*{s}{any_or_epsilon}))'
