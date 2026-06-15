# vllm-project/vllm#32838: [Bug]: CompressedTensorsW4A16Fp4 is not support on turing

| 字段 | 值 |
| --- | --- |
| Issue | [#32838](https://github.com/vllm-project/vllm/issues/32838) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CompressedTensorsW4A16Fp4 is not support on turing

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```text Since v0.14.0, the turing GPU support nvfp4 weights. When deploy GadflyII/GLM-4.7-Flash-NVFP4 on turing, the error "Quantization scheme is not supported for 'the current GPU. Min capability: 80. Current capability: 75." reported. ``` ```text The full log: vllm-glm-4.7-flash-1 | (APIServer pid=1) INFO 01-21 23:26:02 [api_server.py:1272] vLLM API server version 0.14.0 vllm-glm-4.7-flash-1 | (APIServer pid=1) INFO 01-21 23:26:02 [utils.py:263] non-default args: {'model_tag': '/GLM-4.7-Flash', 'enable_auto_tool_choice': True, 'tool_call_parser': 'glm47', 'model': '/GLM-4.7-Flash', 'trust_remote_code': True, 'max_model_len': 4096, 'served_model_name': ['GLM-4.7-Flash'], 'reasoning_parser': 'glm45', 'pipeline_parallel_size': 2, 'kv_cache_memory_bytes': 4294967296, 'max_num_batched_tokens': 1024, 'max_num_seqs': 4} vllm-glm-4.7-flash-1 | (APIServer pid=1) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. vllm-glm-4.7-flash-1 | (APIServer pid=1) The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. vllm-glm-4.7-flash-1 | (APISe...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: CompressedTensorsW4A16Fp4 is not support on turing bug ### Your current environment ### 🐛 Describe the bug ```text Since v0.14.0, the turing GPU support nvfp4 weights. When deploy GadflyII/GLM-4.7-Flash-NVFP4 on...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='glm45', reasoning_par...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: PIServer pid=1) INFO 01-21 23:26:02 [api_server.py:1272] vLLM API server version 0.14.0 vllm-glm-4.7-flash-1 | (APIServer pid=1) INFO 01-21 23:26:02 [utils.py:263] non-default args: {'model_tag': '/GLM-4.7-Flash', 'enab...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: he error "Quantization scheme is not supported for 'the current GPU. Min capability: 80. Current capability: 75." reported. ``` ```text The full log: vllm-glm-4.7-flash-1 | (APIServer pid=1) INFO 01-21 23:26:02 [api_ser...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: (APIServer pid=1) INFO 01-21 23:26:02 [utils.py:263] non-default args: {'model_tag': '/GLM-4.7-Flash', 'enable_auto_tool_choice': True, 'tool_call_parser': 'glm47', 'model': '/GLM-4.7-Flash', 'trust_remote_code': True,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
