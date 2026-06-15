# vllm-project/vllm#12526: [Bug]: Getting torch.distributed.DistStoreError: wait timeout after 600000ms on Multi GPU instance (NC96 - 4xA100s)

| 字段 | 值 |
| --- | --- |
| Issue | [#12526](https://github.com/vllm-project/vllm/issues/12526) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Getting torch.distributed.DistStoreError: wait timeout after 600000ms on Multi GPU instance (NC96 - 4xA100s)

### Issue 正文摘录

### Your current environment ``` DEBUG 01-28 20:44:23 __init__.py:26] No plugins for group vllm.platform_plugins found. INFO 01-28 20:44:23 __init__.py:183] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x86_64) GCC version: (Debian 12.2.0-14) 12.2.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.36 Python version: 3.12.8 (main, Jan 24 2025, 19:38:26) [GCC 12.2.0] (64-bit runtime) Python platform: Linux-5.15.0-1078-azure-x86_64-with-glibc2.36 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100 80GB PCIe GPU 1: NVIDIA A100 80GB PCIe GPU 2: NVIDIA A100 80GB PCIe GPU 3: NVIDIA A100 80GB PCIe Nvidia driver version: 550.127.08 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 48 bits physical, 48 bits virtual Byte Order: Little Endian CPU(s):...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ly detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Linux 12 (bookworm) (x8...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: tStoreError: wait timeout after 600000ms on Multi GPU instance (NC96 - 4xA100s) bug ### Your current environment ``` DEBUG 01-28 20:44:23 __init__.py:26] No plugins for group vllm.platform_plugins found. INFO 01-28 20:4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: _.py:183] Automatically detected platform cuda. Collecting environment information... PyTorch version: 2.5.1+cu124 Is debug build: False CUDA used to build PyTorch: 12.4 ROCM used to build PyTorch: N/A OS: Debian GNU/Li...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Not affected Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability Spec rstack overflow: Mitigation;...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: eral_plugins found. WARNING 01-28 20:08:19 config.py:2318] Casting torch.float16 to torch.bfloat16. INFO 01-28 20:08:26 config.py:520] This model supports multiple tasks: {'embed', 'generate', 'score', 'classify', 'rewa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
