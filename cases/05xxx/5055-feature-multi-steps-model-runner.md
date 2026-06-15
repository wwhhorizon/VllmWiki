# vllm-project/vllm#5055: [Feature]: multi-steps model_runner?

| 字段 | 值 |
| --- | --- |
| Issue | [#5055](https://github.com/vllm-project/vllm/issues/5055) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: multi-steps model_runner?

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, in GPUExecutorAsync's[ execute_model_async](https://github.com/vllm-project/vllm/blob/main/vllm/executor/gpu_executor.py#L117-L118), it use make_async, which bring some schedule cost. Small model would be more suffering from it, like 0.5B may take 20% cost, and 14B-int4 model take about 5%. So I am thinking whether we could have something like decode burst mode? Thus we may output not single token, but >1? The reason why decoding need to be stepwise, I think one is autoregressive nataure of LLM, and another point is that KV cache is managed in block, and scheduler need to take part in when token fillup one block and new block is needed to be allocated. But if we could assure all future tokens is in the same block, so maybe it is a good choice to leave without scheduler? Like current spec_decode's [multi_step_worker](https://github.com/vllm-project/vllm/blob/main/vllm/spec_decode/multi_step_worker.py#L74-L83) did, it could be simply run the model_runner's execute_model several times. Is there any other concerns for if making model_runner as multi-steps? ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: multi-steps model_runner? feature request;stale ### 🚀 The feature, motivation and pitch Currently, in GPUExecutorAsync's[ execute_model_async](https://github.com/vllm-project/vllm/blob/main/vllm/executor/gpu_...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: el would be more suffering from it, like 0.5B may take 20% cost, and 14B-int4 model take about 5%. So I am thinking whether we could have something like decode burst mode? Thus we may output not single token, but >1? Th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ecutor.py#L117-L118), it use make_async, which bring some schedule cost. Small model would be more suffering from it, like 0.5B may take 20% cost, and 14B-int4 model take about 5%. So I am thinking whether we could have...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: I think one is autoregressive nataure of LLM, and another point is that KV cache is managed in block, and scheduler need to take part in when token fillup one block and new block is needed to be allocated. But if we cou...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ressive nataure of LLM, and another point is that KV cache is managed in block, and scheduler need to take part in when token fillup one block and new block is needed to be allocated. But if we could assure all future t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
