# vllm-project/vllm#4242: Load multiple models on the same GPU in the cluster

| 字段 | 值 |
| --- | --- |
| Issue | [#4242](https://github.com/vllm-project/vllm/issues/4242) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Load multiple models on the same GPU in the cluster

### Issue 正文摘录

### Your current environment vllm 0.3.0 ray 2.9.2 ### 🐛 Describe the bug I am trying to serve two models (tinyllama 1b) on the same GPU. I have a cluster of A10 GPU (22G RAM), so I use `@serve.deployment(ray_actor_options={"num_gpus": 0.4},)` and ENGINE_ARGS = AsyncEngineArgs( gpu_memory_utilization= 0.4, model=model_path, max_model_len=128, enforce_eager=True, ) I can only start model on a replica with 40% of GPU and model reserved 10G/22G (GPU RAM). However when I tried to start the second model I got this error, although it created another replica and the usage of the cluster now 0.8/1 from GPU. ``` 024-04-21 15:12:15,310 INFO worker.py:1540 -- Connecting to existing Ray cluster at address: 10.5.8.112:6379... 2024-04-21 15:12:15,317 INFO worker.py:1715 -- Connected to Ray cluster. View the dashboard at 127.0.0.1:8265 (ServeController pid=11766) INFO 2024-04-21 15:12:15,440 controller 11766 deployment_state.py:1545 - Deploying new version of deployment MyModel in application 'model2'. Setting initial target number of replicas to 1. (ServeController pid=11766) INFO 2024-04-21 15:12:15,541 controller 11766 deployment_state.py:1829 - Adding 1 replica to deployment MyModel in applic...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Load multiple models on the same GPU in the cluster bug;stale ### Your current environment vllm 0.3.0 ray 2.9.2 ### 🐛 Describe the bug I am trying to serve two models (tinyllama 1b) on the same GPU. I have a cluster of...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=128, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=N...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=128, download_dir=None, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantizat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 1 15:12:15,440 controller 11766 deployment_state.py:1545 - Deploying new version of deployment MyModel in application 'model2'. Setting initial target number of replicas to 1. (ServeController pid=11766) INFO 2024-04-21...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: eController pid=11766) raise ValueError("No available memory for the cache blocks. " (ServeController pid=11766) ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initial...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
