

import pymysql
import datetime



outp = open('OrgMol.csv','w')
outp.write('\t'.join(['PDB','Chain','Molecule','Organism'])+'\n')

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='125876', db='rss')
cur = conn.cursor()
    
cur.execute('select c.letter,md.file,md.number,m.orgsc,m.mol from chains c join models md on md.id=c.model join '+\
            'molecules m on m.id=c.mol where type="RNA"')

k = 0

for row in cur:

    k += 1
    if k%100==0: print(k,'\t',datetime.datetime.now().isoformat())

    letter      = row[0]
    file        = row[1]
    number      = row[2]
    orgsc       = row[3]
    mol         = row[4]

    pdbfile = file.lower()+'.cif'+str(number)

    res = [pdbfile,letter,mol,orgsc]

    outp.write('\t'.join([str(x) for x in res])+'\n')

outp.close()
cur.close()
conn.close()



