# vllm-project/vllm#17824: [Performance]: waiting 队列能有多长？和哪些启动参数有关？

| 字段 | 值 |
| --- | --- |
| Issue | [#17824](https://github.com/vllm-project/vllm/issues/17824) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: waiting 队列能有多长？和哪些启动参数有关？

### Issue 正文摘录

### Proposal to improve performance 我使用八卡4090启动ds32B模型，然后连续请求了1200个请求，但是我看waiting reqs和runing reqs的数量加起来大约是1000个，想知道vllm是如何控制队列长度的，队列长度和哪些启动参数有关？ ![Image](https://github.com/user-attachments/assets/dfafb417-f995-420d-bbc9-6853f42b19f5) 我的启动命令是：vllm serve llm_model/ds_32B/ --served-model-name deepseek --api-key 12345 --disable-log-requests --trust-remote-code --tensor-parallel-size 8 --max-model-len 25000 --gpu_memory_utilization 0.7 --max-num-seqs 96 --max-num-batched-tokens 18096 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance]: waiting 队列能有多长？和哪些启动参数有关？ performance;stale ### Proposal to improve performance 我使用八卡4090启动ds32B模型，然后连续请求了1200个请求，但是我看waiting reqs和runing reqs的数量加起来大约是1000个，想知道vllm是如何控制队列长度的，队列长度和哪些启动参数有关？ ![Image](https...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ax-num-seqs 96 --max-num-batched-tokens 18096 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nts/assets/dfafb417-f995-420d-bbc9-6853f42b19f5) 我的启动命令是：vllm serve llm_model/ds_32B/ --served-model-name deepseek --api-key 12345 --disable-log-requests --trust-remote-code --tensor-parallel-size 8 --max-model-len 2500...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
