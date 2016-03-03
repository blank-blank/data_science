#=========================================================================
# Purpose: Boulder Data Sceince -> Execute kaggle data science bowl model 
#           on gpu instance  -> AWS
# Date: 20160302
# Author: Tim Lewis
#=========================================================================


import argparse

import boto3


#launch the instance


#boto3 resource

#create images with params




#do the things



#run the model

#============================================================

def test():

    #test requirements...will be done by calling the script, so just let it happen.

    #This function will not call anything that writes to anything else.  Output only
    pass

#=========================================================================
def main():

    #============================================================


    def start_gpu_machine(ami_id, instance_type, kp_name): 
        '''
        create a gpu aws machine running ubuntu
        '''
        ec2 = boto3.resource('ec2', 'us-west-1')


  

        #start gpu instance        
        instances = ec2.create_instances(ImageId=ami_id, MinCount=1, MaxCount=1, KeyName=kp_name, InstanceType=instance_type)

        return instances

    #============================================================

    instance_type = 'g2.2xlarge'
    ami_id = 'ami-1d689c59' #ubuntu 14.04 lts
    kp_name = 'bds_kaggle_cal'
 




    #spin up instance and print it
    instances = start_gpu_machine(ami_id, instance_type, kp_name) 
    print 'creating instance in us-west-1 with ami: %s; instance_type: %s; kp_name: %s' %(ami_id, instance_type, kp_name)

    print instances[0].instance_id

    
    



    


   

#=========================================================================

if __name__ == '__main__':
    main()
