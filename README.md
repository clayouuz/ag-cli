- [ ] # "do as what jyy can do"

	本项目是看到jyy酷炫的cli聊天工具后心生羡慕搞出来的

	致谢@deepseek

	## 使用方法

	首先需要向环境变量或是`src/.env`中添加api key:
	```text
	OPENAI_API_KEY=
	```

	如果使用的不是openai的api还需要
	```text
	OPENAI_API_BASE=
	```

	不优雅地:

	```py
	python ag.py
	```

	优雅地:

	```bash
	#linux:向~/.bashrc下添加一行,自行替换path,windows自行chat()
	alias ag='python /path/to/ag.py'
	```

	## 项目优势

	1. **关注点分离**：

	- CLI参数解析独立于业务逻辑
	- API客户端管理集中处理
	- 每个模式有独立实现文件

	1. **扩展便捷性**：

	- 添加新模式只需：
	    1. 在modes目录创建新文件
	    2. 使用`@register_mode`装饰器注册
	    3. 更新cli.py中的choices列表

	1. **代码可维护性**：

	- 每个文件保持<200行代码
	- 清晰的接口定义
	- 统一的错误处理机制

	1. **配置灵活性**：

	- 模型参数等配置通过CLI传递
	- 客户端配置集中管理
	- 环境变量与代码解耦

	## 项目结构

	```test
	.
	├── ag.py               # 主程序入口
	└── src/                # 核心代码目录
	    ├── __init__.py
	    ├── cli.py          # 命令行参数解析
	    ├── api_client.py   # llm客户端管理
	    └── modes/          # 不同模式处理器
	        ├── __init__.py # (模式路由系统)
	        └── chat.py     # 聊天模式实现
	
	```

	## 扩展指南

	1. 在modes目录创建新文件
	2. 使用`@register_mode`装饰器注册
	3. 更新cli.py中的choices列表

	## 扩展计划

	- [ ] 日志
	- [ ] config
	- [ ] 保存对话历史
	- [ ] 截图接入多模态
	- [ ] cli端修改api与url,设置代理