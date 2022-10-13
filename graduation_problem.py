def count(i,status,skipped):
    global n,skip,cannot_attend,sample_space
    
    #terminating condition
    if i==n:
        if status=='N':
            cannot_attend+=1
        sample_space+=1
        return
    
    #invalid condition if skips 4 or more days continously
    if skipped+1<skip:
        count(i+1,'N',skipped+1)
    
    #if attended the class ('Y') skipped_days resets to 0
    count(i+1,'Y',0)
    

if __name__=='__main__':
    #cannot_attend holds the number of ways he  cannot attend the graduation
    #sample_space holds the total number of valid ways
    cannot_attend,sample_space=0,0
    entered=False
    
    #accepting input for 'number of days' and 'cannot miss classes continously'
    while(not entered):
        try:
            n=int(input('Enter the number of Days:'))
            entered=True
        except:
            pass
    skip=int(input('Enter the number of days he cannot skip the classes (default 4 days): ') or '4')

    count(0,'',0)

    print(f'{cannot_attend}/{sample_space}')
