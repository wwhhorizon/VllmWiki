# vllm-project/vllm#3251: Error when prompt_logprobs + enable_prefix_caching

| 字段 | 值 |
| --- | --- |
| Issue | [#3251](https://github.com/vllm-project/vllm/issues/3251) |
| 状态 | closed |
| 标签 | unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Error when prompt_logprobs + enable_prefix_caching

### Issue 正文摘录

``` File "vllm/model_executor/layers/sampler.py", line 98, in forward logits.div_(sampling_tensors.temperatures.unsqueeze_(dim=1)) RuntimeError: The size of tensor a (5) must match the size of tensor b (117) at non-singleton dimension 0 ``` I think the problem comes from that logits up to 112(16*7blocks) is prefix-cached, and only the last 5 input tokens are computed. To return the prompt logprobs, the sampler is looking for all 117 logits while only recently calculated 5 logits are returned there. It seems the cached 112 logits need to be returned as well. I don't know how...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: imension 0 ``` I think the problem comes from that logits up to 112(16*7blocks) is prefix-cached, and only the last 5 input tokens are computed. To return the prompt logprobs, the sampler is looking for all 117 logits w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: or when prompt_logprobs + enable_prefix_caching unstale ``` File "vllm/model_executor/layers/sampler.py", line 98, in forward logits.div_(sampling_tensors.temperatures.unsqueeze_(dim=1)) RuntimeError: The size of tensor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Error when prompt_logprobs + enable_prefix_caching unstale ``` File "vllm/model_executor/layers/sampler.py", line 98, in forward logits.div_(sampling_tensors.temperatures.unsqueeze_(dim=1)) RuntimeError: The size of ten...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
