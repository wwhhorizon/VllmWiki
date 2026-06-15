# vllm-project/vllm#42060: [Bug]: runai_streamer + MTP drafter fails to load weights from model_streamer local cache

| 字段 | 值 |
| --- | --- |
| Issue | [#42060](https://github.com/vllm-project/vllm/issues/42060) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: runai_streamer + MTP drafter fails to load weights from model_streamer local cache

### Issue 正文摘录

### Your current environment docker image vllm-openai:v0.20.1 ### 🐛 Describe the bug - Model: s3://models/Qwen_Qwen3.6-35B-A3B-FP8/ - Loader: runai_streamer - All model files present in S3 (see listing below). **Behavior:** - If I start vllm (vllm-openai:v0.20.1) without MTP (speculative decoding) enabled, the model loads and serves correctly from S3 via runai_streamer. - If I add `speculative_config={"method": "mtp", ...}` (e.g., for Qwen-3 MTP), the engine fails with: ``` RuntimeError: Cannot find any safetensors model weights with `/root/.cache/vllm/assets/model_streamer/ ` ``` (See full log excerpt below.) - Review of the S3 path shows all expected safetensors (layers-*.safetensors, mtp.safetensors, outside.safetensors, model.safetensors.index.json, etc.) are present. - The error only happens when MTP is enabled, and only during the drafter model load phase. **Theory / Tracing:** - vLLM loads the main model weights from S3 directly via runai_streamer. - For speculative MTP/drafter, vLLM attempts to reload (from a local cache path like `/root/.cache/vllm/assets/model_streamer/ `) and uses the runai_streamer loader's list_safetensors() function. - This function (by design) is no...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: runai_streamer + MTP drafter fails to load weights from model_streamer local cache bug ### Your current environment docker image vllm-openai:v0.20.1 ### 🐛 Describe the bug - Model: s3://models/Qwen_Qwen3.6-35B-A3...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: eights from model_streamer local cache bug ### Your current environment docker image vllm-openai:v0.20.1 ### 🐛 Describe the bug - Model: s3://models/Qwen_Qwen3.6-35B-A3B-FP8/ - Loader: runai_streamer - All model files p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: runai_streamer + MTP drafter fails to load weights from model_streamer local cache bug ### Your current environment docker image vllm-openai:v0.20.1 ### 🐛 Describe the bug - Model: s3://models/Qwen_Qwen3.6-35B-A3...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: .20.1 ### 🐛 Describe the bug - Model: s3://models/Qwen_Qwen3.6-35B-A3B-FP8/ - Loader: runai_streamer - All model files present in S3 (see listing below). **Behavior:** - If I start vllm (vllm-openai:v0.20.1) without MTP...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: sors() function. - This function (by design) is non-recursive and only searches for top-level `*.safetensors` files. - The model_streamer cache structure does NOT expose the weights at the root, and so loader returns no...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
