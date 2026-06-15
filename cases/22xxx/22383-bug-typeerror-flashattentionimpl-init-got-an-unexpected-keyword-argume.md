# vllm-project/vllm#22383: [Bug]: TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'sinks'

| 字段 | 值 |
| --- | --- |
| Issue | [#22383](https://github.com/vllm-project/vllm/issues/22383) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'sinks'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Below are the steps taken to install the environment: ``` pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/cu128 \ ``` Trying to load the model using vllm. Logs below: ``` [2025-08-06 18:00:02,704] [35/MainThread] [INFO] [__main__] Received start command: {'batchSize': 2, 'fakeLLMServer': False, 'hfApiKey': 'REDACTED', 'hfHandlingMode': 'TEXT_GENERATION_LLAMA_2', 'hfModelName': 'openai/gpt-oss-20b', 'hfModelPath': '/data/dataiku/dss_data/model_cache/hf/openai_2fgpt-oss-20b', 'modelOrigin': 'HUGGINGFACE_MODEL', 'modelSettings': {'chatTemplateSettings': {'overrideChatTemplate': False}, 'deviceStrategy': 'NONE', 'enableVaeSlicing': True, 'enableVaeTiling': True, 'engine': 'AUTO', 'guidedDecodingBackend': 'outlines', 'maxModelLen': 65536, 'quantizationMode': 'NONE', 'toolSettings': {'enableTools': False}}, 'supportsImageInputs': False, 'type': 'start', 'useDSSModelCache': True} [2025-08-06 18:00:02,704] [35/ThreadPoolExecutor-0_0] [INFO] [__main__] Python version: 3.12.9 [2025-08-06 18:00:02,704] [35/ThreadPoolExecutor-0_0] [INFO] [_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ent environment ### 🐛 Describe the bug Below are the steps taken to install the environment: ``` pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://down...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: 'outlines', 'maxModelLen': 65536, 'quantizationMode': 'NONE', 'toolSettings': {'enableTools': False}}, 'supportsImageInputs': False, 'type': 'start', 'useDSSModelCache': True} [2025-08-06 18:00:02,704] [35/ThreadPoolExe...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/cu128 \ ``` Trying to load the model using vllm. Logs below: ``` [2025-08-06 18:...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: [Bug]: TypeError: FlashAttentionImpl.__init__() got an unexpected keyword argument 'sinks' bug;stale ### Your current environment ### 🐛 Describe the bug Below are the steps taken to install the environment: ``` pip inst...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: hAttentionImpl.__init__() got an unexpected keyword argument 'sinks' bug;stale ### Your current environment ### 🐛 Describe the bug Below are the steps taken to install the environment: ``` pip install --pre vllm==0.10.1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
