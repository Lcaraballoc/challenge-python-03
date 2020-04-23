import re


def run():
    with open('src/encoded.txt', 'r', encoding='utf-8') as f:
        secret_message = f.read()
        
    m = re.findall('[a-z]', secret_message)
    print(''.join(m))


if __name__ == '__main__':
    run()
