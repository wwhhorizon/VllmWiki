# vllm-project/vllm#34932: RuntimeError: Already borrowed in Hermes tool parser under concurrent load

| 字段 | 值 |
| --- | --- |
| Issue | [#34932](https://github.com/vllm-project/vllm/issues/34932) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> RuntimeError: Already borrowed in Hermes tool parser under concurrent load

### Issue 正文摘录

## Environment - vLLM version: 0.16.0 - Python version: 3.12 - GPU: 2x NVIDIA RTX PRO 6000 Blackwell ## How to reproduce 1. Start vLLM with `--enable-auto-tool-choice --tool-call-parser hermes` 2. Send concurrent `/v1/chat/completions` requests ## Bug description `Hermes2ProToolParser.__init__` calls `tokenizer.encode()` and `tokenizer.decode()` on a shared HuggingFace tokenizer instance on every instantiation. Under concurrent load, the tokenizer's Rust backend panics with `RuntimeError: Already borrowed` due to concurrent mutable borrows via PyO3's `RefCell`. This causes ~1% of requests to return 500 Internal Server Error. ``` File ".../vllm/tool_parsers/hermes_tool_parser.py", line 63, in __init__ self.tool_call_start_token_ids = self.model_tokenizer.encode( File ".../transformers/tokenization_utils_tokenizers.py", line 722 self._tokenizer.no_truncation() RuntimeError: Already borrowed ``` ## Suggested fix The token IDs for ` ` / ` ` are deterministic per tokenizer. Caching them at the class level behind a lock would fix the race and avoid redundant work. Our workaround: [PrimeIntellect-ai/prime-rl#1837](https://github.com/PrimeIntellect-ai/prime-rl/pull/1837).

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: Python version: 3.12 - GPU: 2x NVIDIA RTX PRO 6000 Blackwell ## How to reproduce 1. Start vLLM with `--enable-auto-tool-choice --tool-call-parser hermes` 2. Send concurrent `/v1/chat/completions` requests ## Bug descrip...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ironment - vLLM version: 0.16.0 - Python version: 3.12 - GPU: 2x NVIDIA RTX PRO 6000 Blackwell ## How to reproduce 1. Start vLLM with `--enable-auto-tool-choice --tool-call-parser hermes` 2. Send concurrent `/v1/chat/co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: _init__` calls `tokenizer.encode()` and `tokenizer.decode()` on a shared HuggingFace tokenizer instance on every instantiation. Under concurrent load, the tokenizer's Rust backend panics with `RuntimeError: Already borr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ice --tool-call-parser hermes` 2. Send concurrent `/v1/chat/completions` requests ## Bug description `Hermes2ProToolParser.__init__` calls `tokenizer.encode()` and `tokenizer.decode()` on a shared HuggingFace tokenizer...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ance on every instantiation. Under concurrent load, the tokenizer's Rust backend panics with `RuntimeError: Already borrowed` due to concurrent mutable borrows via PyO3's `RefCell`. This causes ~1% of requests to return...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
