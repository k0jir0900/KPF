# KPF
 Kernel Debuginfo Packet Finder

## Requisitos

- Python 3.x
- Bibliotecas adicionales: `pyfiglet`

## Instalación

1. Clonar el repositorio:

    ```bash
    git clone https://github.com/k0jir0900/KPF.git
    cd KPF
    ```
2. Instala las librerias faltantes con el siguiente comando:

    ```sh
    pip install -r requirements.txt
    ```


## Uso

Busqueda de Kernel unico :

```sh
python3 kernel_finder.py -k <version-kernel>
```

Busqueda de Kernel por listado :

```sh
python3 kernel_finder.py -f <archivo-kernel.txt>
```

## Ejemplos
### Busqueda de Kernel unico :

```sh
python3 kernel_finder.py -k ython3 kernel_finder.py -k 3.10.0-1160.119.1.el7.x86_64
 _  ______  _____
| |/ /  _ \|  ___|
| ' /| |_) | |_
| . \|  __/|  _|
|_|\_\_|   |_|


Kernel-debug Packet Finder

Searching kernel: 3.10.0-1160.119.1.el7.x86_64

+--------------+-----------------------------------------------------------------------------------------------------------------------
|              | Detail
+--------------+-----------------------------------------------------------------------------------------------------------------------
| Distribution | CentOS/RedHat
| Kernel Name  | kernel-debuginfo-3.10.0-1160.119.1.el7.x86_64.rpm
| URL          | http://debuginfo.centos.org/7/x86_64/kernel-debuginfo-3.10.0-1160.119.1.el7.x86_64.rpm
+--------------+-----------------------------------------------------------------------------------------------------------------------
```

### Busqueda de Kernel por listado :

info.txt
```sh
3.10.0-1160.119.1.el7.x86_64
4.15.0-213-generic
```

```sh
python3 kernel_finder.py -k ython3 kernel_finder.py -f info.txt
 _  ______  _____
| |/ /  _ \|  ___|
| ' /| |_) | |_
| . \|  __/|  _|
|_|\_\_|   |_|


Kernel-debug Packet Finder


Searching kernel: 3.10.0-1160.119.1.el7.x86_64
+--------------+-----------------------------------------------------------------------------------------------------------------------
|              | Detail
+--------------+-----------------------------------------------------------------------------------------------------------------------
| Distribución | CentOS/RedHat
| Kernel Name  | kernel-debuginfo-3.10.0-1160.119.1.el7.x86_64.rpm
| URL          | http://debuginfo.centos.org/7/x86_64/kernel-debuginfo-3.10.0-1160.119.1.el7.x86_64.rpm
+--------------+-----------------------------------------------------------------------------------------------------------------------

Searching kernel: 4.15.0-213-generic
+--------------+-----------------------------------------------------------------------------------------------------------------------
|              | Detail
+--------------+-----------------------------------------------------------------------------------------------------------------------
| Distribución | Ubuntu
| Kernel Name  | linux-image-unsigned-4.15.0-213-generic-dbgsym_4.15.0-213.224_amd64.ddeb
| URL          | http://ddebs.ubuntu.com/pool/main/l/linux/linux-image-unsigned-4.15.0-213-generic-dbgsym_4.15.0-213.224_amd64.ddeb
+--------------+-----------------------------------------------------------------------------------------------------------------------
```