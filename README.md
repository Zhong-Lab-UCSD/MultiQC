# Abstract
This modified version of MultiQC added modules named NuGEN_dedup and FCount_cus
- NuGEN_dedup:process the data of deduplication by using NuGEN set for the extracellular RNA project
- FCount_cus: Count the number of genes that appear 0-10 times, 10-100 times and greater then 100 times. 

# Modified files:
**setup.py** (~/MultiQC/setup.py) add 
- 'NuGEN_dedup = multiqc.modules.NuGEN_dedup:MultiqcModule' 
- 'FCount_cus = multiqc.modules.FCount_cus:MultiqcModule' 

to the entry_points section

**search_patterns.yaml**  (~/MultiQC/multiqc/utils/search_patterns.yaml)   add search pattern to the search_patterns.yaml. 

The format of output of NuGEN deduplication is *_dup_log.txt*
The format of output of FCount_cus is *.mergeCount*

```
NuGEN_dedup:
    fn: '*_dup_log.txt'
FCount_cus"
    fn:'*.mergeCount'
```

**config_defaults.yaml** (~/MultiQC/multiqc/utils/config_defaults.yaml)   add the module to the top of module_order in config_defaults.yaml
```
module_order:
    # MultiQC general module for catching output from custom scripts
    - 'custom_content'
    - NuGEN_dedup:
        module_tag:
            - RNA
    - FCount_cus:
        modeule_tag:
            - RNA
```

**README.md** (~/MultiQC/docs/README.md)   add the information of added module NuGEN_dedup and FCount_cus to the post-alignment section of README
```
Post-alignment:
    NuGEN_dedup: modules/NuGEN_dedup.md
    FCount_cus: modules/FCount_cus.md
```

# Added directory and files
**.md**
- NuGEN_dedup.md (~docs/modules/NuGEN_dedup.md) 
- FCount_cus.md** (~docs/modules/FCount_cus.md)

added explianation file under the directory of doc. No meaningful content in this file

**directory**
- NuGEN_dedup (~/MultiQC/multiqc/modules/NuGEN_dedup) 
- FCount_cus** (~/MultiQC/multiqc/modules/FCount_cus)

created directory under the directory of module. The name of directory should be the same as the name of module. This directory will hold the file of ```__init__.py``` and ```moduleName.py```.

**.py**
- NuGEN_dedup.py (~/MultiQC/multiqc/modules/NuGEN_dedup/NuGEN_dedup.py)   
- FCount.py (~/MultiQC/multiqc/modules/FCount_cus/FCount_cus.py) 

The main program for add data to general stats and add section to the multiQC report. Name should be the same as the name of module

**__init__.py** 
- (~/MultiQC/multiqc/modules/NuGEN_dedup/__init__.py)   
- (~/MultiQC/multiqc/modules/FCount_cus/__init__.py)

import all the modules that provided by MultiQC. Also creates the entry point for our module

Cuerrent MultiQC contains following tools. 

[NuGEN_dedup]:
[adapterremoval]: http://multiqc.info/docs/#adapter-removal
[afterqc]:        http://multiqc.info/docs/#afterqc
[bamtools]:       http://multiqc.info/docs/#bamtools
[bbmap]:          http://multiqc.info/docs/#bbmap
[bcftools]:       http://multiqc.info/docs/#bcftools
[bcl2fastq]:      http://multiqc.info/docs/#bcl2fastq
[biobloomtools]:  http://multiqc.info/docs/#biobloom-tools
[bismark]:        http://multiqc.info/docs/#bismark
[bowtie-1]:       http://multiqc.info/docs/#bowtie-1
[bowtie-2]:       http://multiqc.info/docs/#bowtie-2
[busco]:          http://multiqc.info/docs/#busco
[clusterflow]:    http://multiqc.info/docs/#cluster-flow
[conpair]:        http://multiqc.info/docs/#conpair
[cutadapt]:       http://multiqc.info/docs/#cutadapt
[disambiguate]:   http://multiqc.info/docs/#disambiguate
[fastq-screen]:   http://multiqc.info/docs/#fastq-screen
[fastqc]:         http://multiqc.info/docs/#fastqc
[featurecounts]:  http://multiqc.info/docs/#featurecounts
[flexbar]:        http://multiqc.info/docs/#flexbar
[gatk]:           http://multiqc.info/docs/#gatk
[goleft]:         http://multiqc.info/docs/#goleft-indexcov
[hicexplorer]:    http://multiqc.info/docs/#hicexplorer
[hicup]:          http://multiqc.info/docs/#hicup
[hisat2]:         http://multiqc.info/docs/#hisat2
[homer]:          http://multiqc.info/docs/#homer
[htseq]:          http://multiqc.info/docs/#htseq
[jellyfish]:      http://multiqc.info/docs/#jellyfish
[interop]:        http://multiqc.info/docs/#interop
[kallisto]:       http://multiqc.info/docs/#kallisto
[leehom]:         http://multiqc.info/docs/#leehom
[macs2]:          http://multiqc.info/docs/#macs2
[methylqa]:       http://multiqc.info/docs/#methylqa
[peddy]:          http://multiqc.info/docs/#peddy
[picard]:         http://multiqc.info/docs/#picard
[preseq]:         http://multiqc.info/docs/#preseq
[prokka]:         http://multiqc.info/docs/#prokka
[qorts]:          http://multiqc.info/docs/#qorts
[qualimap]:       http://multiqc.info/docs/#qualimap
[quast]:          http://multiqc.info/docs/#quast
[rna_seqc]:       http://multiqc.info/docs/#rna_seqc
[rsem]:           http://multiqc.info/docs/#rsem
[rseqc]:          http://multiqc.info/docs/#rseqc
[salmon]:         http://multiqc.info/docs/#salmon
[samblaster]:     http://multiqc.info/docs/#samblaster
[samtools]:       http://multiqc.info/docs/#samtools
[sargasso]:       http://multiqc.info/docs/#sargasso
[skewer]:         http://multiqc.info/docs/#skewer
[slamdunk]:       http://multiqc.info/docs/#slamdunk
[snpeff]:         http://multiqc.info/docs/#snpeff
[sortmerna]:      http://multiqc.info/docs/#sortmerna
[star]:           http://multiqc.info/docs/#star
[supernova]:      http://multiqc.info/docs/#supernova
[theta2]:         http://multiqc.info/docs/#theta2
[tophat]:         http://multiqc.info/docs/#tophat
[trimmomatic]:    http://multiqc.info/docs/#trimmomatic
[vcftools]:       http://multiqc.info/docs/#vcftools
[verifyBAMID]:    http://multiqc.info/docs/#verifybamid
