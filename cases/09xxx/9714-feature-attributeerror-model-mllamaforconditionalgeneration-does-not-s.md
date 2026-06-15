# vllm-project/vllm#9714: [Feature]: AttributeError: Model MllamaForConditionalGeneration does not support BitsAndBytes quantization yet

| 字段 | 值 |
| --- | --- |
| Issue | [#9714](https://github.com/vllm-project/vllm/issues/9714) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: AttributeError: Model MllamaForConditionalGeneration does not support BitsAndBytes quantization yet

### Issue 正文摘录

### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0 Clang version: Could not collect CMake version: version 3.26.4 Libc version: glibc-2.31 Python version: 3.10.13 (main, Sep 11 2023, 13:44:35) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-122-generic-x86_64-with-glibc2.31 Is CUDA available: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 ### Model Input Dumps `vllm serve unsloth/Llama-3.2-90B-Vision-Instruct-bnb-4bit --quantization bitsandbytes --load-format bitsandbytes --trust-remote-code --enforce-eager` ``` Initializing an LLM engine (v0.6.3.post1) with config: model='unsloth/Llama-3.2-90B-Vision-Instruct-bnb-4bit', speculative_config=None , tokenizer='unsloth/Llama-3.2-90B-Vision-Instruct-bnb-4bit', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True,...

## 现有链接修复摘要

#9720 [Model] Add BNB quantization support for Mllama

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC vers...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Feature]: AttributeError: Model MllamaForConditionalGeneration does not support BitsAndBytes quantization yet feature request ### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: rror: Model MllamaForConditionalGeneration does not support BitsAndBytes quantization yet feature request ### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: F...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: onment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC version: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: itionalGeneration does not support BitsAndBytes quantization yet feature request ### Your current environment Collecting environment information... PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build P...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9720](https://github.com/vllm-project/vllm/pull/9720) | closes_keyword | 0.95 | [Model] Add BNB quantization support for Mllama | FIX #9714 (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
