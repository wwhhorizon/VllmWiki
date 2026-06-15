# vllm-project/vllm#30172: [Bug]: Qwen3-coder fails between 0.11.0 and 0.11.2

| 字段 | 值 |
| --- | --- |
| Issue | [#30172](https://github.com/vllm-project/vllm/issues/30172) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-coder fails between 0.11.0 and 0.11.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `v0.11.0` --- ``` 2025-12-06 13:09:11.513946+08:00 - gpustack.worker.backends.base - INFO - Preparing model files... 2025-12-06 13:09:11.521665+08:00 - gpustack.worker.backends.base - INFO - Model files are ready. 2025-12-06 13:09:11.521735+08:00 - gpustack.worker.serve_manager - INFO - Provisioning model instance qwen3-coder-FIhjt 2025-12-06 13:09:11.521771+08:00 - gpustack.worker.backends.custom - INFO - Starting custom backend model instance: qwen3-coder-FIhjt 2025-12-06 13:09:11.521906+08:00 - gpustack.worker.backends.base - INFO - Using Docker Hub for non-gpustack image; image resolved to: vllm/vllm-openai:v0.11.0 2025-12-06 13:09:11.521995+08:00 - gpustack.worker.backends.custom - INFO - Creating custom backend container workload: qwen3-coder-FIhjt 2025-12-06 13:09:11.522041+08:00 - gpustack.worker.backends.custom - INFO - With image: vllm/vllm-openai:v0.11.0, arguments: [/var/lib/gpustack/cache/huggingface/QuantTrio/Qwen3-Coder-30B-A3B-Instruct-AWQ --port 40061 --served-model-name qwen3-coder --max-model-len=110k --gpu-memory-utilization=0.6 --enable-auto-tool-choice --tool-call-parser=qwen3_xml --reasoning-parser=qwen3],...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: ug `v0.11.0` --- ``` 2025-12-06 13:09:11.513946+08:00 - gpustack.worker.backends.base - INFO - Preparing model files... 2025-12-06 13:09:11.521665+08:00 - gpustack.worker.backends.base - INFO - Model files are ready. 20...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: -06 13:09:11.521906+08:00 - gpustack.worker.backends.base - INFO - Using Docker Hub for non-gpustack image; image resolved to: vllm/vllm-openai:v0.11.0 2025-12-06 13:09:11.521995+08:00 - gpustack.worker.backends.custom...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3-coder fails between 0.11.0 and 0.11.2 bug;stale ### Your current environment ### 🐛 Describe the bug `v0.11.0` --- ``` 2025-12-06 13:09:11.513946+08:00 - gpustack.worker.backends.base - INFO - Preparing mode...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: 0, EP rank 0 [1;36m(EngineCore_DP0 pid=197)[0;0m INFO 12-05 21:09:44 [topk_topp_sampler.py:55] Using FlashInfer for top-p & top-k sampling. [1;36m(EngineCore_DP0 pid=197)[0;0m INFO 12-05 21:09:44 [gpu_model_runner.p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Qwen3-coder fails between 0.11.0 and 0.11.2 bug;stale ### Your current environment ### 🐛 Describe the bug `v0.11.0` --- ``` 2025-12-06 13:09:11.513946+08:00 - gpustack.worker.backends.base - INFO - Preparing mode...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
