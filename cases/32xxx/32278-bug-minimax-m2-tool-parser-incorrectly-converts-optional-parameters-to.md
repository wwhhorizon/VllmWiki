# vllm-project/vllm#32278: [Bug]: MiniMax M2 Tool Parser Incorrectly Converts Optional Parameters to null

| 字段 | 值 |
| --- | --- |
| Issue | [#32278](https://github.com/vllm-project/vllm/issues/32278) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MiniMax M2 Tool Parser Incorrectly Converts Optional Parameters to null

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Bug report mostly written by Claude Code, which found and fixed this bug for me. ## Summary The MiniMax M2 tool parser (`minimax_m2_tool_parser.py`) has a bug that causes all `Optional[T]` parameters to be converted to `null` regardless of their actual values. This makes it impossible to pass actual values to optional string parameters. ## Version Information - **vLLM Version**: 0.14.0rc1.dev414+ga1648c404 - **Affected File**: `vllm/tool_parsers/minimax_m2_tool_parser.py` - **Affected Method**: `_convert_param_value_with_types()` at line 225 ## Description When a tool has an optional parameter (e.g., `logfile: Optional[str]`), the parser incorrectly returns `None` for ANY value passed to that parameter. The bug occurs because the code checks if `"null"` is in the list of allowed types (which it is for `Optional[T]`), rather than checking if the actual value IS null. ## Steps to Reproduce ### 1. Define a tool with an optional string parameter (e.g., as an Open WebUI plugin): ```python class Tool: def run_shell( self, command: str, logfile: Optional[str] = None ) -> str: """Execute a shell command. :param command: The shell command...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s it impossible to pass actual values to optional string parameters. ## Version Information - **vLLM Version**: 0.14.0rc1.dev414+ga1648c404 - **Affected File**: `vllm/tool_parsers/minimax_m2_tool_parser.py` - **Affected...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 25) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: sible to pass actual values to optional string parameters. ## Version Information - **vLLM Version**: 0.14.0rc1.dev414+ga1648c404 - **Affected File**: `vllm/tool_parsers/minimax_m2_tool_parser.py` - **Affected Method**:...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: nal[T]`), rather than checking if the actual value IS null. ## Steps to Reproduce ### 1. Define a tool with an optional string parameter (e.g., as an Open WebUI plugin): ```python class Tool: def run_shell( self, comman...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: iMax M2 Tool Parser Incorrectly Converts Optional Parameters to null bug;stale ### Your current environment ### 🐛 Describe the bug Bug report mostly written by Claude Code, which found and fixed this bug for me. ## Summ...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
