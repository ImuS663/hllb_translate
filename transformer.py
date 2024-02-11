from typing import Any
from read_config import Config
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, PreTrainedTokenizerFast, Pipeline, pipeline


def load_model(config: Config) -> tuple[PreTrainedTokenizerFast, Any]:
    tokenizer = AutoTokenizer.from_pretrained(config.model_name, cache_dir=config.cache_dir)
    model = AutoModelForSeq2SeqLM.from_pretrained(config.model_name, cache_dir=config.cache_dir)

    return tokenizer, model


def pipe(tokenizer: PreTrainedTokenizerFast, model, config: Config, source_lang: str, target_lang: str) -> Pipeline:
    translator = pipeline('translation', model, tokenizer=tokenizer, src_lang=source_lang,tgt_lang=target_lang,
                          max_length=400, device=config.device, batch_size=config.batch_size)

    return translator
