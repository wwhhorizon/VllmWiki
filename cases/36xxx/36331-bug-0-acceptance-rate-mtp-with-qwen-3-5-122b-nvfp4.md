# vllm-project/vllm#36331: [Bug]: 0% acceptance rate (MTP) with Qwen 3.5 122B (NVFP4)

| 字段 | 值 |
| --- | --- |
| Issue | [#36331](https://github.com/vllm-project/vllm/issues/36331) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0% acceptance rate (MTP) with Qwen 3.5 122B (NVFP4)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug MTP has 0% acceptance rate with Qwen3.5-122B-A10B-NVFP4 Script : ```bash export CUDA_VISIBLE_DEVICES=3 export NCCL_CUMEM_ENABLE=0 export VLLM_ENABLE_CUDAGRAPH_GC=1 export VLLM_USE_FLASHINFER_SAMPLER=1 vllm serve /data/models/Qwen3.5-122B-A10B-NVFP4 \ --served-model-name medium \ --port 8001 \ --attention-backend FLASHINFER \ --gpu-memory-utilization 0.90 \ --max-num-seqs 32 \ --max-model-len 128000 \ --mm-encoder-tp-mode data \ --mm-processor-cache-type shm \ --reasoning-parser qwen3 \ --enable-prefix-caching \ --tool-call-parser qwen3_coder \ --trust_remote_code \ --enable-auto-tool-choice ``` Log details Note that Qwen 397B also fails to launch with MTP (NVFP4, tp=4), see #35031. Works fine with Qwen 35B (FP8) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: 0% acceptance rate (MTP) with Qwen 3.5 122B (NVFP4) bug ### Your current environment ### 🐛 Describe the bug MTP has 0% acceptance rate with Qwen3.5-122B-A10B-NVFP4 Script : ```bash export CUDA_VISIBLE_DEVICES=3 e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: 0% acceptance rate (MTP) with Qwen 3.5 122B (NVFP4) bug ### Your current environment ### 🐛 Describe the bug MTP has 0% acceptance rate with Qwen3.5-122B-A10B-NVFP4 Script : ```bash export CUDA_VISIBLE_DEVICES=3 e...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: rt NCCL_CUMEM_ENABLE=0 export VLLM_ENABLE_CUDAGRAPH_GC=1 export VLLM_USE_FLASHINFER_SAMPLER=1 vllm serve /data/models/Qwen3.5-122B-A10B-NVFP4 \ --served-model-name medium \ --port 8001 \ --attention-backend FLASHINFER \...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_me...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: % acceptance rate with Qwen3.5-122B-A10B-NVFP4 Script : ```bash export CUDA_VISIBLE_DEVICES=3 export NCCL_CUMEM_ENABLE=0 export VLLM_ENABLE_CUDAGRAPH_GC=1 export VLLM_USE_FLASHINFER_SAMPLER=1 vllm serve /data/models/Qwe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
