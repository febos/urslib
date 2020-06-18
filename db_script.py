

def files(output):

    output.write('name'     + ' char(4)' + ' unique primary key,')
    output.write(' models'  + ' int,')
    output.write(' type'    + ' varchar(3),')
    output.write(' head'    + ' text,')
    output.write(' date'    + ' date,')
    output.write(' title'   + ' text,')
    output.write(' keywds'  + ' text,')
    output.write(' mdltyp'  + ' text,')
    output.write(' author'  + ' text,')
    output.write(' expdata' + ' text,')
    output.write(' resol'   + ' float(8,3),')
    output.write(' words'   + ' text')

def models(output):

    output.write('id'          + ' int' + ' unique primary key,')
    output.write(' number'     + ' int,')
    output.write(' file'       + ' char(4),')
    output.write(' main'       + ' int,')
    output.write(' rnachains'  + ' int,')
    output.write(' maxrnalen'  + ' int,')
    output.write(' rnalen'     + ' int,')
    output.write(' dnachains'  + ' int,')
    output.write(' maxdnalen'  + ' int,')
    output.write(' dnalen'     + ' int,')
    output.write(' protchains' + ' int,')
    output.write(' maxprotlen' + ' int,')
    output.write(' protlen'    + ' int,')
    output.write(' ligchains'  + ' int,')
    output.write(' maxliglen'  + ' int,')
    output.write(' liglen'     + ' int,')
    output.write(' atoms'      + ' int,')
    output.write(' nucls'      + ' int,')
    output.write(' aminos'     + ' int,')
    output.write(' ligands'    + ' int,')
    output.write(' liglist'    + ' text,')
    output.write(' metlist'    + ' text,')
    output.write(' nrpdb'      + ' int,')
    output.write(' index(file),')
    output.write(' index(nrpdb),')
    output.write(' index(liglist(15)),')
    output.write(' index(metlist(15))')

def molecules(output):

    output.write('id'       + ' int' + ' unique primary key,')
    output.write(' file'    + ' char(4),')
    output.write(' mol_id'  + ' int,')
    output.write(' mol'     + ' text,')
    output.write(' orgsc'   + ' text,')
    output.write(' frag'    + ' text,')
    output.write(' syn'     + ' text,')
    output.write(' ec'      + ' text,')
    output.write(' eng'     + ' text,')
    output.write(' mut'     + ' text,')
    output.write(' details' + ' text,')
    output.write(' orgcat'  + ' text,')
    output.write(' index(file),')
    output.write(' index(id)')

def chains(output):

    output.write('id'           + ' int' + ' unique primary key,')
    output.write(' model'       + ' int,')
    output.write(' mol'         + ' int,')
    output.write(' letter'      + ' varchar(5),')
    output.write(' len'         + ' int,')
    output.write(' liglen'      + ' int,')
    output.write(' type'        + ' varchar(7),')
    output.write(' seq'         + ' text,')
    output.write(' ligseq'      + ' text,')
    output.write(' lubrackets'  + ' text,')
    output.write(' brackets'    + ' text,')
    output.write(' slbrackets'  + ' text,')
    output.write(' start'       + ' varchar(20),')
    output.write(' end'         + ' varchar(20),')
    output.write(' bound'       + ' int,')
    output.write(' share'       + ' float(8,3),')
    output.write(' ligbound'    + ' int,')
    output.write(' ligshare'    + ' float(8,3),')
    output.write(' fake'        + ' int,')
    output.write(' diagram'     + ' int,')
    output.write(' seqbrack'    + ' text,')
    output.write(' sharewcwb'   + ' float(8,3),')
    output.write(' index(model),')
    output.write(' index(type,len)')

def nucls(output):

    output.write('id'           + ' int' + ' unique primary key,')
    output.write(' dssr'        + ' varchar(20),')
    output.write(' model'       + ' int,')
    output.write(' chain'       + ' int,')
    output.write(' letter'      + ' varchar(5),')
    output.write(' thread'      + ' int,')
    output.write(' wing'        + ' int,')
    output.write(' oldwing'     + ' int,')
    output.write(' fstems'      + ' int,')
    output.write(' place'       + ' int,')
    output.write(' num'         + ' int,')
    output.write(' zip'         + ' int,')
    output.write(' mult'        + ' int,')
    output.write(' lumult'      + ' int,')
    output.write(' bps'         + ' int,')
    output.write(' miss'        + ' int,')
    output.write(' chnumindiag' + ' int,')
    output.write(' diagram'     + ' int,')
    output.write(' res'         + ' varchar(3),')
    output.write(' bracket'     + ' char(1),')
    output.write(' slbracket'   + ' char(1),')
    output.write(' cifid'       + ' int,')
    output.write(' index(res),')
    output.write(' index(model),')
    output.write(' index(model,res),')
    output.write(' index(model,chain,res),')
    output.write(' index(chain,res)')
                
def aminos(output):

    output.write('id'      + ' int' + ' unique primary key,')
    output.write(' dssr'   + ' varchar(20),')
    output.write(' model'  + ' int,')
    output.write(' chain'  + ' int,')
    output.write(' letter' + ' varchar(5),')
    output.write(' place'  + ' int,')
    output.write(' num'    + ' int,')
    output.write(' miss'   + ' int,')
    output.write(' res'    + ' varchar(3),')
    output.write(' cifid'  + ' int,')
    output.write(' index(res),')
    output.write(' index(model),')
    output.write(' index(model,res),')
    output.write(' index(model,chain,res),')
    output.write(' index(chain,res)')

def ligands(output):

    output.write('id'      + ' int' + ' unique primary key,')
    output.write(' dssr'   + ' varchar(20),')
    output.write(' model'  + ' int,')
    output.write(' chain'  + ' int,')
    output.write(' letter' + ' varchar(5),')
    output.write(' place'  + ' int,')
    output.write(' num'    + ' int,')
    output.write(' miss'   + ' int,')
    output.write(' cifid'  + ' int,')
    output.write(' index(model)')

def atoms(output):

    output.write('id'        + ' int' + ' unique primary key,')
    output.write(' model'    + ' int,')
    output.write(' chain'    + ' int,')
    output.write(' res'      + ' varchar(20),')
    output.write(' restype'  + ' char(1),')
    output.write(' name'     + ' varchar(5),')
    output.write(' num'      + ' int,')
    output.write(' elem'     + ' varchar(3),')
    output.write(' occup'    + ' float(8,3),')
    output.write(' altloc'   + ' char(1),')
    output.write(' x'        + ' float(8,3),')
    output.write(' y'        + ' float(8,3),')
    output.write(' z'        + ' float(8,3),')
    output.write(' rescifid' + ' int,')
    output.write(' index(model),')
    output.write(' index(model,restype,elem),')
    output.write(' index(model,x,y,z),')
    output.write(' index(restype,elem)')

def BasePairs(output):

    output.write('id'         + ' int' + ' unique primary key,')
    output.write(' model'     + ' int,')
    output.write(' num'       + ' int,')
    output.write(' chain1'    + ' int,')
    output.write(' chain2'    + ' int,')
    output.write(' nucl1'     + ' varchar(20),')
    output.write(' bond'      + ' char(3),')
    output.write(' nucl2'     + ' varchar(20),')
    output.write(' type'      + ' char(2),')
    output.write(' class1'    + ' varchar(10),')
    output.write(' class2'    + ' varchar(10),')
    output.write(' class3'    + ' varchar(10),')
    output.write(' stem'      + ' int,')
    output.write(' oldstem'   + ' int,')
    output.write(' fullstem'  + ' int,')
    output.write(' revstem'   + ' int,')
    output.write(' lustem'    + ' int,')
    output.write(' link'      + ' int,')
    output.write(' helix'     + ' int,')
    output.write(' nuclmult'  + ' int,')
    output.write(' info1'     + ' text,')
    output.write(' info2'     + ' text,')
    output.write(' dist1'     + ' float(8,3),')
    output.write(' dist2'     + ' float(8,3),')
    output.write(' dist3'     + ' float(8,3),')
    output.write(' tor'       + ' float(8,3),')
    output.write(' hbonds'    + ' text,')
    output.write(' hbnum'     + ' int,')
    output.write(' shear'     + ' float(8,3),')
    output.write(' stretch'   + ' float(8,3),')
    output.write(' stagger'   + ' float(8,3),')
    output.write(' buckle'    + ' float(8,3),')
    output.write(' propeller' + ' float(8,3),')
    output.write(' opening'   + ' float(8,3),')
    output.write(' shift'     + ' float(8,3),')
    output.write(' slide'     + ' float(8,3),')
    output.write(' rise'      + ' float(8,3),')
    output.write(' tilt'      + ' float(8,3),')
    output.write(' roll'      + ' float(8,3),')
    output.write(' twist'     + ' float(8,3),')
    output.write(' index(model)')

def towers(output):

    output.write('id'      + ' int' + ' unique primary key,')
    output.write(' model'  + ' int,')
    output.write(' stems'  + ' int,')
    output.write(' chain1' + ' int,')
    output.write(' chain2' + ' int,')
    output.write(' pseudo' + ' int,')
    output.write(' type'   + ' int,')
    output.write(' index(model)')

def links(output):

    output.write('id'       + ' int' + ' unique primary key,')
    output.write(' model'   + ' int,')
    output.write(' chain1'  + ' int,')
    output.write(' chain2'  + ' int,')
    output.write(' bp'      + ' int,')
    output.write(' bptype'  + ' char(2),')
    output.write(' lthread' + ' int,')
    output.write(' lwing'   + ' int,')
    output.write(' rthread' + ' int,')
    output.write(' rwing'   + ' int,')
    output.write(' type'    + ' int,')
    output.write(' depth'   + ' int,')
    output.write(' nucl1'   + ' varchar(20),')
    output.write(' nucl2'   + ' varchar(20),')
    output.write(' class1'  + ' varchar(10),')
    output.write(' class2'  + ' varchar(10),')
    output.write(' class3'  + ' varchar(10),')
    output.write(' dist'    + ' int,')
    output.write(' ss1'     + ' varchar(10),')
    output.write(' ss2'     + ' varchar(10),')
    output.write(' rel'     + ' char(2),')
    output.write(' index(model)')

def stems(output):

    output.write('id'         + ' int' + ' unique primary key,')
    output.write(' model'     + ' int,')
    output.write(' num'       + ' int,')
    output.write(' chain1'    + ' int,')
    output.write(' chain2'    + ' int,')
    output.write(' lseq'      + ' text,')
    output.write(' rseq'      + ' text,')
    output.write(' len'       + ' int,')
    output.write(' leftw'     + ' int,')
    output.write(' rightw'    + ' int,')
    output.write(' pairseq'   + ' text,')
    output.write(' tower'     + ' int,')
    output.write(' loopclass' + ' char(1),')
    output.write(' looptype'  + ' char(1),')
    output.write(' oldstem'   + ' int,')
    output.write(' fullstem'  + ' int,')
    output.write(' mult'      + ' int,')
    output.write(' diagram'   + ' int,')
    output.write(' numindiag' + ' int,')
    output.write(' ecf'       + ' int,')
    output.write(' numinecf'  + ' int,')
    output.write(' jmol'      + ' text,')
    output.write(' loopjmol'  + ' text,')
    output.write(' index(model)')

def StemsOld(output):

    output.write('id'        + ' int' + ' unique primary key,')
    output.write(' model'    + ' int,')
    output.write(' num'      + ' int,')
    output.write(' chain1'   + ' int,')
    output.write(' chain2'   + ' int,')
    output.write(' lseq'     + ' text,')
    output.write(' rseq'     + ' text,')
    output.write(' leftw'    + ' int,')
    output.write(' rightw'   + ' int,')
    output.write(' pairseq'  + ' text,')
    output.write(' fullstem' + ' int,')
    output.write(' stems'    + ' int,')
    output.write(' len'      + ' int,')
    output.write(' mult'     + ' int,')
    output.write(' jmol'     + ' text,')
    output.write(' index(model)')

def StemsFull(output):

    output.write('id'        + ' int' + ' unique primary key,')
    output.write(' model'    + ' int,')
    output.write(' num'      + ' int,')
    output.write(' chain1'   + ' int,')
    output.write(' chain2'   + ' int,')
    output.write(' lseq'     + ' text,')
    output.write(' rseq'     + ' text,')
    output.write(' len'      + ' int,')
    output.write(' leftw'    + ' int,')
    output.write(' rightw'   + ' int,')
    output.write(' stems'    + ' int,')
    output.write(' oldstems' + ' int,')
    output.write(' pairseq'  + ' text,')
    output.write(' mult'     + ' int,')
    output.write(' jmol'     + ' text,')
    output.write(' index(model)')

def wings(output):

    output.write('id'        + ' int' + ' unique primary key,')
    output.write(' model'    + ' int,')
    output.write(' chain'    + ' int,')
    output.write(' stem'     + ' int,')
    output.write(' another'  + ' int,')
    output.write(' prev'     + ' int,')
    output.write(' next'     + ' int,')
    output.write(' prevw'    + ' int,')
    output.write(' nextw'    + ' int,')
    output.write(' type'     + ' char(1),')
    output.write(' start'    + ' varchar(20),')
    output.write(' end'      + ' varchar(20),')
    output.write(' len'      + ' int,')
    output.write(' seq'      + ' text,')
    output.write(' ecf'      + ' int,')
    output.write(' numinecf' + ' int,')
    output.write(' jmol'     + ' text,')
    output.write(' index(stem),')
    output.write(' index(prev),')
    output.write(' index(next),')
    output.write(' index(model)')

def WingsOld(output):

    output.write('id'       + ' int' + ' unique primary key,')
    output.write(' model'   + ' int,')
    output.write(' chain'   + ' int,')
    output.write(' stem'    + ' int,')
    output.write(' another' + ' int,')
    output.write(' prevw'   + ' int,')
    output.write(' nextw'   + ' int,')
    output.write(' type'    + ' char(1),')
    output.write(' start'   + ' varchar(20),')
    output.write(' end'     + ' varchar(20),')
    output.write(' len'     + ' int,')
    output.write(' seq'     + ' text,')
    output.write(' index(model)')

def WingsFull(output):

    output.write('id'       + ' int' + ' unique primary key,')
    output.write(' model'   + ' int,')
    output.write(' chain'   + ' int,')
    output.write(' stem'    + ' int,')
    output.write(' another' + ' int,')
    output.write(' prevw'   + ' int,')
    output.write(' nextw'   + ' int,')
    output.write(' type'    + ' char(1),')
    output.write(' start'   + ' varchar(20),')
    output.write(' end'     + ' varchar(20),')
    output.write(' len'     + ' int,')
    output.write(' seq'     + ' text,')
    output.write(' index(model)')

def threads(output):

    output.write('id'     + ' int' + ' unique primary key,')
    output.write(' model' + ' int,')
    output.write(' chain' + ' int,')
    output.write(' prev'  + ' int,')
    output.write(' next'  + ' int,')
    output.write(' start' + ' varchar(20),')
    output.write(' end'   + ' varchar(20),')
    output.write(' len'   + ' int,')
    output.write(' links' + ' int,')
    output.write(' seq'   + ' text,')
    output.write(' place' + ' int,')
    output.write(' full'  + ' int,')
    output.write(' ext'   + ' int,')
    output.write(' jmol'  + ' text,')
    output.write(' index(model)')

def hairpins(output):

    output.write('id'      + ' int' + ' unique primary key,')
    output.write(' stemid' + ' int,')
    output.write(' model'  + ' int,')
    output.write(' chain'  + ' int,')
    output.write(' wings'  + ' int,')
    output.write(' type'   + ' char(1),')
    output.write(' form'   + ' text,')
    output.write(' len'    + ' int,')
    output.write(' links'  + ' int,')
    output.write(' breaks' + ' int,')
    output.write(' sjmol'  + ' text,')
    output.write(' tjmol'  + ' text,')
    output.write(' sfjmol' + ' text,')
    output.write(' bfjmol' + ' text,')
    output.write(' wjmol'  + ' text,')
    output.write(' miss'   + ' int,')
    output.write(' tlen'   + ' int,')
    output.write(' index(model)')

def bulges(output):

    output.write('id'      + ' int' + ' unique primary key,')
    output.write(' stemid' + ' int,')
    output.write(' model'  + ' int,')
    output.write(' chain1' + ' int,')
    output.write(' chain2' + ' int,')
    output.write(' wings'  + ' int,')
    output.write(' side'   + ' char(1),')
    output.write(' form'   + ' text,')
    output.write(' type'   + ' char(1),')
    output.write(' len'    + ' int,')
    output.write(' links'  + ' int,')
    output.write(' breaks' + ' int,')
    output.write(' sjmol'  + ' text,')
    output.write(' tjmol'  + ' text,')
    output.write(' sfjmol' + ' text,')
    output.write(' bfjmol' + ' text,')
    output.write(' wjmol'  + ' text,')
    output.write(' miss'   + ' int,')
    output.write(' tlen'   + ' int,')
    output.write(' index(model)')

def internals(output):

    output.write('id'      + ' int' + ' unique primary key,')
    output.write(' stemid' + ' int,')
    output.write(' model'  + ' int,')
    output.write(' chain1' + ' int,')
    output.write(' chain2' + ' int,')
    output.write(' wings'  + ' int,')
    output.write(' form'   + ' text,')
    output.write(' type'   + ' char(1),')
    output.write(' len'    + ' int,')
    output.write(' sym'    + ' int,')
    output.write(' links'  + ' int,')
    output.write(' breaks' + ' int,')
    output.write(' sjmol'  + ' text,')
    output.write(' tjmol'  + ' text,')
    output.write(' sfjmol' + ' text,')
    output.write(' bfjmol' + ' text,')
    output.write(' wjmol'  + ' text,')
    output.write(' miss'   + ' int,')
    output.write(' tlen'   + ' int,')
    output.write(' index(model)')

def junctions(output):

    output.write('id'       + ' int' + ' unique primary key,')
    output.write(' stemid'  + ' int,')
    output.write(' model'   + ' int,')
    output.write(' chain1'  + ' int,')
    output.write(' chain2'  + ' int,')
    output.write(' threads' + ' int,')
    output.write(' sides'   + ' int,')
    output.write(' wings'   + ' int,')
    output.write(' sfaces'  + ' int,')
    output.write(' bfaces'  + ' int,')
    output.write(' form'    + ' text,')
    output.write(' type'    + ' char(1),')
    output.write(' len'     + ' int,')
    output.write(' links'   + ' int,')
    output.write(' breaks'  + ' int,')
    output.write(' sjmol'   + ' text,')
    output.write(' tjmol'   + ' text,')
    output.write(' sfjmol'  + ' text,')
    output.write(' bfjmol'  + ' text,')
    output.write(' wjmol'   + ' text,')
    output.write(' miss'    + ' int,')
    output.write(' tlen'    + ' int,')
    output.write(' index(model)')

def threadloop(output):

    output.write('model'      + ' int,')
    output.write(' loopid'    + ' int,')
    output.write(' looptype'  + ' char(1),')
    output.write(' thread'    + ' int,')
    output.write(' num'       + ' int,')
    output.write(' side'      + ' int,')
    output.write(' links'     + ' int,')
    output.write(' seq'       + ' text,')
    output.write(' len'       + ' int,')
    output.write(' loopclass' + ' char(1),')
    output.write(' index(thread),')
    output.write(' index(loopid),')
    output.write(' index(model)')

def wingloop(output):

    output.write('model'     + ' int,')
    output.write(' loopid'   + ' int,')
    output.write(' looptype' + ' char(1),')
    output.write(' wing'     + ' int,')
    output.write(' num'      + ' int,')
    output.write(' side'     + ' int,')
    output.write(' seq'      + ' text,')
    output.write(' len'      + ' int,')
    output.write(' index(model)')

def faceloop(output):

    output.write('model'     + ' int,')
    output.write(' loopid'   + ' int,')
    output.write(' looptype' + ' char(1),')
    output.write(' stem1'    + ' int,')
    output.write(' stem2'    + ' int,')
    output.write(' type'     + ' char(1),')
    output.write(' num'      + ' int,')
    output.write(' index(model)')

def ChainsConcat(output):

    output.write('model'   + ' int,')
    output.write(' chain1' + ' int,')
    output.write(' chain2' + ' int,')
    output.write(' index(model)')

def LuHelices(output):

    output.write('id'     + ' int' + ' unique primary key,')
    output.write(' model' + ' int,')
    output.write(' len'   + ' int,')
    output.write(' seq1'  + ' text,')
    output.write(' seq2'  + ' text,')
    output.write(' form'  + ' text,')
    output.write(' stems' + ' int,')
    output.write(' lones' + ' int,')
    output.write(' index(model)')

def LuStems(output):

    output.write('id'      + ' int' + ' unique primary key,')
    output.write(' model'  + ' int,')
    output.write(' dssr'   + ' int,')
    output.write(' chain1' + ' int,')
    output.write(' chain2' + ' int,')
    output.write(' len'    + ' int,')
    output.write(' lseq'   + ' text,')
    output.write(' rseq'   + ' text,')
    output.write(' form'   + ' text,')
    output.write(' index(model)')

def LuStemHelix(output):

    output.write('model'  + ' int,')
    output.write(' stem'  + ' int,')
    output.write(' helix' + ' int,')
    output.write(' index(model)')

def LuMultiplets(output):

    output.write('id'     + ' int' + ' unique primary key,')
    output.write(' model' + ' int,')
    output.write(' len'   + ' int,')
    output.write(' seq'   + ' text,')
    output.write(' index(model)')

def LuNphbs(output):

    output.write('id'      + ' int' + ' unique primary key,')
    output.write(' model'  + ' int,')
    output.write(' nucl1'  + ' varchar(20),')
    output.write(' nucl2'  + ' varchar(20),')
    output.write(' hbnum'  + ' int,')
    output.write(' hbonds' + ' text,')
    output.write(' stack'  + ' text,')
    output.write(' index(model)')

def LuNonLoops(output):

    output.write('id'     + ' int' + ' unique primary key,')
    output.write(' model' + ' int,')
    output.write(' chain' + ' int,')
    output.write(' len'   + ' int,')
    output.write(' seq'   + ' text,')
    output.write(' break' + ' int,')
    output.write(' start' + ' varchar(20),')
    output.write(' end'   + ' varchar(20),')
    output.write(' index(model)')

def LuKissing(output):

    output.write('id'     + ' int' + ' unique primary key,')
    output.write(' model' + ' int,')
    output.write(' loop1' + ' int,')
    output.write(' loop2' + ' int,')
    output.write(' kiss'  + ' int,')
    output.write(' index(model)')

def LuAminors(output):

    output.write('id'       + ' int' + ' unique primary key,')
    output.write(' model'   + ' int,')
    output.write(' nucl'    + ' varchar(20),')
    output.write(' pair'    + ' int,')
    output.write(' bpdesc'  + ' varchar(40),')
    output.write(' hbonds1' + ' int,')
    output.write(' hbonds2' + ' int,')
    output.write(' type'    + ' varchar(5),')
    output.write(' class'   + ' varchar(5),')
    output.write(' index(model)')

def LuUturns(output):

    output.write('id'      + ' int' + ' unique primary key,')
    output.write(' model'  + ' int,')
    output.write(' chain'  + ' int,')
    output.write(' nucl1'  + ' varchar(20),')
    output.write(' nucl2'  + ' varchar(20),')
    output.write(' hbonds' + ' int,')
    output.write(' index(model)')

def LuZippers(output):

    output.write('id'     + ' int' + ' unique primary key,')
    output.write(' model' + ' int,')
    output.write(' len'   + ' int,')
    output.write(' seq'   + ' text,')
    output.write(' index(model)')

def LuKturns(output):

    output.write('id'     + ' int' + ' unique primary key,')
    output.write(' model' + ' int,')
    output.write(' bp'    + ' int,')
    output.write(' helix' + ' int,')
    output.write(' stem1' + ' int,')
    output.write(' stem2' + ' int,')
    output.write(' iloop' + ' int,')
    output.write(' type'  + ' int,')
    output.write(' index(model)')

def LuHairpins(output):

    output.write('id'     + ' int' + ' unique primary key,')
    output.write(' model' + ' int,')
    output.write(' chain' + ' int,')
    output.write(' len'   + ' int,')
    output.write(' seq'   + ' text,')
    output.write(' stem'  + ' int,')
    output.write(' index(model)')

def LuBulges(output):

    output.write('id'     + ' int' + ' unique primary key,')
    output.write(' model' + ' int,')
    output.write(' chain' + ' int,')
    output.write(' prev'  + ' int,')
    output.write(' next'  + ' int,')
    output.write(' form'  + ' text,')
    output.write(' seq'   + ' text,')
    output.write(' len'   + ' int,')
    output.write(' index(model)')

def LuInternals(output):

    output.write('id'      + ' int' + ' unique primary key,')
    output.write(' model'  + ' int,')
    output.write(' chain1' + ' int,')
    output.write(' chain2' + ' int,')
    output.write(' prev'   + ' int,')
    output.write(' next'   + ' int,')
    output.write(' form'   + ' text,')
    output.write(' sym'    + ' int,')
    output.write(' lseq'   + ' text,')
    output.write(' rseq'   + ' text,')
    output.write(' len'    + ' int,')
    output.write(' index(model)')

def LuJunctions(output):

    output.write('id'       + ' int' + ' unique primary key,')
    output.write(' model'   + ' int,')
    output.write(' threads' + ' int,')
    output.write(' form'    + ' text,')
    output.write(' len'     + ' int,')
    output.write(' index(model)')

def LuJuncThreads(output):

    output.write('junc'   + ' int,')
    output.write(' model' + ' int,')
    output.write(' chain' + ' int,')
    output.write(' num'   + ' int,')
    output.write(' start' + ' varchar(20),')
    output.write(' end'   + ' varchar(20),')
    output.write(' len'   + ' int,')
    output.write(' seq'   + ' text,')
    output.write(' prev'  + ' int,')
    output.write(' index(model)')

def RevStems(output):

    output.write('id'       + ' int' + ' unique primary key,')
    output.write(' model'   + ' int,')
    output.write(' chain1'  + ' int,')
    output.write(' chain2'  + ' int,')
    output.write(' len'     + ' int,')
    output.write(' lseq'    + ' text,')
    output.write(' rseq'    + ' text,')
    output.write(' pairseq' + ' text,')
    output.write(' index(model)')

def NuclMults(output):

    output.write('id'     + ' int' + ' unique primary key,')
    output.write(' model' + ' int,')
    output.write(' nts'   + ' int,')
    output.write(' bps'   + ' int,')
    output.write(' wcwb'  + ' int,')
    output.write(' type'  + ' text,')
    output.write(' index(model)')

def StemMults(output):

    output.write('id'      + ' int' + ' unique primary key,')
    output.write(' model'  + ' int,')
    output.write(' fstems' + ' int,')
    output.write(' nts'    + ' int,')
    output.write(' links'  + ' int,')
    output.write(' nedges' + ' int,')
    output.write(' ledges' + ' int,')
    output.write(' edges'  + ' int,')
    output.write(' npairs' + ' int,')
    output.write(' lpairs' + ' int,')
    output.write(' type'   + ' text,')
    output.write(' index(model)')

def StemNPairs(output):

    output.write('id'      + ' int' + ' unique primary key,')
    output.write(' model'  + ' int,')
    output.write(' fstem1' + ' int,')
    output.write(' fstem2' + ' int,')
    output.write(' nucl'   + ' varchar(20),')
    output.write(' mult'   + ' int,')
    output.write(' index(model)')

def StemLPairs(output):

    output.write('id'      + ' int' + ' unique primary key,')
    output.write(' model'  + ' int,')
    output.write(' link'   + ' int,')
    output.write(' fstem1' + ' int,')
    output.write(' ostem1' + ' int,')
    output.write(' stem1'  + ' int,')
    output.write(' fstem2' + ' int,')
    output.write(' ostem2' + ' int,')
    output.write(' stem2'  + ' int,')
    output.write(' mult'   + ' int,')
    output.write(' nucl1'  + ' varchar(20),')
    output.write(' nucl2'  + ' varchar(20),')
    output.write(' index(model)')

def diagrams(output):

    output.write('id'          + ' int' + ' unique primary key,')
    output.write(' model'      + ' int,')
    output.write(' seq'        + ' varchar(50),')
    output.write(' brackets'   + ' text,')
    output.write(' slbrackets' + ' text,')
    output.write(' sldibrank'  + ' int,')
    output.write(' sllptrank'  + ' int,')
    output.write(' scheme'     + ' text,')
    output.write(' stembrack'  + ' text,')
    output.write(' dibrank'    + ' int,')
    output.write(' lptrank'    + ' int,')
    output.write(' depth'      + ' int,')
    output.write(' nuclseq'    + ' text,')
    output.write(' seqbrack'   + ' text,')
    output.write(' index(model)')

def ecfs(output):

    output.write('id'          + ' int' + ' unique primary key,')
    output.write(' model'      + ' int,')
    output.write(' diagram'    + ' int,')
    output.write(' fullscheme' + ' text,')
    output.write(' scheme'     + ' text,')
    output.write(' signat'     + ' text,')
    output.write(' brackets'   + ' text,')
    output.write(' dibrank'    + ' int,')
    output.write(' lptrank'    + ' int,')
    output.write(' depth'      + ' int,')
    output.write(' parent'     + ' int,')
    output.write(' wingseq'    + ' text,')
    output.write(' jmol'       + ' text,')
    output.write(' chainseq'   + ' text,')
    output.write(' index(model)')

def atompairs(output):

    output.write('id'        + ' int' + ' unique primary key,')
    output.write(' model'    + ' int,')
    output.write(' rchain'   + ' int,')
    output.write(' pchain'   + ' int,')
    output.write(' nucl'     + ' varchar(3),')
    output.write(' amino'    + ' varchar(3),')
    output.write(' rdssr'    + ' varchar(20),')
    output.write(' pdssr'    + ' varchar(20),')
    output.write(' ratomid'  + ' int,')
    output.write(' patomid'  + ' int,')
    output.write(' rname'    + ' varchar(5),')
    output.write(' pname'    + ' varchar(5),')
    output.write(' relem'    + ' char(1),')
    output.write(' pelem'    + ' char(1),')
    output.write(' rjmol'    + ' varchar(15),')
    output.write(' pjmol'    + ' varchar(15),')
    output.write(' power'    + ' float(8,3),')
    output.write(' dist'     + ' float(8,3),')
    output.write(' rcos'     + ' float(8,3),')
    output.write(' pcos'     + ' float(8,3),')
    output.write(' monopair' + ' int,')
    output.write(' index(model)')

def monopairs(output):

    output.write('id'         + ' int' + ' unique primary key,')
    output.write(' model'     + ' int,')
    output.write(' rchain'    + ' int,')
    output.write(' pchain'    + ' int,')
    output.write(' nucl'      + ' varchar(3),')
    output.write(' amino'     + ' varchar(3),')
    output.write(' rdssr'     + ' varchar(20),')
    output.write(' pdssr'     + ' varchar(20),')
    output.write(' rjmol'     + ' varchar(15),')
    output.write(' pjmol'     + ' varchar(15),')
    output.write(' atompairs' + ' int,')
    output.write(' index(model)')

def rfam_family(output):

    output.write('rfam_acc varchar(7) NOT NULL,')
    output.write('rfam_id varchar(40) NOT NULL,')
    output.write('auto_wiki int(10) unsigned NOT NULL,')
    output.write('description varchar(75) DEFAULT NULL,')
    output.write('author tinytext,')
    output.write('seed_source tinytext,')
    output.write('gathering_cutoff double(5,2) DEFAULT NULL,')
    output.write('trusted_cutoff double(5,2) DEFAULT NULL,')
    output.write('noise_cutoff double(5,2) DEFAULT NULL,')
    output.write('comment longtext,')
    output.write('previous_id tinytext,')
    output.write('cmbuild tinytext,')
    output.write('cmcalibrate tinytext,')
    output.write('cmsearch tinytext,')
    output.write('num_seed bigint(20) DEFAULT NULL,')
    output.write('num_full bigint(20) DEFAULT NULL,')
    output.write('num_genome_seq bigint(20) DEFAULT NULL,')
    output.write('num_refseq bigint(20) DEFAULT NULL,')
    output.write('type varchar(50) DEFAULT NULL,')
    output.write('structure_source tinytext,')
    output.write('number_of_species bigint(20) DEFAULT NULL,')
    output.write('number_3d_structures int(11) DEFAULT NULL,')
    output.write('num_pseudoknots int(11) DEFAULT NULL,')
    output.write('tax_seed mediumtext,')
    output.write('ecmli_lambda double(10,5) DEFAULT NULL,')
    output.write('ecmli_mu double(10,5) DEFAULT NULL,')
    output.write('ecmli_cal_db mediumint(9) DEFAULT "0",')
    output.write('ecmli_cal_hits mediumint(9) DEFAULT "0",')
    output.write('maxl mediumint(9) DEFAULT "0",')
    output.write('clen mediumint(9) DEFAULT "0",')
    output.write('match_pair_node tinyint(1) DEFAULT "0",')
    output.write('hmm_tau double(10,5) DEFAULT NULL,')
    output.write('hmm_lambda double(10,5) DEFAULT NULL,')
    output.write('created datetime NOT NULL,')
    output.write('updated timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,')
    output.write('PRIMARY KEY (rfam_acc),')
    output.write('UNIQUE KEY rfam_acc (rfam_acc),')
    output.write('KEY rfam_id (rfam_id),')
    output.write('KEY fk_family_wikitext1_idx (auto_wiki)')


def rfam_pdb(output):

    output.write('rfam_acc varchar(7) NOT NULL,')
    output.write('pdb_id varchar(4) NOT NULL,')
    output.write('chain varchar(4) CHARACTER SET latin1 COLLATE latin1_bin DEFAULT NULL,')
    output.write('pdb_start mediumint(8) NOT NULL,')
    output.write('pdb_end mediumint(8) NOT NULL,')
    output.write('bit_score double(7,2) NOT NULL DEFAULT "0.00",')
    output.write('evalue_score varchar(15) NOT NULL DEFAULT "0",')
    output.write('cm_start mediumint(8) NOT NULL,')
    output.write('cm_end mediumint(8) NOT NULL,')
    output.write('hex_colour varchar(6) DEFAULT "NULL",')
    output.write('is_significant tinyint(1) NOT NULL DEFAULT "1",')
    output.write('KEY fk_pdb_rfam_reg_family1_idx (rfam_acc),')
    output.write('KEY fk_pdb_rfam_reg_pdb1_idx (pdb_id),')
    output.write('KEY rfam_acc (rfam_acc),')
    output.write('KEY is_significant (is_significant)')
    

def build(txtfolder, local = False, update=False):

    if txtfolder[-1] != '/': txtfolder += '/'

    if       local and not update: output = open('raise_local_db.txt' ,'w')
    elif     local and     update: output = open('update_local_db.txt','w')
    elif not local and not update: output = open('raise_db.txt','w')
    else                         : output = open('update_db.txt','w')

    if local: local = ' LOCAL' # LOCAL is for current computer; else - for server
    else    : local = ''

    dbname = 'rss'

    

    functions = {'01files'       : files,       '02models'        : models,   # numbers are for sorting;
                 '03molecules'   : molecules,   '04chains'        : chains,   # sorting are for easy navigation
                 '05nucls'       : nucls,       '06aminos'        : aminos,   # through the sql-script
                 '07ligands'     : ligands,     '08atoms'         : atoms,                          
                 '09BasePairs'   : BasePairs,   '10towers'        : towers,
                 '11links'       : links,       '12stems'         : stems,    
                 '13StemsOld'    : StemsOld,    '14StemsFull'     : StemsFull,   
                 '15wings'       : wings,       '16WingsOld'      : WingsOld,  
                 '17WingsFull'   : WingsFull,   '18threads'       : threads,   
                 '19hairpins'    : hairpins,    '20bulges'        : bulges,   
                 '21internals'   : internals,   '22junctions'     : junctions, 
                 '23threadloop'  : threadloop,  '24wingloop'      : wingloop,
                 '25faceloop'    : faceloop,    '26ChainsConcat'  : ChainsConcat,
                 '27LuHelices'   : LuHelices,   '28LuStems'       : LuStems,
                 '29LuStemHelix' : LuStemHelix, '30LuMultiplets'  : LuMultiplets,
                 '31LuNphbs'     : LuNphbs,     '32LuNonLoops'    : LuNonLoops,
                 '33LuKissing'   : LuKissing,   '34LuAminors'     : LuAminors,
                 '35LuUturns'    : LuUturns,    '36LuZippers'     : LuZippers,
                 '37LuKturns'    : LuKturns,    '38LuHairpins'    : LuHairpins,
                 '39LuBulges'    : LuBulges,    '40LuInternals'   : LuInternals,
                 '41LuJunctions' : LuJunctions, '42LuJuncThreads' : LuJuncThreads,
                 '43RevStems'    : RevStems,    '44NuclMults'     : NuclMults,
                 '45StemMults'   : StemMults,   '46StemNPairs'    : StemNPairs,
                 '47StemLPairs'  : StemLPairs,  '48diagrams'      : diagrams,
                 '49ecfs'        : ecfs,        '50atompairs'     : atompairs,
                 '51monopairs'   : monopairs,   '52rfam_family'   : rfam_family,
                 '53rfam_pdb'    : rfam_pdb} 

    if not update:
        output.write('drop database IF EXISTS ' + dbname + ';\n\n')
        output.write('create database '         + dbname + ';\n\n')

    output.write('use ' + dbname + ';\n\n')

    for table in sorted(functions.keys()):

        if not update:
            output.write('create table ' + table[2:] + ' (') # the [2:] is to cut first two integers (numbers)
            functions[table](output)
            output.write(');\n\n')
            
        elif table[2:] in ('rfam_family','rfam_pdb'):
            output.write('drop table IF EXISTS ' + table[2:] + ';\n\n')
            output.write('create table ' + table[2:] + ' (')
            functions[table](output)
            output.write(');\n\n')
            
        output.write("LOAD DATA" + local + " INFILE '" + txtfolder + table[2:] + ".txt'")
        output.write(' INTO TABLE ' + table[2:] + ';\n\n')
        output.write('SHOW WARNINGS;\n\n')

    if not update: output.write('SET GROUP_CONCAT_MAX_LEN=30000;\n\n')
    
    output.close()

if __name__ == '__main__':

    build('/home/baulin/eugene/work/urs/txts', True)
    build('/home/baulin/rssdb/txts')
    build('/home/baulin/eugene/work/urs/pdb_update/txts', True, True)
    build('/home/baulin/rssdb/txts', False, True)
