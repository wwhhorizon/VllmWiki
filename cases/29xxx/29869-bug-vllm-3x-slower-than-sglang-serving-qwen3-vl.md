# vllm-project/vllm#29869: [Bug]: vLLM 3x slower than SGLang serving Qwen3-VL

| 字段 | 值 |
| --- | --- |
| Issue | [#29869](https://github.com/vllm-project/vllm/issues/29869) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;gemm_linear;model_support;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | fp8;gemm |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 3x slower than SGLang serving Qwen3-VL

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Since the release of Qwen3-VL-8B-FP8, I have been noticing significant performance issues with vLLM vs. SGLang. I’m not sure whether this is due to a fundamental implementation limitation or simply a configuration issue. Running on the H100 PCIE with similar settings (FA3 + DeepGEMM for FP8 gemm), vLLM is 3x slower than SGLang with async serving (SGLang: 50-60 ms/img, vLLM: 170-180 ms/img). I have been trying various nightly images over the past weeks and I can confirm that the same issue is still persistent as of Dec 2nd. Trying various flags doesn't solve the issue. The problem is mainly in the image processing step, serving the text decoder works fine: ``` no image input | in_text_tokens=4096 ish, out_tokens=1: ~2ms/img -> seems ok with image inputs (256 requests in parallel) | in_text_tokens =1, out_tokens=1: 175 ms/img with image inputs (256 requests in parallel) | in_text_tokens =2048 ish, out_tokens=2048: 180 ms/img ``` In my estimates with SGLang, image processing should take about 25 ms/img on a machine with 8 cores for a 512 x 512 ish image. Settings: ``` args: - "--max-model-len" - "16384" - "--max-num-batched-tokens"...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vLLM 3x slower than SGLang serving Qwen3-VL bug ### Your current environment ### 🐛 Describe the bug Since the release of Qwen3-VL-8B-FP8, I have been noticing significant performance issues with vLLM vs. SGLang....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Describe the bug Since the release of Qwen3-VL-8B-FP8, I have been noticing significant performance issues with vLLM vs. SGLang. I’m not sure whether this is due to a fundamental implementation limitation or simply a co...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: environment ### 🐛 Describe the bug Since the release of Qwen3-VL-8B-FP8, I have been noticing significant performance issues with vLLM vs. SGLang. I’m not sure whether this is due to a fundamental implementation limitat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e. The problem is mainly in the image processing step, serving the text decoder works fine: ``` no image input | in_text_tokens=4096 ish, out_tokens=1: ~2ms/img -> seems ok with image inputs (256 requests in parallel) |...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: a configuration issue. Running on the H100 PCIE with similar settings (FA3 + DeepGEMM for FP8 gemm), vLLM is 3x slower than SGLang with async serving (SGLang: 50-60 ms/img, vLLM: 170-180 ms/img). I have been trying vari...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
