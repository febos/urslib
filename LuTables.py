
modelno = 1

def LuHelices(model):

    result  = []

    for h in model.helices:

        ID    = h['ID']
        Len   = h['SIZE']
        seq1  = h['SEQ1']
        seq2  = h['SEQ2']
        form  = h['FORM']
        stems = h['STEMS']
        lones = h['LONES']

        result.append([ID,modelno,Len,seq1,seq2,form,stems,lones])

    return result

def LuStems(model):

    result  = []

    for s in model.lustems:

        ID     = s['ID']
        dssr   = s['DSSRID']
        chain1 = model.bpairs[s['PAIRS'][0]-1]['CHAIN1']
        chain1 = model.chains[chain1]['ID']
        chain2 = model.bpairs[s['PAIRS'][0]-1]['CHAIN2']
        chain2 = model.chains[chain2]['ID']
        Len    = s['LENGTH']
        lseq   = s['SEQ1']
        rseq   = s['SEQ2']
        form   = s['FORM']

        result.append([ID,modelno,dssr,chain1,chain2,Len,lseq,rseq,form])
        
    return result

def LuStemHelix(model):

    result = []

    for s in model.lustems:

        if s['HELIX']: result.append([modelno,s['ID'],s['HELIX']])

        for hel in s['OTHERHELICES']: result.append([modelno,s['ID'],hel])

    return result

def LuMultiplets(model):

    result  = []

    for m in model.lumults:

        ID  = m['ID']
        Len = m['SIZE']
        seq = m['SEQ']

        result.append([ID,modelno,Len,seq])

    return result

def LuNphbs(model):

    result  = []

    for n in model.non_pairs:

        ID     = n['ID']
        nucl1  = n['NUCL1']
        nucl2  = n['NUCL2']
        hbnum  = n['HBONDSNUM']
        hbonds = n['HBONDS']
        stack  = n['STACKING']
        
        result.append([ID,modelno,nucl1,nucl2,hbnum,hbonds,stack])

    return result

def LuNonLoops(model):

    result  = []

    for n in model.non_loops:

        ID    = n['ID']
        ch    = n['START'].split('.')[0]
        if ch not in model.chains: ch = model.headers['MASKEDCHS'][ch]
        chain = model.chains[ch]['ID']
        Len   = n['LENGTH']
        seq   = n['SEQ']
        Break = int(n['BREAK'])
        start = n['START']
        end   = n['END']

        result.append([ID,modelno,chain,Len,seq,Break,start,end])

    return result

def LuKissing(model):

    result  = []

    for k in model.kissing:

        ID     = k['ID']
        loop1  = k['HAIRPIN1']
        loop2  = k['HAIRPIN2']
        lustem = k['KISS']

        result.append([ID,modelno,loop1,loop2,lustem])

    return result

def LuAminors(model):

    result  = []

    for a in model.a_minors:

        ID      = a['ID']
        nucl    = a['NUCL']
        pair    = a['PAIR']
        desc    = model.bpairs[pair-1]['PAIR']
        hbonds1 = len(a['BONDS1'])
        hbonds2 = len(a['BONDS2'])
        Type    = a['TYPE']
        Class   = a['CLASS']

        result.append([ID,modelno,nucl,pair,desc,hbonds1,hbonds2,Type,Class])

    return result

def LuUturns(model):

    result  = []

    for u in model.u_turns:

        ID     = u['ID']
        chain  = model.chains[u['NUCL1'].split('.')[0]]['ID']
        nucl1  = u['NUCL1']
        nucl2  = u['NUCL2']
        hbonds = len(u['BONDS'])

        result.append([ID,modelno,chain,nucl1,nucl2,hbonds])

    return result

def LuZippers(model):

    result  = []

    for z in model.ribzips:

        ID  = z['ID']
        Len = z['LENGTH']
        seq = z['SEQ']

        result.append([ID,modelno,Len,seq])

    return result

def LuKturns(model):

    result  = []

    for kt in model.k_turns:

        ID    = kt['ID']
        bp    = kt['PAIR']
        helix = kt['HELIX']
        stem1 = kt['STEM1']
        stem2 = kt['STEM2']
        iloop = kt['ILOOP']
        Type  = kt['TYPE']

        result.append([ID,modelno,bp,helix,stem1,stem2,iloop,Type])

    return result

def LuHairpins(model):

    result  = []

    for h in model.lu_loops['HAIRPIN']:

        ID     = h['ID']
        chain  = model.chains[h['NUCLS'][0].split('.')[0]]['ID']
        Len    = h['LENGTH']
        seq    = h['SEQ']
        lustem = h['CLOSING']

        result.append([ID,modelno,chain,Len,seq,lustem])

    return result

def LuBulges(model):

    result  = []

    for b in model.lu_loops['BULGE']:

        ID    = b['ID']
        chain = model.chains[b['NUCLS'][0].split('.')[0]]['ID']
        prev  = b['PREV']
        Next  = b['NEXT']
        desc  = b['TYPE']
        seq   = b['SEQ']
        Len   = b['LENGTH']

        result.append([ID,modelno,chain,prev,Next,desc,seq,Len])

    return result

def LuInternals(model):

    result  = []

    for i in model.lu_loops['INTERNAL']:

        ID     = i['ID']
        chain1 = model.chains[i['LNUCLS'][0].split('.')[0]]['ID']
        chain2 = model.chains[i['RNUCLS'][0].split('.')[0]]['ID']
        prev   = i['PREV']
        Next   = i['NEXT']
        desc   = i['TYPE']
        sym    = int(i['SYM'])
        lseq   = i['LSEQ']
        rseq   = i['RSEQ']
        Len    = i['LENGTH']

        result.append([ID,modelno,chain1,chain2,prev,
                       Next,desc,sym,lseq,rseq,Len])
    return result

def LuJunctions(model):

    result  = []

    for j in model.lu_loops['JUNCTION']:

        ID      = j['ID']
        threads = j['THREADS']
        desc    = j['TYPE']
        Len     = j['LENGTH']

        result.append([ID,modelno,threads,desc,Len])

    return result

def LuJuncThreads(model):

    result  = []

    for j in model.lu_loops['JUNCTION']:

        for i in range(j['THREADS']):

            if j['NUCLS'][i]:

                junc   = j['ID']
                chain  = model.chains[j['NUCLS'][i][0].split('.')[0]]['ID']
                num    = i+1
                start  = j['NUCLS'][i][0]
                end    = j['NUCLS'][i][-1]
                Len    = len(j['NUCLS'][i])
                seq    = j['SEQS'][i]
                lustem = j['CLOSING'][i]

                result.append([junc,modelno,chain,num,start,end,Len,seq,lustem])

    return result
