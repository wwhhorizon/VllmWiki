# vllm-project/vllm#43728: [Bug] Inconsistent parameter names (`thinking` vs `enable_thinking`) between reasoning parsers and chat templates causes content:null

| 字段 | 值 |
| --- | --- |
| Issue | [#43728](https://github.com/vllm-project/vllm/issues/43728) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] Inconsistent parameter names (`thinking` vs `enable_thinking`) between reasoning parsers and chat templates causes content:null

### Issue 正文摘录

## Summary Different reasoning parsers and chat templates use inconsistent parameter names (`thinking` vs `enable_thinking`) in `chat_template_kwargs` to control the thinking/reasoning mode. This causes `content: null` and incorrect reasoning/content separation when the parameter name used by the user doesn't match what the reasoning parser reads. ## Current State The `chat_template_kwargs` flows through two independent code paths that read different parameter names: 1. **Chat Template (Jinja2)** — controls whether thinking tokens are injected into the model input 2. **Reasoning Parser (Python)** — controls whether model output is split into reasoning/content These two paths are completely independent and have no synchronization mechanism. ### Reasoning Parsers | Parser | Parameter Read | Default | File | |--------|---------------|---------|------| | `Qwen3ReasoningParser` | `enable_thinking` | `True` | `vllm/reasoning/qwen3_reasoning_parser.py:42` | | `NemotronV3ReasoningParser` | `enable_thinking` | — | `vllm/reasoning/nemotron_v3_reasoning_parser.py:28` | | `HunyuanA13BReasoningParser` | `enable_thinking` | — | `vllm/reasoning/hunyuan_a13b_reasoning_parser.py` | | `DeepSeekV3Re...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: late (Jinja2)** — controls whether thinking tokens are injected into the model input 2. **Reasoning Parser (Python)** — controls whether model output is split into reasoning/content These two paths are completely indepe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: et("thinking", True)) # Proposed - accept both, with enable_thinking as fallback thinking = bool(chat_kwargs.get("thinking", chat_kwargs.get("enable_thinking", True))) ``` This same fix should be applied to all parsers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: two paths are completely independent and have no synchronization mechanism. ### Reasoning Parsers | Parser | Parameter Read | Default | File | |--------|---------------|---------|------| | `Qwen3ReasoningParser` | `enab...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Is Not a Duplicate - #40424 addresses `content:null` for NemotronV3 specifically (different root cause: missing `enable_thinking` kwarg) - #43401 maps `reasoning_effort` to `enable_thinking` (different direction: effort...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: epSeekV3ReasoningParser` | **both** (`thinking or enable_thinking`) | `False` | `vllm/reasoning/deepseek_v3_reasoning_parser.py:33-35` | | `DeepSeekV3ReasoningWithThinkingParser` | **both** | `True` | `vllm/reasoning/de...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
