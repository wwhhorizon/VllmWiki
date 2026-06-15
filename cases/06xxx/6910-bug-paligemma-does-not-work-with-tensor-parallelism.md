# vllm-project/vllm#6910: [Bug]: Paligemma does not work with tensor parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#6910](https://github.com/vllm-project/vllm/issues/6910) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Paligemma does not work with tensor parallelism

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.30.1 Libc version: glibc-2.35 Python version: 3.10.12 (main, Mar 22 2024, 16:50:05) [GCC 11.4.0] (64-bit runtime) Python platform: Linux-6.5.0-1022-aws-x86_64-with-glibc2.35 Is CUDA available: True CUDA runtime version: 12.4.131 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA L4 GPU 1: NVIDIA L4 GPU 2: NVIDIA L4 GPU 3: NVIDIA L4 Nvidia driver version: 535.183.01 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_precompiled.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_engines_runtime_compiled.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_graph.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_heuristic.so.9.1.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops.so.9.1.0 HI...

## 现有链接修复摘要

#6930 [Bugfix] Fix PaliGemma MMP

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: rrent environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.4 LTS (x86_64) GCC ver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Paligemma does not work with tensor parallelism bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 R...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Paligemma does not work with tensor parallelism bug ### Your current environment ```text Collecting environment information... PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 R...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: x async abort: Not affected Versions of relevant libraries: [pip3] flashinfer==0.0.9+cu121torch2.3 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] onnx==1.16.1 [pip3] onnxruntime-gpu==1.18.0 [pip3] sentence-...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: here is an issue during the warmup phase when using tensor parallelism. Reproducible example: ```python from vllm import LLM llm = LLM(model="google/paligemma-3b-mix-448", tensor_parallel_size=2) ``` Exception: ``` INFO...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6930](https://github.com/vllm-project/vllm/pull/6930) | closes_keyword | 0.95 | [Bugfix] Fix PaliGemma MMP | FIXES #6910 --- <details> <!-- inside this <details> section, markdown rendering does not work, so we use raw html here. --> <summary><b> PR Checklist (Click to Expand) </ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
