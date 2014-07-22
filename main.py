# coding: utf-8

import hash_ring

if __name__ == "__main__":
    ip_list = ['10.1.15.10', '10.1.15.11', '10.1.15.12', '10.1.15.13', '10.1.15.14', '10.1.15.15']
    conhash_ring = hash_ring.HashRing(ip_list, 500) 
    
    '''
    uri = "/videos/v/20110926/205763500/205763500/1/f3a89defde4e580e4058149e9059d1d4.ts"
    conhash_value = conhash_ring.get_node(uri)        
    print uri
    print conhash_value
    
    uri = "/videos/v/20110926/205763500/205763500/2/c59965f441f474c6b0dfbe36232bd614.ts"
    conhash_value = conhash_ring.get_node(uri)        
    print uri
    print conhash_value
    '''    
    
    input_file = "./ts.list"
    the_file = open(input_file)
    while 1:        
        line = the_file.readline()
        if not line:
            break        
        line = line.strip("\n")
        line = line.strip("\r")
        if(len(line)>0):
            uri = line
            conhash_value = conhash_ring.get_node(uri)
            print '%s,%s' % (uri, conhash_value)
    