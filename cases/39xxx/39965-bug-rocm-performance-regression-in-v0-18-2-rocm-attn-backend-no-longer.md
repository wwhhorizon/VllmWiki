# vllm-project/vllm#39965: [Bug]: [ROCm] Performance regression in v0.18.2: ROCM_ATTN backend no longer selected by default, falls back to slower TRITON_ATTN

| 字段 | 值 |
| --- | --- |
| Issue | [#39965](https://github.com/vllm-project/vllm/issues/39965) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;attention_kv_cache;gemm_linear;hardware_porting;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | activation;attention;gemm;kernel;triton |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [ROCm] Performance regression in v0.18.2: ROCM_ATTN backend no longer selected by default, falls back to slower TRITON_ATTN

### Issue 正文摘录

### Your current environment ## 🐛 Bug Report ### Summary Prefill performance regressed **~5.5x** between vLLM v0.18.1 and v0.18.2 on ROCm . The root cause is a **backend selection logic change** in `rocm.py` that gates `ROCM_ATTN` (flash-attention) behind a new config flag `use_prefill_decode_attention` which defaults to `False`. Even with `flash-attention` installed, v0.18.2 silently falls back to `TRITON_ATTN`. --- ### Environment | Component | v0.18.1 (Fast) | v0.18.2 (Slow) | |-----------|----------------|----------------| | vLLM | 0.18.1rc1.dev231 | 0.18.2.dev0 | | PyTorch | 2.11.0a0+rocm7.11 | 2.11.0a0+rocm7.11 | | ROCm/HIP | 7.2.53150 | 7.2.53150 | | Triton | 3.6.0 | 3.6.0 | | GPU Architecture | AMD gfx1151 (Strix Halo) | AMD gfx1151 (Strix Halo) | --- ### Performance Impact (measured via `rocprof` model ( Qwen/Qwen3-0.6B ) | Metric | v0.18.1 | v0.18.2 | Diff | |--------|---------|---------|------| | Total GPU time | 2,430 ms | 6,059 ms | **+3,629 ms (2.5x slower)** | | Prefill attention kernel | 813 ms (84 calls) | 4,486 ms (56 calls) | **5.5x slower** | | Decode attention | 194 ms | 36 ms | faster | --- ### Kernel Evidence **v0.18.1** — uses `ROCM_ATTN` (flash-attention):...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: [Bug]: [ROCm] Performance regression in v0.18.2: ROCM_ATTN backend no longer selected by default, falls back to slower TRITON_ATTN bug;rocm ### Your current environment ## 🐛 Bug Report ### Summary Prefill performance re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: [ROCm] Performance regression in v0.18.2: ROCM_ATTN backend no longer selected by default, falls back to slower TRITON_ATTN bug;rocm ### Your current environment ## 🐛 Bug Report ### Summary Prefill performance re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nge** in `rocm.py` that gates `ROCM_ATTN` (flash-attention) behind a new config flag `use_prefill_decode_attention` which defaults to `False`. Even with `flash-attention` installed, v0.18.2 silently falls back to `TRITO...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: decode_attention` which defaults to `False`. Even with `flash-attention` installed, v0.18.2 silently falls back to `TRITON_ATTN`. --- ### Environment | Component | v0.18.1 (Fast) | v0.18.2 (Slow) | |-----------|--------...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: TTN bug;rocm ### Your current environment ## 🐛 Bug Report ### Summary Prefill performance regressed **~5.5x** between vLLM v0.18.1 and v0.18.2 on ROCm . The root cause is a **backend selection logic change** in `rocm.py...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
