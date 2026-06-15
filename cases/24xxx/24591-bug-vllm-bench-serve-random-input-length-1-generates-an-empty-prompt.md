# vllm-project/vllm#24591: [Bug]: `vllm bench serve --random-input-length=1` generates an empty prompt

| 字段 | 值 |
| --- | --- |
| Issue | [#24591](https://github.com/vllm-project/vllm/issues/24591) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: `vllm bench serve --random-input-length=1` generates an empty prompt

### Issue 正文摘录

### Your current environment Since at least the last few weeks (mid August), but probably much further back. ### 🐛 Describe the bug While benchmarking P/D I realized that `--random-input-len=1` results in an empty prompt for some models, specifically DeepSeek-R1. This is due to this chunk in the random dataset: ``` num_special_tokens = int(tokenizer.num_special_tokens_to_add()) real_input_len = max(0, int(input_len) - num_special_tokens) ``` For deepseek-r1 and several other tested models (`facebook/opt-125m`) `tokenizer.num_special_tokens_to_add()` returns 1, meaning the prompt is empty. It also means in many cases we generate fewer tokens than we expect, which throws off perf calculations. When running a benchmark, I would expect the actual prompt to contain the number of random input tokens specified. Num special tokens should not be counted as part of the expected random input tokens (or we should specify that in bench via another parameter). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: August), but probably much further back. ### 🐛 Describe the bug While benchmarking P/D I realized that `--random-input-len=1` results in an empty prompt for some models, specifically DeepSeek-R1. This is due to this chu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: at `--random-input-len=1` results in an empty prompt for some models, specifically DeepSeek-R1. This is due to this chunk in the random dataset: ``` num_special_tokens = int(tokenizer.num_special_tokens_to_add()) real_i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: r). ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: realized that `--random-input-len=1` results in an empty prompt for some models, specifically DeepSeek-R1. This is due to this chunk in the random dataset: ``` num_special_tokens = int(tokenizer.num_special_tokens_to_ad...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: `vllm bench serve --random-input-length=1` generates an empty prompt bug;stale ### Your current environment Since at least the last few weeks (mid August), but probably much further back. ### 🐛 Describe the bug While be...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
