from __future__ import division
import numpy as np
from os.path import expanduser
import sys
import pandas as pd

mydir = expanduser("~/GitHub/GlobalDef")
df = pd.read_csv('interactions-o.tsv', sep='\t')


drop_list = ['sourceTaxonIds', 'sourceTaxonName', 
             'sourceTaxonRank', 'sourceTaxonPathNames', 'sourceTaxonPathIds', 
             'sourceTaxonPathRankNames', 'sourceTaxonSpeciesName', 
             'sourceTaxonSpeciesId', 'sourceTaxonGenusName', 
             'sourceTaxonGenusId', 'sourceTaxonFamilyName', 
             'sourceTaxonFamilyId', 'sourceTaxonOrderName', 
             'sourceTaxonOrderId', 'sourceTaxonClassName', 
             'sourceTaxonClassId', 'sourceTaxonPhylumName', 
             'sourceTaxonPhylumId', 'sourceTaxonKingdomName', 
             'sourceTaxonKingdomId', 'sourceId', 'sourceOccurrenceId', 
             'sourceCatalogNumber', 'sourceBasisOfRecordId', 
             'sourceBasisOfRecordName', 'sourceLifeStageId', 
             'sourceLifeStageName', 'sourceBodyPartId', 'sourceBodyPartName', 
             'sourcePhysiologicalStateId', 'sourcePhysiologicalStateName', 
             'interactionTypeName', 'interactionTypeId', 'targetTaxonId', 
             'targetTaxonIds', 'targetTaxonName', 'targetTaxonRank', 
             'targetTaxonPathNames', 'targetTaxonPathIds', 
             'targetTaxonPathRankNames', 'targetTaxonSpeciesName', 
             'targetTaxonSpeciesId', 'targetTaxonGenusName', 
             'targetTaxonGenusId', 'targetTaxonFamilyName', 
             'targetTaxonFamilyId', 'targetTaxonOrderName', 
             'targetTaxonOrderId', 'targetTaxonClassName', 
             'targetTaxonClassId', 'targetTaxonPhylumName', 
             'targetTaxonPhylumId', 'targetTaxonKingdomName', 
             'targetTaxonKingdomId', 'targetId', 'targetOccurrenceId', 
             'targetCatalogNumber', 'targetBasisOfRecordId', 
             'targetBasisOfRecordName', 'targetLifeStageId', 
             'targetLifeStageName', 'targetBodyPartId', 'targetBodyPartName', 
             'targetPhysiologicalStateId', 'targetPhysiologicalStateName', 
             'localityId', 
             'localityName', 'eventDateUnixEpoch', 'argumentTypeId', 
             'referenceCitation', 'referenceDoi', 'referenceUrl', 
             'sourceCitation', 'sourceNamespace', 'sourceArchiveURI', 
             'sourceDOI', 'sourceLastSeenAtUnixEpoch']

#df.drop(drop_list, axis=1)
#print(list(df))

df = df.drop(drop_list, axis=1)
print(list(df))
#sys.exit()

fname = 'interactions_latlons.txt'
df.to_csv(fname, sep='\t', index=False)