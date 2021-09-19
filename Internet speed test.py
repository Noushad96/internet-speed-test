from speedtest import Speedtest  #install speedtest-cli = warna (No module named 'speedtest') bolega
st=Speedtest()
d=st.download()/1024/1024
print("your Internet download speed is",d,"Mbps") #mera tarika Mbps k iye
print(f"Download speed: {'{:.2f}'.format(st.download()/1024/1024)} Mb/s") #mb/s
print("your Internet upload speed is",st.upload())  # bytes
print("your Internet upload speed is",st.upload())

#.get_servers()
# to get information on all available servers

servers = st.get_servers()
for key, value in servers.items():
    print(key, ' : ', value)

