import paho.mqtt.subscribe as subscribe



msg = subscribe.simple("test", hostname="192.168.1.102")
msg = str(msg)
msg_list = msg.split(sep=",")
msg_list = msg_list[1:65]
piexls = []
for i in msg_list:
    piexls.append(float(i))
print(msg)
print(piexls)
