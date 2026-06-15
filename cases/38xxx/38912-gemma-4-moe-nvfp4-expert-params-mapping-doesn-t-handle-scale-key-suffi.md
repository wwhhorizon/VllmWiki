# vllm-project/vllm#38912: Gemma 4 MoE NVFP4: expert_params_mapping doesn't handle scale key suffixes

| 字段 | 值 |
| --- | --- |
| Issue | [#38912](https://github.com/vllm-project/vllm/issues/38912) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;moe;quantization |
| 子分类 | install |
| Operator 关键词 | fp8;moe;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Gemma 4 MoE NVFP4: expert_params_mapping doesn't handle scale key suffixes

### Issue 正文摘录

## Problem When loading NVFP4-quantized Gemma 4 MoE checkpoints (e.g., `google/gemma-4-26B-A4B-it` quantized with modelopt), the `expert_params_mapping` in `gemma4.py` correctly maps base weight keys but fails for NVFP4 scale keys. The mapping replaces `experts.0.down_proj` → `experts.w2_weight`: ```python moe_name = name.replace(weight_name, param_name) ``` For a base weight key like `experts.0.down_proj.weight`, the code explicitly appends `.weight`: ```python weight_loader(param, loaded_weight, weight_name + ".weight", shard_id=shard_id, expert_id=expert_id) ``` This produces `experts.w2_weight` → found in `params_dict` ✓ But for NVFP4 scale keys, the replacement produces wrong parameter names: | Checkpoint key | After replace | FusedMoE param (actual) | Match? | |---|---|---|---| | `experts.0.down_proj.weight` | `experts.w2_weight.weight` → handled by explicit `.weight` append | `experts.w2_weight` | ✓ | | `experts.0.down_proj.weight_scale` | `experts.w2_weight.weight_scale` | `experts.w2_weight_scale` | ✗ (dot vs underscore) | | `experts.0.down_proj.weight_scale_2` | `experts.w2_weight.weight_scale_2` | `experts.w2_weight_scale_2` | ✗ | | `experts.0.down_proj.input_scale` | `...

## 现有链接修复摘要

#38875 [Bugfix] Fix Gemma4 NVFP4 quantized model weight loading | #39084 Fix Gemma4 NVFP4 expert scale suffix mapping

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: Gemma 4 MoE NVFP4: expert_params_mapping doesn't handle scale key suffixes ## Problem When loading NVFP4-quantized Gemma 4 MoE checkpoints (e.g., `google/gemma-4-26B-A4B-it` quantized with modelopt), the `expert_params_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: For a base weight key like `experts.0.down_proj.weight`, the code explicitly appends `.weight`: ```python weight_loader(param, loaded_weight, weight_name + ".weight", shard_id=shard_id, expert_id=expert_id) ``` This pro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Gemma 4 MoE NVFP4: expert_params_mapping doesn't handle scale key suffixes ## Problem When loading NVFP4-quantized Gemma 4 MoE checkpoints (e.g., `google/gemma-4-26B-A4B-it` quantized with modelopt), the `expert_params_
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: Gemma 4 MoE NVFP4: expert_params_mapping doesn't handle scale key suffixes ## Problem When loading NVFP4-quantized Gemma 4 MoE checkpoints (e.g., `google/gemma-4-26B-A4B-it` quantized with modelopt), the `expert_params_
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ut_scale` | ✗ | The scale keys fall through the mapping, hit the `else` fallback, and crash with: ``` TypeError: FusedMoE.weight_loader() missing 3 required positional arguments: 'weight_name', 'shard_id', and 'expert_i...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38875](https://github.com/vllm-project/vllm/pull/38875) | mentioned | 0.45 | [Bugfix] Fix Gemma4 NVFP4 quantized model weight loading | ires `--moe-backend marlin` for correct moe computation - related: pr #38875 addresses a different gemma 4 nvfp4 issue (audio tower `input_max`) ## tested with - `google/gemma-4-2… |
| [#39084](https://github.com/vllm-project/vllm/pull/39084) | closes_keyword | 0.95 | Fix Gemma4 NVFP4 expert scale suffix mapping | Fixes #38912. Gemma4 MoE expert checkpoint tensors can arrive as bare weights or as suffixed scale tensors like .weight_scale, .weight_scale_2, and .input_scale. The previous mapp |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
