from metadata_extraction.paper_obj import PaperObj

def paperDict_to_paperObj(paper_dict):
    title = safe_dic(paper_dict, "title")
    doi = safe_dic(paper_dict, "doi")
    arxiv = safe_dic(paper_dict, "arxiv")
    file_name = safe_dic(paper_dict,"file_name")
    file_path = safe_dic(paper_dict,"file_path")
    urls = safe_dic(paper_dict,"urls")
    return PaperObj(title=title, doi=doi, arxiv=arxiv, file_name=file_name, file_path=file_path, urls=urls)


def safe_dic(dic, key):
    try:
        return dic[key]
    except:
        return None