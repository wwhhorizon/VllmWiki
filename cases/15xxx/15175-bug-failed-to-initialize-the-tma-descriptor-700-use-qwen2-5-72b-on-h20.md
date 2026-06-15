# vllm-project/vllm#15175: [Bug]: Failed to initialize the TMA descriptor 700 use Qwen2.5 72B on H200

| 字段 | 值 |
| --- | --- |
| Issue | [#15175](https://github.com/vllm-project/vllm/issues/15175) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Failed to initialize the TMA descriptor 700 use Qwen2.5 72B on H200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Qwen2.5 72B inference failed with TP=1, TP=2, but success with TP=4. [qwen_infer_tp2_fp8.log](https://github.com/user-attachments/files/19356727/qwen_infer_tp2_fp8.log) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: inference failed with TP=1, TP=2, but success with TP=4. [qwen_infer_tp2_fp8.log](https://github.com/user-attachments/files/19356727/qwen_infer_tp2_fp8.log) ### Before submitting a new issue... - [x] Make sure you alrea...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: og) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Failed to initialize the TMA descriptor 700 use Qwen2.5 72B on H200 bug;stale ### Your current environment ### 🐛 Describe the bug Qwen2.5 72B inference failed with TP=1, TP=2, but success with TP=4. [qwen_infer_t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Failed to initialize the TMA descriptor 700 use Qwen2.5 72B on H200 bug;stale ### Your current environment ### 🐛 Describe the bug Qwen2.5 72B inference failed with TP=1, TP=2, but success with TP=4. [qwen_infer_tp2_fp8....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
