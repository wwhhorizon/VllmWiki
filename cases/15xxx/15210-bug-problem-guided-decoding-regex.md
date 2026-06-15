# vllm-project/vllm#15210: [Bug]: Problem guided decoding (regex)

| 字段 | 值 |
| --- | --- |
| Issue | [#15210](https://github.com/vllm-project/vllm/issues/15210) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Problem guided decoding (regex)

### Issue 正文摘录

### Your current environment v0.8.1 ### 🐛 Describe the bug After update to v0.8.1 I got this error: ``` File "/opt/venv/lib/python3.12/site-packages/vllm/v1/structured_output/utils.py", line 255, in validate_structured_output_request xgr.Grammar.from_regex(gd_params.regex) File "/opt/venv/lib/python3.12/site-packages/xgrammar/grammar.py", line 179, in from_regex _core.Grammar.from_regex(regex_string, print_converted_ebnf) RuntimeError: [10:59:34] /project/cpp/regex_converter.cc:73: Regex parsing error at position 2: Unclosed '[' ``` The regex I pass is ``` extra_body['guided_regex'] = '[\x00-\u2e7f]+' ``` Is it possible to get this regex running in v0.8.1 and V1? I tried falling back to outlines, but apparently this means falling back to V0 as well: ``` --guided-decoding-backend is not supported by the V1 Engine. Falling back to V0. ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: apparently this means falling back to V0 as well: ``` --guided-decoding-backend is not supported by the V1 Engine. Falling back to V0. ``` ### Before submitting a new issue... - [x] Make sure you already searched for re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: /v1/structured_output/utils.py", line 255, in validate_structured_output_request xgr.Grammar.from_regex(gd_params.regex) File "/opt/venv/lib/python3.12/site-packages/xgrammar/grammar.py", line 179, in from_regex _core.G...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
