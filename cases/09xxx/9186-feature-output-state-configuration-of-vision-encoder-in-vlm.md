# vllm-project/vllm#9186: [Feature]: Output state configuration of vision encoder In VLM

| 字段 | 值 |
| --- | --- |
| Issue | [#9186](https://github.com/vllm-project/vllm/issues/9186) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Output state configuration of vision encoder In VLM

### Issue 正文摘录

### Anything you want to discuss about vllm. When siglip or clip acts as a multimodal vision encoder, there will have several cases: - The output state of an intermediate layer is used without layer normalization - The output state of the last layer is used without layer normalization - The output state of the last layer is used with layer normalization For example, In the `LLaVA-Next` code implementation, `post_layernorm` is not used. #8106 #8155 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Output state configuration of vision encoder In VLM feature request ### Anything you want to discuss about vllm. When siglip or clip acts as a multimodal vision encoder, there will have several cases: - The o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 155 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Output state configuration of vision encoder In VLM feature request ### Anything you want to discuss about vllm. When siglip or clip acts as a multimodal vision encoder, there will have several cases: - The o...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
