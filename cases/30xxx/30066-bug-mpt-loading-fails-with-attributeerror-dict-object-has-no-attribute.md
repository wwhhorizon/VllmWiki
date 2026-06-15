# vllm-project/vllm#30066: [Bug]: MPT loading fails with AttributeError: 'dict' object has no attribute 'clip_qkv' and missing 'num_attention_heads'

| 字段 | 值 |
| --- | --- |
| Issue | [#30066](https://github.com/vllm-project/vllm/issues/30066) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;scheduler_memory;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | activation;attention;cache;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MPT loading fails with AttributeError: 'dict' object has no attribute 'clip_qkv' and missing 'num_attention_heads'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Describe the bug When attempting to load `mosaicml/mpt-7b-instruct` using `vLLM` (pip version), the engine fails initialization due to multiple AttributeErrors. These appear to be regressions in how the configuration object is parsed and accessed for older architectures like MPT. The errors occur in two distinct locations: `vllm/model_executor/models/mpt.py`: The `MPTAttention` class assumes `config.attn_config` is always an `object`, but it can be a `dict`. Accessing attributes directly (e.g., `.clip_qkv`) fails. `vllm/config/model.py`: The logic hardcodes access to standard HuggingFace attributes like `num_attention_heads` and `hidden_size`, but MPT uses `n_heads` and `d_model`, causing the inspection to fail. ## Minimal Reproduction Script Run the following Python script to trigger the error immediately: ```python from vllm import LLM # The model 'mosaicml/mpt-7b-instruct' triggers the initialization logic # that causes the AttributeError. llm = LLM( model="mosaicml/mpt-7b-instruct", tokenizer_mode="auto", trust_remote_code=True, dtype="bfloat16", tensor_parallel_size=1, max_model_len=2048, gpu_memory_utilization=0.9, ) ```...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: bug When attempting to load `mosaicml/mpt-7b-instruct` using `vLLM` (pip version), the engine fails initialization due to multiple AttributeErrors. These appear to be regressions in how the configuration object is parse...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 7b-instruct", tokenizer_mode="auto", trust_remote_code=True, dtype="bfloat16", tensor_parallel_size=1, max_model_len=2048, gpu_memory_utilization=0.9, ) ``` ## Error Logs Error 1: In `vllm/model_executor/models/mpt.py`...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: e to multiple AttributeErrors. These appear to be regressions in how the configuration object is parsed and accessed for older architectures like MPT. The errors occur in two distinct locations: `vllm/model_executor/mod...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: Language Model, we recommend setting "attn_impl" to "flash" instead of "triton". warnings.warn(UserWarning('If not using a Prefix Language Model, we recommend setting "attn_impl" to "flash" instead of "triton".')) INFO...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: object has no attribute 'clip_qkv' and missing 'num_attention_heads' bug;stale ### Your current environment ### 🐛 Describe the bug ## Describe the bug When attempting to load `mosaicml/mpt-7b-instruct` using `vLLM` (pip...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
