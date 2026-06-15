# vllm-project/vllm#16947: [Performance]: Why/How vLLM uses CPU memory?

| 字段 | 值 |
| --- | --- |
| Issue | [#16947](https://github.com/vllm-project/vllm/issues/16947) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Why/How vLLM uses CPU memory?

### Issue 正文摘录

### Proposal to improve performance I am running LLama 70b FP8, the entire model and inference run fit on GPU but I still see around 100GB of CPU RAM usage. Why does vLLM use CPU memory even when inference is running on GPU only? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ory? performance;stale ### Proposal to improve performance I am running LLama 70b FP8, the entire model and inference run fit on GPU but I still see around 100GB of CPU RAM usage. Why does vLLM use CPU memory even when...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: y even when inference is running on GPU only? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: rmance;stale ### Proposal to improve performance I am running LLama 70b FP8, the entire model and inference run fit on GPU but I still see around 100GB of CPU RAM usage. Why does vLLM use CPU memory even when inference...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: Why/How vLLM uses CPU memory? performance;stale ### Proposal to improve performance I am running LLama 70b FP8, the entire model and inference run fit on GPU but I still see around 100GB of CPU RAM usage....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
