# vllm-project/vllm#39652: Gemma4ToolParser.__init__ missing 'tools' parameter causes TypeError

| 字段 | 值 |
| --- | --- |
| Issue | [#39652](https://github.com/vllm-project/vllm/issues/39652) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Gemma4ToolParser.__init__ missing 'tools' parameter causes TypeError

### Issue 正文摘录

## Description `Gemma4ToolParser.__init__()` does not accept the `tools` parameter that its parent class `ToolParser.__init__()` expects, causing a `TypeError` when tool calling is enabled with `--tool-call-parser gemma4`. ## Error ``` {"error":{"message":"Gemma4ToolParser.__init__() takes 2 positional arguments but 3 were given","type":"BadRequestError","param":null,"code":400}} ``` This occurs on any request that includes `tools` in the payload. ## Root Cause The parent class signature is: ```python class ToolParser: def __init__(self, tokenizer: TokenizerLike, tools: list[Tool] | None = None): ``` But `Gemma4ToolParser` only accepts `tokenizer`: ```python class Gemma4ToolParser(ToolParser): def __init__(self, tokenizer: TokenizerLike): super().__init__(tokenizer) ``` ## Fix ```diff --- a/vllm/tool_parsers/gemma4_tool_parser.py +++ b/vllm/tool_parsers/gemma4_tool_parser.py - def __init__(self, tokenizer: TokenizerLike): - super().__init__(tokenizer) + def __init__(self, tokenizer: TokenizerLike, tools=None): + super().__init__(tokenizer, tools) ``` ## Reproduction ```bash vllm serve google/gemma-4-26B-A4B-it \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --enforce-eag...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Gemma4ToolParser.__init__ missing 'tools' parameter causes TypeError ## Description `Gemma4ToolParser.__init__()` does not accept the `tools` parameter that its parent class `ToolParser.__init__()` expects, causing a `T
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 200 }' ``` ## Environment - vLLM: 0.18.2rc1.dev71+ge92668e83 - Image: `docker.io/vllm/vllm-openai-rocm:gemma4` - transformers: 5.5.0 - ROCm 7.2, AMD AI Max+ 395 Affects both `google/gemma-4-26B-A4B-it` and `google/gemma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: - vLLM: 0.18.2rc1.dev71+ge92668e83 - Image: `docker.io/vllm/vllm-openai-rocm:gemma4` - transformers: 5.5.0 - ROCm 7.2, AMD AI Max+ 395 Affects both `google/gemma-4-26B-A4B-it` and `google/gemma-4-31B-it` — any model usi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Gemma4ToolParser.__init__ missing 'tools' parameter causes TypeError ## Description `Gemma4ToolParser.__init__()` does not accept the `tools` parameter that its parent class `ToolParser.__init__()` expects, causing a `T
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ser.__init__() takes 2 positional arguments but 3 were given","type":"BadRequestError","param":null,"code":400}} ``` This occurs on any request that includes `tools` in the payload. ## Root Cause The parent class signat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
