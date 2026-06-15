# vllm-project/vllm#34133: [Bug]: Mistral Large 3 (NVFP4) hangs on initialization - 8x B300 (Blackwell) - "Waiting for core engine"

| 字段 | 值 |
| --- | --- |
| Issue | [#34133](https://github.com/vllm-project/vllm/issues/34133) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;kernel;moe |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Mistral Large 3 (NVFP4) hangs on initialization - 8x B300 (Blackwell) - "Waiting for core engine"

### Issue 正文摘录

### Environment Details * **Hardware:** 8x NVIDIA B300 (Blackwell) SXM6 * **Driver:** 590.44.01 * **CUDA:** 13.1 * **vLLM Version:** `vllm-openai:0.15.1` * **Orchestration:** Kubernetes (512Gi Shared Memory mounted) ### Bug Details I am attempting to serve `Mistral-Large-3-Instruct-2512-NVFP4` on a node with **8x NVIDIA B300 (Blackwell)** GPUs. The engine initializes the workers but hangs indefinitely at the `Waiting for 1 local, 0 remote core engine proc(s) to start` stage. The hang persists even when using `--enforce-eager` to skip CUDA graph capture. I suspect this is a deadlock related to **NCCL initialization on Blackwell** (similar to #33041) or the **multiprocessing spawn method** (similar to #33369). ### Reproduction Steps 1. Deploy to Kubernetes with `VLLM_WORKER_MULTIPROC_METHOD=spawn`. 2. Launch the API server with the command below. 3. Observe logs hanging indefinitely after worker spawning. **Launch Command:** ```bash python3 -m vllm.entrypoints.openai.api_server \ --model /data/hub/Mistral-Large-3-675B-Instruct-2512-NVFP4 \ --tensor-parallel-size 8 \ --max-model-len 65536 \ --enforce-eager \ --gpu-memory-utilization 0.92 \ --disable-custom-all-reduce \ --distributed-...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Mistral Large 3 (NVFP4) hangs on initialization - 8x B300 (Blackwell) - "Waiting for core engine" bug;stale ### Environment Details * **Hardware:** 8x NVIDIA B300 (Blackwell) SXM6 * **Driver:** 590.44.01 * **CUDA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: Mistral Large 3 (NVFP4) hangs on initialization - 8x B300 (Blackwell) - "Waiting for core engine" bug;stale ### Environment Details * **Hardware:** 8x NVIDIA B300 (Blackwell) SXM6 * **Driver:** 590.44.01 * **CUDA:** 13....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: B300 (Blackwell) SXM6 * **Driver:** 590.44.01 * **CUDA:** 13.1 * **vLLM Version:** `vllm-openai:0.15.1` * **Orchestration:** Kubernetes (512Gi Shared Memory mounted) ### Bug Details I am attempting to serve `Mistral-Lar...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Mistral Large 3 (NVFP4) hangs on initialization - 8x B300 (Blackwell) - "Waiting for core engine" bug;stale ### Environment Details * **Hardware:** 8x NVIDIA B300 (Blackwell) SXM6 * **Driver:** 590.44.01 * **CUDA...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tion 0.92 \ --disable-custom-all-reduce \ --distributed-executor-backend mp ``` **Environment Variables:** ```yaml NCCL_P2P_DISABLE: "0" # Have also tried "1" NCCL_DEBUG: "INFO" VLLM_WORKER_MULTIPROC_METHOD: "spawn" ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
