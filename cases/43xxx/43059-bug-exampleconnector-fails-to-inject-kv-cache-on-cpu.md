# vllm-project/vllm#43059: [Bug]: ExampleConnector fails to inject KV cache on CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#43059](https://github.com/vllm-project/vllm/issues/43059) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;slowdown |
| 根因提示 | env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ExampleConnector fails to inject KV cache on CPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `ExampleConnector.start_load_kv` silently fails to write KV cache data into the paged buffer on CPU backends due to two underlying bugs. While the scheduler correctly detects externally-available tokens (logging e.g., External prefix cache hit rate: 88.9%) and bypasses the local prefill stage, the KV data is never actually injected. As a result, the decode worker evaluates an empty context and generates garbage output. ## Steps to Reproduce - Set up a disaggregated Prefill-Decode architecture using ExampleConnector (shared storage) on CPU backends. - Run a prefill request (the prefill worker successfully saves the KV data to disk). - Route the decode request to the decode worker. **Expected Behavior:** The decode worker successfully loads the KV files into the buffer and generates coherent output. **Actual Behavior**: The decode worker finds the files but fails to inject them. The model decodes from an empty context, producing repeated backtick characters. ## Bug 1: Early return when `attn_metadata` is None ### Location `vllm/distributed/kv_transfer/kv_connector/v1/example_connector.py`, lines 166-168 ### Code ```python attn_meta...

## 现有链接修复摘要

#43088 [Bugfix] ExampleConnector fails to inject KV cache on CPU.

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 7: oducing repeated backtick characters. ## Bug 1: Early return when `attn_metadata` is None ### Location `vllm/distributed/kv_transfer/kv_connector/v1/example_connector.py`, lines 166-168 ### Code ```python attn_metadata...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: o the paged buffer on CPU backends due to two underlying bugs. While the scheduler correctly detects externally-available tokens (logging e.g., External prefix cache hit rate: 88.9%) and bypasses the local prefill stage...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: ectly detects externally-available tokens (logging e.g., External prefix cache hit rate: 88.9%) and bypasses the local prefill stage, the KV data is never actually injected. As a result, the decode worker evaluates an e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: but fails to inject them. The model decodes from an empty context, producing repeated backtick characters. ## Bug 1: Early return when `attn_metadata` is None ### Location `vllm/distributed/kv_transfer/kv_connector/v1/e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: output. ## Steps to Reproduce - Set up a disaggregated Prefill-Decode architecture using ExampleConnector (shared storage) on CPU backends. - Run a prefill request (the prefill worker successfully saves the KV data to d...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43088](https://github.com/vllm-project/vllm/pull/43088) | closes_keyword | 0.95 | [Bugfix] ExampleConnector fails to inject KV cache on CPU. | Fix #43059 ### Testing Verified on a CPU-only architecture (`vllm/vllm-openai-cpu:latest`) running a disaggregated prefill-to-decode shared-disk pipeline. The decode worker n |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
