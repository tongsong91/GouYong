#!-*- coding:utf-8 -*-
LIBDIR = 'lib'
#DEFAULT = 'langdao-ec-gb'
DEFAULT = 'lazy-dict'
import gc
import sys
import os.path
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..',LIBDIR))
from pystardict import Dictionary
SUFFIX=['.oft','.gz','.dz']
DICTDIR = os.path.join(sys.prefix,'share','GouYong','dict')
import log
logger = log.get_logger(__name__)

class DictManager():
    def __init__(self):
        self.current_dict_name = DEFAULT
        self.dir = DICTDIR
        walk = os.walk(self.dir)
        self.dicts = walk.next()[1]
        self.dict = None
        logger.info(self.dicts)

    def open_dict(self):
        self.dict_dir = os.path.join(self.dir,self.current_dict_name)
        dict_name=''
        for file in os.listdir(self.dict_dir):
            name,suffix=os.path.splitext(file)
            if suffix in SUFFIX:
                continue
            if dict_name and dict_name != name:
                logger.error("dict broken!")
                return False
            dict_name = name
        #dict dir name maybe not the dict file name.
        del self.dict
        gc.collect()
        self.dict = Dictionary(os.path.join(self.dict_dir,dict_name))
        logger.info("载入%s",os.path.join(self.dict_dir,dict_name))
        
    def change_dict(self,dict_name):
        self.current_dict_name = dict_name
        self.open_dict()


def main():
    d=DictManager()
    d.open_dict()

if __name__=="__main__":
    main()
    #for dict in d.dicts:
        #d.change_dict(dict)
