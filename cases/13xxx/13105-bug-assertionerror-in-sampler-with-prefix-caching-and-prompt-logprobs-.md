# vllm-project/vllm#13105: [Bug]: AssertionError in Sampler with Prefix Caching and Prompt Logprobs Enabled.

| 字段 | 值 |
| --- | --- |
| Issue | [#13105](https://github.com/vllm-project/vllm/issues/13105) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AssertionError in Sampler with Prefix Caching and Prompt Logprobs Enabled.

### Issue 正文摘录

### Your current environment **Description:** When using vLLM with prefix caching enabled (i.e. `enable_prefix_caching=True`), the engine fails during inference with an assertion error in the sampler. The error occurs because the lengths of the `next_token_ids` and `query_indices` do not match. Interestingly, if prefix caching is disabled by setting `enable_prefix_caching=False`, the error goes away. **Reproduction Steps:** 1. **Create a minimal reproduction file:** Save the following as `reproduction.py`: ```python:reproduction.py import asyncio import torch from vllm import AsyncLLMEngine, AsyncEngineArgs, SamplingParams, TokensPrompt async def main(): engine_args = AsyncEngineArgs( model="path/to/model", # Replace with your actual model path tensor_parallel_size=1, gpu_memory_utilization=0.98, dtype=torch.bfloat16, enable_prefix_caching=True, # Bug occurs when prefix caching is enabled. max_num_seqs=1, max_model_len=16384, ) llm = AsyncLLMEngine.from_engine_args(engine_args) input_ids = [100264, 882, 100266, 4438, 1053] sampling_params = SamplingParams( n=1, max_tokens=15, # Ensure max_tokens is larger than len(input_ids) prompt_logprobs=1, ) # Call inference twice; the first c...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: or_parallel_size=1, gpu_memory_utilization=0.98, dtype=torch.bfloat16, enable_prefix_caching=True, # Bug occurs when prefix caching is enabled. max_num_seqs=1, max_model_len=16384, ) llm = AsyncLLMEngine.from_engine_
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ve the following as `reproduction.py`: ```python:reproduction.py import asyncio import torch from vllm import AsyncLLMEngine, AsyncEngineArgs, SamplingParams, TokensPrompt async def main(): engine_args = AsyncEngineArgs...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: fails during the sampling process with an `AssertionError` (due to the mismatch in token lengths), followed by an `AsyncEngineDeadError`. **Workaround:** Disabling prefix caching by setting `enable_prefix_caching=False`...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ionError in Sampler with Prefix Caching and Prompt Logprobs Enabled. bug;stale ### Your current environment **Description:** When using vLLM with prefix caching enabled (i.e. `enable_prefix_caching=True`), the engine fa...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: M fails during the sampling process with an `AssertionError` (due to the mismatch in token lengths), followed by an `AsyncEngineDeadError`. **Workaround:** Disabling prefix caching by setting `enable_prefix_caching=Fals...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
