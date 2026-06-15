# vllm-project/vllm#43954: [Bug]: NVCC compilation error when launching DeepSeek-V4-Flash on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#43954](https://github.com/vllm-project/vllm/issues/43954) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;kernel;operator |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NVCC compilation error when launching DeepSeek-V4-Flash on H100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **vllm version:** ``` root@glusterfs-07:~# pip list | grep vllm vllm 0.21.0 ``` **Server launch command** ```bash python -m vllm.entrypoints.openai.api_server \ --model /mnt/nvme1n1/weights/DeepSeek-V4-Flash \ --served-model-name auto \ --port 8006 \ -tp 4 \ -dp 2 \ --max-num-seqs 96 \ --max-model-len 40960 \ --gpu-memory-utilization 0.9 \ --trust-remote-code \ --kernel-config '{"moe_backend":"auto"}' \ --kv-cache-dtype fp8 \ --enable_expert_parallel ``` **Error:** ``` WorkerProc hit an exception. Traceback (most recent call last): File "/data/miniconda3/envs/xx/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 957, in worker_busy_loop output = func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/data/miniconda3/envs/xx/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/data/miniconda3/envs/xx/lib/python3.11/site-packages/vllm/v1/worker/gpu_worker.py", line 392, in determine_available_memory self.model_runner.profile_run() File "/data/miniconda3/envs/xx/lib/python3.11/site-packages/vllm/v1/worker/gpu_model_runner....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: H100 bug ### Your current environment ### 🐛 Describe the bug **vllm version:** ``` root@glusterfs-07:~# pip list | grep vllm vllm 0.21.0 ``` **Server launch command** ```bash python -m vllm.entrypoints.openai.api_server...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -remote-code \ --kernel-config '{"moe_backend":"auto"}' \ --kv-cache-dtype fp8 \ --enable_expert_parallel ``` **Error:** ``` WorkerProc hit an exception. Traceback (most recent call last): File "/data/miniconda3/envs/xx...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: NVCC compilation error when launching DeepSeek-V4-Flash on H100 bug ### Your current environment ### 🐛 Describe the bug **vllm version:** ``` root@glusterfs-07:~# pip list | grep vllm vllm 0.21.0 ``` **Server lau...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: pu-memory-utilization 0.9 \ --trust-remote-code \ --kernel-config '{"moe_backend":"auto"}' \ --kv-cache-dtype fp8 \ --enable_expert_parallel ``` **Error:** ``` WorkerProc hit an exception. Traceback (most recent call la...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: rker.py", line 392, in determine_available_memory self.model_runner.profile_run() File "/data/miniconda3/envs/xx/lib/python3.11/site-packages/vllm/v1/worker/gpu_model_runner.py", line 5948, in profile_run hidden_states,...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
