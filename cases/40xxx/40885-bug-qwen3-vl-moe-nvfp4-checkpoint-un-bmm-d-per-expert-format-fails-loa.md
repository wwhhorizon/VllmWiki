# vllm-project/vllm#40885: [Bug]: Qwen3-VL-MoE NVFP4 checkpoint (un-BMM'd per-expert format) fails load with IndexError: Dimension out of range

| 字段 | 值 |
| --- | --- |
| Issue | [#40885](https://github.com/vllm-project/vllm/issues/40885) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;hardware_porting;model_support;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;quantization |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-MoE NVFP4 checkpoint (un-BMM'd per-expert format) fails load with IndexError: Dimension out of range

### Issue 正文摘录

# Issue: Qwen3-VL-MoE NVFP4 per-expert checkpoint fails to load **File via**: [New Issue → Bug Report](https://github.com/vllm-project/vllm/issues/new?template=400-bug-report.yml) **Suggested title**: `[Bug]: Qwen3-VL-MoE NVFP4 checkpoint (un-BMM'd per-expert format) fails load with IndexError: Dimension out of range` --- ## Your current environment ## 🐛 Describe the bug vLLM's `qwen3_vl_moe.py` weight loader crashes when loading an NVFP4-quantized Qwen3-VL-MoE checkpoint produced by [NVIDIA TensorRT-Model-Optimizer](https://github.com/NVIDIA/TensorRT-Model-Optimizer) (nvidia-modelopt ≥ 0.43, configs `NVFP4_DEFAULT_CFG` / `NVFP4_AWQ_LITE_CFG`). ### Root cause ModelOpt quantizes Qwen3-VL-MoE by un-BMM'ing the fused `experts.gate_up_proj` / `experts.down_proj` parameter tensors into per-expert `nn.ModuleList`s. The resulting state dict has names like: ``` model.language_model.layers.0.mlp.experts.gate_proj.0.weight_packed model.language_model.layers.0.mlp.experts.gate_proj.0.weight_scale model.language_model.layers.0.mlp.experts.gate_proj.0.weight_scale_2 model.language_model.layers.0.mlp.experts.gate_proj.0.input_scale model.language_model.layers.0.mlp.experts.down_proj.0.weight_pa...

## 现有链接修复摘要

#39256 Support NVFP4 per-expert weight loading for Gemma 4 MoE | #40888 [Bugfix][Model] Qwen3-VL-MoE NVFP4 (ModelOpt) per-expert weight loading | #42763 [Bugfix] qwen3_vl_moe: don't transpose 0-D/1-D scale tensors (#40885) | #42800 [Model] Qwen3-VL-MoE: remap ModelOpt NVFP4 per-expert weight names (#…

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [Bug]: Qwen3-VL-MoE NVFP4 checkpoint (un-BMM'd per-expert format) fails load with IndexError: Dimension out of range # Issue: Qwen3-VL-MoE NVFP4 per-expert checkpoint fails to load **File via**: [New Issue → Bug Report]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Qwen3-VL-MoE NVFP4 checkpoint (un-BMM'd per-expert format) fails load with IndexError: Dimension out of range # Issue: Qwen3-VL-MoE NVFP4 per-expert checkpoint fails to load **File via**: [New Issue → Bug Report]...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Proposed fix Extend `vllm/model_executor/models/qwen3_vl_moe.py`: 1. Precise regex-based `is_fused_expert` detection that only matches the truly-fused BMM tensor format (no intermediate per-expert index) 2. Add an up-fr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: expected to be in range of [-1, 0], but got -2)`. 2. **Name convention mismatch**. Even after fixing the crash, the loader expects Mixtral-style `experts.{N}.gate_proj.*` but ModelOpt emits `experts.gate_proj.{N}.*` (pr...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Qwen3-VL-MoE NVFP4 checkpoint (un-BMM'd per-expert format) fails load with IndexError: Dimension out of range # Issue: Qwen3-VL-MoE NVFP4 per-expert checkpoint fails to load **File via**: [New Issue → Bug Report]...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39256](https://github.com/vllm-project/vllm/pull/39256) | mentioned | 0.45 | Support NVFP4 per-expert weight loading for Gemma 4 MoE | nalogous problem for gemma 4; similar fix pattern applies here. - [pr #39256 (open)](https://github.com/vllm-project/vllm/pull/39256) — nvfp4 per-expert loading for gemma 4 moe (d… |
| [#40888](https://github.com/vllm-project/vllm/pull/40888) | closes_keyword | 0.95 | [Bugfix][Model] Qwen3-VL-MoE NVFP4 (ModelOpt) per-expert weight loading | Fixes: #40885 ## AI assistance disclosure Per `AGENTS.md`, this PR was produced with non-trivial assistance from an AI coding assistant (Anthropic Claude, model `claude-opus-4-7` |
| [#42763](https://github.com/vllm-project/vllm/pull/42763) | mentioned | 0.6 | [Bugfix] qwen3_vl_moe: don't transpose 0-D/1-D scale tensors (#40885) | # NVFP4 MoE checkpoints still depends on the remaining work in # #40885 (name remap + 3-D unpack); this PR just stops the crash # and lets the existing quant-aware loaders see th |
| [#42800](https://github.com/vllm-project/vllm/pull/42800) | closes_keyword | 0.95 | [Model] Qwen3-VL-MoE: remap ModelOpt NVFP4 per-expert weight names (#… | Closes #40885. ## Purpose ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [ ] Th |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
