# vllm-project/vllm#6355: [Installation]: Running ohereForAI/c4ai-command-r-v01 with main pytorch 

| 字段 | 值 |
| --- | --- |
| Issue | [#6355](https://github.com/vllm-project/vllm/issues/6355) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Running ohereForAI/c4ai-command-r-v01 with main pytorch 

### Issue 正文摘录

### Your current environment why is it important: This is a prerequisite to the work on enabling troch.compile on vllm, we need to be able to build vllm with nightly so that we can iterate on changes and try features that are not released yet. current error: Failed to import from vllm._C with ImportError('/home/lsakka/vllm/vllm/_C.abi3.so: undefined symbol: cuTensorMapEncodeTiled') any idea what this could be? It was mentioned that vllm was struggling to upgrade one step version ```text Collecting environment information... WARNING 07-11 16:20:31 _custom_ops.py:14] Failed to import from vllm._C with ImportError('/home/lsakka/vllm/vllm/_C.abi3.so: undefined symbol: cuTensorMapEncodeTiled') PyTorch version: 2.5.0a0+git9c9744c Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Stream 9 (x86_64) GCC version: (GCC) 11.4.1 20231218 (Red Hat 11.4.1-3) Clang version: 17.0.6 (CentOS 17.0.6-5.el9) CMake version: version 3.30.0 Libc version: glibc-2.34 Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.12.0-0_fbk16_zion_7661_geb00762ce6d2-x86_64-with-glibc2.34 Is CUDA available: True CUDA...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 12: [Installation]: Running ohereForAI/c4ai-command-r-v01 with main pytorch installation;stale ### Your current environment why is it important: This is a prerequisite to the work on enabling troch.compile on vllm, we nee
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: struggling to upgrade one step version ```text Collecting environment information... WARNING 07-11 16:20:31 _custom_ops.py:14] Failed to import from vllm._C with ImportError('/home/lsakka/vllm/vllm/_C.abi3.so: undefined...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: pEncodeTiled') PyTorch version: 2.5.0a0+git9c9744c Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: CentOS Stream 9 (x86_64) GCC version: (GCC) 11.4.1 20231218 (Red Hat 11.4.1-3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ]: Running ohereForAI/c4ai-command-r-v01 with main pytorch installation;stale ### Your current environment why is it important: This is a prerequisite to the work on enabling troch.compile on vllm, we need to be able to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [pip3] torchvision==0.19.0a0+d23a6e1 [pip3] transformers==4.42.3 [pip3] triton==3.0.0 [conda] blas 1.0 mkl [conda] mkl 2023.1.0 h213fc3f_46344 [conda] mkl-service 2.4.0 py311h5eee18b_1 [c

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
