# vllm-project/vllm#27181: [Bug]: `check_enough_kv_cache_memory` didn't consider `num_gpu_blocks_override`

| 字段 | 值 |
| --- | --- |
| Issue | [#27181](https://github.com/vllm-project/vllm/issues/27181) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api |
| 子分类 |  |
| Operator 关键词 | cache |
| 症状 |  |
| 根因提示 | memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `check_enough_kv_cache_memory` didn't consider `num_gpu_blocks_override`

### Issue 正文摘录

### Your current environment H100 ### 🐛 Describe the bug I can launch the server with ``` vllm serve facebook/opt-125m --num_gpu_blocks_override=1 .... (EngineCore_DP0 pid=2717573) INFO 10-19 21:10:01 [kv_cache_utils.py:772] Overriding num_gpu_blocks=125643 with num_gpu_blocks_override=1 (EngineCore_DP0 pid=2717573) INFO 10-19 21:10:01 [kv_cache_utils.py:1201] GPU KV cache size: 16 tokens (EngineCore_DP0 pid=2717573) INFO 10-19 21:10:01 [kv_cache_utils.py:1206] Maximum concurrency for 2,048 tokens per request: 0.01x ... ``` However, as there is only one block, no request with length > 16 can be scheduled. the expect behavior should be raising an error during initialization like https://github.com/vllm-project/vllm/blob/f32bf7582e74ef967e657a25fd93186b31a46bed/vllm/v1/core/kv_cache_utils.py#L667-L687 Hope it can be fixed when iterating on https://github.com/vllm-project/vllm/pull/26939, but create a seperate issue to track it. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked ques...

## 现有链接修复摘要

#27238 v1/kv_cache_utils: Respect num_gpu_blocks_override in memory check

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nsider `num_gpu_blocks_override` bug;stale ### Your current environment H100 ### 🐛 Describe the bug I can launch the server with ``` vllm serve facebook/opt-125m --num_gpu_blocks_override=1 .... (EngineCore_DP0 pid=2717...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: `check_enough_kv_cache_memory` didn't consider `num_gpu_blocks_override` bug;stale ### Your current environment H100 ### 🐛 Describe the bug I can launch the server with ``` vllm serve facebook/opt-125m --num_gpu_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ck_enough_kv_cache_memory` didn't consider `num_gpu_blocks_override` bug;stale ### Your current environment H100 ### 🐛 Describe the bug I can launch the server with ``` vllm serve facebook/opt-125m --num_gpu_blocks_over...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: neCore_DP0 pid=2717573) INFO 10-19 21:10:01 [kv_cache_utils.py:1201] GPU KV cache size: 16 tokens (EngineCore_DP0 pid=2717573) INFO 10-19 21:10:01 [kv_cache_utils.py:1206] Maximum concurrency for 2,048 tokens per reques...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development attention_kv_cache;frontend_api cache memory_layout #27238 v1/kv_cache_ut...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27238](https://github.com/vllm-project/vllm/pull/27238) | mentioned | 0.6 | v1/kv_cache_utils: Respect num_gpu_blocks_override in memory check | error even if raw `available_memory` is large. Context - Reported in vllm-project/vllm#27181. - Repro: `vllm serve facebook/opt-125m --num_gpu_blocks_override=1` appears to start,… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
