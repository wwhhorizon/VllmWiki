# vllm-project/vllm#15446: [Bug]: v1 fails when token budget is set to 128K

| 字段 | 值 |
| --- | --- |
| Issue | [#15446](https://github.com/vllm-project/vllm/issues/15446) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nondeterministic;oom |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v1 fails when token budget is set to 128K

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In v1 is enabled in `v0.8.1`, the program runs into OOM when `max_num_batched_tokens` (i.e. max token budget for the scheduler) is set to 128K for Llama 3.1 8B. There is enough KV space based on below log: `INFO 03-25 03:01:40 [kv_cache_utils.py:540] Maximum concurrency for 131,072 tokens per request: 3.05x` Here's a minimal python script to replicate the bug: ```python # command: python test.py import asyncio, time, uuid, pytest from vllm.engine.arg_utils import EngineArgs from vllm.platforms import current_platform from vllm.usage.usage_lib import UsageContext from vllm.v1.engine.core_client import EngineCoreClient, AsyncMPClient from vllm.v1.executor.abstract import Executor from typing import List from vllm.v1.engine import EngineCoreRequest from vllm import SamplingParams if not current_platform.is_cuda(): pytest.skip(reason="V1 currently only supported on CUDA.", allow_module_level=True) MODEL_NAME = "meta-llama/Meta-Llama-3.1-8B-Instruct" def create_dummy_token_ids(size: int, vocab_size: int) -> List[int]: """Create a list of dummy token IDs of specified size. Uses a simple pattern that cycles through tokens 0 to vocab_siz...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: v1 fails when token budget is set to 128K bug;stale ### Your current environment ### 🐛 Describe the bug In v1 is enabled in `v0.8.1`, the program runs into OOM when `max_num_batched_tokens` (i.e. max token budget...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: python script to replicate the bug: ```python # command: python test.py import asyncio, time, uuid, pytest from vllm.engine.arg_utils import EngineArgs from vllm.platforms import current_platform from vllm.usage.usage_l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: hed_tokens` (i.e. max token budget for the scheduler) is set to 128K for Llama 3.1 8B. There is enough KV space based on below log: `INFO 03-25 03:01:40 [kv_cache_utils.py:540] Maximum concurrency for 131,072 tokens per...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: have valid token IDs within the model's vocabulary range while being deterministic. Args: size: Number of token IDs to generate vocab_size: Size of the model's vocabulary Returns: List of token IDs within the valid voca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: eCoreRequest from vllm import SamplingParams if not current_platform.is_cuda(): pytest.skip(reason="V1 currently only supported on CUDA.", allow_module_level=True) MODEL_NAME = "meta-llama/Meta-Llama-3.1-8B-Instruct" de...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
