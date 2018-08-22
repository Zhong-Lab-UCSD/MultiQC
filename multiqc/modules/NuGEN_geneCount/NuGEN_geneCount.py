#!/usr/bin/env python

""" MultiQC module to parse output from FastQC
"""
from __future__ import print_function
#from __future__ import absolute_import
from collections import OrderedDict
import logging
import re
import csv

from multiqc import config
from multiqc.plots import bargraph
from multiqc.modules.base_module import BaseMultiqcModule

# Initialise the logger
log = logging.getLogger(__name__)

class MultiqcModule(BaseMultiqcModule):

    def __init__(self):
        super(MultiqcModule, self).__init__(name='NuGEN_geneCount',
        anchor='NuGEN_geneCount',
        href='sysbio.ucsd.edu',
        info="is a tool for counting genes")

        self.FCount_data = dict()
        self.FCount_keys = list()

        for f in self.find_log_files('NuGEN_geneCount'):
            fileName = f['s_name'][:-11]
            if fileName in self.FCount_data:
                log.debug("Duplicate sample name found! Overwriting: {}".format(f['s_name'][:-11]))
                self.FCount_data = self.parse_FCount_report(f['f'])
                #self.FCount_keys = self.FCount_data.keys()
		#self.FCount_keys = list(self.FCount_data[fileName].keys())
        if len(self.FCount_data) == 0:
                raise UserWarning

        log.info("Found {} reports".format(len(self.FCount_data)))

        #output stats file
        self.write_data_file(self.FCount_data, 'multiqc_geneCount_cus')

        #add col to general stats table
        self.FCount_stats_table()

    def parse_FCount_report(self,f):
        """Parse the mergeCount table"""
        parsed_data = dict()
        #infoList = []

        next(f)
        for l in f.splitlines():
            s = l.split()
            if len(s) != 4:
                return "Incomplete table"
            fileName = s[0]
            count_info = dict()
            count_info["counts > 0"] = s[1]
            count_info["counts > 10"] = s[2]
            count_info["counts > 100"] = s[2]
            
            parsed_data[filename] = count_info
            #infoList.append(fileName)

        return parsed_data

    def FCount_stats_table(self):
        headers = OrderedDict()
        headers['count > 0'] = {
            'title':'count > 0',
            'description':'Count the genes that appear one or more times after the NuGEN deduplication process',
            'scale': 'RdBu'
        }
        headers['count > 0'] = {
            'title':'count > 10',
            'description':'Count the genes that appear ten or more times after the NuGEN deduplication process',
            'scale': 'RdBu',
            'hidden': True
        }
        headers['count > 0'] = {
            'title':'count > 100',
            'description':'Count the genes that appear one hundred or more times after the NuGEN deduplication process',
            'scale': 'RdBu',
            'hidden': True
        }
        self.general_stats_addcols(self.dedup_data,headers)

