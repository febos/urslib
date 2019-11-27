import os
import time
import glob


try:
    from urslib import DB
    from urslib import RfamUpd

except ImportError:
    import DB
    import RfamUpd


def path(form,pdbfolder,dssrfolder,outfolder):

    good_input = 0

    while not good_input:
        
        if os.path.exists(pdbfolder)  and\
           os.path.exists(dssrfolder) and\
           os.path.exists(outfolder):
            good_input = 1

        elif pdbfolder or dssrfolder or outfolder:

            print('Bad paths. Try again...')
            pdbfolder   = input('Please enter the path to folder with %s models: '%form)
            dssrfolder  = input('Please enter the path to folder with dssr outputs: ')
            outfolder   = input('Please enter the path to output folder: ')

        else:

            pdbfolder   = input('Please enter the path to folder with %s models: '%form)
            dssrfolder  = input('Please enter the path to folder with dssr outputs: ')
            outfolder   = input('Please enter the path to output folder: ')

    if  pdbfolder[-1]  not in ('/','\\'): pdbfolder  += '/'
    if dssrfolder[-1]  not in ('/','\\'): dssrfolder += '/'
    if  outfolder[-1]  not in ('/','\\'): outfolder  += '/'

    return pdbfolder,dssrfolder,outfolder

def Changes(): # {table to change : {index to increase : what to add,},}

    return {'files'        :{},
            'models'       :{0: 'models'},
            'molecules'    :{0: 'molecules'},
            'chains'       :{0: 'chains',
                             1: 'models',
                             2: 'molecules',
                            19: 'diagrams'},
            'nucls'        :{0: 'nucls',
                             2: 'models',
                             3: 'chains',
                             5: 'threads',
                             6: 'wings',
                             7: 'WingsOld',
                            11: 'LuZippers',
                            12: 'NuclMults',
                            13: 'LuMultiplets',
                            17: 'diagrams'},
            'aminos'       :{0: 'aminos',
                             2: 'models',
                             3: 'chains'},
            'ligands'      :{0: 'ligands',
                             2: 'models',
                             3: 'chains'},
            'atoms'        :{0: 'atoms',
                             1: 'models',
                             2: 'chains'},
            'BasePairs'    :{0: 'BasePairs',
                             1: 'models',
                             3: 'chains',
                             4: 'chains',
                            12: 'stems',
                            13: 'StemsOld',
                            14: 'StemsFull',
                            15: 'RevStems',
                            16: 'LuStems',
                            17: 'links',
                            18: 'LuHelices',
                            19: 'NuclMults'},
            'towers'       :{0: 'towers',
                             1: 'models',
                             3: 'chains',
                             4: 'chains'},
            'links'        :{0: 'links',
                             1: 'models',
                             2: 'chains',
                             3: 'chains',
                             4: 'BasePairs',
                             6: 'threads',
                             7: 'wings',
                             8: 'threads',
                             9: 'wings'},
            'stems'        :{0: 'stems',
                             1: 'models',
                             3: 'chains',
                             4: 'chains',
                             8: 'wings',
                             9: 'wings',
                            11: 'towers',
                            14: 'StemsOld',
                            15: 'StemsFull',
                            16: 'StemMults',
                            17: 'diagrams',
                            19: 'ecfs'},
            'StemsOld'     :{0: 'StemsOld',
                             1: 'models',
                             3: 'chains',
                             4: 'chains',
                             7: 'WingsOld',
                             8: 'WingsOld',
                            10: 'StemsFull',
                            13: 'StemMults'},
            'StemsFull'    :{0: 'StemsFull',
                             1: 'models',
                             3: 'chains',
                             4: 'chains',
                             8: 'WingsFull',
                             9: 'WingsFull',
                            13: 'StemMults'},
            'wings'        :{0: 'wings',
                             1: 'models',
                             2: 'chains',
                             3: 'stems',
                             4: 'wings',
                             5: 'threads',
                             6: 'threads',
                             7: 'wings',
                             8: 'wings',
                             14:'ecfs'},
            'WingsOld'     :{0: 'WingsOld',
                             1: 'models',
                             2: 'chains',
                             3: 'StemsOld',
                             4: 'WingsOld',
                             5: 'WingsOld',
                             6: 'WingsOld'},
            'WingsFull'    :{0: 'WingsFull',
                             1: 'models',
                             2: 'chains',
                             3: 'StemsFull',
                             4: 'WingsFull',
                             5: 'WingsFull',
                             6: 'WingsFull'},
            'threads'      :{0: 'threads',
                             1: 'models',
                             2: 'chains',
                             3: 'wings',
                             4: 'wings'},
            'hairpins'     :{0: 'hairpins',
                             1: 'stems',
                             2: 'models',
                             3: 'chains'},
            'bulges'       :{0: 'bulges',
                             1: 'stems',
                             2: 'models',
                             3: 'chains',
                             4: 'chains'},
            'internals'    :{0: 'internals',
                             1: 'stems',
                             2: 'models',
                             3: 'chains',
                             4: 'chains'},
            'junctions'    :{0: 'junctions',
                             1: 'stems',
                             2: 'models',
                             3: 'chains',
                             4: 'chains'},
            'threadloop'   :{0: 'models',
                             3: 'threads'},
            'wingloop'     :{0: 'models',
                             3: 'wings'},
            'faceloop'     :{0: 'models',
                             3: 'stems',
                             4: 'stems'},
            'ChainsConcat' :{0: 'models',
                             1: 'chains',
                             2: 'chains'},
            'LuHelices'    :{0: 'LuHelices',
                             1: 'models'},
            'LuStems'      :{0: 'LuStems',
                             1: 'models',
                             3: 'chains',
                             4: 'chains'},
            'LuStemHelix'  :{0: 'models',
                             1: 'LuStems',
                             2: 'LuHelices'},
            'LuMultiplets' :{0: 'LuMultiplets',
                             1: 'models'},
            'LuNphbs'      :{0: 'LuNphbs',
                             1: 'models'},
            'LuNonLoops'   :{0: 'LuNonLoops',
                             1: 'models',
                             2: 'chains'},
            'LuKissing'    :{0: 'LuKissing',
                             1: 'models',
                             2: 'LuHairpins',
                             3: 'LuHairpins',
                             4: 'LuStems'},
            'LuAminors'    :{0: 'LuAminors',
                             1: 'models',
                             3: 'BasePairs'},
            'LuUturns'     :{0: 'LuUturns',
                             1: 'models',
                             2: 'chains'},
            'LuZippers'    :{0: 'LuZippers',
                             1: 'models'},
            'LuKturns'     :{0: 'LuKturns',
                             1: 'models',
                             2: 'BasePairs',
                             3: 'LuHelices',
                             4: 'LuStems',
                             5: 'LuStems',
                             6: 'LuInternals'},
            'LuHairpins'   :{0: 'LuHairpins',
                             1: 'models',
                             2: 'chains',
                             5: 'LuStems'},
            'LuBulges'     :{0: 'LuBulges',
                             1: 'models',
                             2: 'chains',
                             3: 'LuStems',
                             4: 'LuStems'},
            'LuInternals'  :{0: 'LuInternals',
                             1: 'models',
                             2: 'chains',
                             3: 'chains',
                             4: 'LuStems',
                             5: 'LuStems'},
            'LuJunctions'  :{0: 'LuJunctions',
                             1: 'models'},
            'LuJuncThreads':{0: 'LuJunctions',
                             1: 'models',
                             2: 'chains',
                             8: 'LuStems'},
            'RevStems'     :{0: 'RevStems',
                             1: 'models',
                             2: 'chains',
                             3: 'chains'},
            'NuclMults'    :{0: 'NuclMults',
                             1: 'models'},
            'StemMults'    :{0: 'StemMults',
                             1: 'models'},
            'StemNPairs'   :{0: 'StemNPairs',
                             1: 'models',
                             2: 'StemsFull',
                             3: 'StemsFull',
                             5: 'StemMults'},
            'StemLPairs'   :{0: 'StemLPairs',
                             1: 'models',
                             2: 'links',
                             3: 'StemsFull',
                             4: 'StemsOld',
                             5: 'stems',
                             6: 'StemsFull',
                             7: 'StemsOld',
                             8: 'stems',
                             9: 'StemMults'},
            'diagrams'     :{0: 'diagrams',
                             1: 'models'},
            'ecfs'         :{0: 'ecfs',
                             1: 'models',
                             2: 'diagrams',
                            10: 'ecfs'},
            'atompairs'    :{0: 'atompairs',
                             1: 'models',
                             2: 'chains',
                             3: 'chains',
                             8: 'atoms',
                             9: 'atoms',
                            20: 'monopairs'},
            'monopairs'    :{0: 'monopairs',
                             1: 'models',
                             2: 'chains',
                             3: 'chains'}}

def IDs(changes,update,OLDids): # dictionary with changing numbers for adding in tables (to IDs) 

    ids = {}
    for table in changes:
        if not update: ids[table] = 0
        else: ids[table] = OLDids[table]
    return ids

def Outputs(outfolder,ids): # {table: txt,}

    outputs = {}

    for table in ids: outputs[table] = open(outfolder+table+'.txt','w')

    return outputs

def add_ids(tables,ids,changes): # adding ids

    dict_for_loop_elements = {'H':'hairpins','B':'bulges','I':'internals','J':'junctions'}

    for table in tables:

        #### because we don't know which loop-table to use
        if table in ('threadloop','wingloop','faceloop'):

            for line in tables[table]:

                line[1] += ids[dict_for_loop_elements[line[2]]]
        ##################################################

        for line in tables[table]:

            for i in changes[table]:

                if line[i] != '\\N': # if not NULL

                    line[i] += ids[changes[table][i]]

def Print(outputs,tables):

    for table in tables:

        for line in tables[table]:
            #f table=='chains' and 4<=line[1]<=13: print(line[2:4])### - remove
            for value in line:

                outputs[table].write(str(value)+'\t')

            outputs[table].write('\n')

def enlarge(ids,tables):    # increasing ids

    for table in tables: ids[table] += len(tables[table]) 

def Close(outputs): # closing txt-files

    for key in outputs: outputs[key].close()

def txt(form='cif', update=False, OLDids={}, pdbfolder='', dssrfolder='', outfolder=''): # main

    pdbfolder,dssrfolder,outfolder = path(form,pdbfolder,dssrfolder,outfolder)

    RfamUpd.update(outfolder)

    Time    = time.time()
    changes = Changes()
    ids     = IDs(changes,update,OLDids)
    outputs = Outputs(outfolder,ids)
    files   = sorted(glob.glob(pdbfolder+'*.%s*'%form))

    total   = len(files)
    counter = 1
    hundred = 1

    print('Starting...')

    oldfile = 'xxxx'

    for file in files:

        '''
        if counter<=10165:
            counter += 1
            continue
        print(file)
        '''
        #print(file)##
        tables = DB.tables(file,dssrfolder+os.path.basename(file).replace('.%s'%form,'.out'))   # get tables

        add_ids(tables,ids,changes)

        file = tables['models'][0][2]
        if file!=oldfile: mols = len(tables['molecules'])
        else:
            for i in range(len(tables['chains'])):
                tables['chains'][i][2] -= mols
        oldfile = file
        
        Print(outputs,tables)
        enlarge(ids,tables)

        if hundred == 25 or counter==total: # for comfortable command-line output

            print(str(counter)+'/'+str(total))
            hundred = 0

        counter += 1
        hundred += 1

    Close(outputs)
    
    Time = time.time() - Time    
    print('Time: %s h %s min %s sec'%(int(Time//3600),int((Time%3600)//60),int(Time%60)))


if __name__=='__main__':

    txt()
