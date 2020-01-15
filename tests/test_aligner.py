from aligner import (
    BertAligner,
    RobertaAligner,
    GPT2Aligner,
    DistilBertAligner
)
import pytest

def load_sample_en_sents():
    from EN_TEST_SENTS import SPACY_EN_TEST_SENTS
    return SPACY_EN_TEST_SENTS

sentences = load_sample_en_sents()

@pytest.mark.parametrize("model_name,alnr_class",
                        [('bert-base-uncased', BertAligner),
                        ('bert-base-cased', BertAligner),
                         ('gpt2', GPT2Aligner),
                        ('roberta-base', RobertaAligner),
                        ('distilbert-base-uncased', DistilBertAligner)])
def test_aligner(model_name, alnr_class):
    """NOTE: Will be obsolete when the aligner is able to work with transformer auto model"""
    a = alnr_class.from_pretrained(model_name)

    for s in sentences:
        mtokens = [m['token'] for m in a.meta_tokenize(s)]
        tokens = a.tokenize(s)
        assert tokens == mtokens, f"{tokens} \n {mtokens}"
