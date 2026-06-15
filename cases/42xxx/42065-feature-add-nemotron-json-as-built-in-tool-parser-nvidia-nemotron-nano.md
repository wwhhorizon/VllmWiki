# vllm-project/vllm#42065: [Feature]: Add nemotron_json as built-in tool parser (NVIDIA Nemotron-Nano-9B-v2 plugin breaks against v0.20.x module reorg)

| 字段 | 值 |
| --- | --- |
| Issue | [#42065](https://github.com/vllm-project/vllm/issues/42065) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add nemotron_json as built-in tool parser (NVIDIA Nemotron-Nano-9B-v2 plugin breaks against v0.20.x module reorg)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ## Context `nvidia/NVIDIA-Nemotron-Nano-9B-v2` ships an out-of-tree tool-call parser plugin (`nemotron_toolcall_parser_no_streaming.py`) that NVIDIA's own [vLLM cookbook][cookbook] tells users to load via: --enable-auto-tool-choice --tool-parser-plugin " /nemotron_toolcall_parser_no_streaming.py" --tool-call-parser nemotron_json The cookbook pins vLLM to commit `75531a6c…` (2025-08-15). The plugin file in NVIDIA's HF model repo has not been updated since. [cookbook]: https://github.com/NVIDIA-NeMo/Nemotron/blob/main/usage-cookbook/Nemotron-Nano-9B-v2/vllm_cookbook.ipynb ## What breaks on v0.20.x Three import paths in the plugin no longer resolve, plus the `ToolParser.__init__` calling convention changed: | Symbol / surface | Old (Aug-2025 vLLM) | v0.20.1 | |---|---|---| | `ChatCompletionRequest` | `vllm.entrypoints.openai.protocol` | `vllm.entrypoints.openai.chat_completion.protocol` | | `FunctionCall, ToolCall, DeltaFunctionCall, DeltaToolCall, DeltaMessage, ExtractedToolCallInformation` | `vllm.entrypoints.openai.protocol` | `vllm.entrypoints.openai.engine.protocol` | | `ToolParser, ToolParserManager` | `vllm.entrypoints.openai.tool_parser...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ins vLLM to commit `75531a6c…` (2025-08-15). The plugin file in NVIDIA's HF model repo has not been updated since. [cookbook]: https://github.com/NVIDIA-NeMo/Nemotron/blob/main/usage-cookbook/Nemotron-Nano-9B-v2/vllm_co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: emotron-Nano-9B-v2/vllm_cookbook.ipynb ## What breaks on v0.20.x Three import paths in the plugin no longer resolve, plus the `ToolParser.__init__` calling convention changed: | Symbol / surface | Old (Aug-2025 vLLM) |...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: eproduction vLLM 0.20.1 + `vllm serve nvidia/NVIDIA-Nemotron-Nano-9B-v2-NVFP4 --enable-auto-tool-choice --tool-parser-plugin --tool-call-parser nemotron_json` with the upstream plugin file → ImportError chain ending in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: , motivation and pitch ## Context `nvidia/NVIDIA-Nemotron-Nano-9B-v2` ships an out-of-tree tool-call parser plugin (`nemotron_toolcall_parser_no_streaming.py`) that NVIDIA's own [vLLM cookbook][cookbook] tells users to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Nemotron-Nano-9B-v2 plugin breaks against v0.20.x module reorg) feature request ### 🚀 The feature, motivation and pitch ## Context `nvidia/NVIDIA-Nemotron-Nano-9B-v2` ships an out-of-tree tool-call parser plugin (`nemot...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
