# vllm-project/vllm#37858: [Bug]: does not have the attribute 'FakeTensorMode'

| 字段 | 值 |
| --- | --- |
| Issue | [#37858](https://github.com/vllm-project/vllm/issues/37858) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: does not have the attribute 'FakeTensorMode'

### Issue 正文摘录

### Your current environment root@b20654c00b62:/app/model# python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Debian GNU/Linux 12 (bookworm) (x86_64) GCC version : (Debian 12.2.0-14+deb12u1) 12.2.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.36 ============================== PyTorch Info ============================== PyTorch version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.19 (main, Oct 9 2025, 22:46:37) [GCC 12.2.0] (64-bit runtime) Python platform : Linux-3.10.0-1160.119.1.el7.x86_64-x86_64-with-glibc2.36 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA A10 GPU 1: NVIDIA A10 Nvidia driver version : 550.90.12 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : Debian GNU/Linux 12 (bookworm) (x86_64) GCC version : (Debian 12.2.0-14+deb12u1) 12.2.0 Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.36 ==================
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: FakeTensorMode' bug ### Your current environment root@b20654c00b62:/app/model# python collect_env.py Collecting environment information... ============================== System Info ============================== OS : D...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.6 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.10.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.19...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: --gpu-memory-utilization 0.85 \ > --served-model-name=Qwen3.5-27B-FP8 \ > --port=10105 \ > --host=0.0.0.0 \ > --tensor-parallel-size=2 \ > --reasoning-parser qwen3 \ > --enable-auto-tool-choice \ > --tool-call-parser he...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
