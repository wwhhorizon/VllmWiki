# vllm-project/vllm#40604: [Bug]: DeepSeek-R1 hang on 8xB200 after NCCL Initialization

| 字段 | 值 |
| --- | --- |
| Issue | [#40604](https://github.com/vllm-project/vllm/issues/40604) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-R1 hang on 8xB200 after NCCL Initialization

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using vllm 0.19.0 on 8xB200 and trying to run DeepSeek-R1. It keeps waiting for the local engine like: ```bash [Gloo] Rank [Gloo] Rank 6 is connected to [Gloo] Rank 57 is connected to peer ranks. 7Expected number of connected peer ranks is : peer ranks. 7Expected number of connected peer ranks is : 77 is connected to 7 peer ranks. Expected number of connected peer ranks is : 7 (Worker pid=13612) ================================================================================ (Worker pid=13612) [2026-04-22 09:45:39] FlashInfer API Logging - System Information (Worker pid=13612) ================================================================================ (Worker pid=13612) FlashInfer version: 0.6.6 (Worker pid=13612) CUDA toolkit version: 13.0 (Worker pid=13612) cuDNN version: 91501 (Worker pid=13612) Number of GPUs: 8 (Worker pid=13612) GPU 0: NVIDIA B200 (Worker pid=13612) Compute capability: 10.0 (SM100) (Worker pid=13612) GPU 1: NVIDIA B200 (Worker pid=13612) Compute capability: 10.0 (SM100) (Worker pid=13612) GPU 2: NVIDIA B200 (Worker pid=13612) Compute capability: 10.0 (SM100) (Worker pid=13612) GPU 3: NVIDIA B200 (...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: DeepSeek-R1 hang on 8xB200 after NCCL Initialization bug ### Your current environment ### 🐛 Describe the bug I am using vllm 0.19.0 on 8xB200 and trying to run DeepSeek-R1. It keeps waiting for the local engine l...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ========================================== (Worker pid=13612) FlashInfer version: 0.6.6 (Worker pid=13612) CUDA toolkit version: 13.0 (Worker pid=13612) cuDNN version: 91501 (Worker pid=13612) Number of GPUs: 8 (Worker...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: orker pid=13612) [2026-04-22 09:45:39] FlashInfer API Logging - System Information (Worker pid=13612) ================================================================================ (Worker pid=13612) FlashInfer versio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: FER_LOGLEVEL=3 FLASHINFER_JIT_VERBOSE=1 VLLM_LOGGING_LEVEL=DEBUG MOE_CAP_PROFILING_ONLY=1 vllm serve --model deepseek-ai/DeepSeek-R1 --port 8000 --tensor-parallel-size 8 --reasoning-parser deepseek_r1 --trust-remote-cod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: =============================== (Worker pid=13612) [2026-04-22 09:45:39] FlashInfer API Logging - System Information (Worker pid=13612) ================================================================================ (W...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
