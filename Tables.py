try: from urslib import nrpdb
except ImportError: import nrpdb

modelno = 1

place_dict = {'RES':0,'LIGANDS': 1}

def checkNone(param): # checking: NULL or not

    if not param: return '\\N' # if param is of None-type
    else:         return param 

def files(model):

    files = []

    if model.headers['MDLNO'] != 1: return files

    name    = model.headers['PDBFILE']
    models  = model.headers['NUMMDL']
    Type    = model.headers['TYPE']
    head    = model.headers['HEADER']
    date    = model.headers['DATE']
    title   = model.headers['TITLE']
    keywds  = ';'.join(model.headers['KEYWDS'])
    mdltyp  = ';'.join(model.headers['MDLTYP'])
    author  = model.headers['AUTHOR']
    expdata = ';'.join(model.headers['EXPDTA'])
    resol   = model.headers['RESOL']
    words   = model.allwords

    return [[name,models,Type,head,date,title,
             keywds,mdltyp,author,expdata,resol,words]]

def models(model):

    ID      = model.headers['ID']
    number  = model.headers['MDLNO']
    file    = model.headers['PDBFILE']
    main    = int(number == 1)
    nr      = int(main==1 and file in nrpdb.files)
    chains  = {'RNA':0,'DNA':0,'Protein':0,'Unknown':0}
    maxlens = {'RNA':0,'DNA':0,'Protein':0,'Unknown':0}
    lens    = {'RNA':0,'DNA':0,'Protein':0,'Unknown':0}

    for ch in sorted(list(model.chains.keys())):

        Type = model.chains[ch]['TYPE']
        Len  = model.chains[ch]['LENGTH'] 

        if Type in chains: chains[Type] += 1
        if Type in lens:   lens[Type]   += Len
        if Type in maxlens and Len > maxlens[Type]: maxlens[Type] = Len
        
    atoms   = model.ids['ATOM']
    nucls   = model.ids['NUCL']
    aminos  = model.ids['AMINO']
    ligands = model.ids['LIGAND']

    liglist = checkNone(model.headers['LIGLIST'])
    metlist = checkNone(model.headers['METLIST'])

    return [[ID,number,file,main,chains['RNA'],maxlens['RNA'],lens['RNA'],chains['DNA'],
             maxlens['DNA'],lens['DNA'],chains['Protein'],maxlens['Protein'],
             lens['Protein'],chains['Unknown'],maxlens['Unknown'],lens['Unknown'],
             atoms,nucls,aminos,ligands,liglist,metlist,nr]]

def molecules(model):

    result = []

    if model.headers['MDLNO'] != 1: return result

    for mol in model.molecules.values():

        ID     = mol['ID']
        file   = model.headers['PDBFILE']
        mol_id = ID

        dets = {'MOLECULE':'\\N','ORGANISM_SCIENTIFIC':'\\N','FRAGMENT'  :'\\N',
                'SYNONYM' :'\\N','EC'                 :'\\N','ENGINEERED':'\\N',
                'MUTATION':'\\N','OTHER_DETAILS'      :'\\N'}

        for token in dets:

            if mol[token]: dets[token] = mol[token] # filling required tokens

        result.append([ID,file,mol_id,dets['MOLECULE'],dets['ORGANISM_SCIENTIFIC'],dets['FRAGMENT'],
                       dets['SYNONYM'],dets['EC'],dets['ENGINEERED'],dets['MUTATION'],
                       dets['OTHER_DETAILS'],mol['ORGCAT']])
    return result

def chains(model):

    result  = []

    for ch in sorted(list(model.chains.keys())):

        ID         = model.chains[ch]['ID']
        molecule   = model.chains[ch]['MOL_ID']
        letter     = ch 
        Len        = model.chains[ch]['LENGTH']
        liglen     = len(model.chains[ch]['LIGANDS'])
        Type       = model.chains[ch]['TYPE']
        seq        = ','.join(model.chains[ch]['SEQ2'])
        ligseq     = ','.join(model.chains[ch]['LIGSEQ'])
        lubrackets = model.chains[ch]['LUBRACKETS']
        brackets   = model.chains[ch]['BRACKETS']
        slbrackets = model.chains[ch]['SLBRACKETS']
        start      = model.chains[ch]['RES'][0]['DSSR']
        end        = model.chains[ch]['RES'][-1]['DSSR']
        bound      = model.chains[ch]['BOUND']
        share      = bound/Len
        sharewcwb  = model.chains[ch]['BOUNDWCWB']/Len
        ligbound   = model.chains[ch]['LIGBOUND']
        ligshare   = 0
        if liglen:  ligshare = ligbound/liglen
        fake       = int(model.chains[ch]['GARBAGE'])
        diagram    = model.chains[ch]['DIAGRAM']
        seqbrack = ''

        if slbrackets=='\\N': seqbrack = '\\N'
        else:
            for i in range(len(model.chains[ch]['SEQ2'])):
                seqbrack += model.chains[ch]['SEQ2'][i]
                seqbrack += slbrackets[i]

        result.append([ID,modelno,molecule,letter,Len,liglen,Type,seq,ligseq,
                       lubrackets,brackets,slbrackets,start,end,bound,share,
                       ligbound,ligshare,fake,diagram,seqbrack,sharewcwb])
    return result

def nucls(model):

    result  = []

    for ch in sorted(list(model.chains.keys())):

        for where in ('RES','LIGANDS'):

            for i in range(len(model.chains[ch][where])):

                if model.chains[ch][where][i]['TYPE'] in ('RNA', 'DNA'):

                    ID      = model.chains[ch][where][i]['ID']
                    dssr    = model.chains[ch][where][i]['DSSR']
                    chain   = model.chains[ch]['ID']
                    letter  = ch
                    thread  = checkNone(model.chains[ch][where][i]['THREAD'])
                    wing    = checkNone(model.chains[ch][where][i]['WING'])
                    oldwing = checkNone(model.chains[ch][where][i]['OLDWING'])
                    fstems  = model.chains[ch][where][i]['FSTEMS']
                    place   = place_dict[where]
                    num     = i+1
                    Zip     = model.chains[ch][where][i]['ZIP']
                    mult    = model.chains[ch][where][i]['MULT']
                    lumult  = model.chains[ch][where][i]['LUMULT']
                    bps     = model.chains[ch][where][i]['BPS']
                    miss    = int(model.chains[ch][where][i]['MISS'])
                    res     = model.chains[ch][where][i]['NAME']
                    cifid   = model.chains[ch][where][i]['CIFID']
                    
                    if where=='LIGANDS' or model.chains[ch]['DIAGRAM']=='\\N':
                        diagram,chnumindiag = '\\N','\\N'
                        bracket, slbracket  = '\\N','\\N' 
                    else:
                        diagram     = model.chains[ch]['DIAGRAM']
                        chnumindiag = model.diagrams[diagram-1]['SEQ'].find(ch)+1
                        bracket     = model.chains[ch]['BRACKETS'][i]
                        slbracket   = model.chains[ch]['SLBRACKETS'][i]
                        
                    result.append([ID,dssr,modelno,chain,letter,thread,wing,oldwing,
                                   fstems,place,num,Zip,mult,lumult,bps,miss,
                                   chnumindiag,diagram,res,bracket,slbracket,cifid])
    return result
                
def aminos(model):

    result  = []

    for ch in sorted(list(model.chains.keys())):

        for where in ('RES','LIGANDS'):

            for i in range(len(model.chains[ch][where])):

                if model.chains[ch][where][i]['TYPE'] == 'Protein':

                    ID     = model.chains[ch][where][i]['ID']
                    dssr   = model.chains[ch][where][i]['DSSR']
                    chain  = model.chains[ch]['ID']
                    letter = ch
                    place  = place_dict[where]
                    num    = i+1
                    miss   = int(model.chains[ch][where][i]['MISS'])
                    res    = model.chains[ch][where][i]['NAME']
                    cifid  = model.chains[ch][where][i]['CIFID']

                    result.append([ID,dssr,modelno,chain,letter,place,num,miss,res,cifid])
    return result

def ligands(model):

    result  = []

    for ch in sorted(list(model.chains.keys())):

        for where in ('RES','LIGANDS'):

            for i in range(len(model.chains[ch][where])):

                if model.chains[ch][where][i]['TYPE'] == 'Unknown':

                    ID     = model.chains[ch][where][i]['ID']
                    dssr   = model.chains[ch][where][i]['DSSR']
                    chain  = model.chains[ch]['ID']
                    letter = ch
                    place  = place_dict[where]
                    num    = i+1
                    miss   = int(model.chains[ch][where][i]['MISS'])
                    cifid  = model.chains[ch][where][i]['CIFID']

                    result.append([ID,dssr,modelno,chain,letter,place,num,miss,cifid])
    return result

def atoms(model):

    result  = []

    for ch in sorted(list(model.chains.keys())):

        for where in ('RES','LIGANDS'):

            for i in range(len(model.chains[ch][where])):

                for atom in model.chains[ch][where][i]['ATOMS']:

                    ID       = atom['ID']
                    chain    = model.chains[ch]['ID']
                    res      = model.chains[ch][where][i]['DSSR']
                    restype  = model.chains[ch][where][i]['TYPE'][0]
                    if restype == 'U': restype = 'L'
                    name     = atom['NAME']
                    num      = atom['NUM']
                    elem     = atom['ELEM']
                    occup    = atom['OCCUP']
                    altloc   = atom['ALTLOC']
                    x        = atom['X']
                    y        = atom['Y']
                    z        = atom['Z']
                    rescifid = atom['CIFID']

                    result.append([ID,modelno,chain,res,restype,name,num,
                                   elem,occup,altloc,x,y,z,rescifid])
    return result

def BasePairs(model):

    result  = []

    for bp in model.bpairs:

        ID        = bp['ID']
        num       = bp['ID']
        chain1    = model.chains[bp['CHAIN1']]['ID']
        chain2    = model.chains[bp['CHAIN2']]['ID']
        nucl1     = bp['NUCL1'][0]
        bond      = bp['BOND']
        nucl2     = bp['NUCL2'][0]
        Type      = bp['TYPE']
        class1    = bp['CLASS'][0]
        class2    = bp['CLASS'][1]
        class3    = bp['CLASS'][2]
        stem      = checkNone(bp['STEM'])
        oldstem   = checkNone(bp['OLDSTEM'])
        fullstem  = checkNone(bp['FULLSTEM'])
        revstem   = checkNone(bp['REVSTEM'])
        lustem    = checkNone(bp['LUSTEM'])
        link      = checkNone(bp['LINK'])
        luhelix   = checkNone(bp['HELIX'])
        nuclmult  = checkNone(bp['NUCLMULT'])
        info1     = bp['INFO1']
        info2     = bp['INFO2']
        dist1     = bp['DIST1']
        dist2     = bp['DIST2']
        dist3     = bp['DIST3']
        tor       = bp['TOR']
        hbonds    = '; '.join(bp['HBONDS'])
        hbnum     = bp['HBONDSNUM']
        shear     = bp['SHEAR']
        stretch   = bp['STRETCH']
        stagger   = bp['STAGGER']
        buckle    = bp['BUCKLE']
        propeller = bp['PROPELLER']
        opening   = bp['OPENING']

        if not bp['STEP']: shift,slide,rise,tilt,roll,twist = '\\N', '\\N', '\\N', '\\N', '\\N', '\\N'
        else:
            step = bp['STEP'].split(' ')
            shift,slide,rise,tilt,roll,twist = step[0], step[1], step[2], step[3], step[4], step[5], 

        result.append([ID,modelno,num,chain1,chain2,nucl1,bond,nucl2,Type,
                       class1,class2,class3,stem,oldstem,fullstem,revstem,
                       lustem,link,luhelix,nuclmult,info1,info2,dist1,
                       dist2,dist3,tor,hbonds,hbnum,shear,stretch,
                       stagger,buckle,propeller,opening,shift,
                       slide,rise,tilt,roll,twist])
    return result

def towers(model):

    Type_dict = {'H':0,'J':1,'N':2}

    result  = []

    for t in model.towers:

        ID     = t['ID']
        stems  = t['STEMS']
        chain1 = model.chains[t['CHAIN1']]['ID']
        chain2 = model.chains[t['CHAIN2']]['ID']
        pseudo = t['PSEUDO']
        Type   = Type_dict[t['TYPE']]

        result.append([ID,modelno,stems,chain1,chain2,pseudo,Type])

    return result
        

def links(model):

    result  = []

    for l in model.links:

        ID      = l['ID']
        chain1  = model.chains[l['CHAIN1']]['ID']
        chain2  = model.chains[l['CHAIN2']]['ID']
        bp      = l['BP']
        bptype  = l['BPTYPE']
        lthread = checkNone(l['LEFTHRD'])
        rthread = checkNone(l['RIGHTHRD'])
        lwing   = checkNone(l['LEFTWING'])
        rwing   = checkNone(l['RIGHTWING'])
        Type    = l['TYPE']
        depth   = l['DEPTH']
        nucl1   = l['NUCL1'][0]
        nucl2   = l['NUCL2'][0]
        class1  = l['CLASS1']
        class2  = l['CLASS2']
        class3  = l['CLASS3']
        dist    = l['DIST']
        ss1     = checkNone(l['SS1'])
        ss2     = checkNone(l['SS2'])
        rel     = checkNone(l['REL'])

        result.append([ID,modelno,chain1,chain2,bp,bptype,lthread,
                       lwing,rthread,rwing,Type,depth,nucl1,nucl2,
                       class1,class2,class3,dist,ss1,ss2,rel])
    return result

def stems(model):

    result  = []

    for s in model.stems:

        ID        = s['ID']
        num       = s['ID']
        chain1    = model.chains[s['CHAIN1']]['ID']
        chain2    = model.chains[s['CHAIN2']]['ID']
        lseq      = s['LSEQ']
        rseq      = s['RSEQ']
        Len       = s['LEN']
        left      = s['LEFT']
        right     = s['RIGHT']
        pairseq   = s['PAIRSEQ']
        tower     = s['TOWER']
        loopclass = s['LOOPTYPE']
        looptype  = s['LOOPPSEUDO']
        oldstem   = checkNone(s['OLDSTEM'])
        fullstem  = checkNone(s['FULLSTEM'])
        mult      = s['MULT']
        diagram   = s['DIAGRAM']
        numindiag = s['NUMINDIAG']
        ecf       = s['ECF']
        numinecf  = s['NUMINECF']
        jmol      = s['JMOL']
        loopjmol  = s['LOOPJMOL']

        result.append([ID,modelno,num,chain1,chain2,lseq,rseq,Len,left,right,
                       pairseq,tower,loopclass,looptype,oldstem,fullstem,mult,
                       diagram,numindiag,ecf,numinecf,jmol,loopjmol])
    return result

def StemsOld(model):

    result  = []

    for s in model.oldstems:

        ID       = s['ID']
        num      = s['ID']
        chain1   = model.chains[s['CHAIN1']]['ID']
        chain2   = model.chains[s['CHAIN2']]['ID']
        lseq     = s['LSEQ']
        rseq     = s['RSEQ']
        left     = s['LEFT']
        right    = s['RIGHT']
        pairseq  = s['PAIRSEQ']
        fullstem = checkNone(s['FULLSTEM'])
        stems    = s['STEMS']
        Len      = s['LEN']
        mult     = s['MULT']
        jmol     = s['JMOL']

        result.append([ID,modelno,num,chain1,chain2,lseq,rseq,left,
                       right,pairseq,fullstem,stems,Len,mult,jmol])
    return result

def StemsFull(model):

    result  = []

    for s in model.fullstems:

        ID       = s['ID']
        num      = s['ID']
        chain1   = model.chains[s['CHAIN1']]['ID']
        chain2   = model.chains[s['CHAIN2']]['ID']
        lseq     = s['LSEQ']
        rseq     = s['RSEQ']
        Len      = s['LEN']
        left     = s['LEFT']
        right    = s['RIGHT']
        stems    = s['STEMS']
        oldstems = s['OLDSTEMS']
        pairseq  = s['PAIRSEQ']
        mult     = s['MULT']
        jmol     = s['JMOL']

        result.append([ID,modelno,num,chain1,chain2,lseq,rseq,Len,
                       left,right,stems,oldstems,pairseq,mult,jmol])
    return result

def wings(model):

    result  = []

    for w in model.wings['LU']:

        ID       = w['ID']
        chain    = model.chains[w['CHAIN']]['ID']
        stem     = w['STEM']
        another  = w['ANOTHER']
        prev     = checkNone(w['PREV'])
        Next     = checkNone(w['NEXT'])
        prevw    = checkNone(w['PREVW'])
        nextw    = checkNone(w['NEXTW'])
        Type     = w['TYPE']
        start    = w['START'][0]
        end      = w['END'][0]
        Len      = w['LEN']
        seq      = w['SEQ']
        ecf      = w['ECF']
        numinecf = w['NUMINECF']
        jmol     = w['JMOL']

        result.append([ID,modelno,chain,stem,another,prev,Next,prevw,
                       nextw,Type,start,end,Len,seq,ecf,numinecf,jmol])
    return result

def WingsOld(model):

    result  = []

    for w in model.wings['OLD']:

        ID      = w['ID']
        chain   = model.chains[w['CHAIN']]['ID']
        stem    = w['STEM']
        another = w['ANOTHER']
        prevw   = checkNone(w['PREVW'])
        nextw   = checkNone(w['NEXTW'])
        Type    = w['TYPE']
        start   = w['START'][0]
        end     = w['END'][0]
        Len     = w['LEN']
        seq     = w['SEQ']

        result.append([ID,modelno,chain,stem,another,prevw,
                       nextw,Type,start,end,Len,seq])
    return result

def WingsFull(model):

    result  = []

    for w in model.wings['FULL']:

        ID      = w['ID']
        chain   = model.chains[w['CHAIN']]['ID']
        stem    = w['STEM']
        another = w['ANOTHER']
        prevw   = checkNone(w['PREVW'])
        nextw   = checkNone(w['NEXTW'])
        Type    = w['TYPE']
        start   = w['START'][0]
        end     = w['END'][0]
        Len     = w['LEN']
        seq     = w['SEQ']

        result.append([ID,modelno,chain,stem,another,prevw,
                       nextw,Type,start,end,Len,seq])
    return result

def threads(model):

    result  = []

    for t in model.threads:

        ID    = t['ID']
        chain = model.chains[t['CHAIN']]['ID']
        prev  = checkNone(t['PREV'])
        Next  = checkNone(t['NEXT'])
        start = t['START'][0]
        end   = t['END'][0]
        Len   = t['LEN']
        links = t['LINKS']
        seq   = t['SEQ']
        place = place_dict[t['START'][1]]
        full  = int(t['FULL'])
        ext   = t['EXT']
        jmol  = checkNone(t['JMOL'])

        result.append([ID,modelno,chain,prev,Next,start,end,
                       Len,links,seq,place,full,ext,jmol])
    return result

def hairpins(model):

    result  = []

    for h in model.loops['HAIRPIN']:

        ID     = h['ID']
        stem   = h['STEM']
        chain  = model.chains[h['CHAIN']]['ID']
        wings  = h['WINGS']
        Type   = h['PTYPE']
        desc   = h['TYPE']
        Len    = h['LEN']
        TLen   = h['TLEN']
        links  = h['LINKS']
        breaks = h['BREAKS']
        sjmol  = checkNone(h['SJMOL'])
        tjmol  = checkNone(h['TJMOL'])
        sfjmol = checkNone(h['SFJMOL'])
        bfjmol = checkNone(h['BFJMOL'])
        wjmol  = checkNone(h['WJMOL'])
        miss   = int(h['MISS'])

        result.append([ID,stem,modelno,chain,wings,Type,desc,Len,links,
                       breaks,sjmol,tjmol,sfjmol,bfjmol,wjmol,miss,TLen])
        
    return result

def bulges(model):

    result  = []

    for b in model.loops['BULGE']:

        ID     = b['ID']
        stem   = b['STEM']
        chain1 = model.chains[b['CHAIN1']]['ID']
        chain2 = model.chains[b['CHAIN2']]['ID']
        wings  = b['WINGS']
        side   = b['SIDE']
        desc   = b['TYPE']
        Type   = b['PTYPE']
        Len    = b['LEN']
        TLen   = b['TLEN']
        links  = b['LINKS']
        breaks = b['BREAKS']
        sjmol  = checkNone(b['SJMOL'])
        tjmol  = checkNone(b['TJMOL'])
        sfjmol = checkNone(b['SFJMOL'])
        bfjmol = checkNone(b['BFJMOL'])
        wjmol  = checkNone(b['WJMOL'])
        miss   = int(b['MISS'])

        result.append([ID,stem,modelno,chain1,chain2,wings,
                       side,desc,Type,Len,links,breaks,
                       sjmol,tjmol,sfjmol,bfjmol,wjmol,miss,TLen])
    return result

def internals(model):

    result  = []

    for i in model.loops['INTERNAL']:

        ID     = i['ID']
        stem   = i['STEM']
        chain1 = model.chains[i['CHAIN1']]['ID']
        chain2 = model.chains[i['CHAIN2']]['ID']
        wings  = i['WINGS']
        desc   = i['TYPE']
        Type   = i['PTYPE']
        Len    = i['LEN']
        TLen   = i['TLEN']
        sym    = int(i['SYM'])
        links  = i['LINKS']
        breaks = i['BREAKS']
        sjmol  = checkNone(i['SJMOL'])
        tjmol  = checkNone(i['TJMOL'])
        sfjmol = checkNone(i['SFJMOL'])
        bfjmol = checkNone(i['BFJMOL'])
        wjmol  = checkNone(i['WJMOL'])
        miss   = int(i['MISS'])

        result.append([ID,stem,modelno,chain1,chain2,wings,
                       desc,Type,Len,sym,links,breaks,
                       sjmol,tjmol,sfjmol,bfjmol,wjmol,miss,TLen])
    return result

def junctions(model):

    result  = []

    for j in model.loops['JUNCTION']:

        ID      = j['ID']
        stem    = j['STEM']
        chain1  = model.chains[j['CHAIN1']]['ID']
        chain2  = model.chains[j['CHAIN2']]['ID']
        threads = j['THREADSNUM']
        sides   = j['SIDES']
        wings   = j['WINGS']
        sfaces  = j['SFACES']
        bfaces  = j['BFACES']
        desc    = j['TYPE']
        Type    = j['PTYPE']
        Len     = j['LEN']
        TLen    = j['TLEN']
        links   = j['LINKS']
        breaks  = j['BREAKS']
        sjmol   = checkNone(j['SJMOL'])
        tjmol   = checkNone(j['TJMOL'])
        sfjmol  = checkNone(j['SFJMOL'])
        bfjmol  = checkNone(j['BFJMOL'])
        wjmol   = checkNone(j['WJMOL'])
        miss   = int(j['MISS'])
        
        result.append([ID,stem,modelno,chain1,chain2,threads,sides,
                       wings,sfaces,bfaces,desc,Type,Len,links,
                       breaks,sjmol,tjmol,sfjmol,bfjmol,wjmol,miss,TLen])
    return result

def threadloop(model):

    result  = []

    for t in model.loops:
        for l in model.loops[t]:
            for tl in l['TLOOP']:

                loopid    = tl['LOOPID']
                looptype  = tl['LOOPTYPE']
                thread    = tl['THREAD']
                num       = tl['NUM']
                side      = tl['SIDE']
                links     = tl['LINKS']
                seq       = tl['SEQ']
                Len       = tl['LEN']
                loopclass = l['PTYPE']


                result.append([modelno,loopid,looptype,thread,num,side,links,seq,Len,loopclass])

    return result

def wingloop(model):

    result  = []

    for t in model.loops:
        for l in model.loops[t]:
            for wl in l['WLOOP']:

                loopid   = wl['LOOPID']
                looptype = wl['LOOPTYPE']
                wing     = wl['WING']
                num      = wl['NUM']
                side     = wl['SIDE']
                seq      = wl['SEQ']
                Len      = wl['LEN']

                result.append([modelno,loopid,looptype,wing,num,side,seq,Len])

    return result

def faceloop(model):

    result  = []

    for t in model.loops:
        for l in model.loops[t]:
            for fl in l['FLOOP']:

                loopid   = fl['LOOPID']
                looptype = fl['LOOPTYPE']
                stem1    = fl['STEM1']
                stem2    = fl['STEM2']
                Type     = fl['TYPE']
                num      = fl['NUM']

                result.append([modelno,loopid,looptype,stem1,stem2,Type,num])

    return result

def ChainsConcat(model):

    result  = []

    for cc in model.chain_concat:

        chain1 = model.chains[cc.split('-')[0]]['ID']
        chain2 = model.chains[cc.split('-')[1]]['ID']

        result.append([modelno,chain1,chain2])

    return result
