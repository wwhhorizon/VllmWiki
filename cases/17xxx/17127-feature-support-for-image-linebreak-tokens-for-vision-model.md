# vllm-project/vllm#17127: [Feature]: Support for image linebreak tokens for vision model

| 字段 | 值 |
| --- | --- |
| Issue | [#17127](https://github.com/vllm-project/vllm/issues/17127) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support for image linebreak tokens for vision model

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently when GPUModelRunner computes start and end indices https://github.com/vllm-project/vllm/blob/main/vllm/v1/worker/gpu_model_runner.py#L931-L934 it assumes the relative position of placeholder tokens is the same as `encoder_output`, however if we use image linebreak tokens this assumption no longer holds, which will lead to errors when chunked prefill is enabled. For example, say an input image is split into 3 crops and each crop corresponds to 4 placeholder tokens, in our use case we add an token to separate each crop, the full image tokens would be ``` ``` the number of tokens between and is 15, however the length of `encoder_output` would still be 12, so in this case the start and end idx calculation needs to be readjusted to take into account the tokens. My current workaround is 1. include number of linebreak tokens when calculating mm_positions.length from the model 2. adjust start and end indices in `_gather_mm_embeddings` to align the index with `encoder_output` would like to know your thoughts on this, thanks. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make s...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support for image linebreak tokens for vision model feature request ### 🚀 The feature, motivation and pitch Currently when GPUModelRunner computes start and end indices https://github.com/vllm-project/vllm/bl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Support for image linebreak tokens for vision model feature request ### 🚀 The feature, motivation and pitch Currently when GPUModelRunner computes start and end indices https://github.com/vllm-project/vllm/bl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
