# vllm-project/vllm#34553: [Bug]: GLM-5 FP8 on H200 CUDA OOM in sparse_attn_indexer at High Concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#34553](https://github.com/vllm-project/vllm/issues/34553) |
| 状态 | open |
| 标签 | bug |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;fp8;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-5 FP8 on H200 CUDA OOM in sparse_attn_indexer at High Concurrency

### Issue 正文摘录

### Your current environment - vLLM Version: 0.16.0rc2.dev126+gb96f7314b - PyTorch: 2.10.0+cu129 - CUDA: 12.9.86 - GPU: NVIDIA H200 (139.81 GiB) - Driver: 570.148.08 - NCCL: 2.27.5 - Python: 3.12.12 - transformers: 5.2.0.dev0 - flashinfer: 0.6.3 - triton: 3.6.0 - OS: Ubuntu 22.04.5 LTS ### 🐛 Describe the bug When serving GLM-5 FP8 on 8xH200, server crashes with CUDA OOM in `fp8_mqa_logits` during sparse attention indexing at ISL=10240, concurrency=48,64: ```bash torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 9.89 GiB. GPU 5 has a total capacity of 139.81 GiB of which 5.56 GiB is free. Including non-PyTorch memory, this process has 134.24 GiB memory in use. Of the allocated memory 114.70 GiB is allocated by PyTorch, with 532.00 MiB allocated in private pools (e.g., CUDA Graphs), and 10.29 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_ALLOC_CONF=expandable_segments:True to avoid fragmentation. See documentation for Memory Management (https://pytorch.org/docs/stable/notes/cuda.html#environment-variables) ``` Command: ```bash vllm serve zai-org/GLM-5-FP8 \ --tensor-parallel-size 8 \ --speculative-config.metho...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ttn_indexer at High Concurrency bug ### Your current environment - vLLM Version: 0.16.0rc2.dev126+gb96f7314b - PyTorch: 2.10.0+cu129 - CUDA: 12.9.86 - GPU: NVIDIA H200 (139.81 GiB) - Driver: 570.148.08 - NCCL: 2.27.5 -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: GLM-5 FP8 on H200 CUDA OOM in sparse_attn_indexer at High Concurrency bug ### Your current environment - vLLM Version: 0.16.0rc2.dev126+gb96f7314b - PyTorch: 2.10.0+cu129 - CUDA: 12.9.86 - GPU: NVIDIA H200 (139.8...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 570.148.08 - NCCL: 2.27.5 - Python: 3.12.12 - transformers: 5.2.0.dev0 - flashinfer: 0.6.3 - triton: 3.6.0 - OS: Ubuntu 22.04.5 LTS ### 🐛 Describe the bug When serving GLM-5 FP8 on 8xH200, server crashes with CUDA OOM i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: GLM-5 FP8 on H200 CUDA OOM in sparse_attn_indexer at High Concurrency bug ### Your current environment - vLLM Version: 0.16.0rc2.dev126+gb96f7314b - PyTorch: 2.10.0+cu129 - CUDA: 12.9.86 - GPU: NVIDIA H200 (139.8...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rve zai-org/GLM-5-FP8 \ --tensor-parallel-size 8 \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 1 \ --tool-call-parser glm47 \ --reasoning-parser glm45 \ --enable-auto-tool-choice ``` ##...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
