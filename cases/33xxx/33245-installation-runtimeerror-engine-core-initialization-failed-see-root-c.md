# vllm-project/vllm#33245: [Installation]: RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s):

| 字段 | 值 |
| --- | --- |
| Issue | [#33245](https://github.com/vllm-project/vllm/issues/33245) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cuda;gemm;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s):

### Issue 正文摘录

### Your current environment ```text python3 collect_env.py INFO 01-28 02:53:54 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version : Could not collect CMake version : version 4.0.2 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.10 (main, Apr 9 2025, 08:55:05) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.19.0-50-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 Nvidia driver version : 535.86.05 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runt...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Installation]: RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): installation ### Your current environment ```text python3 collect_env.py INFO 01-28 02:53:54 [__init__.py:243] A
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: py INFO 01-28 02:53:54 [__init__.py:243] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: _.py:243] Automatically detected platform cuda. Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ffected Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Vulnerable: Clear CPU buffers attempted, no microcode; SMT Host state unknown Vulnerability Retbleed: Not affected Vulnerability Spec store byp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: , 'model': '/models/Qwen2.5-VL-7B-Instruct', 'trust_remote_code': True, 'dtype': 'bfloat16', 'max_model_len': 32768, 'served_model_name': ['Qwen2.5-VL-7B-Instruct'], 'limit_mm_per_prompt': {'image': 5, 'video': 5}} INFO...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
