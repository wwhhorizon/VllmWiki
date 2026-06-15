# vllm-project/vllm#30375: [Bug]: [TPU] ShapeDtypeStruct error when loading custom safetensors checkpoint on TPU v5litepod

| 字段 | 值 |
| --- | --- |
| Issue | [#30375](https://github.com/vllm-project/vllm/issues/30375) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [TPU] ShapeDtypeStruct error when loading custom safetensors checkpoint on TPU v5litepod

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM-TPU fails to load a **local HuggingFace checkpoint** (safetensors format) on TPU v5litepod with this error: ``` TypeError: Argument 'model.states[0][6]' of shape bfloat16[128] of type is not a valid JAX type. ``` **The core issue:** The Flax NNX model loader in `tpu_inference` creates the model with `ShapeDtypeStruct` shape placeholders, but these placeholders are never replaced with actual weight arrays before JIT compilation. Loading from **HuggingFace Hub works fine** (e.g., `Qwen/Qwen3-0.6B`), but loading the **exact same model architecture from a local directory fails**. ### How to reproduce the bug **Minimal reproduction:** from vllm import LLM # This WORKS: model = LLM("Qwen/Qwen3-0.6B", tensor_parallel_size=4, dtype="bfloat16") # This FAILS with ShapeDtypeStruct error: model = LLM( model="/path/to/local/checkpoint", # Contains model.safetensors + config.json tensor_parallel_size=4, dtype="bfloat16", trust_remote_code=True, )**Checkpoint directory contents:** ``` /path/to/local/checkpoint/ ├── config.json # Valid Qwen3 config with "architectures": ["Qwen3ForCausalLM"] ├── model.safetensors # bfloat16 weights (~1.2GB f...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: environment ### 🐛 Describe the bug vLLM-TPU fails to load a **local HuggingFace checkpoint** (safetensors format) on TPU v5litepod with this error: ``` TypeError: Argument 'model.states[0][6]' of shape bfloat16[128] of...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s**. ### How to reproduce the bug **Minimal reproduction:** from vllm import LLM # This WORKS: model = LLM("Qwen/Qwen3-0.6B", tensor_parallel_size=4, dtype="bfloat16") # This FAILS with ShapeDtypeStruct error: model = L...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: [TPU] ShapeDtypeStruct error when loading custom safetensors checkpoint on TPU v5litepod bug;stale ### Your current environment ### 🐛 Describe the bug vLLM-TPU fails to load a **local HuggingFace checkpoint** (sa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ct error when loading custom safetensors checkpoint on TPU v5litepod bug;stale ### Your current environment ### 🐛 Describe the bug vLLM-TPU fails to load a **local HuggingFace checkpoint** (safetensors format) on TPU v5...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: tly. ### Additional context - We're building an RL environment for LLM evaluation that needs to load custom finetuned checkpoints - JetStream/MaxText can load the same Orbax checkpoints without issues - The safetensors...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
