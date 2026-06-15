# vllm-project/vllm#10766: [Usage]: Removal of vllm.openai.rpc folder in vLLM 0.6.2 release 

| 字段 | 值 |
| --- | --- |
| Issue | [#10766](https://github.com/vllm-project/vllm/issues/10766) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Removal of vllm.openai.rpc folder in vLLM 0.6.2 release 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi Team, I encountered an issue while using the following import statements in my code with vLLM version 0.6.1: from vllm.entrypoints.openai.rpc.client import AsyncEngineRPCClient from vllm.entrypoints.openai.rpc.server import run_rpc_server In the vLLM 0.6.2 release, the vllm.openai.rpc folder was removed. Refer to the sample PR for more details: https://github.com/vllm-project/vllm/pull/8157/files#diff-6558549c25380c16a3e62d4f151d27f37de101635c626a65ae51bcfd8ef72faf As a result, I am now facing import issues. I would prefer not to refactor the entire codebase and instead resolve this by updating the import statements. Could you please suggest a way to achieve this? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: to use vllm Hi Team, I encountered an issue while using the following import statements in my code with vLLM version 0.6.1: from vllm.entrypoints.openai.rpc.client import AsyncEngineRPCClient from vllm.entrypoints.opena...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Removal of vllm.openai.rpc folder in vLLM 0.6.2 release usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi Team, I encountered an is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
