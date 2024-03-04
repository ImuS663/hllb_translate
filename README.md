# hllb_translate

hllb_translate is a set command-line tool that allows you to quickly and efficiently translate text files and specific columns within CSV files using pre-trained machine translation models. This project leverages the power of Hugging Face Transformers.

## Key Features:

- **Supports diverse file formats:** Translate both plain text files and CSV files with ease.
- **Target multiple languages:** Choose from a range of supported languages for your translation needs.
- **Command-line interface:** Simple and intuitive command-line interface for easy use.
- **Progress visualization:** Track the translation progress with a visual indicator.

## Getting Started:

1. Install dependencies: `pip install transformers torch tqdm click`
2. Run the script with appropriate arguments: `py translate.py [OPTIONS] COMMAND [ARGS]...`

## Help

### translate:

```bash
Usage: translate.py [OPTIONS] COMMAND [ARGS]...

  Translate CLI

Options:
  --help  Show this message and exit.

Commands:
  csv    Translate csv file.
  langs  Print all supported languages.
  text   Translate string.
  txt    Translate txt file.
  ```

### translate csv :

```bash
Usage: translate.py csv [OPTIONS] FILENAME COLUMN SOURCE TARGET

  Translate csv file.

  FILENAME is the path to target file.

  COLUMN is the number to target column.

  SOURCE is the Source Language

  TARGET is the Target Language

Options:
  -b, --batch-size INTEGER  Change batch size.  [default: 6]
  -c, --cache-dir PATH      Change cache dir  [default: .cache]
  -d, --device [CPU|CUDA]   Choose device.  [default: CPU]
  -o, --output-dir PATH     Change output dir  [default: output]
  --help                    Show this message and exit.
```

### translate langs:

```bash
Usage: translate.py langs [OPTIONS]

  Print all supported languages.

Options:
  -f, --find TEXT  Find language.
  --help           Show this message and exit.
```

### translate txt:

### translate text:

```bash
Usage: translate.py text [OPTIONS] SOURCE TARGET

  Translate string.

  SOURCE is the Source Language

  TARGET is the Target Language

Options:
  -c, --cache-dir PATH     Change cache dir  [default: .cache]
  -d, --device [CPU|CUDA]  Choose device.  [default: CPU]
  --help                   Show this message and exit.
```

```bash
Usage: translate.py txt [OPTIONS] FILENAME SOURCE TARGET

  Translate txt file.

  FILENAME is the path to target file.

  SOURCE is the Source Language

  TARGET is the Target Language

Options:
  -b, --batch-size INTEGER  Change batch size.  [default: 6]
  -c, --cache-dir PATH      Change cache dir  [default: .cache]
  -d, --device [CPU|CUDA]   Choose device.  [default: CPU]
  -o, --output-dir PATH     Change output dir  [default: output]
  --help                    Show this message and exit.
```

## License:

hllb_translate is licensed under the MIT License: `LICENSE`.

## Other 

This text is the result of a collaboration between a human and a machine learning model.