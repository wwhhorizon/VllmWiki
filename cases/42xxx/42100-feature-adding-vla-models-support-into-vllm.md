# vllm-project/vllm#42100: [Feature]: Adding VLA models support into vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#42100](https://github.com/vllm-project/vllm/issues/42100) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Adding VLA models support into vLLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Background vLLM already provides a high-throughput inference and serving stack for LLMs and multimodal language models. However, Vision-Language-Action (VLA) models used in robotics and autonomous driving are not currently supported as a first-class model family in vLLM. VLA models extend VLMs by taking multimodal observations such as images, language instructions, and robot/vehicle state, and returning actions or trajectories rather than only text tokens. Supporting this class of models in vLLM would enable: - high-throughput batched rollouts for robotics simulation, evaluation, and RL; - a unified serving backend for VLA models instead of one-off policy servers; - reuse of vLLM’s scheduler, request queueing, tensor/pipeline parallelism, metrics, and OpenAI-compatible serving infrastructure; - a clean extension point for future action-output models. There is already implementation work in SGLang that can be used as a reference for scoping and parity testing: - Alpamayo-R1 VLA support: https://github.com/sgl-project/sglang/pull/21059 - π0 VLA support: https://github.com/sgl-project/sglang/pull/23504 - GR00T-N1.7 VLA support: https://gith...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Adding VLA models support into vLLM feature request ### 🚀 The feature, motivation and pitch ### Background vLLM already provides a high-throughput inference and serving stack for LLMs and multimodal language...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Adding VLA models support into vLLM feature request ### 🚀 The feature, motivation and pitch ### Background vLLM already provides a high-throughput inference and serving stack for LLMs and multimodal language...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ture, motivation and pitch ### Background vLLM already provides a high-throughput inference and serving stack for LLMs and multimodal language models. However, Vision-Language-Action (VLA) models used in robotics and au...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: - reuse of vLLM’s scheduler, request queueing, tensor/pipeline parallelism, metrics, and OpenAI-compatible serving infrastructure; - a clean extension point for future action-output models. There is already implementati...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ollouts for robotics simulation, evaluation, and RL; - a unified serving backend for VLA models instead of one-off policy servers; - reuse of vLLM’s scheduler, request queueing, tensor/pipeline parallelism, metrics, and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
