# vllm-project/vllm#40969: [Bug]: DeepSeek-V4-Flash hangs after ~6 requests with cudagraph_mode=FULL_AND_PIECEWISE + chunked prefill on SM 12.x (GB10)

| 字段 | 值 |
| --- | --- |
| Issue | [#40969](https://github.com/vllm-project/vllm/issues/40969) |
| 状态 | open |
| 标签 | DSv4 |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cache;moe;quantization;sampling |
| 症状 | build_error;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V4-Flash hangs after ~6 requests with cudagraph_mode=FULL_AND_PIECEWISE + chunked prefill on SM 12.x (GB10)

### Issue 正文摘录

# [Bug]: DeepSeek-V4-Flash hangs after ~6 requests with `cudagraph_mode=FULL_AND_PIECEWISE` + chunked prefill on SM 12.x (GB10) ### Your current environment ``` - Hardware: 2× DGX Spark (NVIDIA GB10, SM 12.1) connected via 100Gb RoCE - vLLM: built from `4d51588` (V4-Flash main, post #40860 merge), aarch64 - Image: `vllm/vllm-openai:deepseekv4-cu130` - Model: `deepseek-ai/DeepSeek-V4-Flash` (mxfp4 MoE) - Backend: `--moe-backend marlin` (with #40923 SM12.x cubin patch applied locally) - KV cache: `--kv-cache-dtype fp8_ds_mla` - TP=2, max_model_len=32768, prefix-caching on - PyTorch 2.10.0+cu130 (jasl's `torch_compat_v3` shim for `torch.float8_e8m0fnu`) ``` ### 🐛 Describe the bug V4-Flash with `--compilation-config '{"cudagraph_mode": "FULL_AND_PIECEWISE"}'` (the implicit default once `--enforce-eager` is dropped) loads, captures graphs cleanly, and serves the first 5–6 requests correctly. On the **6th–7th** request, the engine silently hangs: requests timeout with no Python exception, no NCCL timeout, no OOM. `nvidia-smi` shows ~100% SM utilization on both ranks but `nvtop` decode tok/s is zero. Recovery requires container restart. The model produces **coherent** text on the request...

## 现有链接修复摘要

#6 Automatically configure KV cache size | #40923 [Kernel] Marlin MoE: include SM 12.x in default arch list

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: /vllm-openai:deepseekv4-cu130` - Model: `deepseek-ai/DeepSeek-V4-Flash` (mxfp4 MoE) - Backend: `--moe-backend marlin` (with #40923 SM12.x cubin patch applied locally) - KV cache: `--kv-cache-dtype fp8_ds_mla` - TP=2, ma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: DeepSeek-V4-Flash hangs after ~6 requests with cudagraph_mode=FULL_AND_PIECEWISE + chunked prefill on SM 12.x (GB10) DSv4 # [Bug]: DeepSeek-V4-Flash hangs after ~6 requests with `cudagraph_mode=FULL_AND_PIECEWISE...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: roduces **coherent** text on the requests that do succeed (so it isn't a numerical/quant issue), and the same workload runs cleanly when restricted to `cudagraph_mode: PIECEWISE` only — or with `--enforce-eager`. Workar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: compilation-config '{"cudagraph_mode": "FULL_AND_PIECEWISE"}'` (the implicit default once `--enforce-eager` is dropped) loads, captures graphs cleanly, and serves the first 5–6 requests correctly. On the **6th–7th** req...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: DeepSeek-V4-Flash hangs after ~6 requests with cudagraph_mode=FULL_AND_PIECEWISE + chunked prefill on SM 12.x (GB10) DSv4 # [Bug]: DeepSeek-V4-Flash hangs after ~6 requests with `cudagraph_mode=FULL_AND_PIECEWISE...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | `/v1/chat/completions` requests, each ~50–100 tokens. around request #6–7 the worker stops emitting tokens but the api connection stays open until client timeout. ### what works (c |
| [#40923](https://github.com/vllm-project/vllm/pull/40923) | mentioned | 0.45 | [Kernel] Marlin MoE: include SM 12.x in default arch list | =2). ### reproduction 1. build vllm at `4d51588` for sm 12.x (apply #40923 for native marlin sm12.x cubin) 2. launch: ```bash vllm serve /models/deepseek-v4-flash \ --tensor-paral… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
