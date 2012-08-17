import os
import re

path = 'cars/2007'
out_path = '../Reviews'
new_path = '../2007'

def create_reviews(path,out_path,new_path,tag=True):
    listing = os.listdir(path)
    os.chdir(path)

    for infile in listing:
        out_filename = infile+"_reviews"

        if '.swp' in infile:
            continue

        f_in = open(infile,'r')
        os.chdir(out_path)
        f_out = open(out_filename,'w')

        if tag:
            for line in f_in:
                m = re.search('<FAVORITE>',line)
                if m:
                    end_pos=line.find('</FAVORITE>')
                    review = line[10:end_pos]+"\n\n"
                    f_out.write(review)
            os.chdir(new_path)
        else:
            for line in f_in:
                f_out.write(line)
            os.chdir(new_path)

        f_in.close()
        f_out.close()

#create_reviews('cars/2007','../Reviews','../2007')
#create_reviews('../2008','../Reviews','../2008')
#create_reviews('../2009','../Reviews','../2009')

#os.chdir('../..')
create_reviews('hotels/beijing','../Reviews','../beijing',False)
create_reviews('../chicago','../Reviews','../chicago',False)
create_reviews('../dubai','../Reviews','../dubai',False)
create_reviews('../las-vegas','../Reviews','../las-vegas',False)
create_reviews('../london','../Reviews','../london',False)
create_reviews('../montreal','../Reviews','../montreal',False)
create_reviews('../new-delhi','../Reviews','../new-delhi',False)
create_reviews('../new-york-city','../Reviews','../new-york-city',False)
create_reviews('../san-francisco','../Reviews','../san-francisco',False)
create_reviews('../shanghai','../Reviews','../shanghai',False)

    
