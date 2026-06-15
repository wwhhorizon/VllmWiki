# vllm-project/vllm#41065: [Bug]: MiniMaxM2Parser.__init__() crashes with unexpected keyword argument 'chat_template_kwargs'

| 字段 | 值 |
| --- | --- |
| Issue | [#41065](https://github.com/vllm-project/vllm/issues/41065) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: MiniMaxM2Parser.__init__() crashes with unexpected keyword argument 'chat_template_kwargs'

### Issue 正文摘录

### Your current environment Not required to reproduce — this is a pure Python logic bug that crashes before any model is loaded. ### 🐛 Describe the bug `MiniMaxM2Parser.__init__()` does not accept `**kwargs`, but `serving.py` always passes `chat_template_kwargs` when instantiating parsers. This causes a `TypeError` crash on **every request** when using the MiniMax M2 parser. **Root cause:** PR #39683 fixed the missing `tools` parameter in `MiniMaxM2Parser.__init__()`, but forgot to also add `**kwargs`. The serving layer at [`serving.py:571-575`](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/chat_completion/serving.py#L571-L575) instantiates all parsers with: ```python self.parser_cls( tokenizer, request.tools, chat_template_kwargs=chat_template_kwargs, # ← MiniMaxM2Parser can't accept this ) ``` But `MiniMaxM2Parser.__init__` is currently: ```python def __init__(self, tokenizer: TokenizerLike, tools: list[Tool] | None = None): # ← missing **kwargs ``` ### Minimal reproduction (no GPU needed) ```python from unittest.mock import MagicMock from vllm.parser.minimax_m2_parser import MiniMaxM2Parser tokenizer = MagicMock() tokenizer.get_vocab.return_value = {"...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ent 'chat_template_kwargs' ### Your current environment Not required to reproduce — this is a pure Python logic bug that crashes before any model is loaded. ### 🐛 Describe the bug `MiniMaxM2Parser.__init__()` does not a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ### Minimal reproduction (no GPU needed) ```python from unittest.mock import MagicMock from vllm.parser.minimax_m2_parser import MiniMaxM2Parser tokenizer = MagicMock() tokenizer.get_vocab.return_value = {" ": 100, " ":...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: d to reproduce — this is a pure Python logic bug that crashes before any model is loaded. ### 🐛 Describe the bug `MiniMaxM2Parser.__init__()` does not accept `**kwargs`, but `serving.py` always passes `chat_template_kwa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ` when instantiating parsers. This causes a `TypeError` crash on **every request** when using the MiniMax M2 parser. **Root cause:** PR #39683 fixed the missing `tools` parameter in `MiniMaxM2Parser.__init__()`, but for...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
