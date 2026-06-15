# vllm-project/vllm#15014: [Bug]: deploy deepseek-r1-awq on 16 x 4090 48G, layer_kv_cache = torch.zeros(kv_cache_shape, [rank0]: RuntimeError: CUDA error: invalid argument

| 字段 | 值 |
| --- | --- |
| Issue | [#15014](https://github.com/vllm-project/vllm/issues/15014) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: deploy deepseek-r1-awq on 16 x 4090 48G, layer_kv_cache = torch.zeros(kv_cache_shape, [rank0]: RuntimeError: CUDA error: invalid argument

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (RayWorkerWrapper pid=12430, ip=192.168.1.3) INFO 03-18 08:32:44 [worker.py:267] model weights take 22.34GiB; non_torch_memory takes 0.24GiB; PyTorch activation peak memory takes 0.37GiB; the rest of the memory reserved for KV Cache is 23.02GiB. [repeated 7x across cluster] ERROR 03-18 08:32:47 [worker_base.py:620] Error executing method 'initialize_cache'. This might cause deadlock in distributed execution. ERROR 03-18 08:32:47 [worker_base.py:620] Traceback (most recent call last): ERROR 03-18 08:32:47 [worker_base.py:620] File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker_base.py", line 612, in execute_method ERROR 03-18 08:32:47 [worker_base.py:620] return run_method(self, method, args, kwargs) ERROR 03-18 08:32:47 [worker_base.py:620] File "/usr/local/lib/python3.10/dist-packages/vllm/utils.py", line 2216, in run_method ERROR 03-18 08:32:47 [worker_base.py:620] return func(*args, **kwargs) ERROR 03-18 08:32:47 [worker_base.py:620] File "/usr/local/lib/python3.10/dist-packages/vllm/worker/worker.py", line 307, in initialize_cache ERROR 03-18 08:32:47 [worker_base.py:620] self._init_cache_engine() ERROR 03-18 08:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: : CUDA error: invalid argument ERROR 03-18 08:32:47 [worker_base.py:620] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ERROR 03-18 08:32:47 [worker_base.py:620] [rank0]: Traceback (most recent call...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: \ --tensor-parallel-size 8 \ --pipeline-parallel-size 2 \ --quantization moe_wna16 \ --gpu-memory-utilization 0.97 \ --calculate-kv-scales \ --served-model-name deepseek-reasoner \ --model /mnt --host 0.0.0.0 \ --port 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: 48G, layer_kv_cache = torch.zeros(kv_cache_shape, [rank0]: RuntimeError: CUDA error: invalid argument bug;stale ### Your current environment ### 🐛 Describe the bug (RayWorkerWrapper pid=12430, ip=192.168.1.3) INFO 03-18...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: (kv_cache_shape, [rank0]: RuntimeError: CUDA error: invalid argument bug;stale ### Your current environment ### 🐛 Describe the bug (RayWorkerWrapper pid=12430, ip=192.168.1.3) INFO 03-18 08:32:44 [worker.py:267] model w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: erWrapper pid=12430, ip=192.168.1.3) INFO 03-18 08:32:44 [worker.py:267] model weights take 22.34GiB; non_torch_memory takes 0.24GiB; PyTorch activation peak memory takes 0.37GiB; the rest of the memory reserved for KV...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
