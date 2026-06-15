# vllm-project/vllm#38550: [Bug]: can't start b200x2 or b200x4 sm100 with nvidia/Qwen3.5-397B-A17B-NVFP4

| 字段 | 值 |
| --- | --- |
| Issue | [#38550](https://github.com/vllm-project/vllm/issues/38550) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: can't start b200x2 or b200x4 sm100 with nvidia/Qwen3.5-397B-A17B-NVFP4

### Issue 正文摘录

# [Bug]: vLLM 0.18.0 hangs on startup with TP=2 on 8×B200 host when using CUDA_VISIBLE_DEVICES subset — symmetric memory + NCCL deadlock ## Summary vLLM 0.18.0 deadlocks during initialization when running with `CUDA_VISIBLE_DEVICES=0,1` (TP=2) on an 8×B200 bare-metal host. The hang occurs in `ncclCommInitRank` and `torch.distributed._symmetric_memory.rendezvous` during the creation of the second NCCL communicator (model parallel group). The same configuration works fine on a 4×B200 host where all GPUs are visible to the process (RunPod). ## Root Cause The issue is caused by two symmetric memory subsystems that fail when the process sees a **subset** of GPUs on a multi-GPU host with MNNVL fabric: 1. **PyTorch symmetric memory** (`SymmMemCommunicator`) — controlled by `VLLM_ALLREDUCE_USE_SYMM_MEM` (default: `1`) 2. **NCCL symmetric memory** (`register_nccl_symmetric_ops`) — controlled by `VLLM_USE_NCCL_SYMM_MEM` (default: `0`, but `is_symmetric_memory_enabled()` still gets called and can trigger NCCL-level symmetric ops) Both perform rendezvous/registration that expects all fabric-connected GPUs to participate, causing a deadlock when only a subset is visible via `CUDA_VISIBLE_DEVIC...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: m rendezvous/registration that expects all fabric-connected GPUs to participate, causing a deadlock when only a subset is visible via `CUDA_VISIBLE_DEVICES`. ## Diagnosis Steps (py-spy traces) **First hang** — `symmetri...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: can't start b200x2 or b200x4 sm100 with nvidia/Qwen3.5-397B-A17B-NVFP4 bug # [Bug]: vLLM 0.18.0 hangs on startup with TP=2 on 8×B200 host when using CUDA_VISIBLE_DEVICES subset — symmetric memory + NCCL deadlock...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: can't start b200x2 or b200x4 sm100 with nvidia/Qwen3.5-397B-A17B-NVFP4 bug # [Bug]: vLLM 0.18.0 hangs on startup with TP=2 on 8×B200 host when using CUDA_VISIBLE_DEVICES subset — symmetric memory + NCCL deadlock...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: can't start b200x2 or b200x4 sm100 with nvidia/Qwen3.5-397B-A17B-NVFP4 bug # [Bug]: vLLM 0.18.0 hangs on startup with TP=2 on 8×B200 host when using CUDA_VISIBLE_DEVICES subset — symmetric memory + NCCL deadlock...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 00 host when using CUDA_VISIBLE_DEVICES subset — symmetric memory + NCCL deadlock ## Summary vLLM 0.18.0 deadlocks during initialization when running with `CUDA_VISIBLE_DEVICES=0,1` (TP=2) on an 8×B200 bare-metal host....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
