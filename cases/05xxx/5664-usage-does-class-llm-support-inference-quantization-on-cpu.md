# vllm-project/vllm#5664: [Usage]: Does class LLM support inference quantization on CPU?

| 字段 | 值 |
| --- | --- |
| Issue | [#5664](https://github.com/vllm-project/vllm/issues/5664) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling |
| 症状 | build_error;oom;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Does class LLM support inference quantization on CPU?

### Issue 正文摘录

### Your current environment Hey Team, I was experimenting with class **LLM** using gptq_marlin on the GPU, and it is incredibly fast. However, when I tried running it on the CPU, it seems that the class does not support CPU usage. Is there an alternative that supports CPU, in case I missed something? Thanks. ``` class LLM: """An LLM for generating texts from given prompts and sampling parameters. This class includes a tokenizer, a language model (possibly distributed across multiple GPUs), and GPU memory space allocated for intermediate states (aka KV cache). Given a batch of prompts and sampling parameters, this class generates texts from the model, using an intelligent batching mechanism and efficient memory management. NOTE: This class is intended to be used for offline inference. For online serving, use the `AsyncLLMEngine` class instead. NOTE: For the comprehensive list of arguments, see `EngineArgs`. Args: model: The name or path of a HuggingFace Transformers model. tokenizer: The name or path of a HuggingFace Transformers tokenizer. tokenizer_mode: The tokenizer mode. "auto" will use the fast tokenizer if available, and "slow" will always use the slow tokenizer. skip_token...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: exts from the model, using an intelligent batching mechanism and efficient memory management. NOTE: This class is intended to be used for offline inference. For online serving, use the `AsyncLLMEngine` class instead. NO...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Usage]: Does class LLM support inference quantization on CPU? usage;stale ### Your current environment Hey Team, I was experimenting with class **LLM** using gptq_marlin on the GPU, and it is incredibly fast. However,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: generates texts from the model, using an intelligent batching mechanism and efficient memory management. NOTE: This class is intended to be used for offline inference. For online serving, use the `AsyncLLMEngine` class...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: r, a language model (possibly distributed across multiple GPUs), and GPU memory space allocated for intermediate states (aka KV cache). Given a batch of prompts and sampling parameters, this class generates texts from t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nd sampling parameters. This class includes a tokenizer, a language model (possibly distributed across multiple GPUs), and GPU memory space allocated for intermediate states (aka KV cache). Given a batch of prompts and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
