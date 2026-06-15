# vllm-project/vllm#30439: [Bug]: Qwen3 Coder parser does not stream tool call arguments

| 字段 | 值 |
| --- | --- |
| Issue | [#30439](https://github.com/vllm-project/vllm/issues/30439) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 Coder parser does not stream tool call arguments

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using qwen3 coder to perform a tool call, does not send a chunk delta until the entire argument is parsed. This is particularly problematic with long tool call parameters, like code. The stream halts until the entire code block is sent, which may be thousands of tokens. There's no indication anything is happening since no chunks are sent. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nt. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: tool call parameters, like code. The stream halts until the entire code block is sent, which may be thousands of tokens. There's no indication anything is happening since no chunks are sent. ### Before submitting a new...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3 Coder parser does not stream tool call arguments bug;stale ### Your current environment ### 🐛 Describe the bug When using qwen3 coder to perform a tool call, does not send a chunk delta until the entire arg...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Qwen3 Coder parser does not stream tool call arguments bug;stale ### Your current environment ### 🐛 Describe the bug When using qwen3 coder to perform a tool call, does not send a chunk delta until the entire arg...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
