# vllm-project/vllm#22054: [Bug]: Voxtral on Docker: Value error, Model architectures ['VoxtralForConditionalGeneration', 'TransformersForMultimodalLM'] failed to be inspected

| 字段 | 值 |
| --- | --- |
| Issue | [#22054](https://github.com/vllm-project/vllm/issues/22054) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Voxtral on Docker: Value error, Model architectures ['VoxtralForConditionalGeneration', 'TransformersForMultimodalLM'] failed to be inspected

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Compose: voxstr: image: 'vllm/vllm-openai:v0.10.0' command: '--model /models/mistralai/Voxtral-Small-24B-2507 --served-model-name mistralai/Voxtral-Small-24B-2507 --tokenizer_mode mistral --config_format mistral --load_format mistral --tensor-parallel-size 1 --tool-call-parser mistral --enable-auto-tool-choice' shm_size: '2g' environment: CUDA_VISIBLE_DEVICES: 3 volumes: - '/home/XXXX/models:/models' restart: 'always' ports: - '8110:8000' deploy: resources: reservations: devices: - driver: nvidia device_ids: ['3'] capabilities: ["gpu"] Error Message: Value error, Model architectures ['VoxtralForConditionalGeneration', 'TransformersForMultimodalLM'] failed to be inspected Docker Log: Attaching to voxstr-1 voxstr-1 | INFO 07-31 21:39:54 [__init__.py:235] Automatically detected platform cuda. voxstr-1 | INFO 07-31 21:39:56 [api_server.py:1755] vLLM API server version 0.10.1.dev1+gbcc0a3cbe voxstr-1 | INFO 07-31 21:39:56 [cli_args.py:261] non-default args: {'enable_auto_tool_choice': True, 'tool_call_parser': 'mistral', 'model': '/models/mistralai/Voxtral-Small-24B-2507', 'tokenizer_mode': 'mistral', 'served_model_name': ['mistralai/...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Voxtral on Docker: Value error, Model architectures ['VoxtralForConditionalGeneration', 'TransformersForMultimodalLM'] failed to be inspected bug ### Your current environment ### 🐛 Describe the bug Compose: voxst...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Voxtral on Docker: Value error, Model architectures ['VoxtralForConditionalGeneration', 'TransformersForMultimodalLM'] failed to be inspected bug ### Your current environment ### 🐛 Describe the bug Compose: voxst...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Voxtral on Docker: Value error, Model architectures ['VoxtralForConditionalGeneration', 'TransformersForMultimodalLM'] failed to be inspected bug ### Your current environment ### 🐛 Describe the bug Compose: voxst...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ROR 07-31 21:40:03 [registry.py:396] from vllm.model_executor.layers.quantization.utils.fp8_utils import ( voxstr-1 | ERROR 07-31 21:40:03 [registry.py:396] File "/usr/local/lib/python3.12/dist-packages/vllm/model_execu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: y", line 69, in voxstr-1 | ERROR 07-31 21:40:03 [registry.py:396] CUTLASS_FP8_SUPPORTED = cutlass_fp8_supported() voxstr-1 | ERROR 07-31 21:40:03 [registry.py:396] ^^^^^^^^^^^^^^^^^^^^^^^ voxstr-1 | ERROR 07-31 21:40:03...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
