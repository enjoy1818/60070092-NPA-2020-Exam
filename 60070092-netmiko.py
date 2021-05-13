import netmiko

def main():
    # Setup connection parameters
    device_ip = "10.0.15.103"
    device_ssh_user = "admin"
    device_ssh_password = "cisco"

    # Open connection and configure route
    connectionTemplate = {'device_type':'cisco_ios', 'host':str(device_ip), \
    'username':device_ssh_user, 'password':device_ssh_password, 'port':22, 'blocking_timeout':20}
    connection = netmiko.ConnectHandler(**connectionTemplate)
    command_1 = ["conf t", "int lo 60070092", "ip addr 192.168.1.1 255.255.255.0"]
    for command in command_1:
        connection.send_command(command, expect_string=r"#")
    connection.disconnect()

main()