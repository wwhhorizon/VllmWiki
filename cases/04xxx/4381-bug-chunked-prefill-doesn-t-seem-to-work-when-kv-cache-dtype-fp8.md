# vllm-project/vllm#4381: [Bug]: Chunked prefill doesn't seem to work when --kv-cache-dtype fp8

| 字段 | 值 |
| --- | --- |
| Issue | [#4381](https://github.com/vllm-project/vllm/issues/4381) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;quantization |
| 子分类 |  |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Chunked prefill doesn't seem to work when --kv-cache-dtype fp8

### Issue 正文摘录

### Your current environment H100 (but I believe it happens in any machine) ### 🐛 Describe the bug ``` --enable-chunked-prefill --num-max-batched-tokens 2048 --kv-cache-dtype "fp8" ``` Seems to be broken with some type incompatibility error.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Chunked prefill doesn't seem to work when --kv-cache-dtype fp8 bug ### Your current environment H100 (but I believe it happens in any machine) ### 🐛 Describe the bug ``` --enable-chunked-prefill --num-max-batched...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: seem to work when --kv-cache-dtype fp8 bug ### Your current environment H100 (but I believe it happens in any machine) ### 🐛 Describe the bug ``` --enable-chunked-prefill --num-max-batched-tokens 2048 --kv-cache-dtype "...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: Chunked prefill doesn't seem to work when --kv-cache-dtype fp8 bug ### Your current environment H100 (but I believe it happens in any machine) ### 🐛 Describe the bug ``` --enable-chunked-prefill --num-max-batched...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Chunked prefill doesn't seem to work when --kv-cache-dtype fp8 bug ### Your current environment H100 (but I believe it happens in any machine) ### 🐛 Describe the bug ``` --enable-chunked-prefill --num-max-batched...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
