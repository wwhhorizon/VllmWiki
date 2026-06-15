# vllm-project/vllm#10823: [Feature]: vllm Multicar inference bnb model TP is not supported

| 字段 | 值 |
| --- | --- |
| Issue | [#10823](https://github.com/vllm-project/vllm/issues/10823) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: vllm Multicar inference bnb model TP is not supported

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am studying bnb model inference, hoping that the multicar inference bnb model can become possible. Currently, in the research process, I found that the bnb multicar inference report ValueError: Prequant BitsAndBytes models with Tp is not supported.Please try with pp. ### Alternatives _No response_ ### Additional context ![微信图片_20241202150919](https://github.com/user-attachments/assets/eecdb9a0-5bfa-407d-ad9d-19393c43cfac) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: vllm Multicar inference bnb model TP is not supported feature request;stale ### 🚀 The feature, motivation and pitch I am studying bnb model inference, hoping that the multicar inference bnb model can become p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: h process, I found that the bnb multicar inference report ValueError: Prequant BitsAndBytes models with Tp is not supported.Please try with pp. ### Alternatives _No response_ ### Additional context ![微信图片_20241202150919...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: multicar inference bnb model can become possible. Currently, in the research process, I found that the bnb multicar inference report ValueError: Prequant BitsAndBytes models with Tp is not supported.Please try with pp....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: vllm Multicar inference bnb model TP is not supported feature request;stale ### 🚀 The feature, motivation and pitch I am studying bnb model inference, hoping that the multicar inference bnb model can become p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
