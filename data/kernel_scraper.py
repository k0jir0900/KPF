import requests
from bs4 import BeautifulSoup
import json
import argparse
from tqdm import tqdm
import os
from urllib.parse import urlparse

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'

allowed_architectures = [
    'i386'
    ,'x86'
    ,'amd64'
    ,'x86_64'
]

exclude_words = [
    "common"
]

with open('data/kernel_repo.json', 'r') as file:
    kernel_repo = json.load(file)

with open('data/distributions.json', 'r') as file:
    distributions = json.load(file)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_distribution_from_url(url):
    domain = urlparse(url).netloc
    for key in distributions:
        if key in domain:
            return distributions[key]
    return 'Unknown'

def fetch_kernel_debuginfo(url, search_pattern, user_agent):
    headers = {
        'User-Agent': user_agent
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error al acceder a la URL {url}: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a')

    kernel_files = []

    for link in links:
        href = link.get('href')
        if href and search_pattern in href:
            if any(arch in href for arch in allowed_architectures) and not any(word in href for word in exclude_words):
                kernel_files.append({
                    "distribucion": get_distribution_from_url(url),
                    "kernel_name": href.split('/')[-1],
                    "url": url + href
                })

    return kernel_files

def main(output_file=None, user_agent=user_agent):
    all_kernel_files = []

    kernel_repo_items = list(kernel_repo.items())
    with tqdm(total=len(kernel_repo_items), desc="Updating kernel list", unit="URL") as pbar:
        for url_base, search_pattern in kernel_repo_items:
            kernel_files = fetch_kernel_debuginfo(url_base, search_pattern, user_agent)
            all_kernel_files.extend(kernel_files)
            pbar.update(1)

    total_kernels = len([kf for kf in all_kernel_files if 'kernel_name' in kf])

    if total_kernels == 0:
        print("No se encontraron archivos que contengan los patrones especificados y arquitecturas permitidas.")
        return

    kernels_by_distribution = {}
    for kernel in all_kernel_files:
        distrib = kernel['distribucion']
        kernels_by_distribution[distrib] = kernels_by_distribution.get(distrib, 0) + 1

    print(f"\n{total_kernels} kernels were identified\n")

    if output_file:
        with open(output_file, 'w') as f:
            json.dump(all_kernel_files, f, indent=4)
    else:
        print(json.dumps(all_kernel_files, indent=4))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scraper de archivos Kernel')
    parser.add_argument('-o', '--output', help='Archivo de salida para guardar los resultados en formato JSON')

    args = parser.parse_args()

    main(output_file=args.output)