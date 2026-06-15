# vllm-project/vllm#9788: [Performance]: Sampler account for most of time comparing to prefill and decode

| 字段 | 值 |
| --- | --- |
| Issue | [#9788](https://github.com/vllm-project/vllm/issues/9788) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Sampler account for most of time comparing to prefill and decode

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Do profiling with qwen2vl, I found that sampler account for most of time during inference, am I right? Is it an issue? ![image](https://github.com/user-attachments/assets/0728adf1-ca22-4aef-a760-aeb81da19ea5) - preprocess: 10ms - vision encoder: 252ms - prefill 46ms + sampler 225ms - (decoding inference 2ms + decoding sampler 18ms ) * 62 = 1240ms ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance]: Sampler account for most of time comparing to prefill and decode bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Do profiling with qwen2vl, I found that s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ing to prefill and decode bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Do profiling with qwen2vl, I found that sampler account for most of time during inference, am I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ent ### Model Input Dumps _No response_ ### 🐛 Describe the bug Do profiling with qwen2vl, I found that sampler account for most of time during inference, am I right? Is it an issue? ![image](https://github.com/user-atta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0ms ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
