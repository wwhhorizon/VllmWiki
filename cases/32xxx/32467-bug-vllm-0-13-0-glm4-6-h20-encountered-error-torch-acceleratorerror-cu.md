# vllm-project/vllm#32467: [Bug]: vLLM 0.13.0, GLM4.6, H20; encountered error: torch.AcceleratorError: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#32467](https://github.com/vllm-project/vllm/issues/32467) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.13.0, GLM4.6, H20; encountered error: torch.AcceleratorError: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug start params: ```text python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8021 --model /apdcephfs_hldy/share_303551921/hunyuan/common/GLM-4.6-FP8 --served-model-name glm4.6 --max-model-len 114688 --tensor-parallel-size 8 --pipeline-parallel-size 1 --trust-remote-code --max-num-seqs 32 --dtype bfloat16 --enable-log-requests --served-model-name glm4.6 --tool-call-parser glm45 --enable-auto-tool-choice Initializing a V1 LLM engine (v0.13.0) with config: model='./GLM-4.6-FP8', speculative_config=None, tokenizer='./GLM-4.6-FP8', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=114688, download_dir=None, load_format=auto, tensor_parallel_size=8, pipeline_parallel_size=1, data_parallel_size=1, disable_custom_all_reduce=False, quantization=compressed-tensors, enforce_eager=False, kv_cache_dtype=auto, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_plugin='', enab...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 7: e_attn_quant': False, 'eliminate_noops': True, 'enable_sp': False, 'fuse_gemm_comms': False, 'fuse_allreduce_rms': False}, 'max_cudagraph_capture_size': 64, 'dynamic_shapes_config': {'type': , 'evaluate_guards': False},...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: port 8021 --model /apdcephfs_hldy/share_303551921/hunyuan/common/GLM-4.6-FP8 --served-model-name glm4.6 --max-model-len 114688 --tensor-parallel-size 8 --pipeline-parallel-size 1 --trust-remote-code --max-num-seqs 32 --...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: thon3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8021 --model /apdcephfs_hldy/share_303551921/hunyuan/common/GLM-4.6-FP8 --served-model-name glm4.6 --max-model-len 114688 --tensor-parallel-size 8 --pipe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: False), observability_config=ObservabilityConfig(show_hidden_metrics_for_version=None, otlp_traces_endpoint=None, collect_detailed_traces=None, kv_cache_metrics=False, kv_cache_metrics_sample=0.01, cudagraph_metrics=Fal...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: celeratorError: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment ### 🐛 Describe the bug start params: ```text python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --por...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
