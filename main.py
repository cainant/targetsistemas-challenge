def check_fib(n: int):
    pertence = 'Esse número pertence a sequência de Fibonacci'
    nao_pertence = 'Esse número não pertence a sequência de Fibonacci'
    def fib(n: int) -> bool:
        if n == 0 or n == 1:
            return True
        
        a, b = 0, 1
        while b <= n:
            if b == n:
                return True
            a, b = b, a + b
        
        return False
    
    if fib(n):
        print(pertence)
    else:
        print(nao_pertence)
    
def check_letter_in_string(string: str, letter: str):
    count = string.count(letter)
    if count == 0:
        print('Não ocorre')
    else:
        print(f'Ocorre {count} vezes')

def loop():
    index = 12
    sum = 0
    k = 1

    while k < index:
        k += 1
        sum += k

    print(sum) # 77

'''
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, 9
b) 2, 4, 8, 16, 32, 64,128
c) 0, 1, 4, 9, 16, 25, 36, 49
d) 4, 16, 36, 64, 100
e) 1, 1, 2, 3, 5, 8, 13
f) 2,10, 12, 16, 17, 18, 19, 200
'''

'''
5)
Para descobrir qual interruptor controla cada lâmpada, 
ligue o primeiro interruptor por alguns minutos e depois desligue-o.
Ligue o segundo interruptor e vá até a sala.
A lâmpada acesa será do segundo interruptor,
a apagada e quente será do primeiro e a apagada e fria do terceiro.
'''