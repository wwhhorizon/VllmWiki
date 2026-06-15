# vllm-project/vllm#35702: [Bug]: Qwen3.5-FP8 Crashes VLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#35702](https://github.com/vllm-project/vllm/issues/35702) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-FP8 Crashes VLLM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The model loads and the server starts properly, but as soon as I send a test request, the application crashes with a fatal error. I have also tried to serve the model with many different parameters, with the same result ```shell vllm serve Qwen/Qwen3.5-35B-A3B-FP8 --reasoning-parser qwen3 --enable-prefix-caching ``` ```shell user at 02:53:56 in ~ took 7m 5.8s [I] ➜ curl http://localhost:9002/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "qwen3.5", "messages": [ { "role": "user", "content": "Solve this riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?" } ], "temperature": 0.6, "max_tokens": 150 }' | jq { "error": { "message": "EngineCore encountered an issue. See stack trace (above) for the root cause.", "type": "InternalServerError", "param": null, "code": 500 } } ``` ```shell root at 02:44:08 in user/docker/vllm [I] ➜ nvidia-smi Mon Mar 2 02:44:10 2026 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 590.48.01 Driver Version: 590.48.01 CUDA Version: 13.1 | +-----------------------------...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ram": null, "code": 500 } } ``` ```shell root at 02:44:08 in user/docker/vllm [I] ➜ nvidia-smi Mon Mar 2 02:44:10 2026 +-----------------------------------------------------------------------------------------+ | NVIDIA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: 00 } } ``` ```shell root at 02:44:08 in user/docker/vllm [I] ➜ nvidia-smi Mon Mar 2 02:44:10 2026 +-----------------------------------------------------------------------------------------+ | NVIDIA-SMI 590.48.01 Driver...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen3.5-FP8 Crashes VLLM bug ### Your current environment ### 🐛 Describe the bug The model loads and the server starts properly, but as soon as I send a test request, the application crashes with a fatal error. I...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3.5-FP8 Crashes VLLM bug ### Your current environment ### 🐛 Describe the bug The model loads and the server starts properly, but as soon as I send a test request, the application crashes with a fatal error. I
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ng;model_support;quantization;sampling_logits cuda;fp8;operator;sampling;triton build_error;crash;nan_inf dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
