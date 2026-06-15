# vllm-project/vllm#37907: [Usage]: Unable to run Qwen3-14B with vLLM (multiple issues)

| 字段 | 值 |
| --- | --- |
| Issue | [#37907](https://github.com/vllm-project/vllm/issues/37907) |
| 状态 | open |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;import_error;oom |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Unable to run Qwen3-14B with vLLM (multiple issues)

### Issue 正文摘录

### Your current environment ```text (root) root@vllm01:~# python collect_env.py Collecting environment information... uv is set ============================== System Info ============================== OS : Debian GNU/Linux forky/sid (x86_64) GCC version : (Debian 15.2.0-15) 15.2.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.42 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13 (main, Mar 10 2026, 18:17:25) [Clang 21.1.4 ] (64-bit runtime) Python platform : Linux-6.17.0-19-generic-x86_64-with-glibc2.42 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA GeForce RTX 5060 Ti GPU 1: NVIDIA GeForce RTX 5060 Ti Nvidia driver version : 580.126.20 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version :...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: = OS : Debian GNU/Linux forky/sid (x86_64) GCC version : (Debian 15.2.0-15) 15.2.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.42 ==========================
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.10.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.13...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: Unable to run Qwen3-14B with vLLM (multiple issues) usage ### Your current environment ```text (root) root@vllm01:~# python collect_env.py Collecting environment information... uv is set =======================...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.6 [pip3] numpy==2.2.6 [pip3] nvidia-cublas==13.1.0.3 [pip3] nvidia-cuda-cupti==13.0.85 [pip3] nvidia-cuda-nvrtc==13.0.88 [p...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: rch version : 2.10.0+cu130 Is debug build : False CUDA used to build PyTorch : 13.0 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
