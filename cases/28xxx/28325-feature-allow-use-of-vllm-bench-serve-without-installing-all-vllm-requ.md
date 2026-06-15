# vllm-project/vllm#28325: [Feature]: Allow use of `vllm bench serve` without installing all vLLM requirements

| 字段 | 值 |
| --- | --- |
| Issue | [#28325](https://github.com/vllm-project/vllm/issues/28325) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow use of `vllm bench serve` without installing all vLLM requirements

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'd like to use `vllm bench serve` as a standalone benchmarking tool to evaluate existing inference endpoints. To do this today requires a full install of vLLM and its requirements to make use of this feature. I am using vLLM's benchmarking in [llm-d-benchmark](https://github.com/llm-d/llm-d-benchmark), which runs the benchmark in a container. The [container image](https://github.com/llm-d/llm-d-benchmark/blob/014c9b359f5ef54a0cd4da40e88e8ff7489484e7/build/Dockerfile#L46C1-L46C67) currently fixes vLLM at commit [ b6381ced9c52271f799a8348fcc98c5f40528cdf](https://github.com/vllm-project/vllm/commit/b6381ced9c52271f799a8348fcc98c5f40528cdf) which allows `benchmark_serving.py` to be run in isolation, but this is becoming outdated. Installing full vLLM requirements in the container results in a multi-gigabyte image that is slow to build, download, and deploy. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature]: Allow use of `vllm bench serve` without installing all vLLM requirements feature request;stale ### 🚀 The feature, motivation and pitch I'd like to use `vllm bench serve` as a standalone benchmarking tool to e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: motivation and pitch I'd like to use `vllm bench serve` as a standalone benchmarking tool to evaluate existing inference endpoints. To do this today requires a full install of vLLM and its requirements to make use of th...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e of `vllm bench serve` without installing all vLLM requirements feature request;stale ### 🚀 The feature, motivation and pitch I'd like to use `vllm bench serve` as a standalone benchmarking tool to evaluate existing in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
