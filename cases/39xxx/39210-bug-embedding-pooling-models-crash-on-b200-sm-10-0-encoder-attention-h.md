# vllm-project/vllm#39210: [Bug] Embedding/pooling models crash on B200 (SM 10.0) — encoder attention hardcodes FA2 which lacks SM100 support

| 字段 | 值 |
| --- | --- |
| Issue | [#39210](https://github.com/vllm-project/vllm/issues/39210) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] Embedding/pooling models crash on B200 (SM 10.0) — encoder attention hardcodes FA2 which lacks SM100 support

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running any pooling/embedding model on B200 crashes with `cudaErrorUnsupportedPtxVersion` on the first inference request. The server starts up fine, but dies as soon as you actually send an embedding request. The root cause: `_forward_encoder_attention()` in `vllm/v1/attention/backends/flash_attn.py` unconditionally calls `flash_attn_varlen_func` -> `_vllm_fa2_C.varlen_fwd`, and the bundled FA2 `.so` only ships `sm_80` cubins. (related to https://github.com/vllm-project/vllm/issues/38411) The decoder path is fine — it uses FlashInfer by default on B200. But the encoder attention path (used by pooling/embedding models and multimodal vision encoders) bypasses backend selection entirely. `--attention-backend TRITON_ATTN` works as a workaround since `triton_attn.py` has its own `_forward_encoder_attention` that doesn't touch FA2. ## Repro ```python import torch from vllm import LLM def main(): print(f"GPU: {torch.cuda.get_device_name(0)}") print(f"Compute capability: {torch.cuda.get_device_capability(0)}") llm = LLM( model="google/embeddinggemma-300m", trust_remote_code=True, gpu_memory_utilization=0.15, ) output = llm.embed("Hello w...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: any pooling/embedding model on B200 crashes with `cudaErrorUnsupportedPtxVersion` on the first inference request. The server starts up fine, but dies as soon as you actually send an embedding request. The root cause: `_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug] Embedding/pooling models crash on B200 (SM 10.0) — encoder attention hardcodes FA2 which lacks SM100 support bug ### Your current environment ### 🐛 Describe the bug Running any pooling/embedding model on B200 cras...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug] Embedding/pooling models crash on B200 (SM 10.0) — encoder attention hardcodes FA2 which lacks SM100 support bug ### Your current environment ### 🐛 Describe the bug Running any pooling/embedding model on B200 cras...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: t. The root cause: `_forward_encoder_attention()` in `vllm/v1/attention/backends/flash_attn.py` unconditionally calls `flash_attn_varlen_func` -> `_vllm_fa2_C.varlen_fwd`, and the bundled FA2 `.so` only ships `sm_80` cu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 200 crashes with `cudaErrorUnsupportedPtxVersion` on the first inference request. The server starts up fine, but dies as soon as you actually send an embedding request. The root cause: `_forward_encoder_attention()` in...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
