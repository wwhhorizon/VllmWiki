# vllm-project/vllm#9600: [Feature]: The problem of low infer speed in MiniCPM3

| 字段 | 值 |
| --- | --- |
| Issue | [#9600](https://github.com/vllm-project/vllm/issues/9600) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: The problem of low infer speed in MiniCPM3

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When I deploy the MiniCPM3-4B in 1*4090, I found the "--force-eager" need to be true. I do not know if because of this, the infer speed is so slow. Generate same tokens, MiniCPM3-4B cost 2~3* time then Qwen2-7B, but in less param then qwen. 1.If the slow problem come from "--force-eager", will it have fix? 2.If the slow problem not come from "--force-eager", how can I got the real promblem? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: speed is so slow. Generate same tokens, MiniCPM3-4B cost 2~3* time then Qwen2-7B, but in less param then qwen. 1.If the slow problem come from "--force-eager", will it have fix? 2.If the slow problem not come from "--fo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: The problem of low infer speed in MiniCPM3 feature request ### 🚀 The feature, motivation and pitch When I deploy the MiniCPM3-4B in 1*4090, I found the "--force-eager" need to be true. I do not know if becaus...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
