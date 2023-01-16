def input_values():
    account = int(input('Input number of Saving Account: '))
    deposit_list = list()
    interest_list = list()
    print('\n')

    for i in range (1,account+1):
        deposit = int(input('Input Principal of SA '+str(i)+': '))
        deposit_list.append(deposit)
    print('\n')
    for i in range (1,account+1):
        interest = float(input('Input interest of SA '+str(i)+': '))
        interest_list.append(interest)
    print('\n')
    Calculate(deposit_list,interest_list)

def Calculate(deposit,interest):
    sum_list = list()
    sum = 0
    for i in range(len(deposit)):
        sum = ((deposit[i] * interest[i])/100) + deposit[i]
        sum_list.append(sum)
    output_total(sum_list)

def output_total(sum):
    indexcheck = 0
    for i in range(1,len(sum)+1):
        print('Total money of SA '+str(i)+' is ',sum[indexcheck])
        indexcheck += 1

input_values()