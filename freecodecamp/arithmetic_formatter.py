# Freecodecamp - Scientific Calc. Python - Project No. 1

def answer(problems):
    solutions=[]
    if len(problems)>5:
        return 'Error: Too many problems.'
    else:
        for problem in problems:
            problem=problem.strip().split()
            try:
                num1 = int(problem[0])
            except:
                return('Error: Numbers must only contain digits.')
                

            try:
                num2 = int(problem[2])
            except:
                return 'Error: Numbers must only contain digits.'
                
     
            if num1>9999 or num2>9999:
                return('Error: Numbers cannot be more than four digits.')
                
            if problem[1] == '+':
                    sum= num1+num2
                    solutions.append(sum)
            elif problem[1] == '-':
                    sum= num1-num2
                    solutions.append(sum)
            else:
                return("Error: Operator must be '+' or '-'.")
    return solutions


            



def arithmetic_arranger(problems, show_answers=False):
    solution=answer(problems)   
    if type(solution) == str:
        return solution
    probleminfos=[]
    for problem in problems:
        info=[]
        problem=problem.strip().split()
        wspace_1=len(problem[0])+2
        wspace_2=len(problem[2])+2
        dashes=max(wspace_1,wspace_2)
        wspace_1 = dashes - len(problem[0])
        wspace_2 = dashes - 1 - len(problem[2])
        info.append(wspace_1)
        info.append(wspace_2)
        info.append(dashes)
        probleminfos.append(info)
    final=''   
    for i in range(len(problems)):
        problem=problems[i]
        problem=problem.strip().split()
        num1=(problem[0])
        final+= probleminfos[i][0]*' '+num1
        if i!=len(problems)-1:
            final+='    '
            
    final+='\n'

    for i in range(len(problems)):
        problem=problems[i]
        problem=problem.strip().split()
        num2=(problem[2])
        final+= problem[1]+probleminfos[i][1]*' '+num2
        if i!=len(problems)-1:
            final+='    '

    
    final+='\n'

    for i in range(len(problems)):
        final+= probleminfos[i][2]*'-'
        if i!=len(problems)-1:
            final+='    '

            
    if show_answers:
        final+='\n'
        for i in range(len(problems)):
            wspace = probleminfos[i][2] - len(str(solution[i]))
            final += wspace * ' ' + str(solution[i])
            if i != len(problems) - 1:
                final += '    '

            
    print(final)
    return final

