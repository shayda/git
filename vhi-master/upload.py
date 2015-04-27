# upload script by Jenia Grubian, 12.02.15 
import urllib2
from datetime import datetime

def upload_vhi_data_by_region_id(id):
	url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R"+str(id).zfill(2)+".txt"
	vhi_url = urllib2.urlopen(url)
	out = open('uploads/vhi_id_'+str(id)+'_'+datetime.now().strftime('%Y-%m-%d_%H:%M:%S')+'.csv','w')
	out.write(vhi_url.read())
	out.close()
	print "vhi_id_"+str(id)+'_'+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+".csv is downloaded..."

