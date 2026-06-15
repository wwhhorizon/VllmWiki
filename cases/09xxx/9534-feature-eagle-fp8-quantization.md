# vllm-project/vllm#9534: [Feature]: EAGLE fp8 quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#9534](https://github.com/vllm-project/vllm/issues/9534) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: EAGLE fp8 quantization

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I trained an eagle model (float16). When my base model uses bf16, the outputs are normal and the draft model accept rate is greater than 0; however, when I use an fp8 base model, only the first token is normal, and the other tokens are all "!", and the draft mode accept rate is 0. Does the eagle model currently not support fp8? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature]: EAGLE fp8 quantization feature request;stale ### 🚀 The feature, motivation and pitch I trained an eagle model (float16). When my base model uses bf16, the outputs are normal and the draft model accept rate is...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: EAGLE fp8 quantization feature request;stale ### 🚀 The feature, motivation and pitch I trained an eagle model (float16). When my base model uses bf16, the outputs are normal and the draft model accept rate is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: equest;stale ### 🚀 The feature, motivation and pitch I trained an eagle model (float16). When my base model uses bf16, the outputs are normal and the draft model accept rate is greater than 0; however, when I use an fp8...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
