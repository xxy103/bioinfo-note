'''https://github.com/StructureFold2/StructureFold2/blob/master/sam_filter.py'''
import subprocess
def get_samtools_version():
    '''Gets the current version of samtools in the path'''
    procced_info = subprocess.Popen('samtools', shell=True, stdin=subprocess.PIPE, 
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True).stdout.read()
    info_lines = procced_info.decode('utf8').split('\n')
    target_line = info_lines[2]
    return target_line
	#return float('.'.join(target_line.split()[1].split('.')[0:2]))

#get_samtools_version()



def get_bowtie2_version():
    '''Gets the current version of bowtie2 in the path'''
    procced_info = subprocess.Popen('bowtie2', shell=True, stdin=subprocess.PIPE, 
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True).stdout.read()
    info_lines = procced_info.decode('utf8').split('\n')
    target_line = info_lines[1] # line 1
    return target_line

get_bowtie2_version()


def get_star_version():
    '''Gets the current version of STAR in the path'''
    procced_info = subprocess.Popen('STAR --version', shell=True, stdin=subprocess.PIPE, 
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True).stdout.read()
    info_lines = procced_info.decode('utf8').split('\n')
    target_line = info_lines[0]
    return target_line

get_star_version()


gef get_star_version2():
    '''Gets the current version of STAR in the path'''
    procced_info = subprocess.Popen('STAR', shell=True, stdin=subprocess.PIPE, 
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True).stdout.read()
    info_lines = procced_info.decode('utf8').split('\n')
    target_line = info_lines[3]
    return target_line

get_star_version2()


def get_cutadapt_version():
    '''Gets the current version of cutadapt in the path'''
    procced_info = subprocess.Popen('cutadapt --version', shell=True, stdin=subprocess.PIPE, 
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True).stdout.read()
    info_lines = procced_info.decode('utf8').split('\n')
    target_line = info_lines[0]
    return target_line

get_cutadapt_version()





