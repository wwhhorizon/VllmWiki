# vllm-project/vllm#38674: [Bug]: Jamba tool parser crashes on Mistral-style [TOOL_CALLS] models with standard HF tokenizer (e.g., Apriel-Nemotron-15b)

| 字段 | 值 |
| --- | --- |
| Issue | [#38674](https://github.com/vllm-project/vllm/issues/38674) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Jamba tool parser crashes on Mistral-style [TOOL_CALLS] models with standard HF tokenizer (e.g., Apriel-Nemotron-15b)

### Issue 正文摘录

### Your current environment vLLM version: v0.18.0 PyTorch version: 2.10.0+cu128 Python version: 3.12 GPU: NVIDIA A100-SXM4-80GB OS: Ubuntu 22.04 ### 🐛 Describe the bug **Model:** ServiceNow-AI/Apriel-Nemotron-15b-Thinker (HuggingFace) The jamba tool call parser hardcodes / XML tags as the expected tool call delimiters. Models that use the Mistral-style [TOOL_CALLS] single-token format with a standard HuggingFace tokenizer (not MistralTokenizer) cannot use any built-in tool parser: The jamba parser crashes because is not in the vocab The mistral parser is not a fit because it expects MistralTokenizer (tekken/sentencepiece) The parser hardcodes the old format in __init__: # vllm/tool_parsers/jamba_tool_parser.py self.tool_calls_start_token: str = " " self.tool_calls_end_token: str = " " ... self.tool_calls_start_token_id = self.vocab.get(self.tool_calls_start_token) self.tool_calls_end_token_id = self.vocab.get(self.tool_calls_end_token) if self.tool_calls_start_token_id is None or self.tool_calls_end_token_id is None: raise RuntimeError( "Jamba Tool parser could not locate tool calls start/end " "tokens in the tokenizer!" ) **How to reproduce** Start the server: ``` vllm serve Ser...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Jamba tool parser crashes on Mistral-style [TOOL_CALLS] models with standard HF tokenizer (e.g., Apriel-Nemotron-15b) bug ### Your current environment vLLM version: v0.18.0 PyTorch version: 2.10.0+cu128 Python ve...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nizer (e.g., Apriel-Nemotron-15b) bug ### Your current environment vLLM version: v0.18.0 PyTorch version: 2.10.0+cu128 Python version: 3.12 GPU: NVIDIA A100-SXM4-80GB OS: Ubuntu 22.04 ### 🐛 Describe the bug **Model:** S...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : v0.18.0 PyTorch version: 2.10.0+cu128 Python version: 3.12 GPU: NVIDIA A100-SXM4-80GB OS: Ubuntu 22.04 ### 🐛 Describe the bug **Model:** ServiceNow-AI/Apriel-Nemotron-15b-Thinker (HuggingFace) The jamba tool call pars...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ool calls start/end " "tokens in the tokenizer!" ) **How to reproduce** Start the server: ``` vllm serve ServiceNow-AI/Apriel-Nemotron-15b-Thinker \ --enable-auto-tool-choice \ --tool-call-parser jamba \ --max-model-len...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tool calls start/end tokens in the tokenizer!", "type": "InternalServerError", "param": null, "code": 500 } } ``` **Server log confirms:** INFO: 127.0.0.1:55058 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
