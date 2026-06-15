# vllm-project/vllm#40252: [Bug]: Qwen3-Next NVFP4 quants silently produce garbage when linear_attn weights are missing from quantization_config.ignore

| 字段 | 值 |
| --- | --- |
| Issue | [#40252](https://github.com/vllm-project/vllm/issues/40252) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;gemm_linear;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;kernel;moe;quantization |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next NVFP4 quants silently produce garbage when linear_attn weights are missing from quantization_config.ignore

### Issue 正文摘录

# [Bug]: Qwen3-Next NVFP4 quants silently produce garbage when `linear_attn` weights are missing from `quantization_config.ignore` ## Your current environment ## 🐛 Describe the bug Every community NVFP4 quant of a Qwen3-Next-family model (Qwen 3.5, 3.6, and presumably 3.7 going forward) ships a `quantization_config.ignore` list that names the **old split tensor names** for the linear-attention block: ``` model.language_model.layers.{i}.linear_attn.in_proj_qkv model.language_model.layers.{i}.linear_attn.in_proj_z model.language_model.layers.{i}.linear_attn.in_proj_b model.language_model.layers.{i}.linear_attn.in_proj_a ``` The actual safetensors shards, however, use the **new combined names**: ``` model.language_model.layers.{i}.linear_attn.in_proj_qkvz model.language_model.layers.{i}.linear_attn.in_proj_ba ``` At load time, vLLM: 1. Sees the combined `in_proj_qkvz` / `in_proj_ba` weights in the checkpoint 2. Checks `quantization_config.ignore` for them — they're not there 3. Attempts to load them as NVFP4-quantized (expecting scale factors that don't exist) 4. **Silently skips them** (log message only: `Parameter layers.X.linear_attn.in_proj_qkvz.weight not found in params_dict, s...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Qwen3-Next NVFP4 quants silently produce garbage when linear_attn weights are missing from quantization_config.ignore # [Bug]: Qwen3-Next NVFP4 quants silently produce garbage when `linear_attn` weights are missi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: the combined-name patterns to the ignore list before serving: ```python import json, pathlib cfg_path = pathlib.Path(".../snapshot/config.json") with open(cfg_path) as f: cfg = json.load(f) ig = cfg["quantization_config...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Next NVFP4 quants silently produce garbage when linear_attn weights are missing from quantization_config.ignore # [Bug]: Qwen3-Next NVFP4 quants silently produce garbage when `linear_attn` weights are missi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ut the nvfp4 path, inference continues with broken weights. ## Steps to reproduce ```bash vllm serve RedHatAI/Qwen3.6-35B-A3B-NVFP4 \ --trust-remote-code --tensor-parallel-size 1 ``` Then: ```bash curl -s -X POST http:/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: en3-Next-family model (Qwen 3.5, 3.6, and presumably 3.7 going forward) ships a `quantization_config.ignore` list that names the **old split tensor names** for the linear-attention block: ``` model.language_model.layers...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
