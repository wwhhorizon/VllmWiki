# vllm-project/vllm#14118: [Bug]: When I use pipeline_parallel_size and tensor_parallel_size for disaggregated prefilling, vllm broken

| 字段 | 值 |
| --- | --- |
| Issue | [#14118](https://github.com/vllm-project/vllm/issues/14118) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When I use pipeline_parallel_size and tensor_parallel_size for disaggregated prefilling, vllm broken

### Issue 正文摘录

### Your current environment ### change for support pipeline-parallel-size ```text #vllm/worker/model_runner.py:1705 if not get_pp_group().is_last_rank: hidden_or_intermediate_states = IntermediateTensors({ "hidden_states": hidden_or_intermediate_states, "residual": torch.empty_like(hidden_or_intermediate_states) }) #vllm/distributed/kv_transfer/kv_connector/simple_connector.py:195 if isinstance(hidden_or_intermediate_states, IntermediateTensors): self.insert(current_tokens, torch.ones_like(current_tokens, dtype=bool), keys, values, hidden_or_intermediate_states['hidden_states'][start_pos:end_pos]) else: self.insert(current_tokens, torch.ones_like(current_tokens, dtype=bool), keys, values, hidden_or_intermediate_states[start_pos:end_pos]) ``` ### 🐛 Describe the bug prefill command ``` VLLM_LOGGING_LEVEL=DEBUG vllm serve /data/llama2/ --tensor-parallel-size 4 --pipeline-parallel-size 2 --trust-remote-code --gpu-memory-utilization 0.8 --max-model-len 35000 --enforce-eager --served-model-name llama --port 8100 --kv-transfer-config '{"kv_connector":"PyNcclConnector","kv_role":"kv_producer","kv_rank":0,"kv_parallel_size":2,"kv_buffer_size":5e9, "kv_ip":"prefill_ip"}' ``` decode command...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: I use pipeline_parallel_size and tensor_parallel_size for disaggregated prefilling, vllm broken bug;stale ### Your current environment ### change for support pipeline-parallel-size ```text #vllm/worker/model_runner.py:1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ### change for support pipeline-parallel-size ```text #vllm/worker/model_runner.py:1705 if not get_pp_group().is_last_rank: hidden_or_intermediate_states = IntermediateTensors({ "hidden_states": hidden_or_intermediate_s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: torch.ones_like(current_tokens, dtype=bool), keys, values, hidden_or_intermediate_states['hidden_states'][start_pos:end_pos]) else: self.insert(current_tokens, torch.ones_l
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: og) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: or_intermediate_states['hidden_states'][start_pos:end_pos]) else: self.insert(current_tokens, torch.ones_like(current_tokens, dtype=bool), keys, values, hidden_or_in

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
