# vllm-project/vllm#24439: [Feature]: Support using their own max_num_seqs in prefill and decode stages in pd hybrid scenario

| 字段 | 值 |
| --- | --- |
| Issue | [#24439](https://github.com/vllm-project/vllm/issues/24439) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support using their own max_num_seqs in prefill and decode stages in pd hybrid scenario

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM currently uses a single max_num_seqs parameter to control the batch size for both prefill and decode stages. Maybe support for PD hybrid scenarios because: - Prefill stage: Requires smaller batches due to higher computational intensity and memory usage per request - Decode stage: Can handle larger batches because of lower computational requirements per request - Resource utilization: Fixed batch size leads to either underutilization (decode) or overload (prefill) Add support for separate max_num_seqs_prefill and max_num_seqs_decode parameters that allow different batch size configurations for each stage, while maintaining backward compatibility. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Support using their own max_num_seqs in prefill and decode stages in pd hybrid scenario feature request;stale ### 🚀 The feature, motivation and pitch vLLM currently uses a single max_num_seqs parameter to con...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Maybe support for PD hybrid scenarios because: - Prefill stage: Requires smaller batches due to higher computational intensity and memory usage per request - Decode stage: Can handle larger batches because of lower comp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: efill and max_num_seqs_decode parameters that allow different batch size configurations for each stage, while maintaining backward compatibility. ### Alternatives _No response_ ### Additional context _No response_ ### B...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
