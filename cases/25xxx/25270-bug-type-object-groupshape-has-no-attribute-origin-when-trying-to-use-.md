# vllm-project/vllm#25270: [Bug]: type object 'GroupShape' has no attribute '__origin__' when trying to use with torch.compile

| 字段 | 值 |
| --- | --- |
| Issue | [#25270](https://github.com/vllm-project/vllm/issues/25270) |
| 状态 | open |
| 标签 | bug;torch.compile;keep-open |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: type object 'GroupShape' has no attribute '__origin__' when trying to use with torch.compile

### Issue 正文摘录

### Your current environment ============================== System Info ============================== OS : Ubuntu 24.04.3 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Aug 14 2025, 17:47:21) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-6.8.0-79-generic-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 13.0.88 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA B200 GPU 1: NVIDIA B200 GPU 2: NVIDIA B200 GPU 3: NVIDIA B200 GPU 4: NVIDIA B200 GPU 5: NVIDIA B200 GPU 6: NVIDIA B200 Nvidia driver version : 580.82.07 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runtime version : N/A Is XNNPACK available : True ===============...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: 'GroupShape' has no attribute '__origin__' when trying to use with torch.compile bug;torch.compile;keep-open ### Your current environment ============================== System Info ============================== OS : Ub...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: untime version : 13.0.88 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA B200 GPU 1: NVIDIA B200 GPU 2: NVIDIA B200 GPU 3: NVIDIA B200 GPU 4: NVIDIA B200 GPU 5: NVIDIA B200 GPU 6: NVIDIA B...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: dio==2.8.0 [pip3] torchvision==0.23.0 [pip3] transformers==4.56.1 [pip3] triton==3.4.0 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: cqm_mbm_total cqm_mbm_local split_lock_detect user_shstk avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req vnmi avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmul...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
