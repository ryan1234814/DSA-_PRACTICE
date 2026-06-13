class Solution:
    def extractMaximum(self,s): 
        li=[]
        number=""
        for i in s:
            if i.isdigit():
                number+=i
            else:
                if number!="":
                    li.append(int(number))
                    number=""
        if number!="":
            li.append(int(number))
        if len(li)==0:
            return -1
        else:
            return max(li)
                