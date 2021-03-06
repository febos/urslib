try:
    from urslib import Merge
    from urslib.SS import ChainOrder, Mask
    from urslib.SS import Wings, Stems,  Threads, Links
    from urslib.SS import Loops, Towers, Multiplets, Sign
    from urslib.SS import Interactions, MetalAndLigand, Relation
    from urslib.SS import Organism,GetMotifPDB
except ImportError:
    import Merge
    from SS import ChainOrder, Mask
    from SS import Wings, Stems,  Threads,    Links
    from SS import Loops, Towers, Multiplets, Sign
    from SS import Interactions, MetalAndLigand, Relation
    from SS import Organism,GetMotifPDB

def SecStruct(pdbmodel, outmodel):

    model = Merge.Model(pdbmodel,outmodel)

    Mask.add(model)
    ChainOrder.add(model)
    Wings.add(model)
    Stems.add(model)
    Threads.add(model)
    Links.add(model)
    Loops.add(model)
    Towers.add(model)
    Multiplets.add(model)
    Sign.add(model)
    Interactions.add(model)
    MetalAndLigand.add(model)
    Relation.add(model)
    Organism.add(model)
    GetMotifPDB.add(model)

    return model

if __name__=='__main__':

    model = SecStruct('/home/baulin/eugene/work/urs/mmCIF/models/1asy.cif1',
                      '/home/baulin/eugene/work/urs/mmCIF/out/1asy.out1')
    

    model.GetMotifPDB(['R.G.617.','R.A.657.','R.G.618.'],'SS/1asy_1_R617_R657_R618.pdb')

    '''
    1asy.cif1	i+1	intramolecular	R.G.617.	R.A.657.	R.G.618.	G-A-G	HC-HC-HC
    LR-LR-SM	R	T-RNA (75-MER)		
    R	T-RNA (75-MER)		X-RAY DIFFRACTION	2.9	16	75	G.617..A.657..G.618.
    '''

    #print('9.G.21.,9.C.59.',model.NuclRelation('9.G.21.','9.C.59.'))
    #print('9.A.3.,9.C.59.',model.NuclRelation('9.A.3.','9.C.59.'))
    #print('9.G.21.,9.A.3.',model.NuclRelation('9.G.21.','9.A.3.'))
    #150  type=I A|G-C	1..9.A.3.|1..9.G.21.,1..9.C.59. WC

    '''
    model = SecStruct('/home/baulin/eugene/work/urs/mmCIF/models/1duh.cif1',
                      '/home/baulin/eugene/work/urs/mmCIF/out/1duh.out1')
    print(len(model.atompairsM))
    print(len(model.atompairsL))
    print(len(model.monopairsM))
    print(len(model.monopairsL))
    print('Metals')
    for pair in model.monopairsM:
        print(pair['RDSSR'],pair['LDSSR'])
    print('Ligands')
    for pair in model.monopairsL:
        print(pair['RDSSR'],pair['LDSSR'])
    print('finish')
    '''
