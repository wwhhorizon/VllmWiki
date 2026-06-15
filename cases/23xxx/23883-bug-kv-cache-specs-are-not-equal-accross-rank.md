# vllm-project/vllm#23883: [Bug]: KV cache specs are not equal accross rank

| 字段 | 值 |
| --- | --- |
| Issue | [#23883](https://github.com/vllm-project/vllm/issues/23883) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: KV cache specs are not equal accross rank

### Issue 正文摘录

### Your current environment $ python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Red Hat Enterprise Linux 9.5 (Plow) (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-5) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.34 ============================== PyTorch Info ============================== PyTorch version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.5 (main, Apr 2 2025, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-5)] (64-bit runtime) Python platform : Linux-5.14.0-284.88.1.el9_2.x86_64-x86_64-with-glibc2.34 ============================== CUDA / GPU Info ============================== Is CUDA available : True CUDA runtime version : Could not collect CUDA_MODULE_LOADING set to : LAZY GPU models and configuration : GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB Nvidia driver version : 550.127.08 cuDNN version : Could not collect HIP runtime version : N/A MIOpen runt...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag | #23974 [Hybrid Allocator] Support Pipeline Parallel

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: : Red Hat Enterprise Linux 9.5 (Plow) (x86_64) GCC version : (GCC) 11.5.0 20240719 (Red Hat 11.5.0-5) Clang version : Could not collect CMake version : Could not collect Libc version : glibc-2.34 ===========
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: version : 2.7.1+cu126 Is debug build : False CUDA used to build PyTorch : 12.6 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.12.5 (m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ur current environment $ python collect_env.py Collecting environment information... ============================== System Info ============================== OS : Red Hat Enterprise Linux 9.5 (Plow) (x86_64) GCC versio...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: num_kv_heads=8, head_size=256, dtype=torch.bfloat16, use_mla=False, sliding_window=None, attention_chunk_size=None, ), ), KVCacheGroupSpec( layer_names=[
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: dia-nvshmem-cu12==3.3.20 [pip3] nvidia-nvtx-cu12==12.6.77 [pip3] pytorch-triton==3.4.0+gitf7888497 [pip3] pyzmq==27.0.2 [pip3] torch==2.7.1 [pip3] torchaudio==2.7.1 [pip3] torchvision==0.22.1 [pip3] transformers==4.55.4...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23884: Should have ROCm label: NO (0 matches) #23883: Should have ROCm label: NO (0 matches) #23881: Should have ROCm label: NO (0 matches) #23880: Should hav |
| [#23974](https://github.com/vllm-project/vllm/pull/23974) | closes_keyword | 0.95 | [Hybrid Allocator] Support Pipeline Parallel | fix #23883 UPD 2025/09/10 Need to be careful about how to partition the layers into groups. In PP case, say if we have - stage 0: full.0, sw.0, sw.1 - stage 1: full.1, sw.2, sw.3 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
