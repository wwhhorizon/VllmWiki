# vllm-project/vllm#43398: SyntaxWarning: invalid escape sequence and spurious trust_remote_code warnings on startup

| 字段 | 值 |
| --- | --- |
| Issue | [#43398](https://github.com/vllm-project/vllm/issues/43398) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> SyntaxWarning: invalid escape sequence and spurious trust_remote_code warnings on startup

### Issue 正文摘录

## Bug Description Two minor issues on every vLLM startup: ### 1. SyntaxWarning: invalid escape sequence `\e` ``` /opt/vllm-source/vllm/entrypoints/openai/chat_completion/protocol.py:346: SyntaxWarning: invalid escape sequence '\e' "(e.g. 'abcdabcdabcd...' or '\emoji \emoji \emoji ...'). This feature " /opt/vllm-source/vllm/entrypoints/openai/completion/protocol.py:176: SyntaxWarning: invalid escape sequence '\e' "(e.g. 'abcdabcdabcd...' or '\emoji \emoji \emoji ...'). This feature " ``` The string literal contains `\emoji` which Python interprets as an invalid escape sequence. Should be either a raw string (`r"..."`) or use `\\emoji`. **Files:** - `vllm/entrypoints/openai/chat_completion/protocol.py:346` - `vllm/entrypoints/openai/completion/protocol.py:176` ### 2. Spurious `trust_remote_code` warning ``` (APIServer pid=1) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. (APIServer pid=1) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. ``` This warning is printed twice on every startup when `--trust-remote-code` is passed, even for models that DO use custom code (e.g., Q...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ed twice on every startup when `--trust-remote-code` is passed, even for models that DO use custom code (e.g., Qwen3-MoE). The warning comes from HuggingFace transformers when `trust_remote_code` is passed to a non-Auto...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ed it. ## Environment - vLLM version: 0.17.1 (via `ghcr.io/llm-d/llm-d-cuda:v0.6.0`) - Python 3.12 - Model: RedHatAI/Qwen3-30B-A3B-FP8-dynamic (reproduces with any model) ## Impact Low severity — these are cosmetic warn...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: cuda:v0.6.0`) - Python 3.12 - Model: RedHatAI/Qwen3-30B-A3B-FP8-dynamic (reproduces with any model) ## Impact Low severity — these are cosmetic warnings that don't affect functionality. However, they clutter logs and ca...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: not pass the flag to classes that don't need it. ## Environment - vLLM version: 0.17.1 (via `ghcr.io/llm-d/llm-d-cuda:v0.6.0`) - Python 3.12 - Model: RedHatAI/Qwen3-30B-A3B-FP8-dynamic (reproduces with any model) ## Imp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: /llm-d/llm-d-cuda:v0.6.0`) - Python 3.12 - Model: RedHatAI/Qwen3-30B-A3B-FP8-dynamic (reproduces with any model) ## Impact Low severity — these are cosmetic warnings that don't affect functionality. However, they clutte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
