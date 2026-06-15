# vllm-project/vllm#35496: [Bug]: RPC call to sample_tokens timed out. Qwen3.5-397B-A17B

| 字段 | 值 |
| --- | --- |
| Issue | [#35496](https://github.com/vllm-project/vllm/issues/35496) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cache;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RPC call to sample_tokens timed out. Qwen3.5-397B-A17B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I followed the deployment instructions at https://github.com/vllm-project/recipes/blob/main/Qwen/Qwen3.5.md and used H200 GPUs for deployment. The service could be deployed initially, but I encountered the following bug: ``` No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv cache quantization). EngineCore encountered a fatal error. (EngineCore_DP0 pid=287050) ERROR 02-27 15:59:56 [core.py:1080] TimeoutError: RPC call to sample_tokens timed out. ``` Subsequently, the entire service crashed and returned the following response: ``` {"error":{"message":"EngineCore encountered an issue. See stack trace (above) for the root cause.","type":"InternalServerError","param":null,"code":500}} ``` Just run this: ``` curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{ "model": "Qwen/Qwen3.5-397B-A17B", "messages": [ {"role": "user", "content": "hello"} ], "temperature": 0.7, "max_tokens": 512 }' ``` ### Before submitting a new issue... - [x] Make sure you already searched for re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ollowed the deployment instructions at https://github.com/vllm-project/recipes/blob/main/Qwen/Qwen3.5.md and used H200 GPUs for deployment. The service could be deployed initially, but I encountered the following bug: `...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: encountered the following bug: ``` No available shared memory broadcast block found in 60 seconds. This typically happens when some processes are hanging or doing some time-consuming work (e.g. compilation, weight/kv ca...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: RPC call to sample_tokens timed out. Qwen3.5-397B-A17B bug ### Your current environment ### 🐛 Describe the bug I followed the deployment instructions at https://github.com/vllm-project/recipes/blob/main/Qwen/Qwen...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ing or doing some time-consuming work (e.g. compilation, weight/kv cache quantization). EngineCore encountered a fatal error. (EngineCore_DP0 pid=287050) ERROR 02-27 15:59:56 [core.py:1080] TimeoutError: RPC call to sam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
