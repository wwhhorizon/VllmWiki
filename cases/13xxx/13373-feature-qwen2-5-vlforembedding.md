# vllm-project/vllm#13373: [Feature]: Qwen2_5_VLForEmbedding

| 字段 | 值 |
| --- | --- |
| Issue | [#13373](https://github.com/vllm-project/vllm/issues/13373) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Qwen2_5_VLForEmbedding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I have trained a "Qwen/Qwen2.5-VL-3B-Instruct" based vlm embedding model. When I try to encode embedding with vllm I got: `ValueError: There is no module or parameter named 'layers' in Qwen2_5_VLForEmbedding` Does the vllm embedding model for Qwen2.5-VL need to be implemented separately? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Qwen2_5_VLForEmbedding feature request;stale ### 🚀 The feature, motivation and pitch I have trained a "Qwen/Qwen2.5-VL-3B-Instruct" based vlm embedding model. When I try to encode embedding with vllm I got: `...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Qwen2_5_VLForEmbedding feature request;stale ### 🚀 The feature, motivation and pitch I have trained a "Qwen/Qwen2.5-VL-3B-Instruct" based vlm embedding model. When I try to encode embedding with vllm I got: `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
