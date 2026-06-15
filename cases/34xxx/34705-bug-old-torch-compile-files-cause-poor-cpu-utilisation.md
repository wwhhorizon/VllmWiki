# vllm-project/vllm#34705: [Bug]: Old torch compile files cause poor CPU utilisation

| 字段 | 值 |
| --- | --- |
| Issue | [#34705](https://github.com/vllm-project/vllm/issues/34705) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Old torch compile files cause poor CPU utilisation

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Poor CPU utilisation observed when changing thread binding via ```VLLM_CPU_OMP_THREADS_BIND```. Problem goes away when you delete the contents of /tmp/torchinductor_* For example, running: ```python reproducer.py``` on a 64 core machine I see good utilisation on all cores (using htop). Then, if I run the below: ``` VLLM_CPU_OMP_THREADS_BIND=0-31 python reproducer.py ``` I see poor utilisation on cores 1-31 After deleting the directory /tmp/torchinductor_*, CPU utilisation is much improved: ``` VLLM_CPU_OMP_THREADS_BIND=0-31 python reproducer.py ``` But gets worse again if I allow auto binding (note only 32 threads in use): ```python reproducer.py``` Reproducer: ``` from vllm import LLM, SamplingParams def repro(): MODEL_NAME = "meta-llama/Llama-3.1-8B" prompts = [ "hello, how are you?", "What is vLLM?", "Can you tell me about Meta's model llama-3.1-8b?", "hello, how are you?", "What is vLLM?", "Can you tell me about Meta's model llama-3.1-8b?", "hello, how are you?", "What is vLLM?", "Can you tell me about Meta's model llama-3.1-8b?" ] llm = LLM(MODEL_NAME) outputs = llm.generate(prompts, sampling_params=SamplingParams(temperatur...

## 现有链接修复摘要

#35119 [compile] Invalidate cache for cpu flags

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Old torch compile files cause poor CPU utilisation bug;torch.compile ### Your current environment ### 🐛 Describe the bug Poor CPU utilisation observed when changing thread binding via ```VLLM_CPU_OMP_THREADS_BIND...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Reproducer: ``` from vllm import LLM, SamplingParams def repro(): MODEL_NAME = "meta-llama/Llama-3.1-8B" prompts = [ "hello, how are you?", "What is vLLM?", "Can you tell me about Meta's model llama-3.1-8b?", "hello, ho...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: te the contents of /tmp/torchinductor_* For example, running: ```python reproducer.py``` on a 64 core machine I see good utilisation on all cores (using htop). Then, if I run the below: ``` VLLM_CPU_OMP_THREADS_BIND=0-3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: g_logits;speculative_decoding cuda;operator;sampling build_error;nan_inf dtype;env_dependency #35119 [compile] Invalidate cache for cpu flags Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35119](https://github.com/vllm-project/vllm/pull/35119) | closes_keyword | 0.95 | [compile] Invalidate cache for cpu flags | Fixes #34705 These two env vars affect the number of OMP threads for inductor-compiled kernels. However they're currently in the set of `ignored_factors` for the compilation cache |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
