# vllm-project/vllm#20367: [Feature]:

| 字段 | 值 |
| --- | --- |
| Issue | [#20367](https://github.com/vllm-project/vllm/issues/20367) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I've encountered a phenomenon where when running the DeepSeek V2 Lite Chat MoE model with vLLM's v1 engine, increasing the number of activated experts boosts prefill processing speed by 100%-300%, while decoder speed remains unchanged. Since more activated experts increase computational parameters, speed should decrease – yet it improves. What causes this? I'm not using Expert Parallelism (EP). What mechanisms in vLLM's MoE handling could explain this behavior? ![Image](https://github.com/user-attachments/assets/be464124-3617-4538-a6c7-a53cfcb910ca) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: feature request ### 🚀 The feature, motivation and pitch I've encountered a phenomenon where when running the DeepSeek V2 Lite Chat MoE model with vLLM's v1 engine, increasing the number of activated experts b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rease – yet it improves. What causes this? I'm not using Expert Parallelism (EP). What mechanisms in vLLM's MoE handling could explain this behavior? ![Image](https://github.com/user-attachments/assets/be464124-3617-453...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ve encountered a phenomenon where when running the DeepSeek V2 Lite Chat MoE model with vLLM's v1 engine, increasing the number of activated experts boosts prefill processing speed by 100%-300%, while decoder speed rema...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ncountered a phenomenon where when running the DeepSeek V2 Lite Chat MoE model with vLLM's v1 engine, increasing the number of activated experts boosts prefill processing speed by 100%-300%, while decoder speed remains...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
