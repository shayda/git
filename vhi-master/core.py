import upload
import sys
import os
import glob
import pandas
pandas.set_option('max_rows', 100)

regions = {}
with open("reg.txt") as f:
	for line in f:
		(key, val) = line.split(':')
		regions[int(key)] = val

regions_new = {}
with open("reg2.txt") as f:
	for line in f:
		(key, val) = line.split(':')
		regions_new[int(key)] = val

def get_data_frame():
	#for i in range(1,28):
	#upload.upload_vhi_data_by_region_id(i)
	
	matches = []
	for k_, v_ in regions.items():
		for k, v in regions_new.items():
			if v==v_:
				matches.append(k)
				break

	path = 'uploads/*.csv'
	files=sorted(glob.glob(path), key=os.path.getmtime)
	i=0
	res = pandas.DataFrame(columns=['Year','Week','SMN','SMT','VCI','TCI','VHI','Less 15','Less 35','Region'])
	for f in files:
		df = pandas.read_csv(f, header=1, index_col=False, names=['Year','Week','SMN','SMT','VCI','TCI','VHI','Less 15','Less 35'])
		df['Region'] = matches[i]
		i+=1
		res = res.append(df, ignore_index=True)
	
	return res


def select_vhi_by_region_and_year(id, year):
	v = get_data_frame()
	print "Series for"+regions_new[id]+"region, year "+str(year)+"\n";
	print v[['Week','VHI']][(v['Year']==year) & (v['Region']==id)]
	minid = v['VHI'][(v['Year']==year) & (v['Region']==id)].idxmin()
	maxid = v['VHI'][(v['Year']==year) & (v['Region']==id)].idxmax()
	print "Minimum: "
	print v.loc[minid]
	print "Maximum: "
	print v.loc[maxid]


def select_years_with_extreme_vhi_by_area_percent(id, percent):
	v = get_data_frame()
	print "Extreme conditions for"+regions_new[id]+"region, with percent of area >"+str(percent)
	print v[['Year','Week','VHI','Less 15']][(v['Region']==id) & (v['Less 15']>percent)]

select_vhi_by_region_and_year(1,2000)
select_years_with_extreme_vhi_by_area_percent(1,7.0)
