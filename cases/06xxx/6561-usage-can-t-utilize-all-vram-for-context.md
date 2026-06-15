# vllm-project/vllm#6561: [Usage]: Can't utilize all VRAM for context

| 字段 | 值 |
| --- | --- |
| Issue | [#6561](https://github.com/vllm-project/vllm/issues/6561) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Can't utilize all VRAM for context

### Issue 正文摘录

### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: RED OS release MUROM (7.3.4) Standard Edition (x86_64) GCC version: (GCC) 11.4.1 20230605 (Red Soft 11.4.0-1) Clang version: Could not collect CMake version: version 3.29.2 Libc version: glibc-2.28 Python version: 3.10.9 (main, Jan 11 2023, 15:21:40) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-6.1.52-1.el7.3.x86_64-x86_64-with-glibc2.28 Is CUDA available: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 Nvidia driver version: 530.30.02 cuDNN version: Could not collect HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Архитектура: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 46 bits physical, 48 bits virtual Порядок байт: Little Endian CPU(s): 32 On-line CPU(s) list: 0-31 ID прроизводителя: GenuineIntel Имя модели: 13th Gen Intel(R) Core(TM) i9-13900K Семейство ЦПУ: 6 Модель: 183 Thread(s) per core: 2 Ядер на сокет: 24 Сокетов: 1 Степпинг: 1 CPU max MHz: 5800,0000 CPU min MHz: 800,0000 BogoMIPS: 59...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: AM for context usage;stale ### Your current environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: RED OS release MUROM (7.3.4) Standa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: RED OS release MUROM (7.3.4) Standard Edition (x86_64) GCC version: (GCC) 11.4....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: ike to use vllm I want to run inference of a Mistral-Nemo-Instruct-2407-FP8 [specific model]([https://huggingface.co/neuralmagic/Mistral-Nemo-Instruct-2407-FP8](url)). Command line: `python -m vllm.entrypoints.openai.ap...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: True CUDA runtime version: 12.1.66 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 4090 Nvidia driver version: 530.30.02 cuDNN version: Could not collect HIP runtime version: N/A...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rent environment ```text PyTorch version: 2.3.1+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: RED OS release MUROM (7.3.4) Standard Edition (x86_64) GCC version: (GCC)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
