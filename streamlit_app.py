import ephem
import matplotlib.pyplot as plt
import os
from datetime import datetime as dt
from datetime import timedelta as td
from matplotlib.animation import ArtistAnimation #アニメーション作成用
from mpl_toolkits.basemap import Basemap #世界地図描画用
line1 = 'QZS-4 (MICHIBIKI-4)'
line2 = '1 42965U 17062A   22057.72757807 -.00000328  00000-0  00000-0 0  9995'
line3 = '2 42965  40.7914   3.5343 0749421 269.5117 284.1873  1.00283299 16058'
epoch_date = "22057.72757807" 
year = int(epoch_date[:2])
year += 2000
datetime = float(epoch_date[2:])
decimal_time = dt(year, 1, 1) + td(datetime - 1)
time_list = [(decimal_time + td(hours=i/60)).strftime("%Y/%m/%d %H:%M:%S") for i in range(0,3600)]
images = [] #画像リスト用
fig = plt.figure() #描画領域を作成

m = Basemap() #世界地図を表示
m.drawcoastlines() #海岸線を表示

for time in time_list:
    image = []
    satellite = ephem.readtle(line1, line2, line3) #TLEパラメータを読み込む
    satellite.compute(time) #指定時刻で実行
    latitude = satellite.sublat / ephem.degree #緯度を取得
    longitude = satellite.sublong / ephem.degree #経度を取得
    x,y = m(longitude, latitude) #XY座標を取得
    image += m.plot(x, y, 'bo', markersize=7) #青丸でプロット
    images.append(image) #画像リストに追加

save_dir = "./" #動画の格納先
ani = ArtistAnimation(fig, images, interval=10, repeat=False) #10ミリ秒毎に図を切り替える
ani.save(os.path.join(save_dir,'orbit.mp4')) #動画を格納