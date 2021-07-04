import os

pre = """
Developed by [ZeroIntensity](https://github.com/ZeroIntensity), under the MIT License.

"""

with open('README.md', 'w+') as f:
    f.write(pre)
    for i in os.listdir('./docs'):
        with open(f'./docs/{i}') as file:
            f.write(f'\n{file.read()}\n')
