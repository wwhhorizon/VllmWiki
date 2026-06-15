# vllm-project/vllm#13816: [Performance]: Regarding PD separation performance

| 字段 | 值 |
| --- | --- |
| Issue | [#13816](https://github.com/vllm-project/vllm/issues/13816) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Regarding PD separation performance

### Issue 正文摘录

### Proposal to improve performance Decoding receiving keys, values, and hidden status will block the calculation. In the previous section, [recv_kv_caches_and-hidden_states ](https://github.com/vllm-project/vllm/blob/main/vllm/worker/model_runner.py)is time-consuming because it blocks model_executable in the execute_model Due to being a post scheduling inference process, this reception will block inference, resulting in an inability to improve throughput. There are two suggestions, one of which can be chosen. 1. Optimize the underlying communication, separate recv from pipe, listen to recv, and immediately accept the completion of decoding after the completion of prefill sending, without the need for decoding to trigger acceptance. The completion of prefill inference requires waiting for the completion of sending before responding 2. Reception and caching are completed before scheduling, and when entering execute, caching and the received keys, values, hidden, etc. are carried This can avoid blocking decoding due to long reception time, thereby improving throughput ### Report of performance regression 'prompt_tokens': 8268 recv_kv_caches_and_hidden_states cost 0.679804801940918 #...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance]: Regarding PD separation performance performance;stale ### Proposal to improve performance Decoding receiving keys, values, and hidden status will block the calculation. In the previous section, [recv_kv_c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: his reception will block inference, resulting in an inability to improve throughput. There are two suggestions, one of which can be chosen. 1. Optimize the underlying communication, separate recv from pipe, listen to re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ove performance Decoding receiving keys, values, and hidden status will block the calculation. In the previous section, [recv_kv_caches_and-hidden_states ](https://github.com/vllm-project/vllm/blob/main/vllm/worker/mode...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: dden_states ](https://github.com/vllm-project/vllm/blob/main/vllm/worker/model_runner.py)is time-consuming because it blocks model_executable in the execute_model Due to being a post scheduling inference process, this r...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
