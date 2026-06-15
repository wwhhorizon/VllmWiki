# vllm-project/vllm#33311: [Feature]: support pixel_values_videos input for VLM

| 字段 | 值 |
| --- | --- |
| Issue | [#33311](https://github.com/vllm-project/vllm/issues/33311) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support pixel_values_videos input for VLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch In RL training, to avoid [Retokenization Drift](https://blog.vllm.ai/2025/10/22/agent-lightning.html), RL frameworks choose `token-in-token-out` for generation. While it works perfect for text/image, there's still some mismatch between video processing. In verl, we `apply_chat_template` to messages with video: https://github.com/verl-project/verl/blob/main/verl/experimental/agent_loop/agent_loop.py#L286-L293 Then pass the prompt_token_ids and **raw video** to vLLM: https://github.com/verl-project/verl/blob/main/verl/workers/rollout/vllm_rollout/vllm_async_server.py#L490 The mismatch occurs in the video processor between client and vLLM server: https://github.com/verl-project/verl/issues/5024 So we may need to support `pixel_values_videos` tensor input to bypass video processor in server side. https://github.com/vllm-project/vllm/blob/main/vllm/multimodal/inputs.py#L71-L82 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/lat...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: feature, motivation and pitch In RL training, to avoid [Retokenization Drift](https://blog.vllm.ai/2025/10/22/agent-lightning.html), RL frameworks choose `token-in-token-out` for generation. While it works perfect for t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: generation. While it works perfect for text/image, there's still some mismatch between video processing. In verl, we `apply_chat_template` to messages with video: https://github.com/verl-project/verl/blob/main/verl/expe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: support pixel_values_videos input for VLM feature request;unstale ### 🚀 The feature, motivation and pitch In RL training, to avoid [Retokenization Drift](https://blog.vllm.ai/2025/10/22/agent-lightning.html),...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support pixel_values_videos input for VLM feature request;unstale ### 🚀 The feature, motivation and pitch In RL training, to avoid [Retokenization Drift](https://blog.vllm.ai/2025/10/22/agent-lightning.html),...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
