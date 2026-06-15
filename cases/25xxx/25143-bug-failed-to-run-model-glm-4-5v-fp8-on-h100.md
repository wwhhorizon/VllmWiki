# vllm-project/vllm#25143: [Bug]: Failed to run model GLM-4.5V-FP8 on H100

| 字段 | 值 |
| --- | --- |
| Issue | [#25143](https://github.com/vllm-project/vllm/issues/25143) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to run model GLM-4.5V-FP8 on H100

### Issue 正文摘录

### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : CentOS Stream 9 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-9) Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.8.0+cu129 Is debug build : False CUDA used to build PyTorch : 12.9 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 4 2025, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-7)] (64-bit runtime) Python platform : Linux-6.4.3-0_fbk15_hardened_2630_gf27365f948db-x86_64-with-glibc2.34 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.93 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H100 GPU 1: NVIDIA H100 GPU 2: NVIDIA H100 GPU 3: NVIDIA H100 GPU 4: NVIDIA H100 GPU 5: NVIDIA H100 GPU 6: NVIDIA H100 GPU 7: NVIDIA H100 Nvidia driver version : 550.90.07 cuDNN version : Pr...

## 现有链接修复摘要

#29889 [Bugfix] respect user-defined flash attention version in ViT attentions

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ============ OS : CentOS Stream 9 (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-9) Clang version : Could not collect CMake version : version 4.1.0 Libc version : glibc-2.34 ===============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: Failed to run model GLM-4.5V-FP8 on H100 bug ### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : CentOS Stream 9 (...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Failed to run model GLM-4.5V-FP8 on H100 bug ### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : Cent
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Failed to run model GLM-4.5V-FP8 on H100 bug ### Your current environment ``` Collecting environment information... ============================== System Info ============================== OS : CentOS Stream 9 (...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: u129 [pip3] torchvision==0.23.0+cu129 [pip3] transformers==4.56.1 [pip3] triton==3.4.0 [conda] Could not collect ============================== vLLM Info ============================== ROCM Version : Could not collect v...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29889](https://github.com/vllm-project/vllm/pull/29889) | closes_keyword | 0.95 | [Bugfix] respect user-defined flash attention version in ViT attentions | fix #27103, #25143, #17392, #28903 in better way. ## Test Plan Run `Qwen/Qwen3-VL-32B-Instruct` successfully with the default FA backend on H100. ```bash vllm serve Qwen/Qwen3-V |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
