from download_pdf.download_pipeline import pdf_download_pipeline
from download_pdf.downloaded_obj import DownloadedObj
import os
import json
from .doi_to_metadata import metaDict_to_metaObj


def meta_to_dwnldd(metadataObj, output_dir):
    """
    @Param metdataObj metadata object will be used to download the pdf
    @Param output_dir output directory to where the pdf will be downloaded
    ----
    :returns
    downloaded Object, which has a filename and filepath
    """
    # takes metadata and downloads the pdf
    if not metadataObj:
        return None
    try:
        file_path = pdf_download_pipeline(doi=metadataObj.doi,output_directory=output_dir)
        file_name = os.path.basename(file_path)
        return DownloadedObj(title=metadataObj.title,doi=metadataObj.doi,arxiv=metadataObj.arxiv,file_name=file_name,file_path=file_path)
    except:
        print("Error while creating the downloaded object")
        return None


def dwnldd_dictionary(dwnldd_obj):
    return {dwnldd_obj.doi: dwnldd_obj.to_dict()}


def downloadedDic_to_downloadedObj(dwnldd_dict):
    title = safe_dic(dwnldd_dict, "title")
    doi = safe_dic(dwnldd_dict, "doi")
    arxiv = safe_dic(dwnldd_dict, "arxiv")
    file_name = safe_dic(dwnldd_dict,"file_name")
    file_path = safe_dic(dwnldd_dict,"file_path")
    return DownloadedObj(title=title, doi=doi, arxiv=arxiv, file_name=file_name, file_path=file_path)


def metaDict_to_downloaded(meta_dict, output_dir):
    meta = metaDict_to_metaObj(meta_dict)
    return meta_to_dwnldd(metadataObj=meta, output_dir=output_dir)


def metaJson_to_downloaded_dic(meta_json, output_dir):
    result = {}
    try:
        with open(meta_json, 'r') as f:
            metas_dict = json.load(f)
    except Exception as e:
        print(str(e) + "Error while opening metadata json")
    for doi in metas_dict:
        meta_dict = safe_dic(metas_dict,doi)
        dwnObj = metaDict_to_downloaded(meta_dict=meta_dict, output_dir= output_dir)
        result.update({dwnObj.doi: dwnObj.to_dict()})
    return result

def metaJson_to_downloadedJson(meta_json, output_dir):
    dict = metaJson_to_downloaded_dic(meta_json, output_dir)
    output_path = output_dir + "/" + "downloaded_metadata.json"
    with open(output_path, 'w+') as out_file:
        json.dump(dict, out_file, sort_keys=True, indent=4,
                  ensure_ascii=False)
    return output_path


def safe_dic(dic, key):
    try:
        return dic[key]
    except:
        return None