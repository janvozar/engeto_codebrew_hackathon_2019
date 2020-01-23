nums = [386, 462, 47, 418, 907, 344, 236, 375, 823,
        566, 597, 978, 328, 615, 953, 345, 399, 162,
        758, 219, 918, 237, 412, 566, 826, 248, 866,
        950, 626, 949, 687, 217, 815, 67, 104, 58, 512,
        24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
        742, 717, 958, 743, 527]
odd_sum = 0
even_sum = 0
absolute_diff = 0

def diff_odd_even(nums,odd_sum, even_sum, absolute_diff):
    for i in range (0, len(nums)):
        if nums[i]%2==0:
            #print('toto je parne cislo pozici ' + str(i))
            #print(str(nums[i]) + ' ' + str(even_sum))
            even_sum = even_sum + nums[i]
            #print(even_sum)
        else:
            #print('toto je neparne cislo na pozici ' + str(i))
            #print(str(nums[i]) + ' ' + str(odd_sum))
            odd_sum = odd_sum + nums[i]
            #print(odd_sum)
    print('Toto je soucet vsech neparnych cisel v listu:')
    print(odd_sum)
    print('Toto je soucet vsech parnych cisel v listu:')
    print(even_sum)
    absolute_diff = abs(odd_sum - even_sum)
    print('Toto je absolutny rozdiel parnych a neparnych cisel v listu:')
    print(absolute_diff)

diff_odd_even(nums, odd_sum, even_sum, absolute_diff)