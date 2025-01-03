import urllib.request
import numpy as np
import multiprocessing
from functools import partial


scale = 0.262
height = 512
width = 512

iamge_dir = "jpg_c/"
data_table = "gz_decals_volunteers_c.csv"


def images_url(RA, DEC, scale, height, width, i):
    str1 = "https://www.legacysurvey.org/viewer/jpeg-cutout?layer=dr8&bands=grz"
    str2 = "&ra={:f}&dec={:f}&pixscale={:f}&width={:d}&height={:d}".format(
        RA[i], DEC[i], scale, height, width
    )
    try:
        urllib.request.urlretrieve(
            str1 + str2, iamge_dir + str(i).rjust(6, "0") + ".jpg"
        )
    except:
        pass
        print(i)


radeg, decdeg = np.genfromtxt(
    data_table, skip_header=1, usecols=(1, 2), delimiter=",", unpack=True
)


# Multi-threading here
def main():
    iterable = np.arange(0, len(radeg), 1)
    pool = multiprocessing.Pool(8)
    func = partial(images_url, radeg, decdeg, scale, height, width)
    pool.map(func, iterable)
    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
