# vllm-project/vllm#37257: [Performance]: vllm and transformer call the same Qwen3-VL-AI4TEST-V1 model, with roughly the same configuration, but the visual label accuracy is 20% lower in testing.

| 字段 | 值 |
| --- | --- |
| Issue | [#37257](https://github.com/vllm-project/vllm/issues/37257) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: vllm and transformer call the same Qwen3-VL-AI4TEST-V1 model, with roughly the same configuration, but the visual label accuracy is 20% lower in testing.

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: vllm and transformer call the same Qwen3-VL-AI4TEST-V1 model, with roughly the same configuration, but the visual label accuracy is 20% lower in testing. performance ### Proposal to improve performance _N...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: vllm and transformer call the same Qwen3-VL-AI4TEST-V1 model, with roughly the same configuration, but the visual label accuracy is 20% lower in testing. performance ### Proposal to improve performance _N...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: TEST-V1 model, with roughly the same configuration, but the visual label accuracy is 20% lower in testing. performance ### Proposal to improve performance _No response_ ### Report of performance regression _No response_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
