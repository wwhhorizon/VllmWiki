# vllm-project/vllm#19801: [Bug]: Loading Qwen3MoE using Transformers backend

| 字段 | 值 |
| --- | --- |
| Issue | [#19801](https://github.com/vllm-project/vllm/issues/19801) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Loading Qwen3MoE using Transformers backend

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve Qwen/Qwen3-30B-A3B --model-impl=transformers Result in error: File ".../vllm/model_executor/models/transformers.py", line 66, in vllm_flash_attention_forward self_attn = attention_instances[module.layer_idx] TypeError: 'NoneType' object is not subscriptable which I believe is a unique bug related to MoE structure, as the dense models of Qwen3 can be served normally with transformers backend. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Loading Qwen3MoE using Transformers backend bug ### Your current environment ### 🐛 Describe the bug vllm serve Qwen/Qwen3-30B-A3B --model-impl=transformers Result in error: File ".../vllm/model_executor/models/tr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: Loading Qwen3MoE using Transformers backend bug ### Your current environment ### 🐛 Describe the bug vllm serve Qwen/Qwen3-30B-A3B --model-impl=transformers Result in error: File ".../vllm/model_executor/models/tr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nd. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Loading Qwen3MoE using Transformers backend bug ### Your current environment ### 🐛 Describe the bug vllm serve Qwen/Qwen3-30B-A3B --model-impl=transformers Result in error: File ".../vllm/model_executor/models/tr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
