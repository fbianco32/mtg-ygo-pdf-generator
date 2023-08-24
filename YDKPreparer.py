import math
import os

script_dir = os.path.dirname(__file__)

with open(script_dir + '/output/ygoInput.txt', 'w') as outfile:
    for fname in os.listdir(script_dir + "/ydkInput"):
        with open(script_dir + "/ydkInput/" + fname) as infile:
            for line in infile:
                if(line.strip('\n').isnumeric()):
                    outfile.write(line)