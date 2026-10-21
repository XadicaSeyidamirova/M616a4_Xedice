rsrp_dbm = -95
p_mw = 10 ** (rsrp_dbm / 10)
print(f" {rsrp_dbm} dBm = {p_mw:.2e} mW")

values  = [ -85, -97, -110, -102, -118]
for v in values:
    if v < -80 :
        print (v, "dBm - low signal, ALERT PLEASE SUPPORT TO  INVESTIGATE AND OPTIMIZE!")
    else: 
        print (v, "dBm - normal, YOUR SIGNAL IS BEING TRANSMITTED PROPERLY, WELL DONE!")                          
        