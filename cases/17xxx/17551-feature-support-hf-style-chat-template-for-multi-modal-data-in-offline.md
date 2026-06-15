# vllm-project/vllm#17551: [Feature]: Support HF-style chat template for multi-modal data in offline chat

| 字段 | 值 |
| --- | --- |
| Issue | [#17551](https://github.com/vllm-project/vllm/issues/17551) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support HF-style chat template for multi-modal data in offline chat

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, we expect `image_url`, `audio_url` etc. to be inside the messages that are passed to the chat template. We would like to expand this to supporting `image`, `audio` etc. inputs, just like in HuggingFace Transformers: ```python messages = [ { "role": "user", "content": [ {"type": "image"}, {"type": "text", "text": "Can you describe this image?"} ] }, ] ```` To avoid having to pass multi-modal inputs separately, we propose the following extension: ```python messages = [ { "role": "user", "content": [ {"type": "image", "image": image}, {"type": "text", "text": "Can you describe this image?"} ] }, ] ```` This lets us pass multi-modal data such as PIL images to `LLM.chat` directly without having to encode them into base64 URLs. ### Alternatives _No response_ ### Additional context cc @ywang96 @Isotr0py @hmellor ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support HF-style chat template for multi-modal data in offline chat good first issue;feature request ### 🚀 The feature, motivation and pitch Currently, we expect `image_url`, `audio_url` etc. to be inside the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: t template for multi-modal data in offline chat good first issue;feature request ### 🚀 The feature, motivation and pitch Currently, we expect `image_url`, `audio_url` etc. to be inside the messages that are passed to th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
