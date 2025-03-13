---
title: README
date: 2025-02-26T21:20:45Z
lastmod: 2025-02-27T17:10:19Z
---

# README

# “do as what jyy can do”

本项目是看到jyy酷炫的cli聊天工具后心生羡慕搞出来的

致谢@deepseek

readme待更新，更改见commit

## 使用方法

运行ag.py，根据提示输入文字即可  
需要设置api

不优雅地:

```
python ag.py
```

优雅地:

linux:向~/.bashrc下添加

```
alias ag='python /path/to/ag.py'
```

windows：在`文档/WindowsPowerShell/Microsoft.PowerShell_profile.ps1`​中添加

```python
function ag {
    python /path/to/ag.py
}
```

path需要替换成`ag.py`​实际路径


## 扩展指南

1. **添加新模式的步骤**：

```python
 # 新建 src/modes/text.py
from src.modes import register_mode
 
@register_mode("text")
def handle_text(client, model):
     """文本批处理模式"""
     # 实现文本处理逻辑
     pass
```

2. **添加新参数的步骤**：

```python
 # 修改 src/cli.py
def parse_args():
    parser = argparse.ArgumentParser(...)
    # 添加新参数
    parser.add_argument("--input-file", help="输入文件路径")
    return parser.parse_args()
```

## 扩展计划

#### 高优先级

* [X] 流式输出
* [X] 添加日志
* [X] config
* [X] 保存对话历史
* [ ] 多模态
* [ ] cli端修改api与url,设置代理

#### 低优先级

* [ ] 异步加载client

‍
