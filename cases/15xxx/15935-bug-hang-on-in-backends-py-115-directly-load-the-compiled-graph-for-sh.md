# vllm-project/vllm#15935: [Bug]: Hang On In ”[backends.py:115] Directly load the compiled graph for shape None from the cache“

| 字段 | 值 |
| --- | --- |
| Issue | [#15935](https://github.com/vllm-project/vllm/issues/15935) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Hang On In ”[backends.py:115] Directly load the compiled graph for shape None from the cache“

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have 2 node , 1 GPU per node, try to do tensor parallel ``` vllm serve "deepseek-ai/DeepSeek-R1-Distill-Llama-70B" --max-model-len 4096 --tensor-parallel-size 2 ``` Hangs On as the follow log until show " [ray_distributed_executor.py:127] Shutting down Ray distributed executor. If you see error log from logging.cc regarding SIGTERM received, please ignore because this is the expected termination process in Ray. " logs ``` Loading safetensors checkpoint shards: 71% Completed | 12/17 [00:20<00:09, 1.81s/it] Loading safetensors checkpoint shards: 76% Completed | 13/17 [00:22<00:07, 1.82s/it] Loading safetensors checkpoint shards: 82% Completed | 14/17 [00:23<00:05, 1.81s/it] Loading safetensors checkpoint shards: 88% Completed | 15/17 [00:25<00:03, 1.82s/it] Loading safetensors checkpoint shards: 94% Completed | 16/17 [00:27<00:01, 1.82s/it] Loading safetensors checkpoint shards: 100% Completed | 17/17 [00:29<00:00, 1.84s/it] Loading safetensors checkpoint shards: 100% Completed | 17/17 [00:29<00:00, 1.73s/it] (RayWorkerWrapper pid=586) (RayWorkerWrapper pid=586) INFO 04-02 00:17:47 [loader.py:447] Loading weights took 29.43 secon...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: Hang On In ”[backends.py:115] Directly load the compiled graph for shape None from the cache“ bug;stale ### Your current environment ### 🐛 Describe the bug I have 2 node , 1 GPU per node, try to do tensor paralle...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Hang On In ”[backends.py:115] Directly load the compiled graph for shape None from the cache“ bug;stale ### Your current environment ### 🐛 Describe the bug I have 2 node , 1 GPU per node, try to do tensor paralle...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ry to do tensor parallel ``` vllm serve "deepseek-ai/DeepSeek-R1-Distill-Llama-70B" --max-model-len 4096 --tensor-parallel-size 2 ``` Hangs On as the follow log until show " [ray_distributed_executor.py:127] Shutting do...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 0, PP rank 0, TP rank 0 (RayWorkerWrapper pid=586) INFO 04-02 00:17:17 [cuda.py:220] Using Flash Attention backend on V1 engine. (RayWorkerWrapper pid=586) INFO 04-02 00:17:17 [gpu_model_runner.py:1174] Starting to load...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: -R1-Distill-Llama-70B... (RayWorkerWrapper pid=586) INFO 04-02 00:17:18 [topk_topp_sampler.py:53] Using FlashInfer for top-p & top-k sampling. (RayWorkerWrapper pid=586) INFO 04-02 00:17:18 [weight_utils.py:265] Using m...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
