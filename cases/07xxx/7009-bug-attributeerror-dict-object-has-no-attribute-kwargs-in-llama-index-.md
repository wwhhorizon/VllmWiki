# vllm-project/vllm#7009: [Bug]: AttributeError: 'dict' object has no attribute 'kwargs' in llama_index.llms.ollama integration with Ray

| 字段 | 值 |
| --- | --- |
| Issue | [#7009](https://github.com/vllm-project/vllm/issues/7009) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'dict' object has no attribute 'kwargs' in llama_index.llms.ollama integration with Ray

### Issue 正文摘录

### Your current environment ### Environment - Python version: 3.10 - Ray version: 2.32.0 - llama-index-llms-ollama version: 0.2.2 ### Issue When trying to use the TinyLlama model with Ray for distributed processing, I encountered the following error: ``` ray.exceptions.RayTaskError(AttributeError): ray::TinyLlamaModel.predict() (pid=36473, ip=192.168.0.5, actor_id=eba9137d3b3152d0648c3ff705000000, repr= ) File "/Users/ersinaksar/Documents/Development/Projects/work/raspberry/raspberry/distributed_tinyllama.py", line 25, in predict File "/home/ubuntu/.venv/lib/python3.10/site-packages/llama_index/legacy/llms/llm.py", line 235, in predict self._log_template_data(prompt, **prompt_args) File "/home/ubuntu/.venv/lib/python3.10/site-packages/llama_index/legacy/llms/llm.py", line 156, in _log_template_data for k, v in ChainMap(prompt.kwargs, prompt_args).items() AttributeError: 'dict' object has no attribute 'kwargs' ``` ### Steps to Reproduce 1. Set up a distributed environment using Ray. 2. Use the following code snippet to run the TinyLlama model: ```python import ray from llama_index.llms.ollama import Ollama from llama_index.core import Settings import sys ray.init(address='auto') @...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ith Ray bug;stale ### Your current environment ### Environment - Python version: 3.10 - Ray version: 2.32.0 - llama-index-llms-ollama version: 0.2.2 ### Issue When trying to use the TinyLlama model with Ray for distribu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: AttributeError: 'dict' object has no attribute 'kwargs' in llama_index.llms.ollama integration with Ray bug;stale ### Your current environment ### Environment - Python version: 3.10 - Ray version: 2.32.0 - llama-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: o attribute 'kwargs' in llama_index.llms.ollama integration with Ray bug;stale ### Your current environment ### Environment - Python version: 3.10 - Ray version: 2.32.0 - llama-index-llms-ollama version: 0.2.2 ### Issue...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ttributeError: 'dict' object has no attribute 'kwargs' ``` ### Steps to Reproduce 1. Set up a distributed environment using Ray. 2. Use the following code snippet to run the TinyLlama model: ```python import ray from ll...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
