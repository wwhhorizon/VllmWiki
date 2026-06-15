# vllm-project/vllm#9975: [Performance]: Any up-to-date and convincing benchmark for chosing the fastest engine ?

| 字段 | 值 |
| --- | --- |
| Issue | [#9975](https://github.com/vllm-project/vllm/issues/9975) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Any up-to-date and convincing benchmark for chosing the fastest engine ?

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance As a user, I want to chose a fastest and easiest-to-use LLM inference and serving engine. But which engine is actually fastest and easiest-to-use? Is there any up-to-date and convincing benchmark? https://blog.vllm.ai/2024/07/25/lfai-perf.html > The vLLM contributors are doubling down to ensure vLLM is a fastest and easiest-to-use LLM inference and serving engine. https://github.com/InternLM/lmdeploy?tab=readme-ov-file ![image](https://github.com/user-attachments/assets/1d4d3b2a-2284-49d8-9212-dc6533897e32) https://lmsys.org/blog/2024-07-25-sglang-llama3/ > SGLang consistently outperforms vLLM, achieving up to 3.1x higher throughput on Llama-70B. ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Performance]: Any up-to-date and convincing benchmark for chosing the fastest engine ? performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc dis...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Performance]: Any up-to-date and convincing benchmark for chosing the fastest engine ? performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc dis...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: a-2284-49d8-9212-dc6533897e32) https://lmsys.org/blog/2024-07-25-sglang-llama3/ > SGLang consistently outperforms vLLM, achieving up to 3.1x higher throughput on Llama-70B. ### Your current environment (if you think it...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: te and convincing benchmark for chosing the fastest engine ? performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance As a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
