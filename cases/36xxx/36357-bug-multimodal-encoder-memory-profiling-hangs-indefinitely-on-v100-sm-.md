# vllm-project/vllm#36357: [Bug]: Multimodal encoder memory profiling hangs indefinitely on V100 (SM 7.0) in v0.17

| 字段 | 值 |
| --- | --- |
| Issue | [#36357](https://github.com/vllm-project/vllm/issues/36357) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cache;cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Multimodal encoder memory profiling hangs indefinitely on V100 (SM 7.0) in v0.17

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On V100 GPUs (SM 7.0), vLLM v0.17.0 hangs indefinitely during multimodal encoder memory profiling at startup. The engine loads weights successfully, reaches the encoder cache profiling step, then never progresses. After 60 seconds the shm_broadcast timeout message repeats indefinitely. This is a regression from v0.15.1 , which works with the exact same build command, hardware, and model. Root cause : v0.15.1 uses AttentionBackendEnum.TORCH_SDPA for the MM encoder attention, which works fine on V100. v0.17.0 switched to AttentionBackendEnum.TRITON_ATTN (via PR #32183 "Triton ViT attention backend"), which deadlocks during the encoder profiling forward pass on SM 7.0. Workaround : Adding --skip-mm-profiling bypasses the encoder profiling step. The server starts successfully and image inference still works — only the startup memory measurement is skipped. Note: --enforce-eager alone does NOT fix the issue. Command to reproduce (hangs indefinitely) bash docker run --gpus all -it \ --ipc = host \ --ulimit memlock = -1 \ --ulimit stack = 67108864 \ -p 8000 :8000 --rm \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -e LD_LIBRARY_PA...

## 现有链接修复摘要

#32183 [MM Encoder] Add Triton ViT attention backend | #36439 [Bugfix] Fall back to TORCH_SDPA for encoder attention on SM<80 GPUs

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: . This is a regression from v0.15.1 , which works with the exact same build command, hardware, and model. Root cause : v0.15.1 uses AttentionBackendEnum.TORCH_SDPA for the MM encoder attention, which works fine on V100....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Multimodal encoder memory profiling hangs indefinitely on V100 (SM 7.0) in v0.17 bug ### Your current environment ### 🐛 Describe the bug On V100 GPUs (SM 7.0), vLLM v0.17.0 hangs indefinitely during multimodal en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Multimodal encoder memory profiling hangs indefinitely on V100 (SM 7.0) in v0.17 bug ### Your current environment ### 🐛 Describe the bug On V100 GPUs (SM 7.0), vLLM v0.17.0 hangs indefinitely during multimodal en...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Multimodal encoder memory profiling hangs indefinitely on V100 (SM 7.0) in v0.17 bug ### Your current environment ### 🐛 Describe the bug On V100 GPUs (SM 7.0), vLLM v0.17.0 hangs indefinitely during multimodal en...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ild command, hardware, and model. Root cause : v0.15.1 uses AttentionBackendEnum.TORCH_SDPA for the MM encoder attention, which works fine on V100. v0.17.0 switched to AttentionBackendEnum.TRITON_ATTN (via PR #32183 "Tr...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32183](https://github.com/vllm-project/vllm/pull/32183) | mentioned | 0.45 | [MM Encoder] Add Triton ViT attention backend | py-px text-[0.9rem]">attentionbackendenum.triton_attn</code> (via pr #32183 "triton vit attention backend"), which deadlocks during the encoder profiling forward pass on sm 7.0.</… |
| [#36439](https://github.com/vllm-project/vllm/pull/36439) | closes_keyword | 0.95 | [Bugfix] Fall back to TORCH_SDPA for encoder attention on SM<80 GPUs | Fixes #36357 — V100 multimodal encoder profiling hangs on SM 7.0. **Root cause**: PR #32183 introduced `TRITON_ATTN` as the default attention backend for multimodal encoder layers |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
