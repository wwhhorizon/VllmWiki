# vllm-project/vllm#11392: [Bug]: [v0.6.5] Streaming tool call responses with the hermes template is inconsistent with the non-stream version.

| 字段 | 值 |
| --- | --- |
| Issue | [#11392](https://github.com/vllm-project/vllm/issues/11392) |
| 状态 | closed |
| 标签 | bug;stale;tool-calling |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [v0.6.5] Streaming tool call responses with the hermes template is inconsistent with the non-stream version.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The streaming feature combined with tool calling is still quite bugged. If we POST the following tool call generation request to vllm endpoint /v1/chat/completions: ```json { "model": "Qwen/Qwen2.5-7B-Instruct", "messages": [ { "role": "system", "content": "# Instructions\n\nYou are an AI assistant integrated into Theia IDE, designed to assist software developers with concise answers to programming-related questions. Your goal is to enhance\nproductivity with quick, relevant solutions, explanations, and best practices. Keep responses short, delivering valuable insights and direct solutions.\n\nUse the following functions to interact with the workspace files as needed:\n- **You can call function: getWorkspaceDirectoryStructure(): Retrieve the complete directory structure of the workspace, listing only directories (no file contents). This structure excludes specific directories,\n such as node_modules and hidden files, ensuring paths are within workspace boundaries.**: Returns the complete directory structure.\n- **You can call function: getWorkspaceFileList(path: string): List files and director...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: l responses with the hermes template is inconsistent with the non-stream version. bug;stale;tool-calling ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The streaming feature comb...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: check with the Qwen2.5-7B-Instruct model. - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: eam version. bug;stale;tool-calling ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The streaming feature combined with tool calling is still quite bugged. If we POST the followin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ith the hermes template is inconsistent with the non-stream version. bug;stale;tool-calling ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug The streaming feature combined with too...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: s. development ci_build;frontend_api;hardware_porting;model_support cuda;triton build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
