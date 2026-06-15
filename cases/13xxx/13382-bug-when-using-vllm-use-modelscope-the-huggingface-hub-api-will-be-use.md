# vllm-project/vllm#13382: [Bug]: When using VLLM_USE_MODELSCOPE, the huggingface_hub API will be used to get the model file list.

| 字段 | 值 |
| --- | --- |
| Issue | [#13382](https://github.com/vllm-project/vllm/issues/13382) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When using VLLM_USE_MODELSCOPE, the huggingface_hub API will be used to get the model file list.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using `export VLLM_USE_MODELSCOPE=True`, the huggingface_hub API will be used to get the model file list. It takes a long time to wait, then return error: ```shell $ export VLLM_USE_MODELSCOPE=True $ export VLLM_USE_V1=1 $ vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-14B --enable-reasoning --reasoning-parser deepseek_r1 INFO 02-17 15:31:16 __init__.py:190] Automatically detected platform cuda. INFO 02-17 15:31:18 api_server.py:891] vLLM API server version 0.7.3.dev133+g84683fa2.d20250214 ... ERROR 02-17 15:33:29 config.py:102] Error retrieving file list: (MaxRetryError("HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /api/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B/tree/main?recursive=True&expand=False (Caused by ConnectTimeoutError( , 'Connection to huggingface.co timed out. (connect timeout=None)'))"), '(Request ID: 1ba47281-d3fd-47d8-b844-bc6c1984d527)'), retrying 1 of 2 ERROR 02-17 15:35:41 config.py:100] Error retrieving file list: (MaxRetryError("HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /api/models/deepseek-ai/DeepSeek-R1-Distill-Qw...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ed platform cuda. INFO 02-17 15:31:18 api_server.py:891] vLLM API server version 0.7.3.dev133+g84683fa2.d20250214 ... ERROR 02-17 15:33:29 config.py:102] Error retrieving file list: (MaxRetryError("HTTPSConnectionPool(h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: When using VLLM_USE_MODELSCOPE, the huggingface_hub API will be used to get the model file list. bug ### Your current environment ### 🐛 Describe the bug When using `export VLLM_USE_MODELSCOPE=True`, the huggingfa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: _r1 INFO 02-17 15:31:16 __init__.py:190] Automatically detected platform cuda. INFO 02-17 15:31:18 api_server.py:891] vLLM API server version 0.7.3.dev133+g84683fa2.d20250214 ... ERROR 02-17 15:33:29 config.py:102] Erro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: buted_parallel;frontend_api;hardware_porting;model_support cuda;operator;triton build_error;crash;nan_inf env_dependency Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: epseek-ai/DeepSeek-R1-Distill-Qwen-14B/tree/main?recursive=True&expand=False (Caused by ConnectTimeoutError( , 'Connection to huggingface.co timed out. (connect timeout=None)'))"), '(Request ID: 1ba47281-d3fd-47d8-b844-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
