# vllm-project/vllm#11067: [Bug]: Actively generated `request` is starved when new requests arrive (tensor parallel)

| 字段 | 值 |
| --- | --- |
| Issue | [#11067](https://github.com/vllm-project/vllm/issues/11067) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Actively generated `request` is starved when new requests arrive (tensor parallel)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Please help me understand problematic scheduler behavior for vLLM openAI API server: `vllm serve Qwen/Qwen2.5-72B-Instruct-GPTQ-Int4 --max-seq_len-to-capture 32768 --max-model-len 32768 -tp 4` 1. Request `A` comes in (prompt: "tell me super long story") and starts being generated immediately. 2. Request `B` arrives (30k tokens prompt), immediately causing Request `A` to pause generation. 3. Once request `B` is fully prompt-processed, token generation resumes for request `A` and begins for request `B`. In other words, prompt-processing always takes precedence over token-generation within `--max-num-seqs` pool. This way it's easy to construct a scenario where request `A` is being starved for quite long. If I understand, the rationale behind this behavior is that prompt-processing fully occupies all `-tp N` GPUs for only one request, while token-generation (sequential in nature) can perform N requests well in parallel. So vLLM tries to feed GPUs with N requests at the time. While this works efficiently for offline generation, it may be problematic for online use case where response generation for...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: LLM tries to feed GPUs with N requests at the time. While this works efficiently for offline generation, it may be problematic for online use case where response generation for one user is paused several times before co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: r for vLLM openAI API server: `vllm serve Qwen/Qwen2.5-72B-Instruct-GPTQ-Int4 --max-seq_len-to-capture 32768 --max-model-len 32768 -tp 4` 1. Request `A` comes in (prompt: "tell me super long story") and starts being gen...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Actively generated `request` is starved when new requests arrive (tensor parallel) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Please help me understand probl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l.) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: arrive (tensor parallel) bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Please help me understand problematic scheduler behavior for vLLM openAI API server: `vllm serve...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
