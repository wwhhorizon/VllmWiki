# vllm-project/vllm#30043: [Performance]: big perf loss between 0.11.2 and 0.12.0 on rms_norm

| 字段 | 值 |
| --- | --- |
| Issue | [#30043](https://github.com/vllm-project/vllm/issues/30043) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: big perf loss between 0.11.2 and 0.12.0 on rms_norm

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression With this function from vllm.model_executor.layers.layernorm import RMSNorm ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression With this function from vllm.model_executor.layers.layernorm import RMSNorm ### Misc discussion on performance _No response_ ### Your cur...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: regression With this function from vllm.model_executor.layers.layernorm import RMSNorm ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nse_ ### Report of performance regression With this function from vllm.model_executor.layers.layernorm import RMSNorm ### Misc discussion on performance _No response_ ### Your current environment (if you think it is nec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
