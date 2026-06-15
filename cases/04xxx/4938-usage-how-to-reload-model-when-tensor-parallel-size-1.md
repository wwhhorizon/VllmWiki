# vllm-project/vllm#4938: [Usage]: How to reload model when tensor_parallel_size > 1 ?

| 字段 | 值 |
| --- | --- |
| Issue | [#4938](https://github.com/vllm-project/vllm/issues/4938) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to reload model when tensor_parallel_size > 1 ?

### Issue 正文摘录

### My Python Script ```python import os os.environ["CUDA_VISIBLE_DEVICES"] = "2,3" import time import torch from vllm import LLM, SamplingParams import gc from vllm.model_executor.parallel_utils.parallel_state import destroy_model_parallel model_name1 = "./Qwen1.5-7B-Chat/" llm1 = LLM(model=model_name1, tensor_parallel_size=2) print("model loaded !") destroy_model_parallel() del llm1 gc.collect() torch.cuda.empty_cache() print("model deleted !") model_name2 = "./Qwen1.5-14B-Chat/" llm2 = LLM(model=model_name2, tensor_parallel_size=2) print("model reloaded !") ``` ### How would you like to use vllm When tensor_parallel_size=1, the program worked well. But when tensor_parallel_size=2, it got stuck with `2024-05-21 16:59:38,442 INFO worker.py:1582 -- Calling ray.init() again after it has already been called.` after "model deleted !"

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to reload model when tensor_parallel_size > 1 ? usage;stale ### My Python Script ```python import os os.environ["CUDA_VISIBLE_DEVICES"] = "2,3" import time import torch from vllm import LLM, SamplingParams...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: n tensor_parallel_size > 1 ? usage;stale ### My Python Script ```python import os os.environ["CUDA_VISIBLE_DEVICES"] = "2,3" import time import torch from vllm import LLM, SamplingParams import gc from vllm.model_execut...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: > 1 ? usage;stale ### My Python Script ```python import os os.environ["CUDA_VISIBLE_DEVICES"] = "2,3" import time import torch from vllm import LLM, SamplingParams import gc from vllm.model_executor.parallel_utils.paral...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to reload model when tensor_parallel_size > 1 ? usage;stale ### My Python Script ```python import os os.environ["CUDA_VISIBLE_DEVICES"] = "2,3" import time import torch from vllm import LLM, SamplingParams...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
