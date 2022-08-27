import subprocess

# subprocess.run("ifconfig", shell=True)
interface = input("Enter your Interface name: ")
mac = input("Enter the new mac address (in format XX:XX:XX:XX:XX:XX) : ")

subprocess.run("ifconfig "+interface+" down", shell=True)
subprocess.run("ifconfig "+interface+" hw ether "+mac, shell=True)

subprocess.run("ifconfig "+interface+" up", shell=True)