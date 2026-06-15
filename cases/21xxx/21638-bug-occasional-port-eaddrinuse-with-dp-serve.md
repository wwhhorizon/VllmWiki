# vllm-project/vllm#21638: [Bug]: Occasional port EADDRINUSE with DP serve

| 字段 | 值 |
| --- | --- |
| Issue | [#21638](https://github.com/vllm-project/vllm/issues/21638) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Occasional port EADDRINUSE with DP serve

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It occasionally hits the following port in use issue. ``` # example command VLLM_LOGGING_LEVEL=DEBUG VLLM_ALL2ALL_BACKEND=pplx VLLM_USE_DEEP_GEMM=1 \ vllm serve meta-llama/Llama-4-Scout-17B-16E --max_model_len 8192 --kv_cache_dtype fp8 \ --enable-expert-parallel --tensor-parallel-size 1 --data-parallel-size 8 --trust-remote-code \ --gpu-memory-utilization 0.9 --disable-log-requests \ --compilation-config '{"full_cuda_graph":true}' 2>&1 \ | tee ~/log/ep_`date +%Y%m%d_%H%M%S`.log ``` ``` (EngineCore_0 pid=2437264) File "/data/users/yming/gitrepos/vllm/vllm/distributed/parallel_state.py", line 977, in init_distributed_environment (EngineCore_0 pid=2437264) torch.distributed.init_process_group( (EngineCore_0 pid=2437264) File "/home/yming/uv_env/vllm/lib64/python3.12/site-packages/torch/distributed/c10d_logger.py", line 81, in wrapper (EngineCore_0 pid=2437264) return func(*args, **kwargs) (EngineCore_0 pid=2437264) ^^^^^^^^^^^^^^^^^^^^^ (EngineCore_0 pid=2437264) File "/home/yming/uv_env/vllm/lib64/python3.12/site-packages/torch/distributed/c10d_logger.py", line 95, in wrapper (EngineCore_0 pid=2437264) func_return = func(*args, **k...

## 现有链接修复摘要

#21894 [Bugfix] Fix port conflict by obtaining a list of open ports upfront

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;fp8;moe;opera...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: serve meta-llama/Llama-4-Scout-17B-16E --max_model_len 8192 --kv_cache_dtype fp8 \ --enable-expert-parallel --tensor-parallel-size 1 --data-parallel-size 8 --trust-remote-code \ --gpu-memory-utilization 0.9 --disable-lo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: =DEBUG VLLM_ALL2ALL_BACKEND=pplx VLLM_USE_DEEP_GEMM=1 \ vllm serve meta-llama/Llama-4-Scout-17B-16E --max_model_len 8192 --kv_cache_dtype fp8 \ --enable-expert-parallel --tensor-parallel-size 1 --data-parallel-size 8 --...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ommand VLLM_LOGGING_LEVEL=DEBUG VLLM_ALL2ALL_BACKEND=pplx VLLM_USE_DEEP_GEMM=1 \ vllm serve meta-llama/Llama-4-Scout-17B-16E --max_model_len 8192 --kv_cache_dtype fp8 \ --enable-expert-parallel --tensor-parallel-size 1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: use issue. ``` # example command VLLM_LOGGING_LEVEL=DEBUG VLLM_ALL2ALL_BACKEND=pplx VLLM_USE_DEEP_GEMM=1 \ vllm serve meta-llama/Llama-4-Scout-17B-16E --max_model_len 8192 --kv_cache_dtype fp8 \ --enable-expert-parallel...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21894](https://github.com/vllm-project/vllm/pull/21894) | closes_keyword | 0.95 | [Bugfix] Fix port conflict by obtaining a list of open ports upfront | Fix port conflict by obtaining a list of open ports upfront ## Purpose Mitigate #21638 by querying a list of open ports in the main process. Race condition still persists, but mu |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
