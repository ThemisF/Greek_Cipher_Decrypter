import random
import math
from collections import OrderedDict


k_Text="ΞΟΖ ΒΣΟΧΔΠ, Α ΞΣΦΘΚΧΟ ΣΝΦΣ ΦΧΘΝΞΣΝ ΞΟΖΓ ΙΧΞΝΤΝΧ ΞΧΦΘΝΛΝΧΘ ΟΘΣΝΞ ΛΝΖΠΞ. ΟΑ ΦΝΤΝΖΞΟΑ ΗΘΩΟΑ ΓΠΦΟΧ, ΒΖΤΝΞ ΟΣΤΣΝΩΞΣ ΟΑΓ ΝΞΟΖΘΝΧ ΟΖΠ ΒΧΧΘΖΠΡ, ΞΑΥΩΜΑΥΣ ΥΧΝ ΡΝΤΑΞΣ ΟΖ ΗΧΟΩΒΧ ΒΗΘΖΞΟΧ ΟΖΠ ΤΣΛΖΓΟΧΞ: «ΒΣΛΧΤΣ ΙΧΞΝΤΝΧ, ΛΝΧ ΦΝΤΝΣΞ ΥΧΝ ΒΝΧ ΓΠΦΟΣΞ ΞΖΠ ΕΝΑΛΑΜΑΥΧ ΟΖΠΞ ΒΠΜΖΠΞ ΟΩΓ ΗΣΘΧΞΒΣΓΩΓ ΣΗΖΦΩΓ ΥΧΝ ΟΖΠΞ ΜΘΠΤΖΠΞ ΟΩΓ ΧΘΦΧΝΩΓ ΙΧΞΝΤΣΩΓ. ΒΗΖΘΩ ΓΧ ΟΖΤΒΑΞΩ ΓΧ ΚΑΟΑΞΩ ΒΝΧ ΦΧΘΑ ΧΗΖ ΟΑ ΒΣΛΧΤΣΝΖΟΑΟΧ ΞΖΠ;»"
K_Text="ξοζ βσοχδπ, α ξσφθκχο σνφς φχθνξσν ξοζγ ιχξντνχ ξχφθνλνχθ οθσνξ λνζπξ. οα φντνζξοα ηθωοα γπφοχ, βζτνξ οστσνωξς οαγ νξοζθνχ οζπ βχχθζπρ, ξαυωμαυς υχν ρνταξς οζ ηχοωβχ βηθζξοχ οζπ τσλζγοχξ: «βσλχτς ιχξντνχ, λνχ φντνσξ υχν βνχ γπφοσξ ξζπ εναλαμαυχ οζπξ βπμζπξ οωγ ησθχξβσγωγ σηζφωγ υχν οζπξ μθπτζπξ οωγ χθφχνωγ ιχξντσωγ. βηζθω γχ οζτβαξω γχ καοαξω βνχ φχθα χηζ οα βσλχτσνζοαοχ ξζπ;»"

abc=["αάΑΆ","βΒ","γΓ","δΔ","εέΕΈ","ζΖ","ηήΗΉ","θΘ","ιϊΐίΙΊ","κΚ","λΛ","μΜ","νΝ","ξΞ","οόΟΌ","πΠ","ρΡ","σςΣ","τΤ","υύΥΎ","φΦ","χΧ","ψΨ","ωώΩΏ"]
ABC="ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
aBC="αάΑΆβΒγΓδΔεέΕΈζΖηήΗΉθΘιϊΐίΙΊκΚλΛμΜνΝξΞοόΟΌπΠρΡσςΣτΤυύΥΎφΦχΧψΨωώΩΏ"


 
#------------------------ analysh_logotexnikoy_keimenoy_kai_dhmioyrgia_ths_listas_twn_alfavitwn ------------------------#


dinn=0
keimena=[]

with open("LargeLogKeim.txt") as fin:
    text=fin.read()
print("Large logotexniko keimeno >>> LargeLogKeim.txt: Extracted")


print("Diairesh logotexnikoy keimenoy")   
for i in range(int(len(text)/len(K_Text))):#kovei to keimeno se mikrotera kommatia megethoys iso toy kryptorafhmenoy
    keimena.append(text[dinn:(len(K_Text)+dinn)])
    dinn=(i+1)*len(K_Text)
print("Plithos ypokeimenwn:",len(keimena))


L_List=[]
def keim_analiser(text):
    GramsInText=0
    bong=0
    myList=[]
    blas=(0,0)
    shortedList=[]
    logo_abc=""
    l_exer=["a"]
    L_List=[]

    #----- posostiaia_analysh_keimenoy -----#
    
    for i in text :#vriskei posa grammata yparxoyn sto keimeno
            if i in aBC:
               GramsInText=GramsInText+1
               
    for i in abc:#vriskei to pososto kathe grammatos
        bong=0
        for ti in text:
            if ti in abc[abc.index(i)]:
                bong=bong+1
        myList.append((ABC[abc.index(i)],bong*100/GramsInText))#ftiaxnei mia lista me kathe gramma kai to pososto emfanishs toy sto keimeno 

     
    #----- posostiaia_taksinomhsh_alfavitoy -----#
    
    while len(shortedList) < 24:#posostiaia taksinomhsh logotexnikhs alfavitas
        for i in myList:
            if i[1]>=blas[1] and i not in shortedList:
                blas=i
        shortedList.append(blas)
        logo_abc= logo_abc + blas[0]
        blas=(0,0)


    #----- evresh_ekseresewn_twn_alfavitwn -----#

    for gi in shortedList:#vriskei tis eksereseis[grammata me idia pososta] sto keimeno
        h=""
        blas=gi
        h=blas[0]
        for i in shortedList:
            if blas[1]==i[1] and blas[0]!=i[0]:
                h=h+i[0]
        if h[0] not in l_exer[(len(l_exer)-1)] and len(h)>=2:
            l_exer.append(h)
        blas=(0,0)
    l_exer.remove(l_exer[0])
    #print(l_exer)

            
    #----- vriskei_oloys_toys_pithanous_sydyasmoys_twn_idiwn_posostwn -----# tributes to Kostas Sagmatopoulos
    
    def syndyasmoFinder(l_exer):#

        new_l_exer=[]
        def fun(str):
            result=[]
            if len(str) == 1:
                result = [str]
            else:
                for letter in str:
                    new_str=remove_letter(str, letter)
                    combs=fun(new_str)
                    for i in combs:
                        result.append(letter+i)
            return result

        def remove_letter(str, letter):#
            result=""
            removed=False
            for i in str:
                if i==letter and not removed:
                    removed=True
                else:
                    result+=i
            return result
        
        for grams in l_exer:
            new_l_exer.append(fun(grams))
            
        return new_l_exer#epistrefei mia lista me oloys toys dynatoys syndiasmoys twn idwn posostwn


    #----- vriskei_oloys_toys_pithanous_sydyasmoys_twn_alfavitwn_symfwna_me_ta_idia_pososta -----#
    
    expList=[]
    newExpList=[]
    syndList=syndyasmoFinder(l_exer)
    
    for Synds in syndList:
        for synd in Synds:
            new_alpha=""
            holdfor=0
            if syndList.index(Synds)==0:
                new_alpha=""
                for gram in logo_abc :
                    if gram in synd and holdfor==0:
                        new_alpha=new_alpha+synd
                        holdfor=len(l_exer[syndList.index(Synds)])
                        
                    if holdfor>0:
                        holdfor=holdfor-1
                        
                    else:
                        new_alpha=new_alpha+gram
                expList.append(new_alpha)
                holdfor=0
            else:
                for alpha in expList:
                    new_alpha=""
                    for gram in alpha:
                        if gram in synd and holdfor==0:
                            new_alpha=new_alpha+synd
                            holdfor=len(l_exer[syndList.index(Synds)])
                            
                        if holdfor>0:
                            holdfor=holdfor-1
                            
                        else:
                            new_alpha=new_alpha+gram
                    newExpList.append(new_alpha)
                    holdfor=0
                    
        if syndList.index(Synds)>0:
            expList=newExpList
            newExpList=[]
                        
    return expList    


prevnum=int
for i in keimena:
    if int((keimena.index(i)+1)/len(keimena)*100)%25==0 and prevnum!=int((keimena.index(i)+1)/len(keimena)*100):
        print("Analysh ypokeimenwn: "+str(int((keimena.index(i)+1)/len(keimena)*100))+"%")
        prevnum=int((keimena.index(i)+1)/len(keimena)*100)
    List=keim_analiser(i)
    for alpha in List:
        L_List.append(alpha)

print("Plithos logotexnikwn alphavitwn: "+str(len(L_List)))


#----- omadopoihsh_kata_70%_omoiothta_alphavitwn -----#

print("\nOmadopoihsh kata 70% omoiothta logotexnikwn alfavitwn: Running...")#pairnei peripoy 20 lepta-------------------------->>>

def logalpha_grouping():#grouparei tis alphavites poy einai kata 70% idies mazi 
    ALL_List=[]
    for i in L_List:#koitaei an yparxei paromoia h idia alphavita sth lista
        All_List=[]
        dinn=0
        for di in L_List:
            dinn=0
            for gram in i:
                if gram == di[i.find(gram)]:
                    dinn=dinn+1
            if dinn >= 17:#an einai 70% idies
                All_List.append(di)
        for i in All_List:
            L_List.remove(i)
        ALL_List.append(All_List)
    
    return ALL_List

with open("log-List-shorted.txt") as f:
    All_log_List=[]
    all_List=[]
    for line in f:
        if line != "- - - - - - -\n":
            all_List.append(line.strip())
        else:
            All_log_List.append(all_List)
            all_List=[]

print("telos_2 log-List-shorted "+str(sum([len(x) for x in All_log_List]))+" All groups "+str(len(All_log_List)))

#All_log_List=list(logalpha_grouping())
print("Omadopoihsh kata 70% omoiothta logotexnikwn alfavitwn: 100%")
print("Plithos omadwn kata 70% omoiwn logotexnikwn alfavitwn: "+str(len(All_log_List)))


#------------------------ analysh_kryptografhmenoy_keimenoy_kai_dhmioyrgia_ths_listas_twn_alfavitwn ------------------------#

def capitalizer(text):#metatrepei kathe gramma toy keimenoy se kefalaio
    S=""
    for kgram in text:
        if kgram in aBC and kgram not in ABC:
            for gri in abc:
                if kgram in gri:
                    S=S+ABC[abc.index(gri)]
        else:
            S=S+kgram
    return S            

K_Text=capitalizer(K_Text)

K_List=[]
K_List=keim_analiser(K_Text)
print("\nAnalysh kryptografhmenoy keimenoy: 100%")
print("Plithos kryptografhmenwn alphavitwn: "+str(len(K_List)))

lengtKeim=0
for i in K_Text:
    if i in aBC:
        lengtKeim=lengtKeim+1
print("Plithos grammatwn sto kryptografhmeno keimeno: "+str(lengtKeim))



#------------------------ telikh_analysh_kai_apokryptografhsh_keimenoy ------------------------#

with open("kef-Greek-words-shorted.txt") as f:#anoigei to arxeio kai ftiaxnei mia shorted lista arxizontas me afksousa seira ws pros to megethos twn leksewn
    words=[]
    Words=[]
    for line in f:
        if line != "- - - - - - -\n":
            Words.append(line.strip())
        else:
            words.append(Words)
            Words=[]
            
print("\nEllhnikes lekseis apo leksiko >>> kef-Greek-words-shorted.txt: Extracted ")
print("Plithos ellhnikwn leksewn: "+str(sum([len(x) for x in words]))+"\n")


#----- synarthsh_apokryptografhshs_keimenoy_(Antikatastash_grammatwn) -----#

def decrypt(myText,k_alfa,L_alfa):#antikathista ta grammata toy keimenoy symfwna me thn logotexnikh alphavita
        S=""
        for i in myText:
            if i in ABC:
                p=k_alfa.find(i)
                S=S+L_alfa[p]
            else:
                S=S+i
        return S


#----- evresh_posostoy_ellhnikothtas_apokryptografhmenoy_keimenou -----#

def pososto_ellhnikothtas(keim):#vriskei poso % ellhniko einai to keimeno
    LekseisKeimenoy=[]
    dinn=0
    synolpososto=0
    mialeksi=""
    for i in keim:#xwrizei to keimeno stis epimerous lekseis toy
        if i in ABC :
            mialeksi=mialeksi+i
        elif len(mialeksi)>0:
            LekseisKeimenoy.append(mialeksi)
            mialeksi=""
            
    for lekshs in LekseisKeimenoy:#koitaei an yparxei paromoia h idia leksh sto words 
        pososto=0
        pithLekseis=[]
        for li in words[len(lekshs)-1]:
            dinn=0
            for numi in range(len(lekshs)):
                if lekshs[numi]==li[numi]:
                    dinn=dinn+1
            if pososto<dinn:
                pososto=dinn
                pithLekseis=[]
            if pososto==dinn:
                pithLekseis.append(li)
                
        #print(lekshs,pithLekseis)
        pososto=(pososto*100)/len(lekshs)#ypologizei poso % ellhnikh einai h leksh
        synolpososto=synolpososto+pososto*len(lekshs)/lengtKeim#athrizei ta pososta twn leksewn kai katalhgei sto apotelesma 

    return synolpososto


#----- evresh_(megalyteroy_posostoy_ellhnikothtas)_kalyteroy_syndiasmoy_krypto-alphavitas_kai_logo-alphavitas -----#

print('Evresh ths veltisths alphavitas gia thn apokryptografhsh: Running...\n')
print("Ekinhsh analyshs gia "+str(len(K_List))+" alphavites\n")

##pososta=[]
##for kalph in K_List:#psaxnei sthn lista me tis krypto-alphavites gia thn kalyetrh
##    print("<---------------> <"+str(K_List.index(kalph))+"> <--------------->")
##    prohg_posos=0
##    for list_alpha in All_log_List:#psaxnei sthn lista me tis logo-alphavites gia thn ypo-lista me ta megalytera pososta ellhnikothtas 
##        pososto = pososto_ellhnikothtas(decrypt(K_Text,kalph,list_alpha[0]))
##        if pososto > prohg_posos:
##            prohg_posos= pososto
##            log=([list_alpha,kalph])
##    print(prohg_posos)
##    pososta.append([prohg_posos,log])
##
##prohg_posos=[0]#vriskei poia apo tis ypo-listes exei to megalytero pososto ellhnikothtas    
##for i in pososta:
##    pososto=i[0]
##    if pososto > prohg_posos[0]:
##        prohg_posos= i

prohg_posos=[75.16129032258065,[['ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΦΘΖΞΒΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΘΦΞΒΖΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΘΦΨΒΞΖ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΦΘΨΖΒΞ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΘΦΒΖΞΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΘΦΒΞΨΖ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΦΘΞΒΖΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΘΦΒΞΖΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΦΘΞΖΒΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΘΦΞΖΨΒ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΦΘΨΒΖΞ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΘΦΨΞΖΒ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΘΦΨΖΞΒ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΦΘΨΞΖΒ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΦΘΞΖΨΒ', 'ΟΙΣΤΑΕΗΚΝΡΩΥΛΓΠΧΜΔΦΘΞΒΖΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΛΓΥΠΧΜΔΘΦΨΞΖΒ', 'ΟΙΣΤΑΕΗΚΝΡΩΥΛΓΠΧΜΔΦΘΒΞΖΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΛΓΥΠΧΜΔΘΦΞΖΒΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΥΓΛΠΧΜΔΘΦΞΒΖΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΛΥΓΠΧΜΔΦΘΨΞΖΒ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΥΛΠΧΜΔΘΦΞΖΒΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΥΛΠΧΜΔΘΦΨΞΒΖ', 'ΟΙΣΤΑΕΗΚΝΡΩΥΓΛΠΧΜΔΘΦΒΞΨΖ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΥΛΠΧΜΔΦΘΞΖΒΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΥΛΠΧΜΔΦΘΨΞΒΖ', 'ΟΙΣΤΑΕΗΚΝΡΩΥΓΛΠΧΜΔΘΦΒΞΖΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΥΛΠΧΜΔΘΦΞΨΖΒ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΥΛΠΧΜΔΦΘΨΒΖΞ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΥΛΠΧΜΔΦΘΞΒΖΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΥΛΠΧΜΔΘΦΒΞΖΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΥΛΠΧΜΔΘΦΨΖΞΒ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΥΛΠΧΜΔΘΦΨΞΖΒ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΥΛΠΧΜΔΘΦΒΖΞΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΥΛΠΧΜΔΦΘΒΞΖΨ', 'ΟΙΣΤΑΕΗΚΝΡΩΓΥΛΠΧΜΔΦΘΒΖΨΞ', 'ΟΙΣΑΤΕΗΚΝΡΩΓΛΥΠΜΧΔΘΦΒΞΨΖ', 'ΟΙΣΑΤΕΗΚΝΡΩΓΛΥΠΜΧΔΘΦΞΒΖΨ', 'ΟΙΣΑΤΕΗΚΝΡΩΓΛΥΠΜΧΔΘΦΒΖΞΨ', 'ΟΙΣΑΤΕΗΚΝΡΩΓΛΥΠΜΧΔΘΦΒΞΖΨ', 'ΟΙΣΑΤΕΗΚΝΡΩΓΛΥΠΜΧΔΘΦΨΞΖΒ', 'ΟΙΣΑΤΕΗΚΝΡΩΓΥΛΠΜΧΔΘΦΒΞΖΨ', 'ΟΙΣΑΤΕΗΚΝΡΩΥΓΛΠΜΧΔΘΦΒΞΖΨ'],'ΧΝΞΟΖΣΑΠΓΘΩΒΤΦΗΛΥΜΙΡΚΕΔΨ']]
        
pr_pososto=(0,0)        
for i in prohg_posos[1][0]:
    pos=pososto_ellhnikothtas(decrypt(K_Text,prohg_posos[1][1],i))
    if pos>pr_pososto[0]:
        pr_pososto=(pos,i)

print('\nEvresh ths veltisths alphavitas gia thn apokryptografhsh: Completed!!!\n')        
print("Veltistos syndiasmos krypto-logo-alphavitas: \nLogo: "+str(pr_pososto[1])+"\nKrypto: "+str(prohg_posos[1][1])+"\nPososto toy veltistoy syndyasmou: "+str(pr_pososto[0])+"\n")

kalph=prohg_posos[1][1]


#----- ekinhsh_analyshs_ths_dothisas_kalyterhs_ypo-listas_kai_ths_loypas_veltiwshs_telikhs_alphavitas -----#

def fin_list_analysation(finList):
    posoList=finList
    countAlpha=(0,0,0)
    posoList.sort(reverse=True,key=lambda x: (pososto_ellhnikothtas(decrypt(K_Text,kalph,x))))
    
    if len(posoList)>5:#pairnei tis 5 prwtes-kalyteres alphavites ap thn finList
        posoList=posoList[0:5]
    
    for log_i in posoList:#vlepei mia mia tis kalyteres alphavites
        LekseisKeimenoy=[]
        kalesLex=[]
        oxiKalesLex=[]
        pososLeksewn=[]
        dinn=0
        mialeksi=""
        generlalph=""
        lexList=""

        keim=decrypt(K_Text,kalph,log_i)
        
        for i in keim:#xwrizei to keimeno stis epimerous lekseis toy
            if i in ABC :
                mialeksi=mialeksi+i
            elif len(mialeksi)>0:
                LekseisKeimenoy.append(mialeksi)
                mialeksi=""

        for lekshs in LekseisKeimenoy:#koitaei an yparxei paromoia h idia leksh sto words kai vazei tis 100% se mia ksexwristei lista
            pososto=0
            dinn=0
            pithLekseis=[]
            for li in words[len(lekshs)-1]:
                dinn=0
                for numi in range(len(lekshs)):
                    if lekshs[numi]==li[numi]:
                        dinn=dinn+1
                if pososto<dinn:
                    pososto=dinn
                    pithLekseis=[]
                if pososto==dinn:
                    pithLekseis.append(li)
            
            if lekshs in pithLekseis and len(lekshs)>4:
                kalesLex.append(lekshs)
                lexList=("".join(OrderedDict.fromkeys(lexList+lekshs)))
            else:
                oxiKalesLex.append(lekshs)

            if lekshs in kalesLex or pososto==len(lekshs):#vazei ta pososta tis pithanes lekseis kai tis idies tis lekseis se mia lista 
                continue
            else:
                pososLeksewn.append([lekshs,(pososto*100)/len(lekshs),pithLekseis])
                
        pososLeksewn.sort(reverse=True,key=lambda x: ( -len(x[2]), x[1], len(x[0])))#shortarei thn lista analogws twn posostwn 
        
        for gram in log_i: #afhnei mono ta grammata ths alphavitas poy yparxoyn stis lekseis poy exoyn vrethei
            if gram in lexList:
                generlalph=generlalph+gram
            else:
                generlalph=generlalph+"-"
 
        print(generlalph,pososto_ellhnikothtas(decrypt(K_Text,kalph,log_i)))
        fin_lalpha_transformation(pososLeksewn,log_i)            
        print("Analysed:",posoList.index(log_i)+1,"out of the best",len(posoList),)
        
        global counter
        global prohgposkeim
        
        if prohgposkeim>countAlpha[1] or prohgposkeim==countAlpha[1]:#vriskei thn "ellhnikoterh" alla kai kalyterh xronika alfavita
            if counter[1]<countAlpha[0] or posoList.index(log_i)==0:
                countAlpha=(counter[1],prohgposkeim,log_i)
        
        counter=[0,0]
        prohgposkeim=0
        
    return countAlpha[1:3]


#----- tropopoiei_thn_logotexnikh_alfavita_analoga_me_tis_allages_poy_proteinei_to_leksiko(π.χ: Θασιλιάς --> Allagh[Θ-Β]) -----# 

def fin_lalpha_transformation(dataLexList,l_alpha):
    
    goodList=dataLexList[0:4]
    list_to_remove=[]
    #print(l_alpha)
    for lex in goodList:
        lex.append([])
        for pithlex in lex[2]:#prosthetei ta grammata se mia ksexwristh lista sto lex
            lex[3].append([])
            for ite in range(len(lex[0])):
                if lex[0][ite] != pithlex[ite]:
                    lex[3][lex[2].index(pithlex)].append([lex[0][ite],pithlex[ite]])
                    
            for grm in lex[3][lex[2].index(pithlex)]:#koitaei an to gramma pros allagh yparxei eidh sthn leksh gia na thn aporipsei
                if grm[1] in lex[0]:
                    list_to_remove.append(lex)
                    
    for lex_remove in goodList:
        if lex_remove in list_to_remove:
            goodList.remove(lex_remove)

    couples_log=[]
    prev_lalpha=l_alpha
    new_lalpha=""
    
    for lx in goodList:#ftiaxnei thn nea alphavita analogws me tis epithimies twn leksewn 
        for lex_couple in lx[3]:
            for couple in lex_couple:
                if couple not in couples_log:
                    couples_log.append(couple)
                    couples_log.append([couple[1],couple[0]])
                    new_lalpha=""
                    
                    for lgrm in prev_lalpha:
                        if lgrm==couple[0]:
                            new_lalpha=new_lalpha+couple[1]

                        elif lgrm==couple[1]:
                            new_lalpha=new_lalpha+couple[0]

                        else:
                            new_lalpha=new_lalpha+lgrm
                    prev_lalpha=new_lalpha

    fin_keimenikos_epeksergasths(new_lalpha)

def fin_keimenikos_epeksergasths(new_lalpha):
    
    LekseisKeimenoy=[]
    kalesLex=[]
    oxiKalesLex=[]
    pososLeksewn=[]
    dinn=0
    mialeksi=""
    generlalph=""
    lexList=""
    keim=decrypt(K_Text,kalph,new_lalpha)
    
    for i in keim:#xwrizei to keimeno stis epimerous lekseis toy
        if i in ABC :
            mialeksi=mialeksi+i
        elif len(mialeksi)>0:
            LekseisKeimenoy.append(mialeksi)
            mialeksi=""

    for lekshs in LekseisKeimenoy:#koitaei an yparxei paromoia h idia leksh sto words kai vazei tis 100% se mia ksexwristei lista
        pososto=0
        dinn=0
        pithLekseis=[]
        for li in words[len(lekshs)-1]:
            dinn=0
            for numi in range(len(lekshs)):
                if lekshs[numi]==li[numi]:
                    dinn=dinn+1
            if pososto<dinn:
                pososto=dinn
                pithLekseis=[]
            if pososto==dinn:
                pithLekseis.append(li)
        
        if lekshs in pithLekseis and len(lekshs)>4:
            kalesLex.append(lekshs)
            lexList=("".join(OrderedDict.fromkeys(lexList+lekshs)))
        else:
            oxiKalesLex.append(lekshs)

        if lekshs in kalesLex or pososto==len(lekshs):#vazei ta pososta tis pithanes lekseis kai tis idies tis lekseis se mia lista 
            continue
        else:
            pososLeksewn.append([lekshs,(pososto*100)/len(lekshs),pithLekseis])
            
    pososLeksewn.sort(reverse=True,key=lambda x: ( -len(x[2]), x[1], len(x[0])))#shortarei thn lista analoga me ta pososta
    
    
    for gram in new_lalpha: #afhnei mono ta grammata ths alphavitas poy yparxoyn stis lekseis poy exoyn vrethei
        if gram in lexList:
            generlalph=generlalph+gram
        else:
            generlalph=generlalph+"-"
            
            
    global counter
    global prohgposkeim
    counter[1]=counter[1]+1
    
    while counter[0]<20:#tha stamathsei na trexei an edw kai 20 epanalhpseis(metatropes tis alphavitas) den yparksei veltiwsh
        pososkeim=pososto_ellhnikothtas(decrypt(K_Text,kalph,new_lalpha))
        if pososkeim>prohgposkeim:
            counter[0]=0
            counter[1]=counter[1]-1
            prohgposkeim=pososkeim
            print(generlalph,pososto_ellhnikothtas(decrypt(K_Text,kalph,new_lalpha)))
        else:
            counter[0]=counter[0]+1
            fin_lalpha_transformation(pososLeksewn,new_lalpha)


counter=[0,0]
prohgposkeim=0

#----- ekinhsh_diadikasias_afksishs_toy_posostoy_ellhnikothtas_ths_yparxoysas_kalyterhs_logotexnikhs_alfavitas_poy_vrethei -----#
fin_list_analysation([(fin_list_analysation(prohg_posos[1][0]))[1]])


#[75.16129032258065, ['ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΦΘΨΖΒΞ', 43, 'ΧΝΞΟΖΣΑΠΓΘΩΒΤΦΗΛΥΜΙΡΚΕΔΨ', 15]] ΟΙΣΤΑΕΗΚΝΡΩΓΛΥΠΧΜΔΦΘΖΞΒΨ #pairnei peripoy 2 meres
