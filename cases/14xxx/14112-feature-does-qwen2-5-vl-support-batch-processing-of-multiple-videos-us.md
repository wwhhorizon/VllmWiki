# vllm-project/vllm#14112: [Feature]: Does Qwen2.5-VL support batch processing of multiple videos using vLLM?

| 字段 | 值 |
| --- | --- |
| Issue | [#14112](https://github.com/vllm-project/vllm/issues/14112) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Does Qwen2.5-VL support batch processing of multiple videos using vLLM?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Description I am currently deploying and running inference of a Qwen2.5-VL model using vLLM as recommended by the official website. When testing the model with multiple video inputs, I noticed that the current implementation processes the videos sequentially (one video at a time). This approach may not be the best choice for performance-critical scenarios, especially when processing multiple videos with similar preprocessing requirements. Is it possible to process multiple videos at once, where frames from different videos are combined into a batch (e.g., [num_videos, num_frames, 3, H, W])? Question Does Qwen2.5-VL already support batch processing of multiple videos? If yes, how to enable it? Are there plans to extend vLLM to support batched video inputs in the near future? If not, what is the recommended way to implement this feature? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequ...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Does Qwen2.5-VL support batch processing of multiple videos using vLLM? feature request;stale ### 🚀 The feature, motivation and pitch Description I am currently deploying and running inference of a Qwen2.5-VL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: en2.5-VL support batch processing of multiple videos using vLLM? feature request;stale ### 🚀 The feature, motivation and pitch Description I am currently deploying and running inference of a Qwen2.5-VL model using vLLM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ing inference of a Qwen2.5-VL model using vLLM as recommended by the official website. When testing the model with multiple video inputs, I noticed that the current implementation processes the videos sequentially (one...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: Qwen2.5-VL model using vLLM as recommended by the official website. When testing the model with multiple video inputs, I noticed that the current implementation processes the videos sequentially (one video at a time). T...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
