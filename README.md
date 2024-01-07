# 简介

- 工作中经常需要对客户的网络设备进行巡检，之前都是用SecureCRT开启记录Log Session，依次远程登录到每个设备上，依次输入巡检命令收集设备巡检信息；

- 本脚本可以在SecureCRT中运行，利用脚本代替手动输入巡检命令的过程。

# 使用方法

1. 在SecureCRT的Session Options —— Terminal —— Mapped Keys， 映射快捷键（如F1），Function选择Run Script，选择本脚本。

2. 之后，按F1执行脚本会弹出如下提示：![13-14-46](https://github.com/icefire-ken/SecureCRT_Script/assets/26742041/0b6db060-fc07-487c-9f3e-865f17357fea)

   使用者按提示输入正确的设备类型就可以开始巡检了。

4. 巡检时记得开启记录Log Session记录回显内容。

# 更新日志

## 2023.12.28

- 添加了锐捷设备类型的巡检命令。

## 2022.05.30

- 初次上传脚本；
- 基本实现自动输入巡检命令功能；
- 可根据手动输入的设备类型，自动输入相应的巡检命令。
