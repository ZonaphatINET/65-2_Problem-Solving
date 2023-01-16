def input_values():
    account = int(input('Input number of Saving Account: '))
    deposit_list = []
    interest_list = []

    for i in range(account):
        deposit = int(input('Input principal of SA {}: '.format(i + 1)))
        deposit_list.append(deposit)
        interest = float(input('Input interest of SA {}: '.format(i + 1)))
        interest_list.append(interest)
    Calculate(deposit_list, interest_list)

def Calculate(deposit, interest):
    sum_list = [((deposit[i] * interest[i])/100) + deposit[i] for i in range(len(deposit))]
    output_total(sum_list)

def output_total(sum):
    for i, total in enumerate(sum):
        print('Total money of SA {} is {}'.format(i + 1, total))

input_values()
