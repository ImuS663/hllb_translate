# hllb_translate

hllb_translate is a set command-line tools that allows you to quickly and efficiently translate text files and specific columns within CSV files using pre-trained machine translation models. This project leverages the power of Hugging Face Transformers.

## Key Features:

- **Supports diverse file formats:** Translate both plain text files and CSV files with ease.
- **Target multiple languages:** Choose from a range of supported languages for your translation needs.
- **Command-line interface:** Simple and intuitive command-line interface for easy use.
- **Progress visualization:** Track the translation progress with a visual indicator.

## Getting Started:

1. Install dependencies: `pip install transformers tqdm`
2. Run the script with appropriate arguments:
   1. Translate text file: `python translate_text_file.py input_file.txt source_lang_code target_lang_code`
   2. Translate CSV file: `python translate_csv_file.py input_file.csv column_number source_lang_code target_lang_code`
   3. Translate text: `python translate_text.py source_lang_code target_lang_code`

## License:

hllb_translate is licensed under the MIT License: `LICENSE`.

## Other 

This text is the result of a collaboration between a human and a machine learning model.