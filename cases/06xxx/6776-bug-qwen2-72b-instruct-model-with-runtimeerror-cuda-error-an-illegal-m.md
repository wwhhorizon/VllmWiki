# vllm-project/vllm#6776: [Bug]: qwen2-72b-instruct model  with RuntimeError: CUDA error: an illegal memory access was encountered 

| 字段 | 值 |
| --- | --- |
| Issue | [#6776](https://github.com/vllm-project/vllm/issues/6776) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: qwen2-72b-instruct model  with RuntimeError: CUDA error: an illegal memory access was encountered 

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.0a0+ebedce2 Is debug build: False CUDA used to build PyTorch: 12.3 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.0 Libc version: glibc-2.35 Python version: 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-4.19.91-014-kangaroo.2.10.13.5c249cdaf.x86_64-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.3.107 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA A100-SXM4-80GB GPU 1: NVIDIA A100-SXM4-80GB GPU 2: NVIDIA A100-SXM4-80GB GPU 3: NVIDIA A100-SXM4-80GB Nvidia driver version: 535.54.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.0.0 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.0.0 /usr/l...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: was encountered bug;stale ### Your current environment ```text PyTorch version: 2.3.0a0+ebedce2 Is debug build: False CUDA used to build PyTorch: 12.3 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug]: qwen2-72b-instruct model with RuntimeError: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ```text PyTorch version: 2.3.0a0+ebedce2 Is debug build: False CUDA used to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: qwen2-72b-instruct model with RuntimeError: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ```text PyTorch version: 2.3.0a0+ebedce2 Is debug build: False CUDA used to...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: transformers==4.42.4 [pip3] transformers-stream-generator==0.0.5 [pip3] triton==3.0.0 [conda] Could not collect ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.5.3.post1 vLLM Build Flags: CUDA Ar...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: RuntimeError: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ```text PyTorch version: 2.3.0a0+ebedce2 Is debug build: False CUDA used to build PyTorch: 12.3 ROCM used to buil...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | dc253 (0x7ff617ab0253 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #4: <unknown function> + 0x94ac3 (0x7ff623912ac3 in /lib/x86_64-linux-gnu/libc.so.6) frame #5: clone + 0x44 (0x |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x125 (0x7ff5b6db9ed5 in /usr/local/lib/python3.10/dist-packa… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xdc253 (0x7ff617ab0253 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unknown fu |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
