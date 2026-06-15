# vllm-project/vllm#42781: [Bug]: Gemma 4 speculative decoding truncating reasoning output

| 字段 | 值 |
| --- | --- |
| Issue | [#42781](https://github.com/vllm-project/vllm/issues/42781) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma 4 speculative decoding truncating reasoning output

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using `pi.dev` I noticed that at some point the reasoning output was getting partially dropped, so I tried to duplicate it with something simple. If I run this a dozen times when MTP is enabled, usually a few of them will have (likely) dropped reasoning traces. Without MTP enabled I don't see the drop at all. The following is the input file and an example truncated output via cURL. Here's the JSON payload in the `@input` file: ```json { "model": "google/gemma-4-31B-it", "messages": [ { "role": "developer", "content": "You are an expert coding assistant operating inside pi, a coding agent harness. You help users by reading files, executing commands, editing code, and writing new files.\n\nAvailable tools:\n- read: Read file contents\n- edit: Make surgical edits to files (find exact text and replace)\n- write: Create or overwrite files\n\nIn addition to the tools above, you may have access to other custom tools depending on the project.\n\nGuidelines:\n- Use bash for file operations like ls, rg, find\n- Use read to examine files instead of cat or sed.\n- Use edit for precise changes (old text must match exactly).\n- Use write...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: d\n- Use read to examine files instead of cat or sed.\n- Use edit for precise changes (old text must match exactly).\n- Use write only for new files or complete rewrites.\n- Be concise in your responses\n- Show file pat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Gemma 4 speculative decoding truncating reasoning output bug ### Your current environment ### 🐛 Describe the bug When using `pi.dev` I noticed that at some point the reasoning output was getting partially dropped...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Gemma 4 speculative decoding truncating reasoning output bug ### Your current environment ### 🐛 Describe the bug When using `pi.dev` I noticed that at some point the reasoning output was getting partially dropped...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: gpu"] ipc: host environment: VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS: "1" HF_HUB_OFFLINE: "1" command: - /root/model - --served-model-name - google/gemma-4-31B-it - --tool-call-parser - gemma4 - --reasoning-parser - ge...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: capabilities: ["gpu"] ipc: host environment: VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS: "1" HF_HUB_OFFLINE: "1" command: - /root/model - --served-model-name - google/gemma-4-31B-it - --tool-call-parser - gemma4 - --reaso...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
