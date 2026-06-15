# vllm-project/vllm#44184: [Bug]: when set kv_cache_dtype to fp8 or fp8_e4m3 causes the d node to crash

| 字段 | 值 |
| --- | --- |
| Issue | [#44184](https://github.com/vllm-project/vllm/issues/44184) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: when set kv_cache_dtype to fp8 or fp8_e4m3 causes the d node to crash

### Issue 正文摘录

### Your current environment vllm v0.21.0 module: deepseek-v3-fp8 same as: GLM5 --tensor-parallel-size 8 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 3 \ --trust-remote-code \ --kv-cache-dtype fp8 \ --kv-transfer-config ### 🐛 Describe the bug Data writes are normal. When using lmcache with the mooncake backend as an external KV cache, the write data type is uint8. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: when set kv_cache_dtype to fp8 or fp8_e4m3 causes the d node to crash bug ### Your current environment vllm v0.21.0 module: deepseek-v3-fp8 same as: GLM5 --tensor-parallel-size 8 \ --speculative-config.method mtp...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: peculative-config.num_speculative_tokens 3 \ --trust-remote-code \ --kv-cache-dtype fp8 \ --kv-transfer-config ### 🐛 Describe the bug Data writes are normal. When using lmcache with the mooncake backend as an external K...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: bug Data writes are normal. When using lmcache with the mooncake backend as an external KV cache, the write data type is uint8. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: seek-v3-fp8 same as: GLM5 --tensor-parallel-size 8 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 3 \ --trust-remote-code \ --kv-cache-dtype fp8 \ --kv-transfer-config ### 🐛 Describe the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
