# vllm-project/vllm#25063: [Bug]: ShardedStateLoader Appears Not to Support MLA Architecture Models Like DeepSeek​

| 字段 | 值 |
| --- | --- |
| Issue | [#25063](https://github.com/vllm-project/vllm/issues/25063) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ShardedStateLoader Appears Not to Support MLA Architecture Models Like DeepSeek​

### Issue 正文摘录

### Your current environment My current environment The output of collect_env.py ```text Collecting environment information... ============================== System Info ============================== OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 10.5.0-1ubuntu1~22.04.2) 10.5.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.11 (main, Jun 4 2025, 08:56:18) [GCC 11.4.0] (64-bit runtime) Python platform : Linux-5.4.119-19.0009.56-x86_64-with-glibc2.35 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : 12.2.140 CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA H20 GPU 1: NVIDIA H20 GPU 2: NVIDIA H20 GPU 3: NVIDIA H20 GPU 4: NVIDIA H20 GPU 5: NVIDIA H20 GPU 6: NVIDIA H20 GPU 7: NVIDIA H20 Nvidia driver version : 535.216.01 cuDNN version :...

## 现有链接修复摘要

#25133 [Bugfix] Fix ShardedStateLoader support for DeepSeek models with MLA scaling parameters

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ========= OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 10.5.0-1ubuntu1~22.04.2) 10.5.0 Clang version : Could not collect CMake version : version 3.22.1 Libc version : glibc-2.35 ===============
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: pt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 avx512_bf16 clzero xsaveerptr wbnoinvd arat avx512vbmi umip avx512_vbmi2 vaes vpclmulqdq avx512_vnni avx512_bitalg avx512_vpopcntdq rdpid fsrm Hypervisor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: ShardedStateLoader Appears Not to Support MLA Architecture Models Like DeepSeek​ bug;stale ### Your current environment My current environment The output of collect_env.py ```text Collecting environment informati...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: ShardedStateLoader Appears Not to Support MLA Architecture Models Like DeepSeek​ bug;stale ### Your current environment My current environment The output of collect_env.py ```text Collecting environment informati...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: transformers==4.55.0 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==3.3.1 [pip3] tritonclient==2.51.0 [pip3] vector-quantize-pytorch==1.23.1 [conda] Could not collect ============================== vLLM Info...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25133](https://github.com/vllm-project/vllm/pull/25133) | closes_keyword | 0.95 | [Bugfix] Fix ShardedStateLoader support for DeepSeek models with MLA scaling parameters | fix specifically addresses the problem mentioned in issue #25063. --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [x] The purpose |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
