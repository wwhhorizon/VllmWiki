# vllm-project/vllm#44092: AMD Development Roadmap (2026 Q2)

| 字段 | 值 |
| --- | --- |
| Issue | [#44092](https://github.com/vllm-project/vllm/issues/44092) |
| 状态 | open |
| 标签 | rocm |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cache;fp8;kernel;moe |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> AMD Development Roadmap (2026 Q2)

### Issue 正文摘录

# AMD Development Roadmap (2026 Q2) *Draft for review — 2026-05-30. Target repo: vllm-project/vllm. Modeled on the SGLang AMD roadmap (sgl-project/sglang#23494). Aligns to the AMD vLLM roadmap deck (2026-05-29).* *Contributions and feedback are welcome.* > **⚠️ Draft / work-in-progress.** This roadmap is a draft and may still be updated. Items, owners, linked tickets, and dates are tentative and subject to change. This is the ROCm counterpart to the overall [vLLM Roadmap Q2 2026](https://github.com/vllm-project/vllm/issues/39749). Legend: ✓ done · ▶ in progress · ○ planned. Each item links a tracked vLLM issue/PR. ## Focus - **Day-0 → Day-N model enablement**: Frontier models (DeepSeek, Llama, Qwen, Kimi) running on ROCm at launch. - **Close the perf gap**: Decode parity vs SGLang / ATOM at concurrency 128/512, on MoE and MLA. - **vLLM V1 engine**: Adopt the V1 engine on ROCm — full-cudagraph, spec-decode, llm-d / P-D. - **No regression**: e2e accuracy + perf regression CI with nightly gating, answering the public "no perf/accuracy regression" ask (#43916). ## Feature and Performance Improvements (Now · June) - **Models** PoC: @tjtanaa @ChuanLi1101 Goal: Land the frontier MoE mode...

## 现有链接修复摘要

#37353 [ROCm][Perf] Skip head repeat_interleave for AITER MLA decode with BF16 KV cache | #39513 [ROCm] 1st stage of enabling torch stable on ROCm. | #40697 [ROCm][Kimi-Linear] Wire FlyDSL gated delta rule decode kernel for KimiDeltaAttention | #40889 [ROCm] Add AITER-accelerated MLA decode for DeepSeek V4 on MI355X | #43718 [ROCm][DeepSeek-V4] Enable CSA multistream decode

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: eration. - ▶ AITER-accelerated MLA decode for DeepSeek-V4 on MI355X (FP4 e2e, TP=8) #40889 - ▶ Wire Kimi-Linear FlyDSL gated delta rule decode kernel #40697 - **Performance** PoC: @maeehart @frida-andersson Goal: Close...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ress.** This roadmap is a draft and may still be updated. Items, owners, linked tickets, and dates are tentative and subject to change. This is the ROCm counterpart to the overall [vLLM Roadmap Q2 2026](https://github.c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: AMD Development Roadmap (2026 Q2) rocm # AMD Development Roadmap (2026 Q2) *Draft for review — 2026-05-30. Target repo: vllm-project/vllm. Modeled on the SGLang AMD roadmap (sgl-project/sglang#23494). Aligns to the AMD...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: the V1 engine on ROCm — full-cudagraph, spec-decode, llm-d / P-D. - **No regression**: e2e accuracy + perf regression CI with nightly gating, answering the public "no perf/accuracy regression" ask (#43916). ## Feature a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 026 Q2) *Draft for review — 2026-05-30. Target repo: vllm-project/vllm. Modeled on the SGLang AMD roadmap (sgl-project/sglang#23494). Aligns to the AMD vLLM roadmap deck (2026-05-29).* *Contributions and feedback are we...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37353](https://github.com/vllm-project/vllm/pull/37353) | mentioned | 0.45 | [ROCm][Perf] Skip head repeat_interleave for AITER MLA decode with BF16 KV cache | ▶ skip head repeat_interleave for aiter mla decode with bf16 kv cache #37353 - **ci & quality** poc: @andreaskaratzas goal: stand up e2e accuracy + perf regression gating on roc |
| [#39513](https://github.com/vllm-project/vllm/pull/39513) | mentioned | 0.45 | [ROCm] 1st stage of enabling torch stable on ROCm. | - ▶ first stage of enabling torch stable on rocm (v1 full-cudagraph) #39513 - ▶ llm-d v0.8.0 well-lit gates on mi300 (mori · p/d · wide-ep) - ▶ pd disaggregation recipes on vl |
| [#40697](https://github.com/vllm-project/vllm/pull/40697) | mentioned | 0.45 | [ROCm][Kimi-Linear] Wire FlyDSL gated delta rule decode kernel for KimiDeltaAttention | 40889 - ▶ wire kimi-linear flydsl gated delta rule decode kernel #40697 - **performance** poc: @maeehart @frida-andersson goal: close the decode gap on mla / dsv4 hot paths |
| [#40889](https://github.com/vllm-project/vllm/pull/40889) | mentioned | 0.45 | [ROCm] Add AITER-accelerated MLA decode for DeepSeek V4 on MI355X | iter-accelerated mla decode for deepseek-v4 on mi355x (fp4 e2e, tp=8) #40889 - ▶ wire kimi-linear flydsl gated delta rule decode kernel #40697 - **performance** poc: @maeehart |
| [#43718](https://github.com/vllm-project/vllm/pull/43718) | mentioned | 0.45 | [ROCm][DeepSeek-V4] Enable CSA multistream decode | int64 source fix - ▶ deepseek-v4 csa multistream decode overlap #43718 - ▶ skip head repeat_interleave for aiter mla decode with bf16 kv cache #37353 - **ci & quality** |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
