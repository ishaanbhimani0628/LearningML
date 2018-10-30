#Import Data Modules for Different Types of Data
import os
import tarfile
from six.moves import urllib

def fetch_from_url_tgz(data_url, data_path, name):
    '''

    :param data_url: where the data is coming from
    :param data_path: where saving the data
    :return: none
    '''
    if not os.path.isdir(data_path):
        os.mkdirs(data_path)#make directory if needed, makes from working directory if not specified?
    tgz_path = os.path.join(data_path, name+".tgz")
    urllib.request.urlretrieve(data_url,tgz_path)#get the data
    data_tgz = tarfile.open(tgz_path)#get tarfile to extract to csv
    data_tgz.extractall(path = data_path)#extract to csv
    data_tgz.close()