# vllm-project/vllm#26524: [Bug]: prepare_kernel_block_sizes doesn't parse UniformTypeKVCacheSpecs

| 字段 | 值 |
| --- | --- |
| Issue | [#26524](https://github.com/vllm-project/vllm/issues/26524) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: prepare_kernel_block_sizes doesn't parse UniformTypeKVCacheSpecs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm running DeepSeekV3.2 on Blackwell and I am seeing a crash on launch coming from this PR: #24486 ``` NotImplementedError: unknown kv cache spec UniformTypeKVCacheSpecs ``` The function `_prepare_kernel_block_sizes` throws an exception if `kv_cache_group.kv_cache_spec` is not an `AttentionSpec`, but it is being received as `UniformTypeKVCacheSpecs` @zhiyuan1i @heheda12345 is this intentional? Any idea why this happens? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#24486 [Hybrid]: Decouple Kernel Block Size from KV Page Size

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cache;cuda;operator;sam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: rent environment ### 🐛 Describe the bug I'm running DeepSeekV3.2 on Blackwell and I am seeing a crash on launch coming from this PR: #24486 ``` NotImplementedError: unknown kv cache spec UniformTypeKVCacheSpecs ``` The...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: prepare_kernel_block_sizes doesn't parse UniformTypeKVCacheSpecs bug ### Your current environment ### 🐛 Describe the bug I'm running DeepSeekV3.2 on Blackwell and I am seeing a crash on launch coming from this PR...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: upport;sampling_logits;speculative_decoding cache;cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency #24486 [Hybrid]: Decouple Kernel Block Size from KV Page Size Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: n launch coming from this PR: #24486 ``` NotImplementedError: unknown kv cache spec UniformTypeKVCacheSpecs ``` The function `_prepare_kernel_block_sizes` throws an exception if `kv_cache_group.kv_cache_spec` is not an...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#24486](https://github.com/vllm-project/vllm/pull/24486) | mentioned | 0.45 | [Hybrid]: Decouple Kernel Block Size from KV Page Size | 2 on blackwell and i am seeing a crash on launch coming from this pr: #24486 ``` notimplementederror: unknown kv cache spec uniformtypekvcachespecs ``` the function `_prepare_kern… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
