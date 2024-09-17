class Solution:
    def intToRoman(self, num: int) -> str:
        # result = ''
        # while num > 0:
        #     n_z = len(str(num))-1
        #     tens = 10**n_z
        #     d = num
        #     num %= tens
        #     result += self.roman(d - num)
        
        # return result
        return self.roman(num)

    
    def roman(self,num):
        n = {
            1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M'
        }
        answer = ''
        while num > 0:
            n_z = len(str(num))-1
            v = 1 if str(num)[0] < '5' or str(num)[0] == '9' else 5
            tens = v*10**n_z if n_z > 0 else v
            if num in n.keys():
                answer += n[num]
                num = 0
            elif v != 5 and num+tens - num % tens in n.keys():
                answer += n[tens]
                answer += n[num+tens - num % tens]
                num = num % tens
                
            else:
                answer += n[tens]
                num -= tens
                
        return answer