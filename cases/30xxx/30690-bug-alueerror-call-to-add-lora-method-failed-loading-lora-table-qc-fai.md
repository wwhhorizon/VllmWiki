# vllm-project/vllm#30690: [Bug]: alueError: Call to add_lora method failed: Loading lora ["table_qc failed: No adapter found for /data/home/zhizhehui/dev/train/table_ocr/Reward_model_train/output/qwen_lora_output/checkpoint-57"]

| 字段 | 值 |
| --- | --- |
| Issue | [#30690](https://github.com/vllm-project/vllm/issues/30690) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: alueError: Call to add_lora method failed: Loading lora ["table_qc failed: No adapter found for /data/home/zhizhehui/dev/train/table_ocr/Reward_model_train/output/qwen_lora_output/checkpoint-57"]

### Issue 正文摘录

### Your current environment (vllm) [zhizhehui@localhost ~]$ python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Kylin Linux Advanced Server V10 (Halberd) (x86_64) GCC version : (GCC) 7.3.0 Clang version : Could not collect CMake version : version 3.16.5 Libc version : glibc-2.28 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 | packaged by Anaconda, Inc. | (main, Oct 21 2025, 20:16:04) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-4.19.90-89.11.v2401.ky10.x86_64-x86_64-with-glibc2.28 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.61 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA RTX A6000 GPU 1: NVIDIA RTX A6000 GPU 2: NVIDIA RTX A6000 GPU 3: NVIDIA RTX A6000 Nvidia driver version : 580.105.08 cuDNN version : Probably one of the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : Kylin Linux Advanced Server V10 (Halberd) (x86_64) GCC version : (GCC) 7.3.0 Clang version : Could not collect CMake version : version 3.16.5 Libc version : glibc-2.28 ============================== PyTor
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.12 |...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ed: No adapter found for /data/home/zhizhehui/dev/train/table_ocr/Reward_model_train/output/qwen_lora_output/checkpoint-57"] bug;stale ### Your current environment (vllm) [zhizhehui@localhost ~]$ python collect_env.py C...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: table_ocr/Reward_model_train/output/qwen_lora_output/checkpoint-57"] bug;stale ### Your current environment (vllm) [zhizhehui@localhost ~]$ python collect_env.py Collecting environment information... ===================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.2 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
