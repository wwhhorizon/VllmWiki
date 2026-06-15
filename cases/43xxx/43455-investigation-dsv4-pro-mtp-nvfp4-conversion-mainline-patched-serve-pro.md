# vllm-project/vllm#43455: [Investigation][DSV4-Pro][MTP] NVFP4 conversion + mainline-patched serve produces 1.82% MTP acceptance vs native checkpoint's 80.56% on fork docker — root cause search

| 字段 | 值 |
| --- | --- |
| Issue | [#43455](https://github.com/vllm-project/vllm/issues/43455) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;model_support;moe;quantization;speculative_decoding |
| 子分类 | install |
| Operator 关键词 | fp8;moe;quantization |
| 症状 | build_error |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Investigation][DSV4-Pro][MTP] NVFP4 conversion + mainline-patched serve produces 1.82% MTP acceptance vs native checkpoint's 80.56% on fork docker — root cause search

### Issue 正文摘录

### Your current environment ``` vLLM mainline @ 39910f2b25 (2026-05-22) + PR #42209 (NVFP4 MoE support for DSV4) — now merged + 4 local DSV4 patches (#43248, #43288, #43290, #43319) 8× NVIDIA B300 SXM6 AC (sm_103a, 288 GB HBM3e each) ``` ### Purpose This is an informational issue, not a bug report. Filed to consolidate the upstream evidence around current V4-Pro MTP draft-acceptance capability, since multiple users (us included) hit "MTP retains and fires but acceptance is much lower than expected" and the right answer involves trusting [the official recipe YAML's `opt_in_features` classification](https://github.com/vllm-project/recipes/blob/main/models/deepseek-ai/DeepSeek-V4-Pro.yaml) rather than chasing a non-existent loader bug. ### Measurement Setup: NVFP4 V4-Pro artifact ([`canada-quant/DeepSeek-V4-Pro-NVFP4-FP8-MTP`](https://huggingface.co/canada-quant/DeepSeek-V4-Pro-NVFP4-FP8-MTP)), upstream-default `single_node_tep` strategy at TP=8 + EP, `--moe-backend flashinfer_trtllm`, `--attention_config.use_fp4_indexer_cache=True`, `--compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE","custom_ops":["all"]}'`, `--speculative-config '{"method":"mtp","num_speculative_tokens":...

## 现有链接修复摘要

#40760 [New Model] Support DeepseekV4 | #42209 Add NVFP4 MOE support for Deepseek V4. | #43248 [Bugfix][compressed-tensors] Wrap `is_static_input_scheme` with `bool()` for `input_quant=None` schemes | #43288 [Bugfix][DSV4] Default scale_fmt to "ue8m0" instead of hard-subscript | #43290 [Bugfix][DSV4] attention: fall back to `weight_scale` when `weight_scale_inv` absent | #43319 [Bugfix][DSV4] MTP draft model: detect BF16 MTP on disk + skip quant_config

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [Investigation][DSV4-Pro][MTP] NVFP4 conversion + mainline-patched serve produces 1.82% MTP acceptance vs native checkpoint's 80.56% on fork docker — root cause search ### Your current environment ``` vLLM mainline @ 39...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Investigation][DSV4-Pro][MTP] NVFP4 conversion + mainline-patched serve produces 1.82% MTP acceptance vs native checkpoint's 80.56% on fork docker — root cause search ### Your current environment ``` vLLM mainline @ 39...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: P acceptance vs native checkpoint's 80.56% on fork docker — root cause search ### Your current environment ``` vLLM mainline @ 39910f2b25 (2026-05-22) + PR #42209 (NVFP4 MoE support for DSV4) — now merged + 4 local DSV4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: B300 SXM6 AC (sm_103a, 288 GB HBM3e each) ``` ### Purpose This is an informational issue, not a bug report. Filed to consolidate the upstream evidence around current V4-Pro MTP draft-acceptance capability, since multipl...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: rt. Filed to consolidate the upstream evidence around current V4-Pro MTP draft-acceptance capability, since multiple users (us included) hit "MTP retains and fires but acceptance is much lower than expected" and the rig...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40760](https://github.com/vllm-project/vllm/pull/40760) | mentioned | 0.45 | [New Model] Support DeepseekV4 | ing @zyongye @woosukkwon since the mtp path discussion has been on pr #40760 and related. |
| [#42209](https://github.com/vllm-project/vllm/pull/42209) | mentioned | 0.45 | Add NVFP4 MOE support for Deepseek V4. | current environment ``` vllm mainline @ 39910f2b25 (2026-05-22) + pr #42209 (nvfp4 moe support for dsv4) — now merged + 4 local dsv4 patches (#43248, #43288, #43290, #43319) 8× nv… |
| [#43248](https://github.com/vllm-project/vllm/pull/43248) | mentioned | 0.45 | [Bugfix][compressed-tensors] Wrap `is_static_input_scheme` with `bool()` for `input_quant=None` schemes | 209 (nvfp4 moe support for dsv4) — now merged + 4 local dsv4 patches (#43248, #43288, #43290, #43319) 8× nvidia b300 sxm6 ac (sm_103a, 288 gb hbm3e each) ``` ### purpose this is a… |
| [#43288](https://github.com/vllm-project/vllm/pull/43288) | mentioned | 0.45 | [Bugfix][DSV4] Default scale_fmt to "ue8m0" instead of hard-subscript | p4 moe support for dsv4) — now merged + 4 local dsv4 patches (#43248, #43288, #43290, #43319) 8× nvidia b300 sxm6 ac (sm_103a, 288 gb hbm3e each) ``` ### purpose this is an inform… |
| [#43290](https://github.com/vllm-project/vllm/pull/43290) | mentioned | 0.45 | [Bugfix][DSV4] attention: fall back to `weight_scale` when `weight_scale_inv` absent | upport for dsv4) — now merged + 4 local dsv4 patches (#43248, #43288, #43290, #43319) 8× nvidia b300 sxm6 ac (sm_103a, 288 gb hbm3e each) ``` ### purpose this is an informational… |
| [#43319](https://github.com/vllm-project/vllm/pull/43319) | mentioned | 0.45 | [Bugfix][DSV4] MTP draft model: detect BF16 MTP on disk + skip quant_config | or dsv4) — now merged + 4 local dsv4 patches (#43248, #43288, #43290, #43319) 8× nvidia b300 sxm6 ac (sm_103a, 288 gb hbm3e each) ``` ### purpose this is an informational issue, n… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
