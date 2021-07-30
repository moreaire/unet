from pyCHX.chx_packages import *
import numpy as np
import matplotlib.py

uid = '3c5a92f4'
sud = get_sid_filenames(db[uid])
for pa in sud[2]:
    if 'master.h5' in pa:
        data_fullpath = pa
uidstr = 'uid=%s'%uid
cmp_path = '/nsls2/xf11id1/analysis/Compressed_Data'
md = get_meta_data( uid )
md['detector'] =='eiger4m_single_image'
bin_frame_number = 1
force_compress = False #True   #force to compress data 
para_compress = True 
reverse= True
rot90= False
imgs = load_data( uid, md['detector'], reverse= reverse, rot90=rot90  )
Chip_Mask= np.array(np.load( '/XF11ID/analysis/2017_1/masks/Eiger4M_chip_mask.npy'), dtype=bool)
BadPix =     np.load('/XF11ID/analysis/2019_2/BadPix_4M.npy'  )  
Chip_Mask.ravel()[BadPix] = 0
pixel_mask =  1- np.int_( np.array( imgs.md['pixel_mask'], dtype= bool)  )
use_local_disk = True
mask_path = '/XF11ID/analysis/2019_3/masks/'
mask_name =  'Nov4_2019_4M_SAXS.npy'
mask = load_mask(mask_path, mask_name, plot_ =  False, image_name = uidstr + '_mask', reverse= reverse, rot90=rot90  ) 
mask =  np.ones(mask.shape)#mask * pixel_mask * Chip_Mask


cmp_file = '/uid_%s.cmp'%md['uid'] 
filename = cmp_path + cmp_file
mask2, avg_img, imgsum, bad_frame_list = compress_eigerdata(imgs,
                                                            mask,
                                                            md,
                                                            filename,
                                                            force_compress = force_compress,
                                                            para_compress= para_compress,
                                                            bad_pixel_threshold = 1e14,
                                                            reverse = reverse,
                                                            rot90 = rot90,
                                                            nobytes = 4,
                                                            bins = bin_frame_number,
                                                            num_sub = 100,
                                                            num_max_para_process = 500,
                                                            with_pickle = True,
                                                            direct_load_data = use_local_disk,
                                                            data_path = data_fullpath)
plt.imshow(avg_img)
plt.show()
np.save(f'{uid}_image_no_mask', avg_img)