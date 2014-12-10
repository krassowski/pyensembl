from pyensembl import EnsemblRelease

ensembl75 = EnsemblRelease(75)

def test_gene_ids():
    # only load chromosome Y to speed up tests
    df = ensembl75.gtf.dataframe(contig="Y")
    assert 'gene_id' in df
    # Ensembl gene ids are formatted like ENSG00000223972
    # which is always length 15
    assert (df['gene_id'].str.len() == 15).all(), \
	df[df['gene_id'].str.len() != 15]
