from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance: Queue):
    file_lines = txt_importer(path_file)
    dict_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines
    }
    if dict_file not in instance.list:
        instance.enqueue(dict_file)
        sys.stdout.write(f"{dict_file}")


def remove(instance: Queue):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        saved_dequeue = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(f"Arquivo {saved_dequeue} removido com sucesso\n")


def file_metadata(instance: Queue, position):
    try:
        sys.stdout.write(f"{instance.search(position)}\n")
    except IndexError:
        sys.stderr.write("Posição inválida\n")
