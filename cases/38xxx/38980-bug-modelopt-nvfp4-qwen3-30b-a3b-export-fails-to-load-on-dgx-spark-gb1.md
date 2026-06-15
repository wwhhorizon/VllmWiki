# vllm-project/vllm#38980: [Bug]: ModelOpt NVFP4 Qwen3-30B-A3B export fails to load on DGX Spark/GB10 (missing _double_scale key)

| 字段 | 值 |
| --- | --- |
| Issue | [#38980](https://github.com/vllm-project/vllm/issues/38980) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cache;fp8;moe;quantization |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ModelOpt NVFP4 Qwen3-30B-A3B export fails to load on DGX Spark/GB10 (missing _double_scale key)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM detects our exported checkpoint as a ModelOpt NVFP4 checkpoint, but fails to load a Qwen3 MoE export on DGX Spark / GB10 before generation starts. The checkpoint was exported successfully in our lab and is already materialized as a packaged HF export with: - `config.json` - `hf_quant_config.json` - `model.safetensors.index.json` - `model-00001-of-00004.safetensors` ... `model-00004-of-00004.safetensors` vLLM recognizes it as `ModelOpt NVFP4`, sees the GPU correctly, and starts the load path, but then fails with: ```text KeyError: layers.28.mlp.experts.w2_weight_quantizer._double_scale ``` Important extra evidence from the exported checkpoint: - the export DOES contain `_double_scale` keys - however, in the HF index they are named with the HF projection names, e.g.: ```text model.layers.28.mlp.experts.0.down_proj.weight_quantizer._double_scale model.layers.28.mlp.experts.0.gate_proj.weight_quantizer._double_scale model.layers.28.mlp.experts.0.up_proj.weight_quantizer._double_scale model.layers.28.mlp.experts.1.down_proj.weight_quantizer._double_scale ... ``` So this does not look like a missing export artifact. It looks more...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: ModelOpt NVFP4 Qwen3-30B-A3B export fails to load on DGX Spark/GB10 (missing _double_scale key) ### Your current environment ### 🐛 Describe the bug vLLM detects our exported checkpoint as a ModelOpt NVFP4 checkpo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: ModelOpt NVFP4 Qwen3-30B-A3B export fails to load on DGX Spark/GB10 (missing _double_scale key) ### Your current environment ### 🐛 Describe the bug vLLM detects our exported checkpoint as a ModelOpt NVFP4 checkpo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: t KeyError: layers.28.mlp.experts.w2_weight_quantizer._double_scale ``` Important extra evidence from the exported checkpoint: - the export DOES contain `_double_scale` keys - however, in the HF index they are named wit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: a missing export artifact. It looks more like a naming/loader contract mismatch for Qwen3 MoE ModelOpt NVFP4. ### Reproduction Our alternative validation script runs the model inside the official NVIDIA vLLM container a...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ted checkpoint as a ModelOpt NVFP4 checkpoint, but fails to load a Qwen3 MoE export on DGX Spark / GB10 before generation starts. The checkpoint was exported successfully in our lab and is already materialized as a pack...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
