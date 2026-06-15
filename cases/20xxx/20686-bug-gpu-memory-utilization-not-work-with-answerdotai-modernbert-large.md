# vllm-project/vllm#20686: [Bug]: gpu_memory_utilization not work with answerdotai/ModernBERT-large

| 字段 | 值 |
| --- | --- |
| Issue | [#20686](https://github.com/vllm-project/vllm/issues/20686) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;fp8;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gpu_memory_utilization not work with answerdotai/ModernBERT-large

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I wanna use vllm to run ModernBERT, and I found a [blog](https://danielvanstrien.xyz/posts/2025/vllm/modern_inference_modernbert.html) that help me to achieve this. Luckily, this latest version of vllm@0.9.2.dev374+gd853520b3 could support ModernBert. However, when I set gpu_memory_utilization to 0.95 and run 10000 examples, it only uses 2G of the 96G H20 card (and run slowly). And the same code with Qwen3-0.6B could utillize 94G and run faster (both are trained to be sequence classify model). The core logic is quite simple: ``` llm = LLM(model=args.model, tensor_parallel_size=args.tensor_parallel_size, quantization='fp8',task='classify',gpu_memory_utilization=0.95) # get some prompt outputs = llm.classify(prompt_text) ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ence_modernbert.html) that help me to achieve this. Luckily, this latest version of vllm@0.9.2.dev374+gd853520b3 could support ModernBert. However, when I set gpu_memory_utilization to 0.95 and run 10000 examples, it on...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: = LLM(model=args.model, tensor_parallel_size=args.tensor_parallel_size, quantization='fp8',task='classify',gpu_memory_utilization=0.95) # get some prompt outputs = llm.classify(prompt_text) ``` ### Before submitting a n...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nly uses 2G of the 96G H20 card (and run slowly). And the same code with Qwen3-0.6B could utillize 94G and run faster (both are trained to be sequence classify model). The core logic is quite simple: ``` llm = LLM(model...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rdware_porting;model_support;quantization cuda;fp8;operator;quantization;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
