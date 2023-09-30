## Insatallar dependencias
```bash
pip install -r requirements.txt

```


## Ejecutar un spider de Scrapy:

```bash
scrapy runspider tu_spider.py -o archivo_salida.csv -t csv --set CLOSESPIDER_ITEMCOUNT=X
```

- `tu_spider.py`: Sustituye esto con el nombre del archivo que contiene tu spider (en este caso, sería `claro.py`).

- `-o archivo_salida.csv`: Especifica el nombre del archivo de salida donde se almacenarán los datos raspados. Puedes cambiar `archivo_salida.csv` al nombre que desees para tu archivo de salida.

- `-t csv`: Indica el formato en el que deseas guardar los datos raspados. En este caso, estamos utilizando CSV como formato de salida.

- `--set CLOSESPIDER_ITEMCOUNT=X`: Esto es opcional, pero puedes usarlo para limitar la cantidad de elementos que se raspan. Reemplaza `X` con el número deseado de elementos. Si no deseas limitar la cantidad, simplemente omite esta parte del comando.

## Selenium

[Link](https://selenium-python.readthedocs.io/getting-started.html)
