# vllm-project/vllm#41565: [Bug]: TurboQuant _continuation_prefill workspace allocation fails at long context — v0.20.0 regression

| 字段 | 值 |
| --- | --- |
| Issue | [#41565](https://github.com/vllm-project/vllm/issues/41565) |
| 状态 | open |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;moe;operator;quantization |
| 症状 | crash;oom |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: TurboQuant _continuation_prefill workspace allocation fails at long context — v0.20.0 regression

### Issue 正文摘录

# [Bug]: TurboQuant `_continuation_prefill` workspace allocation fails at long context — v0.20.0 regression ## Summary On vLLM 0.20.0 with TurboQuant enabled, any prefill request whose cached KV grows beyond ~6-8K tokens triggers an assertion failure in `_continuation_prefill`'s workspace allocation. The workspace is sized to 0.26 MB at startup but `_continuation_prefill` needs ~2 MB at long context, and the workspace is locked against growth after engine init. The same workloads run cleanly on the v0.18-era TQ fork (vibhavagarwal5/PR #38479 base), so this is a v0.20-specific regression introduced when the workspace manager (PR #40941, merged Apr 27) was wired into the TQ continuation prefill path. ## Reproduction **Setup**: 8× RTX A4000 SM86, CUDA 13.0, driver 580.76.05, vLLM 0.20.0 from the GA tag. ```bash vllm serve /path/to/Nemotron-3-Super-120B-AWQ-4bit \ --tensor-parallel-size 8 --gpu-memory-utilization 0.92 \ --max-num-seqs 4 --max-model-len 131072 \ --trust-remote-code --enable-expert-parallel \ --mamba-ssm-cache-dtype float16 \ --kv-cache-dtype turboquant_3bit_nc ``` Send a long prompt: ```python import requests prompt = 'In computational science, ' * 2000 # ~8K tokens af...

## 现有链接修复摘要

#38479 [Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity | #39931 [Feature] TurboQuant: support hybrid models and uniform quantization | #40941 [Attention][TurboQuant] Share dequant buffers, eliminate float16_copy | #41123 fix(kv-cache): allow TurboQuant on hybrid models | #41185 [Bugfix] BailingMoeV2.5: rotate full qk_rope_head_dim in MLA RoPE | #41422 [Attention][TurboQuant] Sparse V tile-skip (opt-in)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: TurboQuant _continuation_prefill workspace allocation fails at long context — v0.20.0 regression # [Bug]: TurboQuant `_continuation_prefill` workspace allocation fails at long context — v0.20.0 regression ## Summ...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: v0.18-era TQ fork (vibhavagarwal5/PR #38479 base), so this is a v0.20-specific regression introduced when the workspace manager (PR #40941, merged Apr 27) was wired into the TQ continuation prefill path. ## Reproduction...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: d into the TQ continuation prefill path. ## Reproduction **Setup**: 8× RTX A4000 SM86, CUDA 13.0, driver 580.76.05, vLLM 0.20.0 from the GA tag. ```bash vllm serve /path/to/Nemotron-3-Super-120B-AWQ-4bit \ --tensor-para...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: TurboQuant _continuation_prefill workspace allocation fails at long context — v0.20.0 regression # [Bug]: TurboQuant `_continuation_prefill` workspace allocation fails at long context — v0.20.0 regression ## Summ...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: -code --enable-expert-parallel \ --mamba-ssm-cache-dtype float16 \ --kv-cache-dtype turboquant_3bit_nc ``` Send a long prompt: ```python import requests prompt = 'In computational science, ' * 2000 # ~8K tokens after to...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38479](https://github.com/vllm-project/vllm/pull/38479) | mentioned | 0.45 | [Attention Backend] TurboQuant: 2-bit KV cache compression with 4x capacity | gine's profile run. - models that do not reproduce: same models on pr #38479 fork (pre-workspace-manager). ## related - pr #40941 (merged apr 27): introduced the workspacemanager… |
| [#39931](https://github.com/vllm-project/vllm/pull/39931) | mentioned | 0.45 | [Feature] TurboQuant: support hybrid models and uniform quantization | its long-context test plan is blocked by this bug on ampere/ada. - pr #39931 #41185 #41123 (hybrid model tq work): unrelated but shares the same family of "dummy run undercounts t… |
| [#40941](https://github.com/vllm-project/vllm/pull/40941) | mentioned | 0.45 | [Attention][TurboQuant] Share dequant buffers, eliminate float16_copy | e models on pr #38479 fork (pre-workspace-manager). ## related - pr #40941 (merged apr 27): introduced the workspacemanager and wired it into tq continuation prefill. likely where… |
| [#41123](https://github.com/vllm-project/vllm/pull/41123) | mentioned | 0.45 | fix(kv-cache): allow TurboQuant on hybrid models | xt test plan is blocked by this bug on ampere/ada. - pr #39931 #41185 #41123 (hybrid model tq work): unrelated but shares the same family of "dummy run undercounts the real worklo… |
| [#41185](https://github.com/vllm-project/vllm/pull/41185) | mentioned | 0.45 | [Bugfix] BailingMoeV2.5: rotate full qk_rope_head_dim in MLA RoPE | g-context test plan is blocked by this bug on ampere/ada. - pr #39931 #41185 #41123 (hybrid model tq work): unrelated but shares the same family of "dummy run undercounts the real… |
| [#41422](https://github.com/vllm-project/vllm/pull/41422) | mentioned | 0.45 | [Attention][TurboQuant] Sparse V tile-skip (opt-in) | tq continuation prefill. likely where the regression originated. - pr #41422 (thetom sparse-v): independent change; its long-context test plan is blocked by this bug on ampere/ada… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
