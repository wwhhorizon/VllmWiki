# vllm-project/vllm#30129: [Feature]: About video input for qwen3vl

| 字段 | 值 |
| --- | --- |
| Issue | [#30129](https://github.com/vllm-project/vllm/issues/30129) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: About video input for qwen3vl

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I tried using base64 encoding to provide video input for vllm inference, but it seems this input method is not yet supported by Qwen3VL (I've seen similar issues reported elsewhere). Currently, I can only specify parameters like fps/maximum frames and then pass the local path or URL of the video. However, in my scenario, my videos are not uniformly sampled; I need to manually sample them first and then input multiple frames. Is there a way to achieve this input method now? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: About video input for qwen3vl feature request;stale ### 🚀 The feature, motivation and pitch I tried using base64 encoding to provide video input for vllm inference, but it seems this input method is not yet s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: (I've seen similar issues reported elsewhere). Currently, I can only specify parameters like fps/maximum frames and then pass the local path or URL of the video. However, in my scenario, my videos are not uniformly samp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: thod is not yet supported by Qwen3VL (I've seen similar issues reported elsewhere). Currently, I can only specify parameters like fps/maximum frames and then pass the local path or URL of the video. However, in my scena...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: About video input for qwen3vl feature request;stale ### 🚀 The feature, motivation and pitch I tried using base64 encoding to provide video input for vllm inference, but it seems this input method is not yet s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
