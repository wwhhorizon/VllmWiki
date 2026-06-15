# vllm-project/vllm#6462: [Bug]: Can't load gemma-2-9b-it with vllm 0.5.2

| 字段 | 值 |
| --- | --- |
| Issue | [#6462](https://github.com/vllm-project/vllm/issues/6462) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 39; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't load gemma-2-9b-it with vllm 0.5.2

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: RED OS release MUROM (7.3.4) Standard Edition (x86_64) GCC version: (GCC) 11.4.1 20230605 (Red Soft 11.4.0-1) Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.28 Python version: 3.10.9 (main, Jan 11 2023, 15:21:40) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.1.52-1.el7.3.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 Nvidia driver version: 530.30.02 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Архитектура: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Порядок байт: Little Endian CPU(s): 32 On-line CPU(s) list: 0-31 ID прроизводителя: GenuineIntel Имя модели: 13th Gen Intel(R) Core(TM) i9-13900K Семейство ЦПУ: 6 Модель: 183 Thread(s) per core: 2 Ядер на сокет: 24 Сокетов: 1 Степпинг: 1 CPU max MHz: 5800,0000 CPU min MHz: 800,0000 BogoMIPS: 59...

## 现有链接修复摘要

#6517 [CI/Build] Build on Ubuntu 20.04 instead of 22.04

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: -9b-it with vllm 0.5.2 bug ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: RED OS release MUROM (7.3.4) Standa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: RED OS release MUROM (7.3.4) Standard Edition (x86_64) GCC version: (GCC) 11.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Can't load gemma-2-9b-it with vllm 0.5.2 bug ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: RED OS rel...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: x async abort: Not affected Versions of relevant libraries: [pip3] flashinfer==0.0.8+cu121torch2.3 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] onnxruntime==1.18.0 [pip3] sen...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ai.api_server --port=8080 --host=0.0.0.0 --model /models/gemma-2-9b-it --quantization fp8 --enforce-eager --seed 1234 --served-model-name gemma-2-9b no issues (except sliding window warning and capping the max length to...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6517](https://github.com/vllm-project/vllm/pull/6517) | mentioned | 0.6 | [CI/Build] Build on Ubuntu 20.04 instead of 22.04 | he version of GLIBC required for vLLM. This should reduce issues like #6462 happening in the future (but not completely prevent them). In the future we might want to consider swit… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
