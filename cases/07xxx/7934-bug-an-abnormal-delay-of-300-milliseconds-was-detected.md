# vllm-project/vllm#7934: [Bug]: An abnormal delay of 300 milliseconds was detected.

| 字段 | 值 |
| --- | --- |
| Issue | [#7934](https://github.com/vllm-project/vllm/issues/7934) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: An abnormal delay of 300 milliseconds was detected.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When we were conducting stress testing on vllm with a load of 30QPS, we found an anomaly with a 300ms delay, which occurred more frequently as the QPS increased. Looking from nsight, one thread's utilization rate was at 100%, but the Python stack was empty. The input token for the experimental data was 40, and the output token was 20. This situation is very strange. For more specific experimental data, please see https://github.com/vllm-project/vllm/issues/7540#issue-2467305273 ![image](https://github.com/user-attachments/assets/ff9057fa-eebf-448d-93db-4a7b992b1d42) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. nsys: https://github.com/skylee-01/experimental_data/blob/main/vllm_300ms_delay.zip

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nd the output token was 20. This situation is very strange. For more specific experimental data, please see https://github.com/vllm-project/vllm/issues/7540#issue-2467305273 ![image](https://github.com/user-attachments/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 42) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: An abnormal delay of 300 milliseconds was detected. bug;stale ### Your current environment ### 🐛 Describe the bug When we were conducting stress testing on vllm with a load of 30QPS, we found an anomaly with a 30...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: t environment ### 🐛 Describe the bug When we were conducting stress testing on vllm with a load of 30QPS, we found an anomaly with a 300ms delay, which occurred more frequently as the QPS increased. Looking from nsight,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
