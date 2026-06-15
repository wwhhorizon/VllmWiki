# vllm-project/vllm#15034: [Usage]: How to identify mix and max pixels for the image

| 字段 | 值 |
| --- | --- |
| Issue | [#15034](https://github.com/vllm-project/vllm/issues/15034) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to identify mix and max pixels for the image

### Issue 正文摘录

### Your current environment I am using qwen2-vl-7b for image data extraction. Currently i have (min-256 * 28 * 28, max-2560 * 28 * 28) pixels on auto processor. I have a image width-2550, height-3301 How to calculate and fix correct min and max pixels here. ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ixels for the image usage;stale ### Your current environment I am using qwen2-vl-7b for image data extraction. Currently i have (min-256 * 28 * 28, max-2560 * 28 * 28) pixels on auto processor. I have a image width-2550...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to identify mix and max pixels for the image usage;stale ### Your current environment I am using qwen2-vl-7b for image data extraction. Currently i have (min-256 * 28 * 28, max-2560 * 28 * 28) pixels on aut...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
