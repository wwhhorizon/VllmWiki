# vllm-project/vllm#40919: [Bug]: RMSNormGated input_guard breaks torch.compile dynamo tracing

| 字段 | 值 |
| --- | --- |
| Issue | [#40919](https://github.com/vllm-project/vllm/issues/40919) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;fp8;operator;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RMSNormGated input_guard breaks torch.compile dynamo tracing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving Qwen3.5 : ```bash python -m vllm.entrypoints.cli.main Qwen/Qwen3.5-35B-A3B-FP8 --gpu-memory-utilization 0.9 --tensor-parallel-size 2 --max-num-seqs 512 --no-enable-prefix-caching --host 127.0.0.1 --port 8000 --no-async-scheduling --compilation-config='{"backend": "eager", "cudagraph_mode": "FULL_AND_PIECEWISE"}' --speculative_config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' --reasoning-parser qwen3 --language-model-only ``` startup fails as torch.compile's dynamo break during the profiling run. ``` WorkerProc hit an exception. Traceback (most recent call last): File "/workspace/zhr/vllm_tmp/vllm/v1/executor/multiproc_executor.py", line 957, in worker_busy_loop output = func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/home/admin/venvs/vllm_tmp/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 124, in decorate_context return func(*args, **kwargs) ^^^^^^^^^^^^^^^^^^^^^ File "/workspace/zhr/vllm_tmp/vllm/v1/worker/gpu_worker.py", line 370, in determine_available_memory self.model_runner.profile_run() File "/workspace/zhr/vllm_tmp/vllm/v1/worker/gpu_model_runner.py", line 5840, in profile_run...

## 现有链接修复摘要

#40921 Bugfix: fix RMSNormGated input_guard torch.compile dynamo tracing on CUDA

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: RMSNormGated input_guard breaks torch.compile dynamo tracing bug ### Your current environment ### 🐛 Describe the bug When serving Qwen3.5 : ```bash python -m vllm.entrypoints.cli.main Qwen/Qwen3.5-35B-A3B-FP8 --g...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: model-only ``` startup fails as torch.compile's dynamo break during the profiling run. ``` WorkerProc hit an exception. Traceback (most recent call last): File "/workspace/zhr/vllm_tmp/vllm/v1/executor/multiproc_executo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: en3.5 : ```bash python -m vllm.entrypoints.cli.main Qwen/Qwen3.5-35B-A3B-FP8 --gpu-memory-utilization 0.9 --tensor-parallel-size 2 --max-num-seqs 512 --no-enable-prefix-caching --host 127.0.0.1 --port 8000 --no-async-sc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ug ### Your current environment ### 🐛 Describe the bug When serving Qwen3.5 : ```bash python -m vllm.entrypoints.cli.main Qwen/Qwen3.5-35B-A3B-FP8 --gpu-memory-utilization 0.9 --tensor-parallel-size 2 --max-num-seqs 512...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: host 127.0.0.1 --port 8000 --no-async-scheduling --compilation-config='{"backend": "eager", "cudagraph_mode": "FULL_AND_PIECEWISE"}' --speculative_config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' --reason...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40921](https://github.com/vllm-project/vllm/pull/40921) | closes_keyword | 0.95 | Bugfix: fix RMSNormGated input_guard torch.compile dynamo tracing on CUDA | fixes #40919 a startup dynamo failure when serving Qwen3.5 `vllm/model_executor/layers/fla/ops/utils.py::input_guard` currently uses: ```python torch.accelerator.device_in |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
