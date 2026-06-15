# vllm-project/vllm#8193: [Feature]: `benchmark_serving.py` should support `--logprobs`

| 字段 | 值 |
| --- | --- |
| Issue | [#8193](https://github.com/vllm-project/vllm/issues/8193) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: `benchmark_serving.py` should support `--logprobs`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The OpenAI API (and by extension vLLM's completions functionality) supports configuring the number of logprobs-per-token to return at the granularity of each request, via the `logprobs` argument. However, `benchmarks/benchmark_serving.py` currently does not configure the `logprobs` argument when generating requests, nor does `benchmarks/benchmark_serving.py` have a `--logprobs` CLI argument. This is an issue because it is desirable to benchmark the impact of different `--logprobs` settings on vLLM performance. So the issue is that (1) `benchmarks/benchmark_serving.py` should support a `--logprobs` argument, and (2) the value of the `--logprobs` CLI argument should configure the underlying `logprobs` argument to the completion requests generated during benchmarking. ### Alternatives In `tests/utils.py`, the function ``` completions_with_server_args( prompts: List[str], model_name: str, server_cli_args: List[str], num_logprobs: Optional[int], max_wait_seconds: int = 240, ) ``` shows how to configure OpenAI API requests with the logprobs argument set. ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: OpenAI API (and by extension vLLM's completions functionality) supports configuring the number of logprobs-per-token to return at the granularity of each request, via the `logprobs` argument. However, `benchmarks/benchm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: `benchmark_serving.py` should support `--logprobs` feature request ### 🚀 The feature, motivation and pitch The OpenAI API (and by extension vLLM's completions functionality) supports configuring the number of...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: `benchmark_serving.py` should support `--logprobs` feature request ### 🚀 The feature, motivation and pitch The OpenAI API (and by extension vLLM's completions functionality) supports configuring the number of...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
