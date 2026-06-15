# vllm-project/vllm#28867: [Bug]: Audit vLLM usages of functools.lru_cache

| 字段 | 值 |
| --- | --- |
| Issue | [#28867](https://github.com/vllm-project/vllm/issues/28867) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Audit vLLM usages of functools.lru_cache

### Issue 正文摘录

### Your current environment n/a ### 🐛 Describe the bug They are emitting warnings in Dynamo that look like ``` (Worker_TP6_EP6 pid=3247488) /home/robertgshaw2-redhat/vllm/.venv/lib64/python3.12/site-packages/torch/_dynamo/variables/functions.py:1692: UserWarning: Dynamo detected a call to a `functools.lru_cache`-wrapped function. Dynamo ignores the cache wrapper and directly traces the wrapped function. Silent incorrectness is only a *potential* risk, not something we have observed. Enable TORCH_LOGS="+dynamo" for a DEBUG stack trace. ``` This is with Deepseek. the question if this results in perf issues or correctness issues. I do see a lot of calls with it: https://github.com/search?q=repo%3Avllm-project%2Fvllm%20functools.lru_cache&type=code See https://vllm-dev.slack.com/archives/C08K1FAHFPH/p1762299354120489 for more context ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Bug]: Audit vLLM usages of functools.lru_cache bug;torch.compile ### Your current environment n/a ### 🐛 Describe the bug They are emitting warnings in Dynamo that look like ``` (Worker_TP6_EP6 pid=3247488) /home/robert...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rrectness issues. I do see a lot of calls with it: https://github.com/search?q=repo%3Avllm-project%2Fvllm%20functools.lru_cache&type=code See https://vllm-dev.slack.com/archives/C08K1FAHFPH/p1762299354120489 for more co...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ools.lru_cache&type=code See https://vllm-dev.slack.com/archives/C08K1FAHFPH/p1762299354120489 for more context ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
