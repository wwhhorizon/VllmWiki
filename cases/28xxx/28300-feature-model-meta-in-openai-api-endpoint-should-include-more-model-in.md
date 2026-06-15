# vllm-project/vllm#28300: [Feature]: model meta in openai api endpoint should include more model information

| 字段 | 值 |
| --- | --- |
| Issue | [#28300](https://github.com/vllm-project/vllm/issues/28300) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: model meta in openai api endpoint should include more model information

### Issue 正文摘录

### 🚀 The feature, motivation and pitch model meta in openai api endpoint should include more model information like max_context_length, "thinking": 1, "citations": 1, ``` "info": { "meta": { "capabilities": { "vision": true, "document": true, "video": true, "audio": true, "citations": true, "thinking_budget": true, "thinking": true }, "short_description": "The most powerful language model in the Qwen series.", "max_context_length": 262144, "max_thinking_generation_length": 81920, "max_summary_generation_length": 32768, "abilities": { "vision": 1, "document": 1, "video": 1, "audio": 1, "mcp": 1, "citations": 1, "thinking_budget": 1, "thinking": 1 }, "chat_type": [ "t2t", "t2v", "t2i", "image_edit", "search", "artifacts", "web_dev", "deep_research", "travel" ], "mcp": [ "image-generation", "code-interpreter", "amap", "fire-crawl" ], "modality": [ "text" ] ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked quest...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: model meta in openai api endpoint should include more model information feature request;stale ### 🚀 The feature, motivation and pitch model meta in openai api endpoint should include more model information li...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: eta in openai api endpoint should include more model information feature request;stale ### 🚀 The feature, motivation and pitch model meta in openai api endpoint should include more model information like max_context_len...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: include more model information like max_context_length, "thinking": 1, "citations": 1, ``` "info": { "meta": { "capabilities": { "vision": true, "document": true, "video": true, "audio": true, "citations": true,
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: "t2v", "t2i", "image_edit", "search", "artifacts", "web_dev", "deep_research", "travel" ], "mcp": [ "image-generation", "code-interpreter", "amap",
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
