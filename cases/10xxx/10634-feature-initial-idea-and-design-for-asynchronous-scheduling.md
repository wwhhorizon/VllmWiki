# vllm-project/vllm#10634: [Feature]: Initial Idea and Design for Asynchronous Scheduling

| 字段 | 值 |
| --- | --- |
| Issue | [#10634](https://github.com/vllm-project/vllm/issues/10634) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Initial Idea and Design for Asynchronous Scheduling

### Issue 正文摘录

### 🚀 The feature, motivation and pitch After incorporating this [pr](https://github.com/vllm-project/vllm/pull/9826) and use, on Llama2-7b, bs=256, and the test data set is ShareGpt. I found that the gap between the two decodes at this time is about 5-6ms (token gap), which still accounts for a large proportion. I have discussed with author @robertgshaw2-neuralmagic @njhill , this problem is caused by the multi-threaded GIL lock problem. ![image](https://github.com/user-attachments/assets/d5118193-7313-40bd-a574-379721582948) At the same time, I made an assumption that if the problem is optimized, the cost of optimizing about 2-3ms can be achieved. I combined it with the current implementation. After making attempts and ideas for asynchronousization, it is initially estimated that it should be optimized to about 200-300us, basically eliminating the token gap. The solution is roughly as shown in the figure below: Combined with current main implementations. Can anyone please help to check if it is possible? ![image](https://github.com/user-attachments/assets/f26c7c24-77ca-4d85-8ed6-9ea571119f17) main implementation 1. Use last_schedule to record the last scheduling result, and also...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Initial Idea and Design for Asynchronous Scheduling feature request;stale ### 🚀 The feature, motivation and pitch After incorporating this [pr](https://github.com/vllm-project/vllm/pull/9826) and use, on Llam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: request comes, directly throw the input_data into the queue and return false data to update the resources needed for the next scheduling. 3. Further split the prepare data part of the GPU so that the GPU updates this in...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: g this [pr](https://github.com/vllm-project/vllm/pull/9826) and use, on Llama2-7b, bs=256, and the test data set is ShareGpt. I found that the gap between the two decodes at this time is about 5-6ms (token gap), which s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: com/vllm-project/vllm/pull/9826) and use, on Llama2-7b, bs=256, and the test data set is ShareGpt. I found that the gap between the two decodes at this time is about 5-6ms (token gap), which still accounts for a large p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
