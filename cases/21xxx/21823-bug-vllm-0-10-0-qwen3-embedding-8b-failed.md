# vllm-project/vllm#21823: [Bug]: vllm==0.10.0 Qwen3-Embedding-8B failed

| 字段 | 值 |
| --- | --- |
| Issue | [#21823](https://github.com/vllm-project/vllm/issues/21823) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm==0.10.0 Qwen3-Embedding-8B failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` uv run vllm serve ./models/Qwen3-Embedding-8B --served-model-name Qwen3-Embedding-8B --host 0.0.0.0 --port 10001 --max_model_len 32768 --gpu-memory-utilization 0.3 ``` Output ``` ,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":512,"local_cache_dir":null} INFO 07-29 18:42:00 [parallel_state.py:1102] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0 WARNING 07-29 18:42:00 [topk_topp_sampler.py:59] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install FlashInfer. INFO 07-29 18:42:00 [gpu_model_runner.py:1843] Starting to load model ./models/Qwen3-Embedding-8B... INFO 07-29 18:42:00 [gpu_model_runner.py:1875] Loading model from scratch... INFO 07-29 18:42:00 [cuda.py:290] Using Flash Attention backend on V1 engine. Loading safetensors checkpoint shards: 0% Completed | 0/4 [00:00<?, ?it/s] ERROR 07-29 18:42:01 [core.py:632] EngineCore failed to start. ERROR 07-29 18:42:01 [core.py:632] Traceback (most recent call last): ERROR 07-2...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 0, TP rank 0, EP rank 0 WARNING 07-29 18:42:00 [topk_topp_sampler.py:59] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best performance, please install...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: plementation of top-p & top-k sampling. For the best performance, please install FlashInfer. INFO 07-29 18:42:00 [gpu_model_runner.py:1843] Starting to load model ./models/Qwen3-Embedding-8B... INFO 07-29 18:42:00 [gpu_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vllm==0.10.0 Qwen3-Embedding-8B failed bug ### Your current environment ### 🐛 Describe the bug ``` uv run vllm serve ./models/Qwen3-Embedding-8B --served-model-name Qwen3-Embedding-8B --host 0.0.0.0 --port 10001...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ed as DP rank 0, PP rank 0, TP rank 0, EP rank 0 WARNING 07-29 18:42:00 [topk_topp_sampler.py:59] FlashInfer is not available. Falling back to the PyTorch-native implementation of top-p & top-k sampling. For the best pe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` Output ``` ,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1],"cudagraph_copy_inputs":false,"full_cuda_graph":false,"max_capture_size":512,"local_cache_dir":null} INFO 07-29 18:42:00 [parallel_state.py:1102] ran...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
