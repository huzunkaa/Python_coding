# encoding: utf-8
'''
@author:Huzunkai
@name:00.jellfish_shell.py.py
@time: 05/16/2023 17:26
@description:制作jellyfish软件批量基因组kmer化的shell脚本
'''
import re
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_path2file", help="", dest="path2file", type=str, default="None")
parser.add_argument("-bar", "--inut_bar2name", help="", dest="inut_bar2name", type=str, default="None")
args = parser.parse_args()
path2file = args.path2file
inut_bar2name = args.inut_bar2name

os.system(f'mkdir /data2/Yixue/huzunkai/develop/01.multi_dPCR/01.database/02.Kle_kmer/00.progress')
os.system(f'mkdir /data2/Yixue/huzunkai/develop/01.multi_dPCR/01.database/02.Kle_kmer/01.result')

#####命令准备区#####
file_process = open('/data2/Yixue/huzunkai/develop/01.multi_dPCR/01.database/process.file','r')
f_pro = file_process.readline()
f_pro = f_pro.replace('\n','')
str3_1 = f_pro
#######finish######

#####shell脚本#####
filew = open('/data2/Yixue/huzunkai/develop/01.multi_dPCR/03.Script/x1_Kle_shell/01.make_kmer.sh','w')
#######finish######

#####正式运行区#####
file = open(f'/data2/Yixue/huzunkai/develop/01.multi_dPCR/01.database/Kle.list','r')
f = file.readlines()
for i in f:
    i = i.replace('\n','')
    ii = re.split('\t',i)

    str1 = f'/data/Yixue/huzunkai/develop/02.Prejoct/09.wuzhongguishu/04.kmer/jellyfish-2.3.0/bin/jellyfish count -m 30 -s 100M -t 4 -o /data2/Yixue/huzunkai/develop/01.multi_dPCR/01.database/02.Kle_kmer/00.progress/{ii[0]} -c 7 /data2/Yixue/huzunkai/develop/01.multi_dPCR/01.database/01.Kle/{ii[1]}'
    str2 = f'/data/Yixue/huzunkai/develop/02.Prejoct/09.wuzhongguishu/04.kmer/jellyfish-2.3.0/bin/jellyfish dump -c -t -U 1000 /data2/Yixue/huzunkai/develop/01.multi_dPCR/01.database/02.Kle_kmer/00.progress/{ii[0]} > /data2/Yixue/huzunkai/develop/01.multi_dPCR/01.database/02.Kle_kmer/00.progress/{ii[0]}_30mer.fa'
    str3_2 = f'/data2/Yixue/huzunkai/develop/01.multi_dPCR/01.database/02.Kle_kmer/00.progress/{ii[0]}_30mer.fa'
    str3_3 = f'> /data2/Yixue/huzunkai/develop/01.multi_dPCR/01.database/02.Kle_kmer/01.result/{ii[0]}_30mer.format.fa'
    str3 = str3_1+str3_2+str3_3
    filew.write('%s\n%s\n%s\n'%(str1,str2,str3))
    filew.write('\n')
