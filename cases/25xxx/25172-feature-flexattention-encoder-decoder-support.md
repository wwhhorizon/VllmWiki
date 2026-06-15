# vllm-project/vllm#25172: [Feature]: FlexAttention + encoder_decoder support

| 字段 | 值 |
| --- | --- |
| Issue | [#25172](https://github.com/vllm-project/vllm/issues/25172) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: FlexAttention + encoder_decoder support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently on compute capability < 8.0 (Turing, Volta) encoder_decoder raises `NotImplementedError: FlexAttention does not support encoder_decoder attention` Tested on `openai/whisper-large-v3` + T4 + vllm/vllm-openai:nightly-0f7acdd73ca6316c8ae0474c0a9c4fc264e87a7b cc @russellb @DarkLight1337 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: FlexAttention + encoder_decoder support feature request;stale ### 🚀 The feature, motivation and pitch Currently on compute capability < 8.0 (Turing, Volta) encoder_decoder raises `NotImplementedError: FlexAtt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: uest;stale ### 🚀 The feature, motivation and pitch Currently on compute capability < 8.0 (Turing, Volta) encoder_decoder raises `NotImplementedError: FlexAttention does not support encoder_decoder attention` Tested on `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: lementedError: FlexAttention does not support encoder_decoder attention` Tested on `openai/whisper-large-v3` + T4 + vllm/vllm-openai:nightly-0f7acdd73ca6316c8ae0474c0a9c4fc264e87a7b cc @russellb @DarkLight1337 ### Alter...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
