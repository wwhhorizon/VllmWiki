# vllm-project/vllm#14923: [Feature]: Ensure benchmark serving do not import vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#14923](https://github.com/vllm-project/vllm/issues/14923) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Ensure benchmark serving do not import vLLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM's benchmark serving script is expected to be a standalone inference client that only requires minimum dependencies. Currently, it still imports `vllm` conditionally. The task is as follows: 1. Clearly define a requirements txt for benchmark serving client ``` numpy pandas Pillow tqdm transformers datasets ``` 2. Add a CI test that create a new uv environment and execute the script. Ensure there is no vLLM present. This can be part of existing tests for benchmark scripts. https://github.com/vllm-project/vllm/blob/main/.buildkite/run-benchmarks.sh 3. Make sure the existing usage of vLLM is moved to inlining whatever utility method is required. ### Alternatives _No response_ ### Additional context See #14879 for discussion, cc @houseroad @ywang96 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature]: Ensure benchmark serving do not import vLLM good first issue;feature request ### 🚀 The feature, motivation and pitch vLLM's benchmark serving script is expected to be a standalone inference client that only r...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Feature]: Ensure benchmark serving do not import vLLM good first issue;feature request ### 🚀 The feature, motivation and pitch vLLM's benchmark serving script is expected to be a standalone inference client that only r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 96 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e]: Ensure benchmark serving do not import vLLM good first issue;feature request ### 🚀 The feature, motivation and pitch vLLM's benchmark serving script is expected to be a standalone inference client that only requires...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
