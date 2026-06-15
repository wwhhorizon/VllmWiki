# vllm-project/vllm#19261: [Performance]: 在H20 运行vllm:v0.9.0 llama2-0.2B模型LoRA推理 ,执行模型Forward时Pytroch Dynamo 在CPU侧遍历；

| 字段 | 值 |
| --- | --- |
| Issue | [#19261](https://github.com/vllm-project/vllm/issues/19261) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: 在H20 运行vllm:v0.9.0 llama2-0.2B模型LoRA推理 ,执行模型Forward时Pytroch Dynamo 在CPU侧遍历；

### Issue 正文摘录

### Your current environment ```text python3 /usr/local/lib/python3.12/dist-packages/vllm/collect_env.py ``` Collecting environment information... ![Image](https://github.com/user-attachments/assets/4c150e55-998a-4c95-9e82-c98f5502c87b) ============================== System Info ============================== OS : Ubuntu 24.04.1 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : Could not collect Libc version : glibc-2.39 ============================== PyTorch Info ============================== PyTorch version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (main, Feb 4 2025, 14:48:35) [GCC 13.3.0] (64-bit runtime) Python platform : Linux-5.10.0-136.13.2.89.vo1sp1.x86_64-x86_64-with-glibc2.39 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.8.61 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDIA H20...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 24.04.1 LTS (x86_64) GCC version : (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 Clang version : 18.1.3 (1ubuntu1) CMake version : Could not collect Libc version : glibc-2.39 ==============
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: es xfd cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local avx_vnni avx512_bf16 wbnoinvd dtherm ida arat pln pts avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.7.0+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.3 (m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: 在H20 运行vllm:v0.9.0 llama2-0.2B模型LoRA推理 ,执行模型Forward时Pytroch Dynamo 在CPU侧遍历； usage;stale ### Your current environment ```text python3 /usr/local/lib/python3.12/dist-packages/vllm/collect_env.py ``` Collect...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: lm:v0.9.0 llama2-0.2B模型LoRA推理 ,执行模型Forward时Pytroch Dynamo 在CPU侧遍历； usage;stale ### Your current environment ```text python3 /usr/local/lib/python3.12/dist-packages/vllm/collect_env.py ``` Collecting environment informat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
