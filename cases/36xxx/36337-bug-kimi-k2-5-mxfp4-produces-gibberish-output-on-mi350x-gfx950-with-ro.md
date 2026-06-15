# vllm-project/vllm#36337: [Bug]: Kimi-K2.5-MXFP4 produces gibberish output on MI350X (gfx950) with ROCm 7.2

| 字段 | 值 |
| --- | --- |
| Issue | [#36337](https://github.com/vllm-project/vllm/issues/36337) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;distributed_parallel;hardware_porting;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | activation;gemm;kernel;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Kimi-K2.5-MXFP4 produces gibberish output on MI350X (gfx950) with ROCm 7.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `amd/Kimi-K2.5-MXFP4` loads and serves successfully on 4x MI350X (gfx950) with TP=4, but produces **complete gibberish output** — mixed Chinese/English/symbols with no coherent text. #### Reproduce ```bash # Using custom image built from rocm/vllm-dev:base_gfx950_therock_base_20260123 # with vLLM v0.17.0 compiled for gfx950 vllm serve amd/Kimi-K2.5-MXFP4 \ --tensor-parallel-size 4 \ --enforce-eager \ --trust-remote-code \ --mm-encoder-tp-mode data \ --tool-call-parser kimi_k2 \ --reasoning-parser kimi_k2 # Then: curl http://localhost:8000/v1/completions \ -H 'Content-Type: application/json' \ -d '{"model": "amd/Kimi-K2.5-MXFP4", "prompt": "The capital of France is", "max_tokens": 32}' ``` #### Observed output ```json { "text": " on. ad-namespace. \" # da.°a and df t. $ dop_{$~f + … I, T, from turned8 T" } ``` The gibberish is consistent across requests and endpoints (`/v1/completions` and `/v1/chat/completions`). The `content` field is always `null` with all output going to `reasoning`, which is itself incoherent. #### What works correctly - Model loads all 64/64 safetensors shards (133.68 GiB across 4 GPUs) - `quantization=quark...

## 现有链接修复摘要

#36422 [ROCm][Bugfix] Fix MXFP4 MoE emulate fallback logic on MX-capable hardware

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Kimi-K2.5-MXFP4 produces gibberish output on MI350X (gfx950) with ROCm 7.2 bug;rocm ### Your current environment ### 🐛 Describe the bug `amd/Kimi-K2.5-MXFP4` loads and serves successfully on 4x MI350X (gfx950) wi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: from rocm/vllm-dev:base_gfx950_therock_base_20260123 # with vLLM v0.17.0 compiled for gfx950 vllm serve amd/Kimi-K2.5-MXFP4 \ --tensor-parallel-size 4 \ --enforce-eager \ --trust-remote-code \ --mm-encoder-tp-mode data...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: 133.68 GiB across 4 GPUs) - `quantization=quark` is detected correctly - AITER fused_moe kernels activate: `[fused_moe] using 2stage default for (256, 64, 7168, 512, 384, 8, 'ActivationType.Silu', 'torch.bfloat16', 'tor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Kimi-K2.5-MXFP4 produces gibberish output on MI350X (gfx950) with ROCm 7.2 bug;rocm ### Your current environment ### 🐛 Describe the bug `amd/Kimi-K2.5-MXFP4` loads and serves successfully on 4x MI350X (gfx950) wi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: st:8000/v1/completions \ -H 'Content-Type: application/json' \ -d '{"model": "amd/Kimi-K2.5-MXFP4", "prompt": "The capital of France is", "max_tokens": 32}' ``` #### Observed output ```json { "text": " on. ad-namespace....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36422](https://github.com/vllm-project/vllm/pull/36422) | closes_keyword | 0.95 | [ROCm][Bugfix] Fix MXFP4 MoE emulate fallback logic on MX-capable hardware | Fixes #36337 ## Test plan - [x] Unit test `test_quark_moe_emulate.py` passes (14/14 cases, 0.13s, no GPU needed) - [ ] Verify `amd/Kimi-K2.5-MXFP4` on MI350X with `VLLM_ROCM_USE_ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
