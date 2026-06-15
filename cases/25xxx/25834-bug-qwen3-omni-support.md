# vllm-project/vllm#25834: [Bug]: Qwen3 Omni Support

| 字段 | 值 |
| --- | --- |
| Issue | [#25834](https://github.com/vllm-project/vllm/issues/25834) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3 Omni Support

### Issue 正文摘录

### Your current environment (vllm) tcdri@LinSeerCube-DR6000:~/script/qwen3-omni/Qwen3-Omni-30B-A3B-Instruct$ python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.9.21 (main, Dec 11 2024, 16:24:11) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-6.8.0-79-generic-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.2.91 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20-3e GPU 1: NVIDIA H20-3e GPU 2: NVIDIA H20-3e GPU 3: NVIDIA H20-3e GPU 4: NVIDIA H20-3e GPU 5: NVIDIA H20-3e GPU 6: NVIDIA H20-3e GPU 7...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.5 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.35 ============
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Qwen3 Omni Support bug ### Your current environment (vllm) tcdri@LinSeerCube-DR6000:~/script/qwen3-omni/Qwen3-Omni-30B-A3B-Instruct$ python collect_env.py Collecting environment information... ===================...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.9.21 (m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: _by_modality ERROR 09-28 19:19:56 [multiproc_executor.py:585] return profiler.get_mm_max_contiguous_tokens( ERROR 09-28 19:19:56 [multiproc_executor.py:585] File "/home/tcdri/miniconda3/envs/vllm/lib/python3.9/site-pack...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 2.7.0 [pip3] torchvision==0.22.0 [pip3] transformers==4.57.0.dev0 [pip3] triton==3.3.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-cublas-cu12 12.6.4.1 pypi_0 pypi [conda] nvidia-cuda-cupt

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
