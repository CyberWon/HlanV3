# V3.0.1
1. 改动了框架.使其能从配置文件读取运行方式.
```ini
[runmode]
web = runFlask
console = runConsole

对应的是在mod下入口文件.

web->mod/runFlask
console->mod/runConsole

ext/runFlask 为web入口之后处理的.
其他同理

```