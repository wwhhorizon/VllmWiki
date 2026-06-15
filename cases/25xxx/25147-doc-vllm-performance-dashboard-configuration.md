# vllm-project/vllm#25147: [Doc]: vllm performance dashboard configuration

| 字段 | 值 |
| --- | --- |
| Issue | [#25147](https://github.com/vllm-project/vllm/issues/25147) |
| 状态 | closed |
| 标签 | documentation;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: vllm performance dashboard configuration

### Issue 正文摘录

### 📚 The doc issue I am trying to replicate similar results present here https://hud.pytorch.org/benchmark/llms?repoName=vllm-project%2Fvllm on a H100 machine for gpt-oss-20B model, but I see a lot of difference between my tests and the dashboard values for these Median TTFT(ms), p99 ITL(ms) and p99 TTFT(ms) metrics. Could anyone please help me in getting the exact config used to obtain the dashboard results like vllm version, torch version etc. @huydhn could you help me get those details. ### Suggest a potential alternative/fix _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Doc]: vllm performance dashboard configuration documentation;stale ### 📚 The doc issue I am trying to replicate similar results present here https://hud.pytorch.org/benchmark/llms?repoName=vllm-project%2Fvllm on a H100...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: https://hud.pytorch.org/benchmark/llms?repoName=vllm-project%2Fvllm on a H100 machine for gpt-oss-20B model, but I see a lot of difference between my tests and the dashboard values for these Median TTFT(ms), p99 ITL(ms)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: trying to replicate similar results present here https://hud.pytorch.org/benchmark/llms?repoName=vllm-project%2Fvllm on a H100 machine for gpt-oss-20B model, but I see a lot of difference between my tests and the dashbo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: getting the exact config used to obtain the dashboard results like vllm version, torch version etc. @huydhn could you help me get those details. ### Suggest a potential alternative/fix _No response_ ### Before submittin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Doc]: vllm performance dashboard configuration documentation;stale ### 📚 The doc issue I am trying to replicate similar results present here https://hud.pytorch.org/benchmark/llms?repoName=vllm-project%2Fvllm on a H100...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
