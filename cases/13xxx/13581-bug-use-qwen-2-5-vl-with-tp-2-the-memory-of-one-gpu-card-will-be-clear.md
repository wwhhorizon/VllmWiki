# vllm-project/vllm#13581: [Bug]: Use Qwen 2.5-VL with TP=2, the memory of one GPU card will be cleared to zero during the request.

| 字段 | 值 |
| --- | --- |
| Issue | [#13581](https://github.com/vllm-project/vllm/issues/13581) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Use Qwen 2.5-VL with TP=2, the memory of one GPU card will be cleared to zero during the request.

### Issue 正文摘录

### Your current environment use version: 0.7.2. model_name: qwen2.5-vl args： images=4, tp=2. GPU:A10. ### 🐛 Describe the bug detail: When I use Qwen 2.5-VL with TP=2, the memory of one GPU card will be cleared to zero during the request.And,Other GPUs are functioning normally, but their GPU utilization rate is at 100%. The log is not any error msg and Handing request. ![Image](https://github.com/user-attachments/assets/f28aea27-4107-48c8-8f7f-c6458c96b1c7) ![Image](https://github.com/user-attachments/assets/e1bc1897-b9ab-4a30-b021-bca1d83f7290) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Use Qwen 2.5-VL with TP=2, the memory of one GPU card will be cleared to zero during the request. bug;stale ### Your current environment use version: 0.7.2. model_name: qwen2.5-vl args： images=4, tp=2. GPU:A10. #...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: with TP=2, the memory of one GPU card will be cleared to zero during the request. bug;stale ### Your current environment use version: 0.7.2. model_name: qwen2.5-vl args： images=4, tp=2. GPU:A10. ### 🐛 Describe the bug d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: to zero during the request. bug;stale ### Your current environment use version: 0.7.2. model_name: qwen2.5-vl args： images=4, tp=2. GPU:A10. ### 🐛 Describe the bug detail: When I use Qwen 2.5-VL with TP=2, the memory of...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 90) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
