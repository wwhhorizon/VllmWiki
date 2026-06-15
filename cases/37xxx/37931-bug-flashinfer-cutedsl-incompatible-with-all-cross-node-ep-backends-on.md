# vllm-project/vllm#37931: [Bug]: `flashinfer_cutedsl` incompatible with all cross-node EP backends on GB200 NVL72

| 字段 | 值 |
| --- | --- |
| Issue | [#37931](https://github.com/vllm-project/vllm/issues/37931) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;model_support;moe;quantization |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;moe |
| 症状 | mismatch;slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `flashinfer_cutedsl` incompatible with all cross-node EP backends on GB200 NVL72

### Issue 正文摘录

### Your current environment ### Current environment - **vLLM version:** 0.17.2rc1 - **GPU:** GB200 NVL72 (4 GPUs per node, MNNVL enabled) - **Model:** DeepSeek-R1-0528-FP4 (NVFP4) - **Deployment:** P/D disaggregation, cross-node EP8/EP32 ### 🐛 Describe the bug ### Description `flashinfer_cutedsl` cannot be used with any A2A backend that supports cross-node EP on GB200 NVL72: **Path 1: `deepep_low_latency` + `flashinfer_cutedsl`** DeepEP buffer init fails cross-node: `RuntimeError: Failed: CUDA error /tmp/ep_kernels_workspace/DeepEP/csrc/deep_ep.cpp:226 'invalid resource handle'` root cause: `Buffer.runtime.sync()` exchanges IPC handles via shared memory, which doesn't work across physical nodes. `VLLM_DEEPEP_LOW_LATENCY_USE_MNNVL=1` only affects data transfer, not the init path. **Path 2: `flashinfer_nvlink_one_sided` + `flashinfer_cutedsl`** Rejected at startup: `ValueError: NvFp4 MoE backend 'FLASHINFER_CUTEDSL' does not support the deployment configuration since kernel does not support ('standard',) activation format.` root cause: `select_nvfp4_moe_backend()` determines activation format via `config.moe_parallel_config.use_deepep_ll_kernels`. this flag is only `True` for `deep...

## 现有链接修复摘要

#40263 [WIP][Bugfix] flashinfer cutedsl nvfp4 moe compatibility with cross-node all2all backends

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ]: `flashinfer_cutedsl` incompatible with all cross-node EP backends on GB200 NVL72 bug ### Your current environment ### Current environment - **vLLM version:** 0.17.2rc1 - **GPU:** GB200 NVL72 (4 GPUs per node, MNNVL e...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 200 NVL72 (4 GPUs per node, MNNVL enabled) - **Model:** DeepSeek-R1-0528-FP4 (NVFP4) - **Deployment:** P/D disaggregation, cross-node EP8/EP32 ### 🐛 Describe the bug ### Description `flashinfer_cutedsl` cannot be used w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ** 0.17.2rc1 - **GPU:** GB200 NVL72 (4 GPUs per node, MNNVL enabled) - **Model:** DeepSeek-R1-0528-FP4 (NVFP4) - **Deployment:** P/D disaggregation, cross-node EP8/EP32 ### 🐛 Describe the bug ### Description `flashinfer...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: `flashinfer_cutedsl` incompatible with all cross-node EP backends on GB200 NVL72 bug ### Your current environment ### Current environment - **vLLM version:** 0.17.2rc1 - **GPU:** GB200 NVL72 (4 GPUs per node, MNN...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: er init to use MNNVL instead of CUDA IPC for handle exchange ### How to reproduce ```bash # Path 1 - DeepEP IPC failure (multi-node) vllm serve --enable-expert-parallel \ --all2all-backend deepep_low_latency \ --moe-bac...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40263](https://github.com/vllm-project/vllm/pull/40263) | closes_keyword | 0.95 | [WIP][Bugfix] flashinfer cutedsl nvfp4 moe compatibility with cross-node all2all backends | Fixes #37931 ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [ ] The purpose of the PR, s |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
