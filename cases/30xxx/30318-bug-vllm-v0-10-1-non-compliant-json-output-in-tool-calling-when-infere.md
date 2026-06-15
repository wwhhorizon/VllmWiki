# vllm-project/vllm#30318: [Bug]: vllm v0.10.1 - Non-compliant JSON Output in Tool Calling When Inferencing DeepSeek-V3.1-Terminus

| 字段 | 值 |
| --- | --- |
| Issue | [#30318](https://github.com/vllm-project/vllm/issues/30318) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm v0.10.1 - Non-compliant JSON Output in Tool Calling When Inferencing DeepSeek-V3.1-Terminus

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When inferring, the following issue occurs with a certain probability: the result returned through tool calling may not be a complete JSON string. common result: ``` { "role": "assistant", "content": " -", "tool_calls": [ { "id": "chatcmpl-tool-xxx", "type": "function", "function": { "name": "read_file", "arguments": "{\"path\": \"/Users/xxx/Desktop/xxx/projects/cline/src/core/task/index.ts\", \"limit\": 50}" } } ] } ``` uncommon result ``` { "role": "assistant", "content": "让我继续查看这个文件的关键部分：", "tool_calls": [ { "id": "chatcmpl-tool-xxx", "type": "function", "function": { "name": "read_file", "arguments": "{\"path\": \"/Users/xxx/Desktop/xxx/projects/cline/src/core/task/index.ts\", \"offset\": 100, \"limit\": 50" } } ] } ``` In the arguments section, a closing brace ```}``` is missing at the end. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: g]: vllm v0.10.1 - Non-compliant JSON Output in Tool Calling When Inferencing DeepSeek-V3.1-Terminus bug ### Your current environment ### 🐛 Describe the bug When inferring, the following issue occurs with a certain prob...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nd. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Yo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
