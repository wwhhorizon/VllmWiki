# vllm-project/vllm#28097: [Bug]: ZeroDivisionError caused by dividing by pbar.format_dict["elapsed"] in LLM._run_engine() when use_tqdm=True

| 字段 | 值 |
| --- | --- |
| Issue | [#28097](https://github.com/vllm-project/vllm/issues/28097) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ZeroDivisionError caused by dividing by pbar.format_dict["elapsed"] in LLM._run_engine() when use_tqdm=True

### Issue 正文摘录

### Your current environment (abbreviated) ### 🐛 Describe the bug According to the vLLM's source code(`vllm/entrypoints/llm.py:1746`), there is a `tqdm`(progress bar library)-related code like below. https://github.com/vllm-project/vllm/blob/428bc7bf1c54674956dd24f00db43dbcf3655c4d/vllm/entrypoints/llm.py#L1746C54-L1746C81 The given code calculates `total_in_toks` divided by `pbar.format_dict["elapsed"]` in order to calculate the value of the variable `in_spd`. However, according to the [`tqdm` library's documentation](https://tqdm.github.io/docs/tqdm/), that `elapsed` field indicates the number of seconds elapsed since start. If that value is zero (or extremely close to zero) at the time of division, this leads to a `ZeroDivisionError`. In my situation (using the `DeepSeek‑OCR` model via vLLM), all output from vLLM is suppressed (via `quiet_stdio()`), and when I call `llm.generate(..., use_tqdm=True)` (the default value of `use_tqdm` is `True` currently) I consistently get `ZeroDivisionError: integer division or modulo by zero` error with the following traceback logs: ``` ╭────────────────────────────────── Traceback (most recent call last) ───────────────────────────────────╮ │...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: │ │ 64 │ │ │ skip_special_tokens=False, │ │ 65 │ │ ) │ │ 66 │ │
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: ZeroDivisionError caused by dividing by pbar.format_dict["elapsed"] in LLM._run_engine() when use_tqdm=True bug;stale ### Your current environment (abbreviated) ### 🐛 Describe the bug According to the vLLM's sour...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: pbar.format_dict["elapsed"] in LLM._run_engine() when use_tqdm=True bug;stale ### Your current environment (abbreviated) ### 🐛 Describe the bug According to the vLLM's source code(`vllm/entrypoints/llm.py:1746`), there...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ne. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: │ │ 64 │ │ │ skip_special_tokens=False, │ │ 65 │ │ ) │ │ 66 │ │

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
