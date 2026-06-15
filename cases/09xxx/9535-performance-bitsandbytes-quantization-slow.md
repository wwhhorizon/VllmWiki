# vllm-project/vllm#9535: [Performance]: bitsandbytes quantization slow

| 字段 | 值 |
| --- | --- |
| Issue | [#9535](https://github.com/vllm-project/vllm/issues/9535) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: bitsandbytes quantization slow

### Issue 正文摘录

### Proposal to improve performance Improve bitsandbytes quantization inference speed ### Report of performance regression I'm testing llama-3.2-1b on a toy dataset. For offline inference using the LLM class, the original model from Huggingface took 45 seconds but the 4-bit model (both inflight quantized and unsloth quantized) took 71 seconds. I wonder if I'm not serving the quantized models properly or is it expected that bnb quantization leads to very slow inference speed due to being under optimized at this point. ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` Can't run this on my work machine. ``` A100-80GB vllm==0.6.3.post1 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ation inference speed ### Report of performance regression I'm testing llama-3.2-1b on a toy dataset. For offline inference using the LLM class, the original model from Huggingface took 45 seconds but the 4-bit model (b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: utput of `python collect_env.py` Can't run this on my work machine. ``` A100-80GB vllm==0.6.3.post1 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot li...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ove bitsandbytes quantization inference speed ### Report of performance regression I'm testing llama-3.2-1b on a toy dataset. For offline inference using the LLM class, the original model from Huggingface took 45 second...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: stions. performance model_support;quantization quantization slowdown env_dependency Proposal to improve performance
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Performance]: bitsandbytes quantization slow performance;stale ### Proposal to improve performance Improve bitsandbytes quantization inference speed ### Report of performance regression I'm testing llama-3.2-1b on a to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
