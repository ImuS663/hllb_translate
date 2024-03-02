from torch import cuda
from typing import Any
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, PreTrainedTokenizerFast, Pipeline, pipeline


def load_model(cache_dir: Path) -> tuple[PreTrainedTokenizerFast, Any]:
    tokenizer = AutoTokenizer.from_pretrained('facebook/nllb-200-distilled-600M', cache_dir=cache_dir)
    model = AutoModelForSeq2SeqLM.from_pretrained('facebook/nllb-200-distilled-600M', cache_dir=cache_dir)

    return tokenizer, model


def pipe(tokenizer: PreTrainedTokenizerFast, model, source_lang: str, target_lang: str,
         batch_size: int, device: str) -> Pipeline:
    translator = pipeline('translation', model, tokenizer=tokenizer, src_lang=source_lang,
                          tgt_lang=target_lang, max_length=400, batch_size=batch_size,
                          device='cuda' if device == 'cuda' and cuda.is_available() else 'cpu')

    return translator
