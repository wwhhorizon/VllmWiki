# vllm-project/vllm#14360: [Performance]: Multimodal embeds input reduces service throughput

| 字段 | 值 |
| --- | --- |
| Issue | [#14360](https://github.com/vllm-project/vllm/issues/14360) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Multimodal embeds input reduces service throughput

### Issue 正文摘录

### Proposal to improve performance vllm version 0.6.5 Refer to [the link ](https://docs.vllm.ai/en/latest/serving/multimodal_inputs.html)to directly transfer audio embeds to the server As concurrency increases, throughput cannot continue to improve. When QPS=16, there is a multimodal input RPS=18 and a pure text input RPS=50, with a difference of nearly three times 1. It has been investigated and is not caused by the merging of embeddings 2. When checking in the execute_model, the request batch for multimodal data is very high, close to 16, while the request batch for plain text is less than 10 At present, it is speculated that the transmission of multi_madal_data from MQLLCient to MQLLServe may cause a decrease in throughput. We hope to provide suggestions. ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e throughput performance;stale ### Proposal to improve performance vllm version 0.6.5 Refer to [the link ](https://docs.vllm.ai/en/latest/serving/multimodal_inputs.html)to directly transfer audio embeds to the server As...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Performance]: Multimodal embeds input reduces service throughput performance;stale ### Proposal to improve performance vllm version 0.6.5 Refer to [the link ](https://docs.vllm.ai/en/latest/serving/multimodal_inputs.ht...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: or plain text is less than 10 At present, it is speculated that the transmission of multi_madal_data from MQLLCient to MQLLServe may cause a decrease in throughput. We hope to provide suggestions. ### Report of performa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: Multimodal embeds input reduces service throughput performance;stale ### Proposal to improve performance vllm version 0.6.5 Refer to [the link ](https://docs.vllm.ai/en/latest/serving/multimodal_inputs.ht...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ormance]: Multimodal embeds input reduces service throughput performance;stale ### Proposal to improve performance vllm version 0.6.5 Refer to [the link ](https://docs.vllm.ai/en/latest/serving/multimodal_inputs.html)to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
