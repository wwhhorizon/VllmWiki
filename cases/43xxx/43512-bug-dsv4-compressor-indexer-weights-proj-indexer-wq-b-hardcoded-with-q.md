# vllm-project/vllm#43512: [Bug][DSV4] compressor / indexer.weights_proj / indexer.wq_b hardcoded with quant_config=None; breaks load of artifacts that calibrate these attention sub-modules

| 字段 | 值 |
| --- | --- |
| Issue | [#43512](https://github.com/vllm-project/vllm/issues/43512) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;fp8;kernel;operator;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug][DSV4] compressor / indexer.weights_proj / indexer.wq_b hardcoded with quant_config=None; breaks load of artifacts that calibrate these attention sub-modules

### Issue 正文摘录

### Summary In `vllm/models/deepseek_v4/compressor.py` and `vllm/models/deepseek_v4/nvidia/ops/attention.py`, the **compressor's `fused_wkv_wgate`** module and the **indexer's `weights_proj`** / **indexer's `compressor.fused_wkv_wgate`** / **indexer's `wq_b`** modules are constructed with **`quant_config=None`** — i.e. unconditionally as unquantized BF16 modules. This breaks loading of any DSv4-Flash artifact whose calibration recipe quantizes these attention sub-modules. ### Repro Artifact: `canada-quant/DeepSeek-V4-Flash-W4A16-FP8-MTP` (per the predecessor `canada-quant/DeepSeek-V4-Flash-W4A16-FP8` recipe, attention path is FP8_BLOCK including the compressor and indexer). ```python import safetensors.torch as st with st.safe_open("model-00001-of-00004.safetensors", framework="pt") as f: t = f.get_tensor("layers.10.attn.compressor.wkv.weight") ts = f.get_tensor("layers.10.attn.compressor.wkv.weight_scale") print(t.dtype, t.shape) # torch.float8_e4m3fn torch.Size([1024, 4096]) print(ts.dtype, ts.shape) # torch.bfloat16 torch.Size([8, 32]) (block 128×128 scales) ``` vLLM source (current `vllm/models/deepseek_v4/compressor.py:215-227`): ```python self.fused_wkv_wgate = MergedColumnP...

## 现有链接修复摘要

#43290 [Bugfix][DSV4] attention: fall back to `weight_scale` when `weight_scale_inv` absent | #43515 [Bugfix][DSV4] Plumb quant_config into compressor.fused_wkv_wgate and indexer.weights_proj | #43655 [Bugfix][DSV4] Plumb quant_config + route compressor GEMM through quant-aware dispatch

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 10: g][DSV4] compressor / indexer.weights_proj / indexer.wq_b hardcoded with quant_config=None; breaks load of artifacts that calibrate these attention sub-modules ### Summary In `vllm/models/deepseek_v4/compressor.py` and...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: `canada-quant/DeepSeek-V4-Flash-W4A16-FP8` recipe, attention path is FP8_BLOCK including the compressor and indexer). ```python import safetensors.torch as st with st.safe_open("model-00001-of-00004.safetensors", framew...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None → `UnquantizedLinearMethod` (same as today). **Option B — deeper: dispatch per-module based on artifact's config_groups** The model class inspects `config.quantization_config.config_groups` at __init__ time and per...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ules. This breaks loading of any DSv4-Flash artifact whose calibration recipe quantizes these attention sub-modules. ### Repro Artifact: `canada-quant/DeepSeek-V4-Flash-W4A16-FP8-MTP` (per the predecessor `canada-quant/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: equant_compressor.py), 166 weights, ~1.5 min wall). Detailed in [`RECIPE_RTX6000PRO.md`](https://github.com/canada-quant/dsv4-flash-w4a16-fp8-mtp/blob/main/RECIPE_RTX6000PRO.md#34-compressor--indexerweights_proj-are-fp8...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43290](https://github.com/vllm-project/vllm/pull/43290) | mentioned | 0.45 | [Bugfix][DSV4] attention: fall back to `weight_scale` when `weight_scale_inv` absent | option a is ~6 lines of changes; happy to file a pr. ### related - #43290 — added a `weight_scale_inv → weight_scale` fallback in this same `nvidia/ops/attention.py` file. this is… |
| [#43515](https://github.com/vllm-project/vllm/pull/43515) | closes_keyword | 0.95 | [Bugfix][DSV4] Plumb quant_config into compressor.fused_wkv_wgate and indexer.weights_proj | Fixes #43512. `DeepseekCompressor.fused_wkv_wgate` and `DeepseekV4Indexer.weights_proj` were constructed with a hard-coded `quant_config=None` on the NVIDIA DSv4 path. Any DSv4-Fl |
| [#43655](https://github.com/vllm-project/vllm/pull/43655) | closes_keyword | 0.95 | [Bugfix][DSV4] Plumb quant_config + route compressor GEMM through quant-aware dispatch | Fixes #43512. Two fixes combined into one shippable unit: 1. **(cherry-pick from #43515)** Plumb model-level `quant_config` into `compressor.fused_wkv_wgate` and `indexer.wei |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
