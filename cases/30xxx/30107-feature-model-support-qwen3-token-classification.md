# vllm-project/vllm#30107: [Feature]: Model Support: Qwen3 Token Classification

| 字段 | 值 |
| --- | --- |
| Issue | [#30107](https://github.com/vllm-project/vllm/issues/30107) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Model Support: Qwen3 Token Classification

### Issue 正文摘录

### 🚀 The feature, motivation and pitch May I know if it's possible to support **Qwen3ForTokenClassification** (https://github.com/huggingface/transformers/blob/main/src/transformers/models/qwen3/modeling_qwen3.py#L541) for token classification? It seems that there is currently no such class support in vLLM (https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/registry.py#L240), which means the architecture cannot be overridden. e.g. `vllm serve /tmp/sg_mount/mlop_pii_svc/pii_model_60K --tensor-parallel-size 1 --runner pooling --host 0.0.0.0 --hf-overrides '{"architectures": ["Qwen3ForTokenClassification"]}' --port 8080 --task classify` Full logs: ``` bash-5.1# vllm serve /tmp/sg_mount/mlop_pii_svc/pii_model_60K --tensor-parallel-size 1 --runner pooling --host 0.0.0.0 --hf-overrides '{"architectures": ["Qwen3ForTokenClassification"]}' --port 8080 --task classify INFO 12-05 04:20:43 [scheduler.py:216] Chunked prefill is enabled with max_num_batched_tokens=2048. WARNING 12-05 04:20:43 [argparse_utils.py:90] argument 'task' is deprecated (APIServer pid=10278) INFO 12-05 04:20:43 [api_server.py:1977] vLLM API server version 0.11.2 (APIServer pid=10278) INFO 12-05...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: rver pid=10278) INFO 12-05 04:20:43 [api_server.py:1977] vLLM API server version 0.11.2 (APIServer pid=10278) INFO 12-05 04:20:43 [utils.py:253] non-default args: {'model_tag': '/tmp/sg_mount/mlop_pii_svc/pii_model_60K'...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Feature]: Model Support: Qwen3 Token Classification feature request ### 🚀 The feature, motivation and pitch May I know if it's possible to support **Qwen3ForTokenClassification** (https://github.com/huggingface/transfo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: IServer pid=10278) INFO 12-05 04:20:48 [model.py:1968] Downcasting torch.float32 to torch.float16. (APIServer pid=10278) INFO 12-05 04:20:48 [model.py:1745] Using max model len 40960 (APIServer pid=10278) INFO 12-05 04:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Model Support: Qwen3 Token Classification feature request ### 🚀 The feature, motivation and pitch May I know if it's possible to support **Qwen3ForTokenClassification** (https://github.com/huggingface/transfo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: o, device_config=cuda, structured_outputs_config=StructuredOutputsConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_parser='', reasoning_parser_p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
