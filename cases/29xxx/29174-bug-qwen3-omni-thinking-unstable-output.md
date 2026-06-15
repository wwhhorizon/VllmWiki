# vllm-project/vllm#29174: [Bug]: Qwen3 Omni thinking unstable output

| 字段 | 值 |
| --- | --- |
| Issue | [#29174](https://github.com/vllm-project/vllm/issues/29174) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3 Omni thinking unstable output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When i used the v0.11.2, i test the qwen3-omni-think, i started the serve with --no-enable-prefix-caching, --disable-mm-xxxx Here are some combinations: 1、 only audio - ok 2、 only video - ok 3、 audio + video - output null sometimes, when i first run 1 then 3, 2 then 3, it was correct But the v0.11.1rc4 is correct ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ect ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Qwen3 Omni thinking unstable output bug;stale ### Your current environment ### 🐛 Describe the bug When i used the v0.11.2, i test the qwen3-omni-think, i started the serve with --no-enable-prefix-caching, --disabl
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Qwen3 Omni thinking unstable output bug;stale ### Your current environment ### 🐛 Describe the bug When i used the v0.11.2, i test the qwen3-omni-think, i started the serve with --no-enable-prefix-caching, --disab...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rrent environment ### 🐛 Describe the bug When i used the v0.11.2, i test the qwen3-omni-think, i started the serve with --no-enable-prefix-caching, --disable-mm-xxxx Here are some combinations: 1、 only audio - ok 2、 onl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
