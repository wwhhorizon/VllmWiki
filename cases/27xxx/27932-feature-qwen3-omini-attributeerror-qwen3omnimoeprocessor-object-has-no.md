# vllm-project/vllm#27932: [Feature]: Qwen3 Omini AttributeError: 'Qwen3OmniMoeProcessor' object has no attribute '_get_num_multimodal_tokens'

| 字段 | 值 |
| --- | --- |
| Issue | [#27932](https://github.com/vllm-project/vllm/issues/27932) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cuda;operator;quantization;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Qwen3 Omini AttributeError: 'Qwen3OmniMoeProcessor' object has no attribute '_get_num_multimodal_tokens'

### Issue 正文摘录

### 🚀 The feature, motivation and pitch INFO 11-02 00:22:03 [__init__.py:216] Automatically detected platform cuda. [1;36m(APIServer pid=1735408)[0;0m INFO 11-02 00:22:07 [api_server.py:1839] vLLM API server version 0.11.0 [1;36m(APIServer pid=1735408)[0;0m INFO 11-02 00:22:07 [utils.py:233] non-default args: {'model_tag': '/gemini/space/yifq/zhaozy/models/Qwen/Qwen3-Omni-30B-A3B-Thinking', 'model': '/gemini/space/yifq/zhaozy/models/Qwen/Qwen3-Omni-30B-A3B-Thinking', 'trust_remote_code': True, 'tensor_parallel_size': 2} [1;36m(APIServer pid=1735408)[0;0m The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. [1;36m(APIServer pid=1735408)[0;0m Unrecognized keys in `rope_scaling` for 'rope_type'='default': {'mrope_interleaved', 'interleaved', 'mrope_section'} [1;36m(APIServer pid=1735408)[0;0m INFO 11-02 00:22:07 [model.py:547] Resolved architecture: TransformersForMultimodalLM [1;36m(APIServer pid=1735408)[0;0m `torch_dtype` is deprecated! Use `dtype` instead! [1;36m(APIServer pid=1735408)[0;0m INFO 11-02 00:22:07 [model.py:1510] Using max model len 65536 [1;36m(APIServer pid=1735408)[0;0m INFO 11-02 00:22:07 [schedul...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: eProcessor' object has no attribute '_get_num_multimodal_tokens' feature request;stale ### 🚀 The feature, motivation and pitch INFO 11-02 00:22:03 [__init__.py:216] Automatically detected platform cuda. [1;36m(APIServe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: =1735408)[0;0m INFO 11-02 00:22:07 [api_server.py:1839] vLLM API server version 0.11.0 [1;36m(APIServer pid=1735408)[0;0m INFO 11-02 00:22:07 [utils.py:233] non-default args: {'model_tag': '/gemini/space/yifq/zhaozy/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Feature]: Qwen3 Omini AttributeError: 'Qwen3OmniMoeProcessor' object has no attribute '_get_num_multimodal_tokens' feature request;stale ### 🚀 The feature, motivation and pitch INFO 11-02 00:22:03 [__init__.py:216] Aut...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: TransformersForMultimodalLM [1;36m(APIServer pid=1735408)[0;0m `torch_dtype` is deprecated! Use `dtype` instead! [1;36m(APIServer pid=1735408)[0;0m INFO 11-02 00:22:07 [model.py:1510] Using max model len 65536 [1;3...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
