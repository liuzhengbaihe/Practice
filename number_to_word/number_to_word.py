tg = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
tn = {0:'ten', 1:'eleven', 2:'twelve', 3:'thirteen', 4:'fourteen', 5:'fifteen',
        6:'sixteen', 7:'seventeen', 8:'eighteen', 9:'nineteen'}
wn = {2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}

bg_nu = ['', 'thousand', 'million', 'billion']

number = raw_input('please input a number:')
nu_length = len(number)
result = ''
sk = 0
if not number:
    print 'zero'
for index in range(nu_length):
    reverse_index = nu_length-index
    if reverse_index%3 == 2:
        if number[index] == '1':
            result += tn[int(number[index+1])] + ' '
            sk = 1
        elif number[index] != '0':
            result += wn[int(number[index])] + ' '
    elif number[index] != '0':
        if not sk:
            result += tg[int(number[index])] + ' '
            sk = 0
        if reverse_index%3 == 0:
            result += 'hundred' + ' '
    if reverse_index%3 == 1:
        result += bg_nu[reverse_index/3] + ' '
print result
