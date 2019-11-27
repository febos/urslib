modelno = 1

def RevStems(model):

    result  = []

    for rs in model.revstems:

        ID      = rs['ID']
        chain1  = model.chains[rs['CHAIN1']]['ID']
        chain2  = model.chains[rs['CHAIN2']]['ID']
        Len     = rs['LEN']
        lseq    = rs['LSEQ']
        rseq    = rs['RSEQ']
        pairseq = rs['PAIRSEQ']

        result.append([ID,modelno,chain1,chain2,Len,lseq,rseq,pairseq])
        
    return result

def NuclMults(model):

    result = []

    for nm in model.nuclmults:

        ID   = nm['ID']
        nts  = len(nm['NTS'])
        bps  = len(nm['BPS'])
        wcwb = nm['WCWB']
        Type = nm['TYPE']

        result.append([ID,modelno,nts,bps,wcwb,Type])

    return result


def StemMults(model):

    result = []

    for sm in model.stemmults:

        ID     = sm['ID']
        fstems = len(sm['FSTEMS'])
        nts    = len(sm['NTS'])
        links  = len(sm['LINKS'])
        nedges = sm['NEDGES']
        ledges = sm['LEDGES']
        edges  = sm['EDGES']
        npairs = len(sm['NPAIRS'])
        lpairs = len(sm['LPAIRS'])
        Type   = sm['TYPE']

        result.append([ID,modelno,fstems,nts,links,nedges,
                       ledges,edges,npairs,lpairs,Type])
    return result

def StemNPairs(model):

    result = []

    for sp in model.stempairs['N']:

        ID     = sp['ID']
        fstem1 = sp['FSTEM1']
        fstem2 = sp['FSTEM2']
        nucl   = sp['NUCL']
        mult   = sp['MULT']

        result.append([ID,modelno,fstem1,fstem2,nucl,mult])

    return result

def StemLPairs(model):

    result = []

    for sp in model.stempairs['L']:

        ID     = sp['ID']
        link   = sp['LINK']
        fstem1 = sp['FSTEM1']
        ostem1 = sp['OSTEM1']
        stem1  = sp['STEM1']
        fstem2 = sp['FSTEM2']
        ostem2 = sp['OSTEM2']
        stem2  = sp['STEM2']
        mult   = sp['MULT']
        nucl1  = sp['NUCL1']
        nucl2  = sp['NUCL2']

        result.append([ID,modelno,link,fstem1,ostem1,stem1,
                       fstem2,ostem2,stem2,mult,nucl1,nucl2])
    return result

def diagrams(model):

    result = []

    for d in model.diagrams:

        ID         = d['ID']
        seq        = d['SEQ']
        brackets   = d['BRACKETS']
        slbrackets = d['SLBRACKETS']
        sldibrank  = d['SLDIBRANK']
        sllptrank  = d['SLLPTRANK']
        scheme     = ','.join([str(i) for i in d['SCHEME']])
        stembrack  = d['STEMBRACK']
        dibrank    = d['DIBRANK']
        lptrank    = d['LPTRANK']
        depth      = d['DEPTH']
        nuclseq    = ','.join(d['NUCLSEQ'])
        seqbrack   = d['SEQBRACK']

        result.append([ID,modelno,seq,brackets,slbrackets,sldibrank,
                       sllptrank,scheme,stembrack,dibrank,lptrank,
                       depth,nuclseq,seqbrack])
    return result

def ecfs(model):

    result = []

    for d in model.diagrams:
        for e in d['ECFS']:

            ID         = e['ID']
            diagram    = e['DIAGRAM']
            fullscheme = ','.join([str(i) for i in e['FULLSCHEME']])
            scheme     = ','.join([str(i) for i in e['SCHEME']])
            signat     = e['SIGNATURE']
            brackets   = e['BRACKETS']
            dibrank    = e['DIBRANK']
            lptrank    = e['LPTRANK']
            depth      = e['DEPTH']
            parent     = e['PARENT']
            wingseq    = e['WINGSEQ']
            jmol       = e['JMOL']
            chainseq   = e['CHAINSEQ']

            result.append([ID,modelno,diagram,fullscheme,scheme,signat,
                           brackets,dibrank,lptrank,depth,parent,
                           wingseq,jmol,chainseq])
    return result

def atompairs(model):

    result = []

    for a in model.atompairs:

        ID       = a['ID']
        rchain   = a['RCHAIN']
        pchain   = a['PCHAIN']
        nucl     = a['NUCL']
        amino    = a['AMINO']
        rdssr    = a['RDSSR']
        pdssr    = a['PDSSR']
        ratomid  = a['RATOMID']
        patomid  = a['PATOMID']
        rname    = a['RNAME']
        pname    = a['PNAME']
        relem    = a['RELEM']
        pelem    = a['PELEM']
        rjmol    = a['RJMOL']
        pjmol    = a['PJMOL']
        power    = a['POWER']
        dist     = a['DIST']
        rcos     = a['RCOS']
        pcos     = a['PCOS']
        monopair = a['MONOPAIR']

        result.append([ID,modelno,rchain,pchain,nucl,amino,rdssr,pdssr,
                       ratomid,patomid,rname,pname,relem,pelem,rjmol,
                       pjmol,power,dist,rcos,pcos,monopair])
    return result

def monopairs(model):

    result = []

    for m in model.monopairs:

        ID        = m['ID']
        rchain    = m['RCHAIN']
        pchain    = m['PCHAIN']
        nucl      = m['NUCL']
        amino     = m['AMINO']
        rdssr     = m['RDSSR']
        pdssr     = m['PDSSR']
        rjmol     = m['RJMOL']
        pjmol     = m['PJMOL']
        atompairs = m['ATOMPAIRS']

        result.append([ID,modelno,rchain,pchain,nucl,amino,
                       rdssr,pdssr,rjmol,pjmol,atompairs])
    return result



