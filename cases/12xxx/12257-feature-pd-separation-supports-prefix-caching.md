# vllm-project/vllm#12257: [Feature]: PD separation supports prefix caching

| 字段 | 值 |
| --- | --- |
| Issue | [#12257](https://github.com/vllm-project/vllm/issues/12257) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: PD separation supports prefix caching

### Issue 正文摘录

### 🚀 The feature, motivation and pitch [kv transfer agent](https://github.com/vllm-project/vllm/blob/main/vllm/distributed/kv_transfer/kv_transfer_agent.py) recv_kv_caches_and_hidden_states and send_kv_caches_and_hidden_states failed to support prefix caching Mainly due to the following code in [simple_connector.py](https://github.com/vllm-project/vllm/blob/main/vllm/distributed/kv_transfer/kv_connector/simple_connector.py) L159, L215 'seq_lens = model_input.attn_metadata.seq_lens' If the prefix caching is opened and hit, the hit part in the previous text will be marked as calculated, and input_token will be the uncalculated part ### Alternatives Idea: After opening prefix caching, only prefix and transfer increments to decode. Therefore, consider subtracting context_lens from seq_lens to solve this problem? 'seq_lens = (model_input.attn_metadata.seq_lens_tensor - model_input.attn_metadata.context_lens_tensor).tolist()' ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answ...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: PD separation supports prefix caching feature request;stale ### 🚀 The feature, motivation and pitch [kv transfer agent](https://github.com/vllm-project/vllm/blob/main/vllm/distributed/kv_transfer/kv_transfer_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: v_connector/simple_connector.py) L159, L215 'seq_lens = model_input.attn_metadata.seq_lens' If the prefix caching is opened and hit, the hit part in the previous text will be marked as calculated, and input_token will b...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ted/kv_transfer/kv_connector/simple_connector.py) L159, L215 'seq_lens = model_input.attn_metadata.seq_lens' If the prefix caching is opened and hit, the hit part in the previous text will be marked as calculated, and i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
