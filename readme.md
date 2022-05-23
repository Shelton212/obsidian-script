# Usage - 用法

通过obsidian的[shellcommands](https://github.com/Taitava/obsidian-shellcommands)插件实现脚本的调用，每条命令都可以单独设置shortcut

命令示例：

```python
python D:\WorkSpace\vscode\script\python\openURL.py
```

# Scripts list - 脚本列表

## 1. openURL.py

原因：

- 头部的Front-matter中会写from（内容来源），一般直接填上链接，但在Front-matter中无法直接像md语法中的链接点击访问，因此写了这个脚本

思路：

- 选中url后，脚本模拟复制，并将剪切板的内容返回python，调用浏览器访问