# vllm-project/vllm#36613: [Bug]: CUDA ILM (Illegal Memory Access) crash when enabling MTP for Qwen3.5-397B-A17B under high concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#36613](https://github.com/vllm-project/vllm/issues/36613) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA ILM (Illegal Memory Access) crash when enabling MTP for Qwen3.5-397B-A17B under high concurrency

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Description:** I am experiencing a critical crash (CUDA ILM / Illegal Memory Access error) when serving the `Qwen3.5-397B-A17B` model with Multi-Token Prediction (MTP) enabled under high concurrent requests, same as https://github.com/vllm-project/vllm/issues/34948#issuecomment-3977914704. The service runs perfectly fine under the same high-concurrency workload when MTP is disabled. The crash only occurs when the `--speculative-config` parameter is explicitly added and the server is hit with a high volume of concurrent requests. **Steps to Reproduce:** 1. Start the vLLM(0.17.0) server with the `Qwen3.5-397B-A17B` model and the following speculative decoding configuration: ```bash vllm serve Qwen/Qwen3.5-397B-A17B \ --host 0.0.0.0 \ --port 8000 \ --tensor-parallel-size 8 \ --max-model-len 262144 \ --reasoning-parser qwen3 \ --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' ``` 2. Send high-concurrency requests to the server. 3. The server will suddenly crash with a CUDA ILM error during request processing. **Control Test (Works Fine):** If I run the exact same command *without* the `--speculative-conf...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nt environment ### 🐛 Describe the bug **Description:** I am experiencing a critical crash (CUDA ILM / Illegal Memory Access error) when serving the `Qwen3.5-397B-A17B` model with Multi-Token Prediction (MTP) enabled und...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: CUDA ILM (Illegal Memory Access) crash when enabling MTP for Qwen3.5-397B-A17B under high concurrency bug ### Your current environment ### 🐛 Describe the bug **Description:** I am experiencing a critical crash (C...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: CUDA ILM (Illegal Memory Access) crash when enabling MTP for Qwen3.5-397B-A17B under high concurrency bug ### Your current environment ### 🐛 Describe the bug **Description:** I am experiencing a critical crash (C...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: B` model with Multi-Token Prediction (MTP) enabled under high concurrent requests, same as https://github.com/vllm-project/vllm/issues/34948#issuecomment-3977914704. The service runs perfectly fine under the same high-c...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
