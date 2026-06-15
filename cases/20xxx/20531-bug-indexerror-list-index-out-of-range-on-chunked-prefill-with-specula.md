# vllm-project/vllm#20531: [Bug]: IndexError: list index out of range on chunked prefill with speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#20531](https://github.com/vllm-project/vllm/issues/20531) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | runtime_err |
| Operator 关键词 | quantization |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: IndexError: list index out of range on chunked prefill with speculative decoding

### Issue 正文摘录

### Environment Engine Configuration: ``` V1 LLM engine (v0.9.1) with config: - model='/tmp/model/' - speculative_config=SpeculativeConfig(method='eagle3', model='/tmp/model/eagle_head/', num_spec_tokens=5) - tensor_parallel_size=8 - pipeline_parallel_size=1 - quantization=compressed-tensors - max_seq_len=131072 ``` Prefix caching and chunked prefill are enabled by default V1 behavior. This issue also occurred in vLLM v0.8.5.post1 and has been hard to reproduce. Model: `Llama-3.3-70B-Instruct` Hardware: 8 H200 GPUs ### 🐛 Describe the bug `IndexError` with chunked prefill and speculative decoding. https://github.com/vllm-project/vllm/blob/9fb52e523abf7bdaf7e60cf2971edb5a1b13dc08/vllm/v1/worker/gpu_model_runner.py#L1612 ### Error Logs #### Worker Stack Trace (across multiple ranks): ```text IndexError: list index out of range Traceback (most recent call last): File "/usr/local/lib/python3.11/dist-packages/vllm/v1/executor/multiproc_executor.py", line 522, in worker_busy_loop output = func(*args, **kwargs) File "/usr/local/lib/python3.11/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context return func(*args, **kwargs) File "/usr/local/lib/python3.11/dist-packages/...

## 现有链接修复摘要

#21876 [Bugfix] Mask OOV tokens IDs from the Rejection Sampler

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: IndexError: list index out of range on chunked prefill with speculative decoding bug;stale ### Environment Engine Configuration: ``` V1 LLM engine (v0.9.1) with config: - model='/tmp/model/' - speculative_config=...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ked prefill with speculative decoding bug;stale ### Environment Engine Configuration: ``` V1 LLM engine (v0.9.1) with config: - model='/tmp/model/' - speculative_config=SpeculativeConfig(method='eagle3', model='/tmp/mod...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: e063-786b-4cf9-8ebc-548f201ed419', resumed_from_preemption=false, new_token_ids=[t1], new_block_ids=[[]], num_computed_tokens=t2 ), CachedRequestData( req_id='93ae9bbb-f390-4f02-9d16-ddcba4e3b6d2', resumed
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: vior. This issue also occurred in vLLM v0.8.5.post1 and has been hard to reproduce. Model: `Llama-3.3-70B-Instruct` Hardware: 8 H200 GPUs ### 🐛 Describe the bug `IndexError` with chunked prefill and speculative decoding...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: uantization;scheduler_memory;speculative_decoding quantization crash env_dependency #21876 [Bugfix] Mask OOV tokens IDs from the Rejection Sampler Environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21876](https://github.com/vllm-project/vllm/pull/21876) | mentioned | 0.6 | [Bugfix] Mask OOV tokens IDs from the Rejection Sampler | sampling of OOV token ids causes the engine to crash as described in #20531 This seems to be because the kernel pads the vocabulary size with `-inf` and Triton's argmax function s… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
