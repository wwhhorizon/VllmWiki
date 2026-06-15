# vllm-project/vllm#43980: [Bug]: setting kv_cache_dtype to fp8 or fp8_e4m3 causes the d node to crash

| 字段 | 值 |
| --- | --- |
| Issue | [#43980](https://github.com/vllm-project/vllm/issues/43980) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: setting kv_cache_dtype to fp8 or fp8_e4m3 causes the d node to crash

### Issue 正文摘录

### Your current environment vllm v0.21.0 module: deepseek-v3-fp8 ### 🐛 Describe the bug Data writes are normal. When using lmcache with the mooncake backend as an external KV cache, the write data type is uint8. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: setting kv_cache_dtype to fp8 or fp8_e4m3 causes the d node to crash bug ### Your current environment vllm v0.21.0 module: deepseek-v3-fp8 ### 🐛 Describe the bug Data writes are normal. When using lmcache with th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: bug Data writes are normal. When using lmcache with the mooncake backend as an external KV cache, the write data type is uint8. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: are normal. When using lmcache with the mooncake backend as an external KV cache, the write data type is uint8. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
