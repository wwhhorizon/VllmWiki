# vllm-project/vllm#3543: [Usage]: model not support lora but listed in supported models

| 字段 | 值 |
| --- | --- |
| Issue | [#3543](https://github.com/vllm-project/vllm/issues/3543) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: model not support lora but listed in supported models

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0 Clang version: Could not collect CMake version: Could not collect Libc version: glibc-2.27 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.4.0-150-generic-x86_64-with-glibc2.27 Is CUDA available: True CUDA runtime version: 11.4.120 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA GeForce RTX 3090 GPU 1: NVIDIA GeForce RTX 3090 Nvidia driver version: 535.113.01 ### How would you like to use vllm I try to run the following commond: python -m vllm.entrypoints.openai.api_server \ --model /home/T3090U1/CZ/model/Qwen1.5-7B-Chat/ \ --enable-lora \ --lora-modules sql-lora=/home/T3090U1/CZ/model/output_sft_qwen_0320/ error message: ValueError: Model Qwen2ForCausalLM does not support LoRA, but LoRA is enabled. Support for this model may be added in the future. However, the document of vllm https://docs.vllm.ai/en/latest/models/supported_models....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Your current environment Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC vers...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: model not support lora but listed in supported models usage;stale ### Your current environment Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: onment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nvironment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 18.04.6 LTS (x86_64) GCC version: (Ubuntu 7.5.0-3ubuntu1~18.04) 7....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: model not support lora but listed in supported models usage;stale ### Your current environment Collecting environment information... PyTorch version: 2.1.2+cu121 Is debug build: False CUDA used to build PyTorch...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
