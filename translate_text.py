import json
import sys

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

import read_config


def main():
    source_lang = sys.argv[1]
    target_lang = sys.argv[2]

    config = read_config.read('config.json')

    tokenizer = AutoTokenizer.from_pretrained(config.model_name, cache_dir=config.cache_dir)
    model = AutoModelForSeq2SeqLM.from_pretrained(config.model_name, cache_dir=config.cache_dir)

    translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang=source_lang,
                          tgt_lang=target_lang, max_length=400, device=config.device, batch_size=config.batch_size)

    is_exit = False

    while not is_exit:
        text = input('Enter text: ')

        if text == 'exit()':
            is_exit = True
            print('Exit!')
        elif text == 'change_lang()':
            source_lang = input('Enter source: ')
            target_lang = input('Enter target: ')

            translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang=source_lang,
                                  tgt_lang=target_lang, max_length=400, device=config.device,
                                  batch_size=config.batch_size)
        else:
            result = translator(text)[0]['translation_text']
            print(result)


if __name__ == '__main__':
    sys.exit(main())
