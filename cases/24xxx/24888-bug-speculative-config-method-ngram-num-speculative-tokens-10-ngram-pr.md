# vllm-project/vllm#24888: [Bug]: --speculative-config '{"method": "ngram", "num_speculative_tokens": 10, "ngram_prompt_lookup_max": 10}' does not work

| 字段 | 值 |
| --- | --- |
| Issue | [#24888](https://github.com/vllm-project/vllm/issues/24888) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: --speculative-config '{"method": "ngram", "num_speculative_tokens": 10, "ngram_prompt_lookup_max": 10}' does not work

### Issue 正文摘录

### Your current environment `vllm serve [model] ----speculative-config '{"method": "ngram", "num_speculative_tokens": 10, "ngram_prompt_lookup_max": 10}'` does not work. Pass in any model you would like. ### 🐛 Describe the bug ## Bug: `--speculative-config` argument parsing fails with AttributeError ### Problem When running `vllm serve (model) --speculative-config`, the command fails because the argument gets parsed differently than expected, causing it to be converted into a `SpeculativeConfig` object instead of remaining as a dictionary. ### Root Cause The issue occurs in `vllm/engine/arg_utils.py` where `--speculative-config` is added through the VllmConfig argument group: ```python vllm_kwargs = get_kwargs(VllmConfig) vllm_group = parser.add_argument_group( title="VllmConfig", description=VllmConfig.__doc__, ) vllm_group.add_argument("--speculative-config", **vllm_kwargs["speculative_config"]) ``` This causes the argument to be automatically parsed into a `SpeculativeConfig` object. However, downstream code expects it to be a dictionary and calls `.get()` on it, resulting in: ``` AttributeError: 'SpeculativeConfig' object has no attribute 'get' ``` This error occurs in `vllm/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: --speculative-config '{"method": "ngram", "num_speculative_tokens": 10, "ngram_prompt_lookup_max": 10}' does not work bug ### Your current environment `vllm serve [model] ----speculative-config '{"method": "ngram...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: --speculative-config '{"method": "ngram", "num_speculative_tokens": 10, "ngram_prompt_lookup_max": 10}' does not work bug ### Your current environment `vllm serve [model] ----speculative-config '{"method": "ngram...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ts. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
