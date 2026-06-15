# vllm-project/vllm#9581: [Performance]: The performance of version 0.6.3 is weaker than that of version 0.6.2 in stress testing. 

| 字段 | 值 |
| --- | --- |
| Issue | [#9581](https://github.com/vllm-project/vllm/issues/9581) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: The performance of version 0.6.3 is weaker than that of version 0.6.2 in stress testing. 

### Issue 正文摘录

### Proposal to improve performance The performance of version 0.6.3 is weaker than that of version 0.6.2 in stress testing. Scenario: Agent Stress Testing Data: Input 50 tokens, output 20 tokens. Version 0.6.3: 22 QPS, with a significant drop after reaching the maximum value. ![image](https://github.com/user-attachments/assets/9c8a3db8-8eaa-4ac8-9802-a099b1fb69e8) Version 0.6.2: 24 QPS, with available performance reaching over 90% at 36 QPS. The decline after reaching the maximum value is gradual. ![image](https://github.com/user-attachments/assets/85abb7f5-6550-4405-b245-aa656185b729) Under the same conditions, comparing version 0.6.3 with 0.6.2, it was found that the prefill time for version 0.6.3 is about 13ms longer per instance than version 0.6.2. The main reason is a pause of 200-300 microseconds between two blocks. Conditions for obtaining the data: Using batch_size=20, offline use of LLMEngine with 50 iterations to get the data. ![image](https://github.com/user-attachments/assets/cba1b3f2-7644-4bbb-8209-f1851d58ba4b) ![image](https://github.com/user-attachments/assets/267e7824-6d62-4a50-8395-e364f9c8eb0a) https://github.com/skylee-01/experimental_data/blob/main/nsys_vllm_...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 6.3 is weaker than that of version 0.6.2 in stress testing. performance;stale ### Proposal to improve performance The performance of version 0.6.3 is weaker than that of version 0.6.2 in stress testing. Scenario: Agent...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: formance of version 0.6.3 is weaker than that of version 0.6.2 in stress testing. performance;stale ### Proposal to improve performance The performance of version 0.6.3 is weaker than that of version 0.6.2 in stress tes...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Performance]: The performance of version 0.6.3 is weaker than that of version 0.6.2 in stress testing. performance;stale ### Proposal to improve performance The performance of version 0.6.3 is weaker than that of versi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: on 0.6.2. The main reason is a pause of 200-300 microseconds between two blocks. Conditions for obtaining the data: Using batch_size=20, offline use of LLMEngine with 50 iterations to get the data. ![image](https://gith...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
