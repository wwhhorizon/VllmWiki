# vllm-project/vllm#442: docker env cannot launch openai.server

| 字段 | 值 |
| --- | --- |
| Issue | [#442](https://github.com/vllm-project/vllm/issues/442) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> docker env cannot launch openai.server

### Issue 正文摘录

docker: `nvcr.io/nvidia/pytorch:22.12-py3` command: `python -m vllm.entrypoints.openai.api_server --host [0.0.0.0](http://0.0.0.0/) --port 8080` Error: ``` root@ip-172-31-1-200:/workspace# python -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8080 Traceback (most recent call last): File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.8/runpy.py", line 87, in _run_code exec(code, run_globals) File "/usr/local/lib/python3.8/dist-packages/vllm/entrypoints/openai/api_server.py", line 17, in from fastchat.model.model_adapter import get_conversation_template File "/usr/local/lib/python3.8/dist-packages/fastchat/model/__init__.py", line 1, in from fastchat.model.model_adapter import ( File "/usr/local/lib/python3.8/dist-packages/fastchat/model/model_adapter.py", line 13, in import accelerate File "/usr/local/lib/python3.8/dist-packages/accelerate/__init__.py", line 3, in from .accelerator import Accelerator File "/usr/local/lib/python3.8/dist-packages/accelerate/accelerator.py", line 34, in from .checkpointing import load_accelerator_state, load_custom_state, save_accelerator_state, save_custom...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: docker env cannot launch openai.server docker: `nvcr.io/nvidia/pytorch:22.12-py3` command: `python -m vllm.entrypoints.openai.api_server --host [0.0.0.0](http://0.0.0.0/) --port 8080` Error: ``` root@ip-172-31-1-200:/wor
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /vllm/entrypoints/openai/api_server.py", line 17, in from fastchat.model.model_adapter import get_conversation_template File "/usr/local/lib/python3.8/dist-packages/fastchat/model/__init__.py", line 1, in from fastchat....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
