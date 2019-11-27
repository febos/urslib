import pymysql
import glob

try:
    from urslib import Build
    from urslib import DSSR
except ImportError:
    import Build
    import DSSR

def RemoveOld(pdb):

    res = ['delete from files where name="%s";'%pdb,
           'delete from models where file="%s";'%pdb,
           'delete from molecules where file="%s";'%pdb]

    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='125876', db='rss')
    cur = conn.cursor()

    cur.execute('select id from models where file="%s";'%pdb)

    mids = []

    for row in cur: mids.append(str(row[0]))

    if not mids: return []

    mids = ','.join(mids)

    tables = ['chains','nucls','aminos','ligands','atoms','BasePairs','towers',
    'links','stems','StemsOld','StemsFull','wings','WingsOld','WingsFull',
    'threads','hairpins','bulges','internals','junctions','threadloop',
    'wingloop','faceloop','ChainsConcat','LuHelices','LuStems','LuStemHelix',
    'LuMultiplets','LuNphbs','LuNonLoops','LuKissing','LuAminors','LuUturns',
    'LuZippers','LuKturns','LuHairpins','LuBulges','LuInternals','LuJunctions',
    'LuJuncThreads','RevStems','NuclMults','StemMults','StemNPairs','StemLPairs',
    'diagrams','ecfs','atompairs','monopairs']

    for table in tables: res.append('delete from %s where model in (%s);'%(table,mids))

    cur.close()
    conn.close()

    return res

def IDS():

    ids ={}

    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='125876', db='rss')
    cur = conn.cursor()
    
    for table in Build.Changes():

        cur.execute('desc {}'.format(table))
        flag = False
        for row in cur:
            if row[0]=='id':
                flag = True
                break

        if flag: cur.execute("SELECT max(id)  FROM {}".format(table))
        else   : cur.execute("SELECT count(*) FROM {}".format(table))

        ids[table] = cur.fetchone()[0]

    cur.close()
    conn.close()

    return ids

def LoadToMySQL(PathToPDB):

    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='125876', db='rss')
    cur = conn.cursor()
    cur.execute('source {}update_local_db.txt'.format(PathToPDB))
    cur.close()
    conn.close()

def Update(form,PathToPDB):

    PathToFiles  = PathToPDB + 'files/'
    PathToModels = PathToPDB + 'models/'
    PathToOut    = PathToPDB + 'out/'
    PathToTxts   = PathToPDB + 'txts/'

    
    if   form=='cif': import SplitmmCIF as Split
    elif form=='pdb': import SplitPDB   as Split
    else:
        print('Format has to be either cif or pdb')
        exit(1)

    Split.All(PathToFiles,PathToModels)
    DSSR.run_all(PathToModels,PathToOut,form)
    OLDids = IDS()

    files = sorted(glob.glob(PathToFiles+'*.%s*'%form))

    script = open('/home/baulin/eugene/work/urs/pdb_update/update_db_new.txt','w')
    scriptlocal = open('/home/baulin/eugene/work/urs/pdb_update/update_local_db_new.txt','w')

    script.write('use rss;\n\n')
    scriptlocal.write('use rss;\n\n')

    for file in files:

        pdb = file.split('/')[-1].split('.')[0]

        instrs = RemoveOld(pdb)
        for instr in instrs:
            script.write(instr+'\n\n')
            scriptlocal.write(instr+'\n\n')

    with open('/home/baulin/eugene/work/urs/pdb_update/update_db.txt','r') as f:
        for line in f:
            script.write(line)

    with open('/home/baulin/eugene/work/urs/pdb_update/update_local_db.txt','r') as f:
        for line in f:
            scriptlocal.write(line)

    script.close()
    scriptlocal.close()
    
    Build.txt(form,True,OLDids,PathToModels,PathToOut,PathToTxts)
    #LoadToMySQL(PathToPDB)

if __name__=='__main__':

    Update('cif','/home/baulin/eugene/work/urs/pdb_update/')
