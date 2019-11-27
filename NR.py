import glob

try: from urslib import RSS
except ImportError: import RSS

modres = {'02I':'a',  '0A':'a',  '0C':'c',  '0G':'g',  '0U':'u', '0U1':'u', '10C':'c', '12A':'a',
          '1CC':'c', '1MA':'a', '1MG':'g', '1RN':'u', '1SC':'c', '218':'u', '23G':'g', '29G':'u',
          '29H':'u', '2AD':'a', '2AU':'u', '2BA':'a', '2BP':'g', '2IA':'a', '2MA':'a', '2MG':'g',
          '2MU':'u', '2PR':'g', '2QB':'u', '2SG':'g', '31H':'a', '31M':'a', '365':'a', '3AD':'a',
          '3AT':'a', '3AU':'u', '3AY':'u', '3DA':'a', '3TD':'u', '45A':'a', '4BW':'a', '4M2':'a',
          '4OC':'c', '4SU':'u', '574':'a', '5AA':'a', '5BU':'u', '5CF':'c', '5CG':'g', '5CM':'c',
          '5FU':'u', '5GP':'g', '5GS':'u', '5IC':'c', '5IU':'u', '5MC':'c', '5MU':'u', '6AP':'a',
          '6FC':'c', '6FU':'u', '6GO':'g', '6GS':'u', '6GU':'g', '6HA':'a', '6HC':'c', '6HG':'g',
          '6HT':'u', '6IA':'a', '6MD':'a', '6MZ':'a', '7AT':'a', '7DG':'g', '7MG':'g', '84T':'a',
          '8AN':'a', '8OG':'g', '8XA':'a', '8XC':'c', '8XG':'g', '8XU':'u', '9DG':'g', 'A23':'a',
          'A2F':'a', 'A2L':'a', 'A2M':'a', 'A2P':'a', 'A3P':'a', 'A44':'a', 'A5A':'a', 'A5L':'a',
          'A5M':'c', 'A5O':'a', 'A6A':'a', 'A6C':'c', 'A6G':'g', 'A6U':'u', 'A7E':'a', 'A9Z':'a',
          'ACP':'a', 'ADN':'a', 'ADP':'a', 'ADS':'a', 'AET':'a', 'AF2':'a', 'AG9':'c', 'AGS':'a',
          'AMO':'a', 'AMP':'a', 'ANP':'a', 'ANZ':'a', 'AP7':'a', 'APC':'a', 'APN':'a',  'AS':'a',
          'AT7':'a', 'ATL':'u', 'ATP':'a', 'AVC':'a', 'BGM':'g', 'BGR':'g', 'BRU':'u', 'C2E':'g',
          'C2L':'c', 'C43':'c', 'C5L':'c', 'C5P':'c', 'C6G':'g', 'CAR':'c', 'CBR':'c', 'CBV':'c',
          'CCC':'c', 'CDP':'c', 'CFL':'c', 'CFZ':'c', 'CG1':'g',  'CH':'c', 'CH1':'c', 'CPN':'c',
          'CSG':'c', 'CSL':'c', 'CTP':'c', 'CVC':'a', 'DCT':'c', 'DCZ':'c', 'DGP':'g', 'DGT':'g',
          'DJF':'a', 'DOC':'c', 'DTP':'a', 'DUT':'u', 'DX4':'g', 'EEM':'a', 'EPE':'c', 'F3N':'a',
          'F3O':'a', 'FHU':'u', 'FMU':'u', 'FYA':'a', 'G2L':'g', 'G2P':'g', 'G46':'g', 'G48':'g',
          'G7M':'g', 'GAO':'g', 'GCP':'g', 'GDO':'g', 'GDP':'g', 'GF2':'g', 'GFL':'g', 'GH3':'g',
          'GMP':'g', 'GNG':'g', 'GNP':'g', 'GOM':'a', 'GPN':'g', 'GRB':'g',  'GS':'g', 'GSU':'a',
          'GTP':'g', 'GUN':'g', 'H2U':'u', 'HPA':'g',   'I':'g',  'IC':'u',  'IG':'a', 'ILA':'a',
           'IU':'u', 'LCA':'a', 'LCC':'c', 'LCG':'g', 'LKC':'c', 'LLP':'u', 'LMS':'a', 'LSS':'a',
          'M2G':'g', 'M3O':'a', 'M5M':'c', 'M7G':'g', 'MA6':'a', 'MAD':'a', 'MGT':'g', 'MIA':'a',
          'MMT':'u', 'MNU':'u', 'MSP':'a', 'MTU':'g', 'N5C':'c', 'N5M':'c', 'N6G':'a', 'N79':'a',
          'NCU':'c', 'NF2':'u', 'NTT':'u', 'O2C':'c', 'OMC':'c', 'OMG':'g', 'OMU':'u', 'ONE':'u',
          'P5P':'a', 'PDU':'u', 'PGN':'g', 'PGP':'g', 'PLR':'u', 'PPU':'a', 'PQ0':'g', 'PQ1':'g',
          'PRF':'g', 'PSD':'a', 'PST':'u', 'PSU':'u', 'PYI':'u', 'PYO':'u', 'PYY':'u', 'QSI':'a',
          'QUO':'g', 'RIA':'a', 'RPC':'c', 'RSP':'c', 'RSQ':'c', 'RUS':'u', 'S4C':'c', 'SAH':'a',
          'SAM':'a',  'SC':'c', 'SDG':'g', 'SFG':'a', 'SRA':'a', 'SSA':'a', 'SSU':'u', 'SUR':'u',
          'T2T':'u', 'T39':'u', 'T3P':'u', 'T6A':'a', 'TAF':'u', 'TCP':'u', 'TEP':'g', 'TLN':'u',
          'TM2':'u', 'TPN':'u', 'TSB':'a', 'TSP':'u',  'TT':'u', 'U2L':'u', 'U33':'u', 'U34':'u',
          'U36':'u', 'U37':'u', 'U3H':'u', 'U5P':'u', 'U8U':'u', 'UAR':'u', 'UBD':'u', 'UD5':'u',
          'UDP':'u', 'UFT':'u', 'UMS':'u', 'UPV':'u', 'UR3':'u', 'URU':'u', 'US5':'u', 'UTP':'u',
          'UZR':'u', 'VAA':'a', 'XAN':'g', 'XAR':'a', 'XCR':'c', 'XGR':'g', 'XTR':'u', 'XUG':'g',
          'Y5P':'u',  'YG':'g', 'YMP':'a', 'YYG':'g',
           'DA':'A',  'DG':'G',  'DC':'C',  'DT':'U',
            'A':'A',   'G':'G',   'C':'C',   'U':'U'}

def ModRes(char):
    if char not in modres: return 'N'
    else: return modres[char].upper()

file = open('RNAset.csv','w')
file.write(';'.join(['ID','PDB_ID','Date','RESOL','METHOD','Length','Letter','MISS_Nucl','MISS_Atoms',
                     'BPS','Sequence','DBN','Molecule','Organism','Fragment','Synthesized','EC',
                     'Engineered','Mutations','Details','#Stems','#Ligands','Ligands','#Metals','Metals',
                     '#Aminos','Aminos','BoundChains','Sequence2'])+'\n')

structs = sorted(glob.glob('/home/baulin/eugene/work/urs/mmCIF/models/'+'*.cif*'))

Atoms = {'G':23,'A':22,'U':20,'C':20}

ID = 1
ids = {}

kkk = 0

for struct in structs:
    model = RSS.SecStruct(struct,struct.replace('models','out').replace('.cif','.out'))
    pdb = model.headers['PDBFILE'] + '_' + struct[struct.find('.cif')+4:]

    bps = {}
    stems = {}

    for ch in model.chains: # marking ids
        bps[ch] = 0
        stems[ch] = 0
        if model.chains[ch]['TYPE'] =='RNA' and model.chains[ch]['LENGTH']>=6:
            ids[pdb+ch] = ID
            ID += 1

    for bp in model.bpairs: # counting bps
        bps[bp['CHAIN1']] += 1
        if bp['CHAIN1']!=bp['CHAIN2']: bps[bp['CHAIN2']] += 1 
    
    for stm in model.stems: # counting stems
        stems[stm['CHAIN1']] += 1
        if stm['CHAIN1']!=stm['CHAIN2']: stems[stm['CHAIN2']] += 1 


    for ch in model.chains:
        if model.chains[ch]['TYPE'] =='RNA' and model.chains[ch]['LENGTH']>=6:

            kkk += 1
            if kkk%100==0: print(kkk,'/',16941)

            result = [ids[pdb+ch],pdb,model.headers['DATE'],] # ID, PDB_ID, Date

            if type(model.headers['RESOL']) != float: result.append('') # RESOL
            else: result.append(' '+str(model.headers['RESOL']))

            result.append(model.headers['EXPDTA'][0]) # METHOD

            result.append(model.chains[ch]['LENGTH']) #Length

            result.append(ch) #Letter

            missnucl = sum([int(x['MISS']) for x in model.chains[ch]['RES'] if x['TYPE']=='RNA']) #MISS_Nucl
            result.append(missnucl)

            missatoms = -3 #MISS_Atoms
            for res in model.chains[ch]['RES']:
                if res['TYPE'] == 'RNA' and res['NAME'] in ('A','C','G','U') and not res['MISS']:
                    missatoms += Atoms[res['NAME']] - len(res['ATOMS'])
            result.append(missatoms)

            result.append(bps[ch]) #BPS            
            
            result.append(','.join(model.chains[ch]['SEQ'])) #Sequence
            
            result.append(model.chains[ch]['SLBRACKETS']) #DBN

            mol = model.chains[ch]['MOL_ID']
            result.append(model.molecules[mol]['MOLECULE']) #Molecule
            result.append(model.molecules[mol]['ORGANISM_SCIENTIFIC']) #Organism
            result.append(model.molecules[mol]['FRAGMENT']) #Fragment
            result.append(model.molecules[mol]['SYNTHETIC']) #Synthesized
            result.append(model.molecules[mol]['EC']) #EC
            result.append(model.molecules[mol]['ENGINEERED']) #Engineered
            result.append(model.molecules[mol]['MUTATION']) #Mutations
            result.append(model.molecules[mol]['OTHER_DETAILS']) #Details

            result.append(stems[ch]) #Stems 

            aminos,ligands,metals = {},{},{}
            for k in model.monopairs:
                if k['RDSSR'][:k['RDSSR'].find('.')]==ch and k['PDSSR'] not in aminos: aminos[k['PDSSR']] = 1
            for k in model.monopairsL:
                if k['RDSSR'][:k['RDSSR'].find('.')]==ch and k['LDSSR'] not in ligands: ligands[k['LDSSR']] = 1
            for k in model.monopairsM:
                if k['RDSSR'][:k['RDSSR'].find('.')]==ch and k['LDSSR'] not in metals: metals[k['LDSSR']] = 1
            aminotypes = ','.join(sorted(set([x.split('.')[1] for x in aminos.keys()])))
            ligtypes = ','.join(sorted(set([x.split('.')[1] for x in ligands.keys()])))
            metaltypes = ','.join(sorted(set([x.split('.')[1] for x in metals.keys()])))
            result.append(len(ligands)) # #Ligands
            result.append(ligtypes)     # Ligands
            result.append(len(metals))  # #Metals
            result.append(metaltypes)   # Metals
            result.append(len(aminos))  # #Aminos
            result.append(aminotypes)   # Aminos

            boundchains = []
            for concat in model.chain_concat:
                chs = concat.split('-')
                if chs[0]==ch and pdb+chs[1] in ids: boundchains.append(ids[pdb+chs[1]])
                elif chs[1]==ch and pdb+chs[0] in ids: boundchains.append(ids[pdb+chs[0]])

            result.append(','.join([str(x) for x in boundchains]))

            result.append(''.join([ModRes(x) for x in model.chains[ch]['SEQ']])) #Sequence2
            
            #print(result)
            
            file.write(';'.join([str(x).replace(';',',') for x in result])+'\n')

file.close()
