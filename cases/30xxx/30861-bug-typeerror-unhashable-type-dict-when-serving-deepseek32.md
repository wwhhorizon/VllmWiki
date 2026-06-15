# vllm-project/vllm#30861: [Bug]:  TypeError: unhashable type: 'dict' when serving deepseek32

| 字段 | 值 |
| --- | --- |
| Issue | [#30861](https://github.com/vllm-project/vllm/issues/30861) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cache;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]:  TypeError: unhashable type: 'dict' when serving deepseek32

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I use the script below to start the ds32 model, it raise `TypeError: unhashable type: 'dict'` as shown follow. It looks like this error was introduced by #29627. cc @LucasWilkinson - running script ```bash vllm serve deepseek-ai/DeepSeek-V3.2 \ --tensor-parallel-size 8 \ --tokenizer-mode deepseek_v32 \ --tool-call-parser deepseek_v32 \ --enable-auto-tool-choice \ --reasoning-parser deepseek_v3 ``` - error information ```bash se, num_tokens_across_dp: None DEBUG 12-17 09:15:39 [v1/worker/gpu_model_runner.py:3056] ubatch_slices: None, ubatch_slices_padded: None INFO 12-17 09:16:39 [distributed/device_communicators/shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization). INFO 12-17 09:17:39 [distributed/device_communicators/shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization). INFO 12-17 09:18:3...

## 现有链接修复摘要

#29627 [Attention] Cache attention metadata builds across hybrid KV-cache groups

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: communicators/shm_broadcast.py:542] No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: l ERROR 12-17 09:19:46 [v1/executor/multiproc_executor.py:824] self._build_attention_metadata( ERROR 12-17 09:19:46 [v1/executor/multiproc_executor.py:824] File "/root/Code/vllm_dev/vllm/vllm/v1/worker/gpu_model_runner....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization). INFO 12-17 09:17:39 [distributed/device_communicators/shm_broadcast.py:542] No available shared memory broadcast block foun...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🐛 Describe the bug When I use the script below to start the ds32 model, it raise `TypeError: unhashable type: 'dict'` as shown follow. It looks like this error was introduced by #29627. cc @LucasWilkinson - running...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29627](https://github.com/vllm-project/vllm/pull/29627) | mentioned | 0.45 | [Attention] Cache attention metadata builds across hybrid KV-cache groups | 'dict'` as shown follow. it looks like this error was introduced by #29627. cc @lucaswilkinson - running script ```bash vllm serve deepseek-ai/deepseek-v3.2 \ --tensor-paralle |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
