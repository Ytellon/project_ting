from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    def_list = list()
    queue_list = instance.list
    for files in queue_list:
        ocurrencies_list = list()
        for index, line in enumerate(files["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                ocurrencies_list.append({"linha": index})
        if len(ocurrencies_list) > 0:
            def_list.append({
                "palavra": word,
                "arquivo": files["nome_do_arquivo"],
                "ocorrencias": ocurrencies_list
            })
    return def_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
