import json
import sys

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


def main():
    with open('config.json') as config_file:
        data = json.load(config_file)

    source_lang = sys.argv[1]
    target_lang = sys.argv[2]

    cache_dir = data['cache_dir']
    model_name = data['model_name']
    device = data['device']
    batch_size = data['batch_size']

    tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir=cache_dir)

    translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang=source_lang,
                          tgt_lang=target_lang, max_length=400, device=device, batch_size=batch_size)

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
                                  tgt_lang=target_lang, max_length=400, device=device, batch_size=batch_size)
        else:
            result = translator(text)[0]['translation_text']
            print(result)


if __name__ == '__main__':
    sys.exit(main())
