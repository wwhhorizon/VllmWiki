# vllm-project/vllm#42870: [Bug]: Multiple model files still trigger ImageProcessorFast DeprecationWarning post transformers v5.4 refactor

| 字段 | 值 |
| --- | --- |
| Issue | [#42870](https://github.com/vllm-project/vllm/issues/42870) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Multiple model files still trigger ImageProcessorFast DeprecationWarning post transformers v5.4 refactor

### Issue 正文摘录

### What Static imports of deprecated `*ImageProcessorFast` symbols still trigger transformers `DeprecationWarning` across four model files under `vllm/model_executor/models/`. #42700 fixed the same family for `qwen3_vl.py` (one file); the other four were not covered. ### Reproduction ``` $ docker run --rm --gpus '"device=1"' --entrypoint python3 \ vllm/vllm-openai:v0.20.0 -W default -c \ "import vllm.model_executor.models.lfm2_vl" [transformers] Accessing `Lfm2VlImageProcessorFast` from `.models.lfm2_vl.image_processing_lfm2_vl`. Returning `Lfm2VlImageProcessor` instead. Behavior may be different and this alias will be removed in future versions. ``` Same form of warning fires on each of: | File | Imported symbol | Replacement (per transformers warning text) | |---|---|---| | `vllm/model_executor/models/lfm2_vl.py` | `Lfm2VlImageProcessorFast` (+ `find_closest_aspect_ratio`, `round_by_factor` from the deprecated submodule path) | `Lfm2VlImageProcessor` | | `vllm/model_executor/models/gemma3n_mm.py` | `SiglipImageProcessorFast` | `SiglipImageProcessor` | | `vllm/model_executor/models/interns1.py` | `GotOcr2ImageProcessorFast` | `GotOcr2ImageProcessor` | | `vllm/model_executor/mode...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Multiple model files still trigger ImageProcessorFast DeprecationWarning post transformers v5.4 refactor ### What Static imports of deprecated `*ImageProcessorFast` symbols still trigger transformers `Deprecation...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Fast DeprecationWarning post transformers v5.4 refactor ### What Static imports of deprecated `*ImageProcessorFast` symbols still trigger transformers `DeprecationWarning` across four model files under `vllm/model_execu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 4 (merged 2026-03-19, "🚨🚨 Refactor Image Processors to support different backends") dropped the `Fast` suffix for image processors and reshaped the underlying class layout. - vLLM's `requirements/common.txt` already pin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: the `Fast` suffix for image processors and reshaped the underlying class layout. - vLLM's `requirements/common.txt` already pins around the breaking transitions (`!= 5.4.*, != 5.5.0`), but the import-site warnings on th...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: submodule path) | `Lfm2VlImageProcessor` | | `vllm/model_executor/models/gemma3n_mm.py` | `SiglipImageProcessorFast` | `SiglipImageProcessor` | | `vllm/model_executor/models/interns1.py` | `GotOcr2ImageProcessorFast` |...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
