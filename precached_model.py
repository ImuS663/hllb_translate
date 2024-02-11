import sys
import read_config
import transformer


def main():
    model_name = sys.argv[1]

    config = read_config.read('config.json')
    
    print('Start load:', model_name)

    transformer.load_model(config)

    input('Load completed, press any key...')


if __name__ == '__main__':
    sys.exit(main())
