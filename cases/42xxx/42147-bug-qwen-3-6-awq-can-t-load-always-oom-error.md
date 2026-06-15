# vllm-project/vllm#42147: [Bug]: Qwen 3.6 awq can't load, always OOM error

| 字段 | 值 |
| --- | --- |
| Issue | [#42147](https://github.com/vllm-project/vllm/issues/42147) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen 3.6 awq can't load, always OOM error

### Issue 正文摘录

### Your current environment ``` uv is set ============================== System Info ============================== OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Mar 23 2026, 19:04:32) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.17.0-23-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.2.78 CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 4090 Nvidia driver version : 595.58.03 cuDNN version : Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.22.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.22.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.22....

## 现有链接修复摘要

#42159 fix: honor CUDA graph memory profiling opt-out

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.4 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0 Clang version : Could not collect CMake version : version 3.28.3 Libc version : glibc-2.39 ===============
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Qwen 3.6 awq can't load, always OOM error bug ### Your current environment ``` uv is set ============================== System Info ============================== OS : Ubuntu 24.04.4 LT
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.8.post1 [pip3] numpy==2.3.5 [pip3] nvidia-cublas==13.1.0.3 [pip3] nvidia-cuda-cupti==13.0.85 [pip3] nvidia-cuda-nvrtc==13.0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.11.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A XPU used to build PyTorch : N/A ============================== Python Environment ========================...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: memory even if I enabled huge cpu offload. ``` (z3) z@z3:~$ VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS=0 vllm serve cyankiwi/Qwen3.6-35B-A3B-AWQ-4bit --gpu-memory-utilization 0.6 --kv-cache-dtype fp8 --max-model-len 65536...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42159](https://github.com/vllm-project/vllm/pull/42159) | closes_keyword | 0.95 | fix: honor CUDA graph memory profiling opt-out | Fixes #42147. ## Duplicate-work check - Checked issue comments for #42147. - Checked open PRs for `42147 in:body`: no matches. - Checked open PRs for CUDA graph memory profiling |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
