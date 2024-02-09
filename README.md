# hllb_translate

hllb_translate is a set command-line tools that allows you to quickly and efficiently translate text files and specific columns within CSV files using pre-trained machine translation models. This project leverages the power of Hugging Face Transformers.

## Key Features:

- **Supports diverse file formats:** Translate both plain text files and CSV files with ease.
- **Target multiple languages:** Choose from a range of supported languages for your translation needs.
- **Configurable settings:** Customize the translation process through a JSON configuration file.
- **Command-line interface:** Simple and intuitive command-line interface for easy use.
- **Progress visualization:** Track the translation progress with a visual indicator.

## Getting Started:

1. Install dependencies: `pip install transformers tqdm`
2. Configure `config.json` with your desired settings (model name, languages, etc.).
3. Run the script with appropriate arguments:
   1. Translate text file: `python translate_text_file.py input_file.txt source_lang_code target_lang_code`
   2. Translate CSV file: `python translate_csv_file.py input_file.csv column_number source_lang_code target_lang_code`
   3. Translate text: `python translate_text.py source_lang_code target_lang_code`

### Config:

```json
{
    "cache_dir": ".cache", 
    "model_name": "facebook/nllb-200-distilled-600M",
    "device": "cuda",
    "batch_size": 16,
    "output_dir": "output"
}
```
`cache_dir`: any directory witch sufficient empty space;

`model_name`: any translate model with [Hugging Face](https://huggingface.co/models?other=translation);

`device`: `cpu` or `cuda`;

`batch_size`: up speed translate at the expense of batched text, requires additional RAM and GPU memory;

`output_dir`: any convenient directory.

## License:

hllb_translate is licensed under the MIT License: `LICENSE`.

## Other 

This text is the result of a collaboration between a human and a machine learning model.