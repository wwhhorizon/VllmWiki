# vllm-project/vllm#38837: [Bug]: Gemma4ToolParser.__init__() missing `tools` parameter — 400 error on tool calls

| 字段 | 值 |
| --- | --- |
| Issue | [#38837](https://github.com/vllm-project/vllm/issues/38837) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma4ToolParser.__init__() missing `tools` parameter — 400 error on tool calls

### Issue 正文摘录

## 🐛 Describe the bug `Gemma4ToolParser.__init__()` only accepts `(self, tokenizer)` but the base class `ToolParser.__init__()` expects `(self, tokenizer, tools)`. When vLLM instantiates the parser, it passes both arguments, resulting in: ``` 400 Gemma4ToolParser.__init__() takes 2 positional arguments but 3 were given ``` ### How to reproduce 1. Serve a Gemma 4 model with tool calling enabled: ```bash vllm serve nvidia/Gemma-4-31B-IT-NVFP4 \ --enable-auto-tool-choice \ --tool-call-parser gemma4 ``` 2. Send a chat completion request with `tools` specified 3. Get `400` error immediately ### Root cause The `tools` parameter was added to the base `ToolParser` class (in #38029), but `Gemma4ToolParser` (added in #38826) was written against the old signature. Every other tool parser accepts `(tokenizer, tools)`: ```python # All other parsers (mistral, hermes, functiongemma, etc.) def __init__(self, tokenizer: TokenizerLike, tools: list[Tool] | None = None): super().__init__(tokenizer, tools) # Gemma4ToolParser (broken) def __init__(self, tokenizer: TokenizerLike): super().__init__(tokenizer) ``` ### Suggested fix Three-line change in `vllm/tool_parsers/gemma4_tool_parser.py`: ```diff -f...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: l-parser gemma4 ``` 2. Send a chat completion request with `tools` specified 3. Get `400` error immediately ### Root cause The `tools` parameter was added to the base `ToolParser` class (in #38029), but `Gemma4ToolParse...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ith tool calling enabled: ```bash vllm serve nvidia/Gemma-4-31B-IT-NVFP4 \ --enable-auto-tool-choice \ --tool-call-parser gemma4 ``` 2. Send a chat completion request with `tools` specified 3. Get `400` error immediatel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: super().__init__(tokenizer, tools) ``` - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Gemma4ToolParser.__init__() missing `tools` parameter — 400 error on tool calls ## 🐛 Describe the bug `Gemma4ToolParser.__init__()` only accepts `(self, tokenizer)` but the base class `ToolParser.__init__()` expe...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: __init__() takes 2 positional arguments but 3 were given ``` ### How to reproduce 1. Serve a Gemma 4 model with tool calling enabled: ```bash vllm serve nvidia/Gemma-4-31B-IT-NVFP4 \ --enable-auto-tool-choice \ --tool-c...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
