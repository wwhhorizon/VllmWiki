# vllm-project/vllm#43743: [DSv4] [SM 12.0] fp8_einsum has no SM 12.0 fallback — blocks mainline serve on consumer Blackwell (follow-up to #41834)

| 字段 | 值 |
| --- | --- |
| Issue | [#43743](https://github.com/vllm-project/vllm/issues/43743) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;triton |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [DSv4] [SM 12.0] fp8_einsum has no SM 12.0 fallback — blocks mainline serve on consumer Blackwell (follow-up to #41834)

### Issue 正文摘录

## DSv4 attention `fp8_einsum` has no SM 12.0 fallback in mainline — blocks consumer Blackwell serve > _Disclosure (per [`AGENTS.md`](https://github.com/vllm-project/vllm/blob/main/AGENTS.md#accountability)): drafted with AI assistance; all references verified by hand against vllm-project/vllm@`e19b9b104` and jasl/vllm@`27fd665b` source trees on 2026-05-27. The human submitter (@pasta-paul / canada-quant) defends every claim._ ### Summary On RTX PRO 6000 Blackwell (SM 12.0), vllm-project/vllm@main + [`#43722`](https://github.com/vllm-project/vllm/pull/43722) + [`#43723`](https://github.com/vllm-project/vllm/pull/43723) + [`#41834`](https://github.com/vllm-project/vllm/pull/41834) (full overlay) + [`#40923`](https://github.com/vllm-project/vllm/pull/40923) + [`#43655`](https://github.com/vllm-project/vllm/pull/43655) (rebased) gets DSv4-Flash artifacts past engine init + Marlin/Triton dispatch + cudagraph capture, then **fails at first forward pass** with: ``` RuntimeError: Assertion error (csrc/apis/../jit_kernels/impls/../heuristics/../../utils/layout.hpp:39): t.dim() == N at vllm/utils/deep_gemm.py:317 fp8_einsum at vllm/models/deepseek_v4/attention.py (forward) ``` Root cause:...

## 现有链接修复摘要

#40923 [Kernel] Marlin MoE: include SM 12.x in default arch list | #41834 [New Model][Nvidia] Add SM12x support for DeepSeek V4 Flash with essential fixes | #43655 [Bugfix][DSV4] Plumb quant_config + route compressor GEMM through quant-aware dispatch | #43722 [Bugfix][Quantization] Refuse block-FP8 in MarlinFP8.can_implement

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [DSv4] [SM 12.0] fp8_einsum has no SM 12.0 fallback — blocks mainline serve on consumer Blackwell (follow-up to #41834) ## DSv4 attention `fp8_einsum` has no SM 12.0 fallback in mainline — blocks consumer Blackwell serv...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [DSv4] [SM 12.0] fp8_einsum has no SM 12.0 fallback — blocks mainline serve on consumer Blackwell (follow-up to #41834) ## DSv4 attention `fp8_einsum` has no SM 12.0 fallback in mainline — blocks consumer Blackwell serv...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [DSv4] [SM 12.0] fp8_einsum has no SM 12.0 fallback — blocks mainline serve on consumer Blackwell (follow-up to #41834) ## DSv4 attention `fp8_einsum` has no SM 12.0 fallback in mainline — blocks consumer Blackwell serv...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n def deepseek_v4_fp8_einsum(equation, a, a_scale, b, b_scale, out, *, recipe): if _use_deepseek_v4_sm12x_triton_fp8_einsum(equation, recipe, b_scale): deepseek_v4_sm12x_fp8_einsum(a, a_scale, b, b_scale, out) else: fp8...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [DSv4] [SM 12.0] fp8_einsum has no SM 12.0 fallback — blocks mainline serve on consumer Blackwell (follow-up to #41834) ## DSv4 attention `fp8_einsum` has no SM 12.0 fallback in mainline — blocks consumer Blackwell serv...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40923](https://github.com/vllm-project/vllm/pull/40923) | mentioned | 0.45 | [Kernel] Marlin MoE: include SM 12.x in default arch list | nblocks mainline dsv4 serve on sm 12.0 (after #41834, #43722, #43723, #40923, #43655 also land). estimated diff size: ~500 lines (most of it is the existing triton kernel + a cust… |
| [#41834](https://github.com/vllm-project/vllm/pull/41834) | mentioned | 0.45 | [New Model][Nvidia] Add SM12x support for DeepSeek V4 Flash with essential fixes | hub.com/vllm-project/vllm/issues/43564#issuecomment-4550184475 - pr [`#41834`](https://github.com/vllm-project/vllm/pull/41834) — fixes `tf32_hc_prenorm_gemm` sm 12.0 dispatch; th… |
| [#43655](https://github.com/vllm-project/vllm/pull/43655) | mentioned | 0.45 | [Bugfix][DSV4] Plumb quant_config + route compressor GEMM through quant-aware dispatch | mainline dsv4 serve on sm 12.0 (after #41834, #43722, #43723, #40923, #43655 also land). estimated diff size: ~500 lines (most of it is the existing triton kernel + a custom-op wr… |
| [#43722](https://github.com/vllm-project/vllm/pull/43722) | mentioned | 0.45 | [Bugfix][Quantization] Refuse block-FP8 in MarlinFP8.can_implement | einsum`. this unblocks mainline dsv4 serve on sm 12.0 (after #41834, #43722, #43723, #40923, #43655 also land). estimated diff size: ~500 lines (most of it is the existing triton… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
