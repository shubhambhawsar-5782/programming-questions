#generate binary bit using recursion
for _ in range(int(input())):
    def append_bits(x,l):
        return [x+ele for ele in l]

    def generate_bits(n):
        if n==0:return[]
        if n==1:return['0','1']
        else:
            return(append_bits('0',generate_bits(n-1))+append_bits('1',generate_bits(n-1)))
    print(generate_bits(int(input())))