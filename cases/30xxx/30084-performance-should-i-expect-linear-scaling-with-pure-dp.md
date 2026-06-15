# vllm-project/vllm#30084: [Performance]: Should I expect linear scaling with pure DP?

| 字段 | 值 |
| --- | --- |
| Issue | [#30084](https://github.com/vllm-project/vllm/issues/30084) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Should I expect linear scaling with pure DP?

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I decided to benchmark vLLM 0.11.2 with pure DP of Qwen/Qwen2.5-32B-Instruct deployment(before benchmarking DP+EP with Qwen/Qwen3-30B-A3B-Instruct-2507) on DP1 vs DP8 (H200): DP1 deployment: ``` vllm serve ${MODEL_NAME} \ --port 8000 \ --trust-remote-code ``` DP8 deployment: ``` vllm serve ${MODEL_NAME} \ --port 8000 \ --trust-remote-code \ --data-parallel-size 8 \ --data-parallel-size-local 8 ``` My benchmark roughly looks like this: ``` for rate in [10, 20, ... 100, 200, ... 1000, 2000, ... 100000]: vllm bench serve \ --host "$HOST" \ --model Qwen/Qwen2.5-32B-Instruct \ --dataset-name random \ --random-input-len 128 \ --random-output-len 128 \ --num-prompts 10000 \ --request-rate "$rate" \ --ignore-eos ``` Should I expect ~8x scaling? Result show only ~4x (duration, request throughput, tokens throughput, etc...) cc @KeitaW @amanshanbhag ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and ask...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I decided to benchmark vLLM 0.11.2 with pure DP of Qwen/Qwen2.5-32B-Instruct deployment(...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ssion on performance I decided to benchmark vLLM 0.11.2 with pure DP of Qwen/Qwen2.5-32B-Instruct deployment(before benchmarking DP+EP with Qwen/Qwen3-30B-A3B-Instruct-2507) on DP1 vs DP8 (H200): DP1 deployment: ``` vll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Should I expect linear scaling with pure DP? performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I dec...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: mance regression _No response_ ### Misc discussion on performance I decided to benchmark vLLM 0.11.2 with pure DP of Qwen/Qwen2.5-32B-Instruct deployment(before benchmarking DP+EP with Qwen/Qwen3-30B-A3B-Instruct-2507)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
