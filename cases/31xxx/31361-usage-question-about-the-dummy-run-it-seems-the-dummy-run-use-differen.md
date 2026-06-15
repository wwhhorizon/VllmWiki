# vllm-project/vllm#31361: [Usage]: Question about the dummy run。It seems the dummy run use different precision?

| 字段 | 值 |
| --- | --- |
| Issue | [#31361](https://github.com/vllm-project/vllm/issues/31361) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Question about the dummy run。It seems the dummy run use different precision?

### Issue 正文摘录

### Question I am trying to modify vllm. especially the **tp** communication, i'am tring to **break all-reduce into reduce-scatter + all-gather**. However I encountered precision problem, after i print the hidden states. it seems each layer has around +-0.01 diff, when it accumulated over all the layers, the result seems to be a huge difference. I thought it may be my implementation error. But after I checked the log, I see some dummy run before executing real request. **I checked the dummy run's data. It perfectly matches between all-reduce & reduce-scatter + all-gather**, which means each layer is exactly same with no accumulated error. So I wonder 1. Can you tell me where there is two dummy run. in My example of Qwen3-32B, one seqlen is max model len, one seqlen is 1024 2. Can you possibly tell me What may influence the precision ? ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: onder 1. Can you tell me where there is two dummy run. in My example of Qwen3-32B, one seqlen is max model len, one seqlen is 1024 2. Can you possibly tell me What may influence the precision ? ### How would you like to...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: sage]: Question about the dummy run。It seems the dummy run use different precision? usage ### Question I am trying to modify vllm. especially the **tp** communication, i'am tring to **break all-reduce into reduce-scatte...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e]: Question about the dummy run。It seems the dummy run use different precision? usage ### Question I am trying to modify vllm. especially the **tp** communication, i'am tring to **break all-reduce into reduce-scatter +...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ** communication, i'am tring to **break all-reduce into reduce-scatter + all-gather**. However I encountered precision problem, after i print the hidden states. it seems each layer has around +-0.01 diff, when it accumu...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
