# vllm-project/vllm#5342: [Speculative decoding]: `AttributeError: 'NoneType' object has no attribute 'numel'` when exceeding draft context length

| 字段 | 值 |
| --- | --- |
| Issue | [#5342](https://github.com/vllm-project/vllm/issues/5342) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Speculative decoding]: `AttributeError: 'NoneType' object has no attribute 'numel'` when exceeding draft context length

### Issue 正文摘录

### Your current environment vllm-0.4.3 ### 🐛 Describe the bug When I use the speculative mode and prompt_length+output_length > 2048, the error occurs When I use the speculative mode, I use the following parameters, which produces this error: Parameters： Base_model: llama2-70B Speculative_model: llama1.1b engine_args = EngineArgs( model=base_path, tokenizer=base_path, trust_remote_code=True, tensor_parallel_size=4, gpu_memory_utilization=0.90, enforce_eager=True, speculative_model=draft_path, num_speculative_tokens=4, dtype=torch.float16, use_v2_block_manager=True ) And the prompt tokens length is 2040 the output tokens is 50 ( when prompt_length+output_length > 2048 ，the error occurs ) Error: RayWorkerWrapper pid=142935) 07d92dd514d4:142935:143254 [0] transport/net_ib.cc:100 NCCL WARN NET/IB : mlx5_3:1 Got async event : GID table change (RayWorkerWrapper pid=142935) (RayWorkerWrapper pid=142935) 07d92dd514d4:142935:143254 [0] transport/net_ib.cc:100 NCCL WARN NET/IB : mlx5_3:1 Got async event : GID table change (RayWorkerWrapper pid=143111) ERROR 06-07 16:53:17 worker_base.py:148] Error executing method start_worker_execution_loop. This might cause deadlock in distributed execut...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Speculative decoding]: `AttributeError: 'NoneType' object has no attribute 'numel'` when exceeding draft context length bug;stale ### Your current environment vllm-0.4.3 ### 🐛 Describe the bug When I use the speculat
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: er=True, speculative_model=draft_path, num_speculative_tokens=4, dtype=torch.float16, use_v2_block_manager=True ) And the prompt tokens length is 2040 the output tokens is 50 ( when prompt_length+output_length > 2048 ，t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: e the following parameters, which produces this error: Parameters： Base_model: llama2-70B Speculative_model: llama1.1b engine_args = EngineArgs( model=base_path, tokenizer=base_path, trust_remote_code=True, tensor_paral...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: el=draft_path, num_speculative_tokens=4, dtype=torch.float16, use_v2_block_manager=True ) And the prompt tokens length is 2040 the output tokens is 50 ( when prompt_length+output_length > 2048 ，the error occurs ) Error:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
