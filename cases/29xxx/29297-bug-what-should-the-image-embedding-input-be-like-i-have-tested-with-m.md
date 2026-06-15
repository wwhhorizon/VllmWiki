# vllm-project/vllm#29297: [Bug]: What should the image embedding input be like? I have tested with multiple cases but it all fails

| 字段 | 值 |
| --- | --- |
| Issue | [#29297](https://github.com/vllm-project/vllm/issues/29297) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: What should the image embedding input be like? I have tested with multiple cases but it all fails

### Issue 正文摘录

### Your current environment ```text ============================== System Info ============================== OS : Red Hat Enterprise Linux release 8.10 (Ootpa) (x86_64) GCC version : (GCC) 8.5.0 20210514 (Red Hat 8.5.0-26) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.28 ============================== PyTorch Info ============================== PyTorch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.19 (main, Oct 21 2025, 16:43:05) [GCC 11.2.0] (64-bit runtime) Python platform : Linux-4.18.0-553.50.1.el8_10.x86_64-x86_64-with-glibc2.28 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB Nvidia driver version : 575.51.03 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ==============================...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: : Red Hat Enterprise Linux release 8.10 (Ootpa) (x86_64) GCC version : (GCC) 8.5.0 20210514 (Red Hat 8.5.0-26) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.28 ============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10.19 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: version : Could not collect CUDA_MODULE_LOADING set to : GPU models and configuration : GPU 0: NVIDIA A100-SXM4-40GB GPU 1: NVIDIA A100-SXM4-40GB Nvidia driver version : 575.51.03 cuDNN version : Could not collect HIP r...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.5.2 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: orch version : 2.9.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.10...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
