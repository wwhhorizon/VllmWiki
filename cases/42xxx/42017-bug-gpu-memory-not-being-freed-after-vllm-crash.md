# vllm-project/vllm#42017: [Bug]: GPU memory not being freed after vLLM crash

| 字段 | 值 |
| --- | --- |
| Issue | [#42017](https://github.com/vllm-project/vllm/issues/42017) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPU memory not being freed after vLLM crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Set up env like this: ```bash uv venv --python 312 source .venv/bin/activate uv pip install vllm --torch-backend=auto ``` then run this ``` SAFETENSORS_FAST_GPU=1 vllm serve \ MiniMaxAI/MiniMax-M2.7 --trust-remote-code \ --enable-auto-tool-choice --tool-call-parser minimax_m2 \ --reasoning-parser minimax_m2_append_think \ --gpu-memory-utilization 0.95 --cpu-offload-gb 300 ``` get this error ``` (EngineCore pid=36444) ValueError: To serve at least one request with the models's max seq len (204800), (48.44 GiB KV cache is needed, which is larger than the available KV cache memory (24.85 GiB). Based on the available memory, the estimated maximum model length is 105056. Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine. See https://docs.vllm.ai/en/latest/configuration/conserving_memory/ for more details. [rank0]:[W508 10:49:32.296904081 ProcessGroupNCCL.cpp:1575] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator()) (APIServer pid=3...

## 现有链接修复摘要

#42074 [Bugfix] Reset offloader singleton in shutdown() to prevent GPU memory leak

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: like this: ```bash uv venv --python 312 source .venv/bin/activate uv pip install vllm --torch-backend=auto ``` then run this ``` SAFETENSORS_FAST_GPU=1 vllm serve \ MiniMaxAI/MiniMax-M2.7 --trust-remote-code \ --enable-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: is about 40 GB of GPU memory unfreed on the GPU when viewed via `nvidia-smi`. but there is no process attached to it. we have to reboot our server. ### Before submitting a new issue... - [x] Make sure you already search...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: [Bug]: GPU memory not being freed after vLLM crash bug ### Your current environment ### 🐛 Describe the bug Set up env like this: ```bash uv venv --python 312 source .venv/bin/activate uv pip install vllm --torch-backend...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: venv --python 312 source .venv/bin/activate uv pip install vllm --torch-backend=auto ``` then run this ``` SAFETENSORS_FAST_GPU=1 vllm serve \ MiniMaxAI/MiniMax-M2.7 --trust-remote-code \ --enable-auto-tool-choice --too...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: EngineCore pid=36444) ValueError: To serve at least one request with the models's max seq len (204800), (48.44 GiB KV cache is needed, which is larger than the available KV cache memory (24.85 GiB). Based on the availab...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42074](https://github.com/vllm-project/vllm/pull/42074) | closes_keyword | 0.95 | [Bugfix] Reset offloader singleton in shutdown() to prevent GPU memory leak | Fixes #42017 **Why this is not a duplicate PR:** No existing open PR addresses the offloader singleton lifecycle in `shutdown()`. PR #38503 fixed several other shutdown-path leaks |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
