>>> import skyfield.api
# TLEを読み込む
>>> sats = skyfield.api.load.tle_file("http://celestrak.org/NORAD/elements/gp.php?GROUP=last-30-days&FORMAT=tle", reload=True)
# 衛星が何個含まれているか？
>>> len(sats)
156
# 0番目の衛星をみてみる
>>> sats[0]
<EarthSatellite GPS BIIR-2  (PRN 13) catalog #24876 epoch 2023-01-26 17:25:39 UTC>
>>> ts = skyfield.api.load.timescale()
>>> sat = sats[0]

# 衛星の現在の位置を取得してみる
>>> sat.at(ts.now())
<Geocentric ICRS position and velocity at date t center=399 target=-124876>

# 座標を取得してみる
>>> sat.at(ts.now()).position
<Distance [-1.48650828e-04  2.47026029e-05  9.16709615e-05] au>

# メートル単位で欲しい
>>> sat.at(ts.now()).position.m
array([-22229143.44338772,   3673091.13254689,  13733781.9073863 ])

# 速度も得られる
>>> sat.velocity.m_per_s
array([ 1611.64563397, -2842.84923151,  2128.79653024])
