# vllm-project/vllm#634: Tensor Parallel on A10G - llamav2

| 字段 | 值 |
| --- | --- |
| Issue | [#634](https://github.com/vllm-project/vllm/issues/634) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Tensor Parallel on A10G - llamav2

### Issue 正文摘录

Hi all, I am using vLLM worker to serve up llama v2 13b model. Please check my engine args below ``` 2023-08-01 00:41:32 | INFO | __main__ | Using engine args: 2023-08-01 00:41:32 | INFO | __main__ | engine_args.model: /opt/resources/model/XX/ 2023-08-01 00:41:32 | INFO | __main__ | engine_args.tokenizer: /opt/resources/model/XX/ 2023-08-01 00:41:32 | INFO | __main__ | engine_args.tokenizer_mode: slow 2023-08-01 00:41:32 | INFO | __main__ | engine_args.download_dir: None 2023-08-01 00:41:32 | INFO | __main__ | engine_args.use_np_weights: False 2023-08-01 00:41:32 | INFO | __main__ | engine_args.use_dummy_weights: False 2023-08-01 00:41:32 | INFO | __main__ | engine_args.dtype: auto 2023-08-01 00:41:32 | INFO | __main__ | engine_args.seed: 0 2023-08-01 00:41:32 | INFO | __main__ | engine_args.worker_use_ray: True 2023-08-01 00:41:32 | INFO | __main__ | engine_args.pipeline_parallel_size: 1 2023-08-01 00:41:32 | INFO | __main__ | engine_args.tensor_parallel_size: 4 2023-08-01 00:41:32 | INFO | __main__ | engine_args.block_size: 16 2023-08-01 00:41:32 | INFO | __main__ | engine_args.swap_space: 4 2023-08-01 00:41:32 | INFO | __main__ | engine_args.gpu_memory_utilization: 0.95 2023-08...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: el/XX/ ``` When I try to run using a single/dual (with tensor parallel) A100, it works just fine. However, when I try to use 2 or 4 A10Gs the model never ends up getting served/loaded. My `nvidia-smi` mem usage looks li...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ne 2023-08-01 00:41:32 | INFO | __main__ | engine_args.use_np_weights: False 2023-08-01 00:41:32 | INFO | __main__ | engine_args.use_dummy_weights: False 2023-08-01 00:41:32 | INFO | __main__ | engine_args.dtype: auto 2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Tensor Parallel on A10G - llamav2 bug Hi all, I am using vLLM worker to serve up llama v2 13b model. Please check my engine args below ``` 2023-08-01 00:41:32 | INFO | __main__ | Using engine args: 2023-08-01 00:41:32 |...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: dummy_weights: False 2023-08-01 00:41:32 | INFO | __main__ | engine_args.dtype: auto 2023-08-01 00:41:32 | INFO | __main__ | engine_args.seed: 0 2023-08-01 00:41:32 | INFO | __main__ | engine_args.worker_use_ray: True 2...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: y: False 2023-08-01 00:41:32 | INFO | __main__ | engine_args.disable_log_requests: False 2023-08-01 00:41:32 | INFO | __main__ | Loading model /opt/resources/model/XX/ ``` When I try to run using a single/dual (with ten...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
