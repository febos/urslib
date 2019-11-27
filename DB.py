

try:
    from urslib import RSS
    from urslib import Tables
    from urslib import LuTables
    from urslib import ExtraTables

except ImportError:
    import RSS
    import Tables
    import LuTables
    import ExtraTables

def tables(pdbmodel,outmodel):

    model = RSS.SecStruct(pdbmodel,outmodel)

    return {'files'         : Tables.files(model),
            'models'        : Tables.models(model),
            'molecules'     : Tables.molecules(model),
            'chains'        : Tables.chains(model),
            'nucls'         : Tables.nucls(model),
            'aminos'        : Tables.aminos(model),
            'ligands'       : Tables.ligands(model),
            'atoms'         : Tables.atoms(model),
            'BasePairs'     : Tables.BasePairs(model),
            'towers'        : Tables.towers(model),
            'links'         : Tables.links(model),
            'stems'         : Tables.stems(model),
            'StemsOld'      : Tables.StemsOld(model),
            'StemsFull'     : Tables.StemsFull(model),
            'wings'         : Tables.wings(model),
            'WingsOld'      : Tables.WingsOld(model),
            'WingsFull'     : Tables.WingsFull(model),
            'threads'       : Tables.threads(model),
            'hairpins'      : Tables.hairpins(model),
            'bulges'        : Tables.bulges(model),
            'internals'     : Tables.internals(model),
            'junctions'     : Tables.junctions(model),
            'threadloop'    : Tables.threadloop(model),
            'wingloop'      : Tables.wingloop(model),
            'faceloop'      : Tables.faceloop(model),
            'ChainsConcat'  : Tables.ChainsConcat(model),
            'LuHelices'     : LuTables.LuHelices(model),
            'LuStems'       : LuTables.LuStems(model),
            'LuStemHelix'   : LuTables.LuStemHelix(model),
            'LuMultiplets'  : LuTables.LuMultiplets(model),
            'LuNphbs'       : LuTables.LuNphbs(model),
            'LuNonLoops'    : LuTables.LuNonLoops(model),
            'LuKissing'     : LuTables.LuKissing(model),
            'LuAminors'     : LuTables.LuAminors(model),
            'LuUturns'      : LuTables.LuUturns(model),
            'LuZippers'     : LuTables.LuZippers(model),
            'LuKturns'      : LuTables.LuKturns(model),
            'LuHairpins'    : LuTables.LuHairpins(model),
            'LuBulges'      : LuTables.LuBulges(model),
            'LuInternals'   : LuTables.LuInternals(model),
            'LuJunctions'   : LuTables.LuJunctions(model),
            'LuJuncThreads' : LuTables.LuJuncThreads(model),
            'RevStems'      : ExtraTables.RevStems(model),
            'NuclMults'     : ExtraTables.NuclMults(model),
            'StemMults'     : ExtraTables.StemMults(model),
            'StemNPairs'    : ExtraTables.StemNPairs(model),
            'StemLPairs'    : ExtraTables.StemLPairs(model),
            'diagrams'      : ExtraTables.diagrams(model),
            'ecfs'          : ExtraTables.ecfs(model),
            'atompairs'     : ExtraTables.atompairs(model),
            'monopairs'     : ExtraTables.monopairs(model)}
