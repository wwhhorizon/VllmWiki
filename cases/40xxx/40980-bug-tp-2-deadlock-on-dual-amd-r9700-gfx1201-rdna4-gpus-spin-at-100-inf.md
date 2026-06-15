# vllm-project/vllm#40980: [Bug]: TP=2 deadlock on dual AMD R9700 (gfx1201/RDNA4) — GPUs spin at 100%, inference blocked

| 字段 | 值 |
| --- | --- |
| Issue | [#40980](https://github.com/vllm-project/vllm/issues/40980) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;gemm;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TP=2 deadlock on dual AMD R9700 (gfx1201/RDNA4) — GPUs spin at 100%, inference blocked

### Issue 正文摘录

### Your current environment - **vLLM**: v0.19.1+rocm721 (also reproduced on v0.19.2rc1.dev215+g32e45636e) - **PyTorch**: 2.11.0 (built from source for gfx1201) - **ROCm**: 7.2.1 - **RCCL**: 2.27.7 (built from source with `--amdgpu_targets gfx1201`) - **OS**: Fedora 43 (toolbox container, Ubuntu 24.04 base image) - **GPUs**: 2x AMD Radeon R9700 (gfx1201), 16 GB VRAM each - **CPU**: AMD Ryzen 9 9900X3D - **Also present**: 1x iGPU gfx1036 (excluded via `HIP_VISIBLE_DEVICES=0,1`) ### 🐛 Describe the bug # Summary Tensor Parallel = 2 across two AMD Radeon R9700 (gfx1201) GPUs results in a complete deadlock. The server starts, routes are registered, but both GPUs immediately sit at 100% utilization with no active requests. Inference requests hang indefinitely and return no tokens. TP=1 works flawlessly on the same hardware and software stack. ## Reproduction ```bash HIP_VISIBLE_DEVICES=0,1 NCCL_P2P_DISABLE=1 \ VLLM_ROCM_USE_AITER=0 \ vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct \ --host 0.0.0.0 --port 8000 \ --tensor-parallel-size 2 --max-num-seqs 1 \ --max-model-len 104857 --gpu-memory-utilization 0.98 \ --dtype auto --enforce-eager \ --attention-backend TRITON_ATTN --mm-encoder-at...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ker_TP0 pid=10859) INFO 08:32:22 [backends.py:391] Compiling a graph for compile range (1, 2048) takes 2.48 s (Worker_TP0 pid=10859) INFO 08:32:25 [gpu_worker.py:440] Available KV cache memory: 22.83 GiB (EngineCore pid...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ual AMD R9700 (gfx1201/RDNA4) — GPUs spin at 100%, inference blocked bug;rocm ### Your current environment - **vLLM**: v0.19.1+rocm721 (also reproduced on v0.19.2rc1.dev215+g32e45636e) - **PyTorch**: 2.11.0 (built from...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: tion ```bash HIP_VISIBLE_DEVICES=0,1 NCCL_P2P_DISABLE=1 \ VLLM_ROCM_USE_AITER=0 \ vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct \ --host 0.0.0.0 --port 8000 \ --tensor-parallel-size 2 --max-num-seqs 1 \ --max-model-l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: DEVICES=0,1 NCCL_P2P_DISABLE=1 \ VLLM_ROCM_USE_AITER=0 \ vllm serve meta-llama/Meta-Llama-3.1-8B-Instruct \ --host 0.0.0.0 --port 8000 \ --tensor-parallel-size 2 --max-num-seqs 1 \ --max-model-len 104857 --gpu-memory-ut...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: TP=2 deadlock on dual AMD R9700 (gfx1201/RDNA4) — GPUs spin at 100%, inference blocked bug;rocm ### Your current environment - **vLLM**: v0.19.1+rocm721 (also reproduced on v0.19.2rc1.dev215+g32e45636e) - **PyTor...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
