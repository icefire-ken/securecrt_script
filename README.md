# 简介

- 工作中经常需要对客户的网络设备进行巡检，如果工程师PC可以接入到客户的网络中去使用远程登录的方式巡检（如SSH），使用[Devices_Inspection脚本](https://github.com/icefire-ken/Devices_Inspection)就可以完成巡检操作；

- 但是偶尔也会遇到直接从Console口登录设备进行巡检的情况，就需要从SecureCRT软件依次输入多个命令收集巡检信息的操作；

- 本脚本可以在SecureCRT中运行，利用脚本代替手动输入巡检命令的过程。 

# 使用方法

1. 在SecureCRT的Session Options —— Terminal —— Mapped Keys， 映射快捷键（如F1），Function选择Run Script，选择本脚本。

2. 之后，按F1执行脚本会弹出如下提示：

   ![13-14-46](https://github.com/icefire-ken/SecureCRT_Script/assets/26742041/0b6db060-fc07-487c-9f3e-865f17357fea)

   按提示输入正确的【设备类型】就可以开始巡检了。

## 注意事项：

- 本脚本只是代替人工手动输入巡检命令的过程，并不涉及登录。

- 巡检时记得开启记录Log Session记录回显内容。

- 执行脚本前CLI预先进入设备全局模式，保证巡检命令能够被正确执行。

# 目前支持的设备类型

- cisco
- huawei
- h3c
- asa
- nxos
- a10
- ruijie
- linux（待更新）

# 更新日志

## 待更新

- 添加了Linux设备类型的巡检命令。（可根据使用需求自行更改）

## 2023.12.28

- 添加了锐捷设备类型的巡检命令。

## 2022.05.30

- 初次上传脚本；
- 基本实现自动输入巡检命令功能；
- 可根据手动输入的设备类型，自动输入相应的巡检命令。
