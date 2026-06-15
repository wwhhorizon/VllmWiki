# vllm-project/vllm#36907: [Bug]: `resolve_chat_template_kwargs` silently drops chat template kwargs when `chat_template` is passed in as chat template name instead of Jinja

| 字段 | 值 |
| --- | --- |
| Issue | [#36907](https://github.com/vllm-project/vllm/issues/36907) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `resolve_chat_template_kwargs` silently drops chat template kwargs when `chat_template` is passed in as chat template name instead of Jinja

### Issue 正文摘录

## 🐛 Describe the bug When a user passes a **chat template name** (e.g. `"tool_use"`, `"default"`) instead of an actual Jinja template string via the `chat_template` parameter, the `resolve_chat_template` → `resolve_chat_template_kwargs` pipeline silently drops valid template kwargs like `tools`, `documents`, etc. This happens because the template name string is never resolved to the actual Jinja content before being parsed for variable detection. ### Root Cause The issue spans two functions in [`vllm/renderers/hf.py`](https://github.com/vllm-project/vllm/blob/releases/v0.17.0/vllm/renderers/hf.py): **1. `resolve_chat_template` ([L110](https://github.com/vllm-project/vllm/blob/releases/v0.17.0/vllm/renderers/hf.py#L110))** — Priority 1 returns the `chat_template` string as-is without checking whether it's a Jinja template or a template name: ```python def resolve_chat_template(tokenizer, chat_template, tools, *, model_config): # 1st priority: The given chat template if chat_template is not None: return chat_template # returns "tool_use" verbatim, not the Jinja content ... ``` HuggingFace tokenizers support named templates via `tokenizer.chat_template` being a `dict` (e.g. `{"defau...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: tion. ### Root Cause The issue spans two functions in [`vllm/renderers/hf.py`](https://github.com/vllm-project/vllm/blob/releases/v0.17.0/vllm/renderers/hf.py): **1. `resolve_chat_template` ([L110](https://github.com/vl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ves a name to the actual Jinja string. But `resolve_chat_template` short-circuits at Priority 1 and never calls `get_chat_template` when `chat_template is not None`. **2. `resolve_chat_template_kwargs` ([L433](https://g...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ts. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
