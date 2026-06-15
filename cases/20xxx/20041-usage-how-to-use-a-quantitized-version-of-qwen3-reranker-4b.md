# vllm-project/vllm#20041: [Usage]: How to use a quantitized version of Qwen3-Reranker-4B

| 字段 | 值 |
| --- | --- |
| Issue | [#20041](https://github.com/vllm-project/vllm/issues/20041) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use a quantitized version of Qwen3-Reranker-4B

### Issue 正文摘录

### Your current environment Option 1: Use fp16 instead of fp8 pythonfrom vllm import LLM model_name = "Qwen/Qwen3-Reranker-4B" def get_model() -> LLM: return LLM( model=model_name, task="score", dtype="float16", hf_overrides={ "architectures": ["Qwen3ForSequenceClassification"], "classifier_from_token": ["no", "yes"], "is_original_qwen3_reranker": True, }, ) model = get_model() Option 2: Use bfloat16 pythondef get_model() -> LLM: return LLM( model=model_name, task="score", dtype="bfloat16", hf_overrides={ "architectures": ["Qwen3ForSequenceClassification"], "classifier_from_token": ["no", "yes"], "is_original_qwen3_reranker": True, }, ) Option 3: Try auto dtype with explicit GPU memory fraction pythondef get_model() -> LLM: return LLM( model=model_name, task="score", dtype="auto", gpu_memory_utilization=0.8, hf_overrides={ "architectures": ["Qwen3ForSequenceClassification"], "classifier_from_token": ["no", "yes"], "is_original_qwen3_reranker": True, }, ) but is not supported ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already se...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Usage]: How to use a quantitized version of Qwen3-Reranker-4B usage;stale ### Your current environment Option 1: Use fp16 instead of fp8 pythonfrom vllm import LLM model_name = "Qwen/Qwen3-Reranker-4B" def get_model()...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Usage]: How to use a quantitized version of Qwen3-Reranker-4B usage;stale ### Your current environment Option 1: Use fp16 instead of fp8 pythonfrom vllm import LLM model_name = "Qwen/Qwen3-Reranker-4B" def get_model()...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: How to use a quantitized version of Qwen3-Reranker-4B usage;stale ### Your current environment Option 1: Use fp16 instead of fp8 pythonfrom vllm import LLM model_name = "Qwen/Qwen3-Reranker-4B" def get_model()...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: sk="score", dtype="float16", hf_overrides={ "architectures": ["Qwen3ForSequenceClassification"], "classifier_from_token": ["no", "yes"], "is_original_qwen3_reranker": True, }, ) model = get_model() Option 2: Use bfloat1...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: reranker": True, }, ) Option 3: Try auto dtype with explicit GPU memory fraction pythondef get_model() -> LLM: return LLM( model=model_name, task="score", dtype="auto", gpu_memory_utilization=0.8, hf_overrides={ "archit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
