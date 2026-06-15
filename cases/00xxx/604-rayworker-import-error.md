# vllm-project/vllm#604: RayWorker import error

| 字段 | 值 |
| --- | --- |
| Issue | [#604](https://github.com/vllm-project/vllm/issues/604) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> RayWorker import error

### Issue 正文摘录

When import `vllm` I got following error ``` Traceback (most recent call last): File " ", line 1, in File "/code/vllm/vllm/__init__.py", line 4, in from vllm.engine.async_llm_engine import AsyncLLMEngine File "/code/vllm/vllm/engine/async_llm_engine.py", line 7, in from vllm.engine.llm_engine import LLMEngine File "/code/vllm/vllm/engine/llm_engine.py", line 9, in from vllm.engine.ray_utils import initialize_cluster, ray, RayWorker ImportError: cannot import name 'RayWorker' from 'vllm.engine.ray_utils' ``` It seems `ray` requires `pandas` I haven't installed it.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: RayWorker import error When import `vllm` I got following error ``` Traceback (most recent call last): File " ", line 1, in File "/code/vllm/vllm/__init__.py", line 4, in from vllm.engine.async_llm_engine import AsyncL

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
