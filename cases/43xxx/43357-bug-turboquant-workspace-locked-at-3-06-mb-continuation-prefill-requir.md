# vllm-project/vllm#43357: [Bug]: TurboQuant workspace locked at 3.06 MB — continuation_prefill requires 12 MB on any prompt >4096 tokens (Qwen3.6-27B NVFP4 hybrid, Blackwell SM120)

| 字段 | 值 |
| --- | --- |
| Issue | [#43357](https://github.com/vllm-project/vllm/issues/43357) |
| 状态 | open |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TurboQuant workspace locked at 3.06 MB — continuation_prefill requires 12 MB on any prompt >4096 tokens (Qwen3.6-27B NVFP4 hybrid, Blackwell SM120)

### Issue 正文摘录

### Your current environment Current environment Cannot run collect_env.py on host — vLLM runs inside Podman container. Container image: docker.io/vllm/vllm-openai:nightly (pulled 2026-05-21) vLLM version: 0.21.1rc1.dev169+ga6682d1d2 GPU: NVIDIA RTX Pro 6000 Blackwell (SM120, 96GB GDDR7) CUDA: 13.0 (cu130 nightly) OS: Bazzite Linux (Fedora immutable, based on Fedora 41) Container runtime: Podman rootless Model: sakamakismile/Huihui-Qwen3.6-27B-abliterated-NVFP4-MTP Architecture: Qwen3-Next hybrid (GDN linear attention + full attention layers) Quantization: ModelOpt NVFP4 (--quantization modelopt) 🐛 Describe the bug Any request whose prompt exceeds ~4096 tokens crashes the vLLM engine with a workspace locking assertion error in _continuation_prefill . Short requests (&lt;4096 tokens) complete successfully. The engine must be restarted after each crash. Critically: changing --max-num-batched-tokens does not affect the workspace allocation. Tested with 4096, 8192, and 32768 — workspace is always locked at 3.06 MB regardless of this value. Launch command podman run --name vllm-qwen36 \ --gpus all --network=host \ -v /path/to/models:/models:Z \ --ipc=host -d \ -e VLLM_MEMORY_PROFILER_E...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ill requires 12 MB on any prompt >4096 tokens (Qwen3.6-27B NVFP4 hybrid, Blackwell SM120) bug ### Your current environment Current environment Cannot run collect_env.py on host — vLLM runs inside Podman container. Conta...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: TurboQuant workspace locked at 3.06 MB — continuation_prefill requires 12 MB on any prompt >4096 tokens (Qwen3.6-27B NVFP4 hybrid, Blackwell SM120) bug ### Your current environment Current environment Cannot run c
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ect_env.py on host — vLLM runs inside Podman container. Container image: docker.io/vllm/vllm-openai:nightly (pulled 2026-05-21) vLLM version: 0.21.1rc1.dev169+ga6682d1d2 GPU: NVIDIA RTX Pro 6000 Blackwell (SM120, 96GB G...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: TurboQuant workspace locked at 3.06 MB — continuation_prefill requires 12 MB on any prompt >4096 tokens (Qwen3.6-27B NVFP4 hybrid, Blackwell SM120) bug ### Your current environment Current environment Cannot run...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: , 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63] Using TURBOQUANT attention backend out of potential backends: ['TURBOQUANT'] Using FlashInferCutlassNvFp4LinearKernel for NVFP4 GEMM Setting attention block size to 3072 tok...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
