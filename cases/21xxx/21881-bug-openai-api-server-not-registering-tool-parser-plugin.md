# vllm-project/vllm#21881: [Bug]: openai API server not registering `tool-parser-plugin`

| 字段 | 值 |
| --- | --- |
| Issue | [#21881](https://github.com/vllm-project/vllm/issues/21881) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: openai API server not registering `tool-parser-plugin`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to use custom tool call parsers, the server will not register a `tool-parser-plugin`. For a minimal tool call parser: ```python from typing import Any, Optional, Union from vllm.entrypoints.openai.tool_parsers import ToolParserManager, ToolParser from vllm.entrypoints.openai.protocol import ExtractedToolCallInformation from vllm.entrypoints.openai.protocol import DeltaMessage from vllm.entrypoints.openai.protocol import ChatCompletionRequest from vllm.transformers_utils.tokenizer import AnyTokenizer @ToolParserManager.register_module(["example"]) class ExampleToolParser(ToolParser): def __init__(self, tokenizer: AnyTokenizer): super().__init__(tokenizer) def adjust_request( self, request: ChatCompletionRequest) -> ChatCompletionRequest: return request def extract_tool_calls_streaming( self, *args, **kwargs, ) -> Union[DeltaMessage, None]: return DeltaMessage( role="assistant", content="", tool_calls=[], ) def extract_tool_calls( self, *args, **kwargs, ) -> ExtractedToolCallInformation: return ExtractedToolCallInformation(tools_called=False, tool_calls=[], content=text) ``` The following command produces an error: ```b...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: olParser from vllm.entrypoints.openai.protocol import ExtractedToolCallInformation from vllm.entrypoints.openai.protocol import DeltaMessage from vllm.entrypoints.openai.protocol import ChatCompletionRequest from vllm.t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: -parser-plugin`. For a minimal tool call parser: ```python from typing import Any, Optional, Union from vllm.entrypoints.openai.tool_parsers import ToolParserManager, ToolParser from vllm.entrypoints.openai.protocol imp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: module named 'libtpu' DEBUG 07-29 22:01:55 [__init__.py:52] Checking if CUDA platform is available. DEBUG 07-29 22:01:55 [__init__.py:76] Exception happens when checking CUDA platform: NVML Shared Library Not Found DEBU...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: this problem in a linux environment with `vllm==0.10.0` and was able to reproduce the problem on my mac on the main branch. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: lInformation: return ExtractedToolCallInformation(tools_called=False, tool_calls=[], content=text) ``` The following command produces an error: ```bash python -m vllm.entrypoints.openai.api_serve

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
