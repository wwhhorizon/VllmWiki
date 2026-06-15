# vllm-project/vllm#32598: [Bug]: "Fatal Python error: none_dealloc" after 4 days deployment

| 字段 | 值 |
| --- | --- |
| Issue | [#32598](https://github.com/vllm-project/vllm/issues/32598) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: "Fatal Python error: none_dealloc" after 4 days deployment

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After observing code arount the error, it seems like that requests dict in GPUModelRunner is not safe enough when multiprocess is applied, need to add lock when pop the finished req_ids. ``` def _update_states(self, scheduler_output: "SchedulerOutput") -> None: """Update the cached states and the persistent batch with the scheduler output. The updated states are used by the `_prepare_inputs` function to create the input GPU tensors for the model. The SamplingMetadata is updated and copied to the GPU if there is a new/resumed/paused/finished request in the batch. """ # Remove finished requests from the cached states. for req_id in scheduler_output.finished_req_ids: self.requests.pop(req_id, None) self.num_prompt_logprobs.pop(req_id, None) # Remove the finished requests from the persistent batch. # NOTE(woosuk): There could be an edge case where finished_req_ids and # scheduled_req_ids overlap. This happens when a request is aborted and # then resubmitted with the same ID. In this case, we treat them as two # distinct requests - clearing the cached states for the first request # and handling the second as a new request. for req_id...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: "Fatal Python error: none_dealloc" after 4 days deployment bug;stale ### Your current environment ### 🐛 Describe the bug After observing code arount the error, it seems like that requests dict in GPUModelRunner i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: create the input GPU tensors for the model. The SamplingMetadata is updated and copied to the GPU if there is a new/resumed/paused/finished request in the batch. """ # Remove finished requests from the cached states. fo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: observing code arount the error, it seems like that requests dict in GPUModelRunner is not safe enough when multiprocess is applied, need to add lock when pop the finished req_ids. ``` def _update_states(self, scheduler...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
