# vllm-project/vllm#43511: [Bug][DSV4][dynamo] nvidia/ops/attention.py wo_a access is dynamo-unsafe; forces --enforce-eager on Option-Y MTP artifacts (~10× decode slowdown on SM 12.0)

| 字段 | 值 |
| --- | --- |
| Issue | [#43511](https://github.com/vllm-project/vllm/issues/43511) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | attention;fp8;kernel;moe;operator;quantization |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug][DSV4][dynamo] nvidia/ops/attention.py wo_a access is dynamo-unsafe; forces --enforce-eager on Option-Y MTP artifacts (~10× decode slowdown on SM 12.0)

### Issue 正文摘录

### Summary `vllm/models/deepseek_v4/nvidia/ops/attention.py:370` accesses `self.wo_a.weight_scale_inv` (or the `weight_scale` fallback from #43290) via a `getattr(..., None)` pattern that **trips dynamo's `_getattr_static`** during `torch.compile` tracing. The trace fails with `ObservedAttributeError` when the MTP block — preserved at BF16 in Option-Y artifacts — has no scale attribute at all, forcing users to set `--enforce-eager` and losing ~10× decode throughput on SM 12.0 (Blackwell consumer/server). ### Repro Artifact: `canada-quant/DeepSeek-V4-Flash-W4A16-FP8-MTP` — main expert weights at W4A16, attention path at FP8_BLOCK, MTP block (layer 43) preserved at BF16 per Option Y. Hardware: NVIDIA RTX PRO 6000 Blackwell Server Edition (SM 12.0), TP=2. vLLM build: `jasl/vllm@ds4-sm120-preview-dev` (SHA `c79225692`), which has the post-refactor `vllm/models/deepseek_v4/nvidia/ops/attention.py` layout. Launch any serve **without** `--enforce-eager`. The cudagraph profile run crashes at: ``` File "vllm/models/deepseek_v4/nvidia/ops/attention.py", line 370, in forward wo_a_scale = self.wo_a.weight_scale torch._dynamo.exc.ObservedAttributeError: 'ColumnParallelLinear' object has no at...

## 现有链接修复摘要

#43290 [Bugfix][DSV4] attention: fall back to `weight_scale` when `weight_scale_inv` absent | #43319 [Bugfix][DSV4] MTP draft model: detect BF16 MTP on disk + skip quant_config

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 9: dels/deepseek_v4/nvidia/ops/attention.py:370` accesses `self.wo_a.weight_scale_inv` (or the `weight_scale` fallback from #43290) via a `getattr(..., None)` pattern that **trips dynamo's `_getattr_static`** during `torch...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: , None)` pattern that **trips dynamo's `_getattr_static`** during `torch.compile` tracing. The trace fails with `ObservedAttributeError` when the MTP block — preserved at BF16 in Option-Y artifacts — has no scale attrib...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: orces --enforce-eager on Option-Y MTP artifacts (~10× decode slowdown on SM 12.0) ### Summary `vllm/models/deepseek_v4/nvidia/ops/attention.py:370` accesses `self.wo_a.weight_scale_inv` (or the `weight_scale` fallback f...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: ile` tracing. The trace fails with `ObservedAttributeError` when the MTP block — preserved at BF16 in Option-Y artifacts — has no scale attribute at all, forcing users to set `--enforce-eager` and losing ~10× decode thr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: te at all, forcing users to set `--enforce-eager` and losing ~10× decode throughput on SM 12.0 (Blackwell consumer/server). ### Repro Artifact: `canada-quant/DeepSeek-V4-Flash-W4A16-FP8-MTP` — main expert weights at W4A...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43290](https://github.com/vllm-project/vllm/pull/43290) | mentioned | 0.45 | [Bugfix][DSV4] attention: fall back to `weight_scale` when `weight_scale_inv` absent | e first per the project's standard contribution flow. ### related - #43290 — added the `getattr(..., none)` fallback; this issue is the dynamo-safety follow-up. - #43319 — auto-de… |
| [#43319](https://github.com/vllm-project/vllm/pull/43319) | mentioned | 0.45 | [Bugfix][DSV4] MTP draft model: detect BF16 MTP on disk + skip quant_config | tr(..., none)` fallback; this issue is the dynamo-safety follow-up. - #43319 — auto-detect bf16 mtp from safetensors index → skip `quant_config` on the mtp draft tower at load tim… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
