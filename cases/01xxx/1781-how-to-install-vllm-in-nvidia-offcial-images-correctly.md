# vllm-project/vllm#1781: How to install vllm in NVIDIA offcial images correctly?

| 字段 | 值 |
| --- | --- |
| Issue | [#1781](https://github.com/vllm-project/vllm/issues/1781) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> How to install vllm in NVIDIA offcial images correctly?

### Issue 正文摘录

I am using the offical images built by NVIDIA: nvcr.io/nvidia/pytorch:23.10-py3. This image has pre-build torch 2.1.0a0+32f93b1. Then I run the contrainer and use "pip install vllm", but this command will uninstall the pre-build pytorch 2.1.0a0+32f93b1 and re-install torch 2.1.0 which lead to the following error when I use vllm in fschat: Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/usr/local/lib/python3.10/dist-packages/fastchat/serve/vllm_worker.py", line 21, in from fastchat.serve.model_worker import ( File "/usr/local/lib/python3.10/dist-packages/fastchat/serve/model_worker.py", line 18, in from fastchat.model.model_adapter import ( File "/usr/local/lib/python3.10/dist-packages/fastchat/model/__init__.py", line 1, in from fastchat.model.model_adapter import ( File "/usr/local/lib/python3.10/dist-packages/fastchat/model/model_adapter.py", line 15, in import accelerate File "/usr/local/lib/python3.10/dist-packages/accelerate/__init__.py", line 3, in from .accelerator import Accelerator Fil...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: How to install vllm in NVIDIA offcial images correctly? I am using the offical images built by NVIDIA: nvcr.io/nvidia/pytorch:23.10-py3. This image has pre-build torch 2.1.0a0+32f93b1. Then I run the contrainer and use...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: es/fastchat/serve/vllm_worker.py", line 21, in from fastchat.serve.model_worker import ( File "/usr/local/lib/python3.10/dist-packages/fastchat/serve/model_worker.py", line 18, in from fastchat.model.model_adapter impor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
