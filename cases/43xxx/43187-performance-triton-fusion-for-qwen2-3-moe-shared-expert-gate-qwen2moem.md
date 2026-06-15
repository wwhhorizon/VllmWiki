# vllm-project/vllm#43187: [Performance]: Triton fusion for Qwen2/3-MoE shared-expert gate (Qwen2MoeMLP/Qwen3MoeMLP)

| 字段 | 值 |
| --- | --- |
| Issue | [#43187](https://github.com/vllm-project/vllm/issues/43187) |
| 状态 | open |
| 标签 | performance;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;gemm_linear;hardware_porting;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;gemm;kernel;moe;operator;triton |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Performance]: Triton fusion for Qwen2/3-MoE shared-expert gate (Qwen2MoeMLP/Qwen3MoeMLP)

### Issue 正文摘录

### Proposal to improve performance In `vllm/model_executor/models/qwen2_moe.py:119-120` (also reused by `qwen3_next.py` via re-export of `Qwen2MoeMLP`) and the byte-identical duplicate in `qwen3_moe.py:131-132`, the shared-expert gate runs as: ```python if self.expert_gate is not None: out = F.sigmoid(self.expert_gate(x)[0]) * out ``` For Qwen3-Next configs (`shared_expert_gate = ReplicatedLinear(H, 1)` → `weight.shape == [1, H]`), this expands at runtime into three back-to-back memory-bound GPU kernels (skinny `[N,H]×[H,1]` GEMM → sigmoid on `[N,1]` → broadcast multiply `[N,1]·[N,H]`) plus two HBM-resident intermediates. A single Triton kernel that does one row at a time — load `x_row`, load `weight`, compute `sigmoid(dot)`, load `out_row`, store `out_row * gate` — collapses them into one pass and removes both intermediates. I have a working patch (Triton kernel + Python wrapper with a shape-guard fallback + parametrized correctness test) and a full A/B sweep on MI355x — numbers in the "Misc" section. Before opening a PR, I'd like to confirm maintainers want this fusion to land alongside the existing FSE work, given the points below. ### Relationship to existing FSE work This is...

## 现有链接修复摘要

#37800 [ROCm][Perf] Add MXFP4 linear method and enable shared expert fusion | #39280 [ROCm][Perf] Add Fused Shared Expert (FSE) support for Qwen3-Next | #43190 [Kernel] Fuse Qwen2/3-MoE shared-expert sigmoid gate into a Triton kernel

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: n on performance **Setup:** single MI355x, `Qwen3-Next-80B-A3B-Instruct-FP8`, vLLM 0.19.1, TP=1, AITER on, FSE not enabled. Three workload shapes (balanced ISL=OSL=1024 / decode-heavy ISL=1024/OSL=8192 / prefill-heavy I...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: + Python wrapper with a shape-guard fallback + parametrized correctness test) and a full A/B sweep on MI355x — numbers in the "Misc" section. Before opening a PR, I'd like to confirm maintainers want this fusion to land...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Performance]: Triton fusion for Qwen2/3-MoE shared-expert gate (Qwen2MoeMLP/Qwen3MoeMLP) performance;rocm ### Proposal to improve performance In `vllm/model_executor/models/qwen2_moe.py:119-120` (also reused by `qwen3_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: for Qwen2/3-MoE shared-expert gate (Qwen2MoeMLP/Qwen3MoeMLP) performance;rocm ### Proposal to improve performance In `vllm/model_executor/models/qwen2_moe.py:119-120` (also reused by `qwen3_next.py` via re-export of `Qw...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: verlapping. FSE (`VLLM_ROCM_USE_AITER_FUSION_SHARED_EXPERTS`, default `False`) bypasses the call site at the MoE-block level when the user is on ROCm + AITER **and** has explicitly opted in. For every other configuratio...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37800](https://github.com/vllm-project/vllm/pull/37800) | mentioned | 0.45 | [ROCm][Perf] Add MXFP4 linear method and enable shared expert fusion | used_moe codeowners), @tpopp @dllehr-amd (fse authors), @chuanli1101 (#37800 author). ### your current environment (if you think it is necessary) ```text the output of `python col… |
| [#39280](https://github.com/vllm-project/vllm/pull/39280) | mentioned | 0.45 | [ROCm][Perf] Add Fused Shared Expert (FSE) support for Qwen3-Next | low. ### relationship to existing fse work this is complementary to #39280 (aiter fse) rather than overlapping. fse (`vllm_rocm_use_aiter_fusion_shared_experts`, default `false`)… |
| [#43190](https://github.com/vllm-project/vllm/pull/43190) | closes_keyword | 0.95 | [Kernel] Fuse Qwen2/3-MoE shared-expert sigmoid gate into a Triton kernel | Resolves #43187. `Qwen2MoeMLP.forward` / `Qwen3MoeMLP.forward` currently apply the shared-expert gate as `F.sigmoid(self.expert_gate(x)[0]) * out`, which dispatches three separa |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
