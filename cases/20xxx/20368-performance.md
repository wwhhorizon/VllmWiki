# vllm-project/vllm#20368: [Performance]:

| 字段 | 值 |
| --- | --- |
| Issue | [#20368](https://github.com/vllm-project/vllm/issues/20368) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]:

### Issue 正文摘录

### Proposal to improve performance ![Image](https://github.com/user-attachments/assets/7c7d91d1-cf2f-4f91-bee7-1fdfcbd0c15b) I've encountered a phenomenon where when running the DeepSeek V2 Lite Chat MoE model with vLLM's v1 engine, increasing the number of activated experts boosts prefill processing speed by 100%-300%, while decoder speed remains unchanged. Since more activated experts increase computational parameters, speed should decrease – yet it improves. What causes this? I'm not using Expert Parallelism (EP). What mechanisms in vLLM's MoE handling could explain this behavior? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rease – yet it improves. What causes this? I'm not using Expert Parallelism (EP). What mechanisms in vLLM's MoE handling could explain this behavior? ### Report of performance regression _No response_ ### Misc discussio...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ve encountered a phenomenon where when running the DeepSeek V2 Lite Chat MoE model with vLLM's v1 engine, increasing the number of activated experts boosts prefill processing speed by 100%-300%, while decoder speed rema...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: with vLLM's v1 engine, increasing the number of activated experts boosts prefill processing speed by 100%-300%, while decoder speed remains unchanged. Since more activated experts increase computational parameters, spee...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: M's MoE handling could explain this behavior? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ncountered a phenomenon where when running the DeepSeek V2 Lite Chat MoE model with vLLM's v1 engine, increasing the number of activated experts boosts prefill processing speed by 100%-300%, while decoder speed remains...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
