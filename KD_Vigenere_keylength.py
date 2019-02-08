
def get_IoC(strng):
    n=len(strng)
    IoC=0
    if n-1:
        IoC=(1/(float(n)*(n-1)))*(sum([strng.count(a)*(strng.count(a)-1) for a in set(strng)]))
    return(IoC)

def get_possible_key_ls(avg_IoC_arr):
    cpy=avg_IoC_arr.copy()
    avg_IoC_arr.sort(reverse=True)
    key_ls=[cpy.index(avg_IoC_arr[0])+2,cpy.index(avg_IoC_arr[1])+2]
    return(key_ls)

def get_key_len(strng,shift):
    avg_IoC_arr=[]
    for n in range(2,shift+1):
        IoC_sum=0.0
        avg_IoC=0.0
        for i in range(n):
            s=""
            for j in range(0,len(strng[i:]),n):
                s+=(strng[i:][j])
            IoC=get_IoC(s)
            IoC_sum+=IoC
        avg_IoC=IoC_sum/n
        avg_IoC_arr.append(avg_IoC)
    for k in avg_IoC_arr:
        print(str(avg_IoC_arr.index(k)+2)+" shift, IoC="+str(k))
    pos_key_ls=get_possible_key_ls(avg_IoC_arr)
    print("Best two possible key lengths:",pos_key_ls)
        
        
strng="QHDLXNQLYNGAIGWBCERJFEARNIBKXUSVGZXKYNPXXTKGAATZRQCRFYIDCCLYXHUQXEIXFAFGEAMMALYRGAYXQMTGACDJSYRTLEXUVRVIYFFEGXFKOYSPHGBBYTRESOXUNTXXAKLUAWYDINAAWCZWIFVMCROIUCEIFJYDJAYZJBEOTMUSGAGAYYQNIPTFPYMCBOYDYYSVGWDOJTBZLMFBYJXLQCUDRRIGMIUYWMQUUFRPCZQHTVJOUJSMNRVQQZEJYLACNHRFCPTFENZYEJCLYMBQUCGUMYQDBUAWLQTMOAXCZJBEABHQJYEAMQQDNIRLNTUINRMCYUJAQTZQMGOEXUDEONQPIDBXWNKNIEUNQMBQDUFGXLFXYBVKNTEZCBFJGJUTVHHMBWOZIFQNCTLMBQELYVGNTUHIAXNQUHSROYZJCEFUIACVOBFVAEGBBHGNEIMOHIYRIOZQ"
get_key_len(strng,14)

#Returns
#2 shift, IoC=0.0402126447693184
#3 shift, IoC=0.040925992938376836
#4 shift, IoC=0.040655987795575894
#5 shift, IoC=0.03879598662207358
#6 shift, IoC=0.042133363712311085
#7 shift, IoC=0.06341991341991342
#8 shift, IoC=0.039876091089793446
#9 shift, IoC=0.039084967320261434
#10 shift, IoC=0.03768115942028986
#11 shift, IoC=0.04353816914792524
#12 shift, IoC=0.04320616162721425
#13 shift, IoC=0.039668174962292614
#14 shift, IoC=0.060213308197179176
#Best two possible key lengths: [7, 14]
