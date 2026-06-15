# vllm-project/vllm#30401: [Bug]: EAGLE3 failure with gpt-oss 20b and 120b

| 字段 | 值 |
| --- | --- |
| Issue | [#30401](https://github.com/vllm-project/vllm/issues/30401) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: EAGLE3 failure with gpt-oss 20b and 120b

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I get this error when trying to use speculative decoding with gpt-oss models, models used: gpt-oss 20b and 120b eagle3 models used: RedHatAI/gpt-oss-20b-speculator.eagle3 nvidia/gpt-oss-120b-Eagle3 and all fail for some reason. code: ```python llm = LLM( "/kaggle/input/gpt-oss-120b/transformers/default/1", dtype="bfloat16", max_num_seqs=6, max_model_len=32768, trust_remote_code=True, tensor_parallel_size=1, gpu_memory_utilization=0.96, speculative_config={ "model": "/kaggle/input/nvidia-gpt-oss-120b-eagle3/transformers/default/1", "draft_tensor_parallel_size": 1, "num_speculative_tokens": 3, "method": "eagle3", }, ) ``` Logs and Error: ``` INFO 12-10 16:32:58 [utils.py:233] non-default args: {'trust_remote_code': True, 'dtype': 'bfloat16', 'max_model_len': 32768, 'gpu_memory_utilization': 0.96, 'max_num_seqs': 6, 'disable_log_stats': True, 'speculative_config': {'model': '/kaggle/input/nvidia-gpt-oss-120b-eagle3/transformers/default/1', 'draft_tensor_parallel_size': 1, 'num_speculative_tokens': 3, 'method': 'eagle3'}, 'model': '/kaggle/input/gpt-oss-120b/transformers/default/1'} The argument `trust_remote_code` is to be used with...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: llm = LLM( "/kaggle/input/gpt-oss-120b/transformers/default/1", dtype="bfloat16", max_num_seqs=6, max_model_len=32768, trust_remote_code=True, tensor_parallel_size=1, gpu_memory_utilization=0.96, speculative_config={ "m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: EAGLE3 failure with gpt-oss 20b and 120b bug;stale ### Your current environment ### 🐛 Describe the bug I get this error when trying to use speculative decoding with gpt-oss models, models used: gpt-oss 20b and 12...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: toss'), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None), seed=0, served_model_name=/kaggle/input/gpt-oss-120b/transformers/default/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: EAGLE3 failure with gpt-oss 20b and 120b bug;stale ### Your current environment ### 🐛 Describe the bug I get this error when trying to use speculative decoding with gpt-oss models, models used: gpt-oss 20b and 12...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='openai_gptoss'), obse...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
