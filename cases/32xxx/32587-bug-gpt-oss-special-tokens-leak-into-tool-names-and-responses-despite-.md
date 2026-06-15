# vllm-project/vllm#32587: [Bug]: gpt-oss special tokens leak into tool names and responses despite `reasoning_parser: "openai_gptoss"`

| 字段 | 值 |
| --- | --- |
| Issue | [#32587](https://github.com/vllm-project/vllm/issues/32587) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: gpt-oss special tokens leak into tool names and responses despite `reasoning_parser: "openai_gptoss"`

### Issue 正文摘录

### Your current environment ## Environment | Component | Version | | ---------------- | -------------------- | | vLLM | 0.13.0 | | Model | `openai/gpt-oss-20b` | | GPU | NVIDIA H100 | | Python | 3.11 | | deepagents | 0.3.5 | | langchain-openai | 1.1.7 | | langchain | 1.2.3 | ### 🐛 Describe the bug ## Server Configuration ```yaml model: openai/gpt-oss-20b served_model_name: gpt-oss-20b gpu_memory_utilization: 0.93 tensor_parallel_size: 1 max_num_batched_tokens: 8192 enable_prefix_caching: false reasoning_parser: openai_gptoss tool_call_parser: openai enable_auto_tool_choice: true ``` ## Bug Description When using `gpt-oss-20b` with tool calling enabled, special tokens (` commentary`) are **leaking into tool names and response content**, despite having `reasoning_parser: "openai_gptoss"` configured. ### Use Case I'm building a multi-agent code generation system using the [deepagents](https://github.com/langchain-ai/deepagents) framework. The orchestrator agent coordinates multiple subagents and uses tools like `ls`, `write_file`, `task`, etc. to generate code. ### Observed Issues Both issues occur **intermittently** - the model may work correctly for the first few steps, but random...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: gpt-oss special tokens leak into tool names and responses despite `reasoning_parser: "openai_gptoss"` bug ### Your current environment ## Environment | Component | Version | | ---------------- | --------------
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: | Model | `openai/gpt-oss-20b` | | GPU | NVIDIA H100 | | Python | 3.11 | | deepagents | 0.3.5 | | langchain-openai | 1.1.7 | | langchain | 1.2.3 | ### 🐛 Describe the bug ##
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: gpt-oss special tokens leak into tool names and responses despite `reasoning_parser: "openai_gptoss"` bug ### Your current environment ## Environment | Component | Version | | ---------------- | ---
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: r_parallel_size: 1 max_num_batched_tokens: 8192 enable_prefix_caching: false reasoning_parser: openai_gptoss tool_call_parser: openai enable_auto_tool_choice: true ``` ## Bug Description When using `gpt-oss-20b` with to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ith.langchain.com/public/feccb7b6-21c9-4257-97c0-26563306672c/r 2. **BadRequestError on follow-up requests**: When the corrupted response is added to message history and sent in a subsequent request, vLLM rejects it wit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
