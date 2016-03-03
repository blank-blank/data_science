#=======================================================================
# set up the machine to run kaggle comp model on gpu instance in AWS ec2
# goal: start an EC2 instance from AWS, load a model on the instance 
# kaggle competition for BDS
# Author: Tim Leiws
#=======================================================================
import sys
import os
import pip
#import do_gpu_model


def install(package):
    '''
    install specified package using pip
    '''
    pip.main(['install', package])


def test_dependencies_installed():

    try:
        import boto3
    except:

        install('boto3')

import pip


    #todo: need boto3 at least, maybe ansible, maybe paramiko?

    




def main():

        
    '''
    desc:
        run an instance on aws with boto3
    req: 
        keras -> theano -> gpu -> aws -> boto3 -> pip
    '''

    #================================================
    def ensure_root_user():

        if not(os.getuid() == 0):
        
            sys.exit('Must be root to run this script')


         
    #================================================

    

    ensure_root_user()
    


     
    #ensure dependencies are installed on this machine 
    test_dependencies_installed()
    
if __name__ == '__main__':
    main()
