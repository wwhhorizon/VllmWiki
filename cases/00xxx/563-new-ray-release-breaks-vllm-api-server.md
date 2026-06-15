# vllm-project/vllm#563: New Ray Release Breaks VLLM API Server

| 字段 | 值 |
| --- | --- |
| Issue | [#563](https://github.com/vllm-project/vllm/issues/563) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> New Ray Release Breaks VLLM API Server

### Issue 正文摘录

Hi all, thanks for making such a great repo! I noticed that installing vllm from source now installs ray==2.6.1 and this results in the following error when trying to run an api_server: python3 -m vllm.entrypoints.api_server Traceback (most recent call last): File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main return _run_code(code, main_globals, None, File "/usr/lib/python3.10/runpy.py", line 86, in _run_code exec(code, run_globals) File "/home/vllm/vllm/vllm/entrypoints/api_server.py", line 10, in from vllm.engine.async_llm_engine import AsyncLLMEngine File "/home/vllm/vllm/vllm/engine/async_llm_engine.py", line 7, in from vllm.engine.llm_engine import LLMEngine File "/home/vllm/vllm/vllm/engine/llm_engine.py", line 9, in from vllm.engine.ray_utils import initialize_cluster, ray, RayWorker File "/home/vllm/vllm/vllm/engine/ray_utils.py", line 8, in from ray.air.util.torch_dist import TorchDistributedWorker File "/home/vllm/.local/lib/python3.10/site-packages/ray/air/__init__.py", line 1, in from ray.air.checkpoint import Checkpoint File "/home/vllm/.local/lib/python3.10/site-packages/ray/air/checkpoint.py", line 22, in from ray.air._internal.remote_storage impo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: M API Server Hi all, thanks for making such a great repo! I noticed that installing vllm from source now installs ray==2.6.1 and this results in the following error when trying to run an api_server: python3 -m vllm.entr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
