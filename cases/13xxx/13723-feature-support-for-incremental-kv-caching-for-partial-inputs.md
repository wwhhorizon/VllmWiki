# vllm-project/vllm#13723: [Feature]: Support for Incremental KV Caching for Partial Inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#13723](https://github.com/vllm-project/vllm/issues/13723) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for Incremental KV Caching for Partial Inputs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We are developing voice bots where the ASR (Automatic Speech Recognition) model provides partial transcriptions before the final result is available. I’m wondering if VLLM supports or could support an API that allows incremental KV caching for these partial inputs. The goal is to avoid recomputing the entire input sequence when the final transcription is ready, which could help reduce generation latency. Is this feasible within VLLM’s architecture? Would love to hear any thoughts on this. Thanks! ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support for Incremental KV Caching for Partial Inputs feature request;stale ### 🚀 The feature, motivation and pitch We are developing voice bots where the ASR (Automatic Speech Recognition) model provides par...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: hen the final transcription is ready, which could help reduce generation latency. Is this feasible within VLLM’s architecture? Would love to hear any thoughts on this. Thanks! ### Alternatives _No response_ ### Addition...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ch could help reduce generation latency. Is this feasible within VLLM’s architecture? Would love to hear any thoughts on this. Thanks! ### Alternatives _No response_ ### Additional context _No response_ ### Before submi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e are developing voice bots where the ASR (Automatic Speech Recognition) model provides partial transcriptions before the final result is available. I’m wondering if VLLM supports or could support an API that allows inc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
