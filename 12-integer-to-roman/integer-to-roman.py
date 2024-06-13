class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        while num > 0:
            n_z = len(str(num))-1
            tens = 10**n_z
            d = num
            num %= tens
            result += self.roman(d - num)
        
        return result

    
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
        n_z = len(str(num))-1
        answer = ''
        while num > 0:
            v = 1 if str(num)[0] < '5' or str(num)[0] == '9' else 5
            tens = v*10**n_z
            if num in n.keys():
                answer += n[num]
                break
            elif num+tens in n.keys():
                answer += n[tens]
                answer += n[num+tens]
                break
                
            else:
                answer += n[tens]
                num -= tens
                
        return answer