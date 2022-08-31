# $language = "Python"
# $interface = "1.0"


cisco_cmds_list = ['terminal length 0',
                   'show clock detail',
                   'show inventory',
                   'show env all',
                   'show module all',
                   'show environment',
                   'show power',
                   'show redundancy',
                   'show redundancy switchover history',
                   'dir',
                   'show bootvar',
                   'show processes cpu',
                   'show processes memory',
                   'show license udi',
                   'show license all',
                   'show license feature',
                   'show logging',
                   'show version',
                   'show vtp status',
                   'show vtp password',
                   'show vlan brief',
                   'show ip interface brief',
                   'show cdp neighbors',
                   'show ip route',
                   'show ip ospf neighbor',
                   'show ip ospf interface brief',
                   'show ip eigrp neighbors',
                   'show ip eigrp interfaces',
                   'verify /md5 system:running-config',
                   'show running-config',
                   'terminal length 24']

huawei_cmds_list = ['screen-length 0 temporary',
                    'display clock',
                    'display esn',
                    'display environment',
                    'display power',
                    'dir flash:',
                    'display cpu',
                    'display cpu history',
                    'display memory',
                    'display license',
                    'display log',
                    'display version',
                    'display vlan',
                    'display interface brief',
                    'display ip interface brief',
                    'display lldp neighbor brief',
                    'display ip routing-table',
                    'display ospf peer',
                    'display ospf interface',
                    'display current-configuration',
                    'screen-length 24 temporary']

h3c_cmds_list = ['screen-length disable',
                 'display clock',
                 'display device manuinfo',
                 'display fan',
                 'display transceiver disgnosis interface',
                 'display environment',
                 'display power',
                 'display boot-loader',
                 'display cpu',
                 'display cpu history',
                 'display memory summary',
                 'display license',
                 'display license feature',
                 'display log',
                 'display version',
                 'display vlan brief',
                 'display interface brief',
                 'display ip interface brief',
                 'display lldp neighbor-information brief',
                 'display ip routing-table',
                 'display ospf peer',
                 'display ospf interface',
                 'display current-configuration',
                 'undo screen-length disable']

ciscoasa_cmds_list = ['terminal pager 0',
                      'show inventory',
                      'dir',
                      'show bootvar',
                      'show cpu usage detailed',
                      'show memory',
                      'show license udi',
                      'show license all',
                      'show license feature',
                      'show logging',
                      'show version',
                      'show failover state',
                      'show failover',
                      'show vlan',
                      'show interface ip brief',
                      'show route',
                      'show ospf neighbor',
                      'show ospf interface brief',
                      'show eigrp neighbors',
                      'show eigrp interfaces',
                      'verify /md5 system:running-config',
                      'show running-config',
                      'terminal pager 24']

nxos_cmds_list = ['terminal length 0',
                  'show clock detail',
                  'show inventory',
                  'show module',
                  'show environment',
                  'show vdc',
                  'show redundancy status',
                  'show vpc',
                  'dir',
                  'show boot',
                  'show processes cpu',
                  'show processes memory',
                  'show license',
                  'show license host-id',
                  'show license usage',
                  'show logging',
                  'show version',
                  'show vtp status',
                  'show vtp password',
                  'show vlan brief',
                  'show ip interface brief',
                  'show interface brief',
                  'show cdp neighbors',
                  'show ip route',
                  'show ip ospf neighbor',
                  'show ip ospf interface brief',
                  'show ip eigrp neighbors',
                  'show ip eigrp interfaces',
                  'show running-config',
                  'terminal length 24']

a10_cmds_list = ['terminal length 0',
                 'show clock',
                 'show version',
                 'show cpu',
                 'show memory',
                 'show log',
                 'show ip interfaces',
                 'show interfaces brief',
                 'show vrrp-a',
                 'show running-config',
                 'terminal length 24']

end_cmd = '\n'

sleep_time = 2

supported_device_type = ['cisco', 'huawei', 'h3c', 'asa', 'nxos', 'a10']

device_type = crt.Dialog.Prompt('请输入支持的设备类型：\n  cisco、huawei、h3c、asa、nxos、a10', '请确认设备类型')

if device_type not in supported_device_type:
    crt.Dialog.MessageBox('尚不支持的设备类型。', '设备类型错误', 48)

crt.Screen.Synchronous = True


def main():
    crt.Screen.Send(end_cmd * 3)
    if device_type == 'cisco':
        for cmd in cisco_cmds_list:
            crt.Screen.Send(cmd + end_cmd * 4)
            crt.Sleep(sleep_time)
    elif device_type == 'huawei':
        for cmd in huawei_cmds_list:
            crt.Screen.Send(cmd + end_cmd * 4)
            crt.Sleep(sleep_time)
    elif device_type == 'h3c':
        for cmd in h3c_cmds_list:
            crt.Screen.Send(cmd + end_cmd * 4)
            crt.Sleep(sleep_time)
    elif device_type == 'asa':
        for cmd in ciscoasa_cmds_list:
            crt.Screen.Send(cmd + end_cmd * 4)
            crt.Sleep(sleep_time)
    elif device_type == 'nxos':
        for cmd in nxos_cmds_list:
            crt.Screen.Send(cmd + end_cmd * 4)
            crt.Sleep(sleep_time)
    elif device_type == 'a10':
        for cmd in a10_cmds_list:
            crt.Screen.Send(cmd + end_cmd * 4)
            crt.Sleep(sleep_time)


main()