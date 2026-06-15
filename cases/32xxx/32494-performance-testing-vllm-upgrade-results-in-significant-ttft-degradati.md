# vllm-project/vllm#32494: [Performance]: Testing vLLM upgrade results in significant TTFT degradation

| 字段 | 值 |
| --- | --- |
| Issue | [#32494](https://github.com/vllm-project/vllm/issues/32494) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Testing vLLM upgrade results in significant TTFT degradation

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression I am currently running vLLM 0.9.0 with the V1 engine. Recently, I have been testing an upgrade to v0.13.0 as the latest stable release. However, I am seeing some significant regression in TTFT first token generation and want to understand if this is expected. I understand there is some degradation expected with async scheduler, and the regression is significantly pronounced at higher concurrency. Testing is done with Llama 2 13b model. [llm_engine_concurrent_benchmark.py](https://github.com/user-attachments/files/24683537/llm_engine_concurrent_benchmark.py) ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: Testing vLLM upgrade results in significant TTFT degradation performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I am currently running vLLM 0.9.0 with...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ignificantly pronounced at higher concurrency. Testing is done with Llama 2 13b model. [llm_engine_concurrent_benchmark.py](https://github.com/user-attachments/files/24683537/llm_engine_concurrent_benchmark.py) ### Misc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Testing vLLM upgrade results in significant TTFT degradation performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression I am currently running vLLM 0.9.0 with the V1 engine....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
