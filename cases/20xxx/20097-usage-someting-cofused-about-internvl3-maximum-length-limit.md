# vllm-project/vllm#20097: [Usage]: someting cofused about InternVL3 maximum length limit

| 字段 | 值 |
| --- | --- |
| Issue | [#20097](https://github.com/vllm-project/vllm/issues/20097) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: someting cofused about InternVL3 maximum length limit

### Issue 正文摘录

### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18 (main, Jun 5 2025, 13:14:17) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.8.0-60-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A40 GPU 1: NVIDIA A40 GPU 2: NVIDIA A40 GPU 3: NVIDIA A40 GPU 4: NVIDIA A40 GPU 5: NVIDIA A40 GPU 6: NVIDIA A40 GPU 7: NVIDIA A40 Nvidia driver version : 570.169 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/lib...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 12.3.0-1ubuntu1~22.04) 12.3.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 =================
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Usage]: someting cofused about InternVL3 maximum length limit usage ### Your current environment ```text Collecting environment information... ============================== System Info ============================== OS
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.7.1+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.18 (...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: rt 8001 --tensor-parallel-size 8 --limit-mm-per-prompt image=5,video=0 --dtype bfloat16 --max-num-seqs 1 --max-seq-len 20480 ``` But found same warning no matter how I adjust '--max-seq-len' about model such as: ``` Tok...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ed Vulnerability Meltdown: Not affected Vulnerability Mmio stale data: Mitigation; Clear CPU buffers; SMT vulnerable Vulnerability Reg file data sampling: Not affected Vulnerability Retbleed: Not affected Vulnerability...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
