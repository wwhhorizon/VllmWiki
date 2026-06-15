# vllm-project/vllm#23056: [Bug]: Incorrect video rotary embedding calculation in Qwen2.5-Omni due to missing `second_per_grid_ts` mapping

| 字段 | 值 |
| --- | --- |
| Issue | [#23056](https://github.com/vllm-project/vllm/issues/23056) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | shape_align |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Incorrect video rotary embedding calculation in Qwen2.5-Omni due to missing `second_per_grid_ts` mapping

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## TL;DR vLLM fails to correctly extract `second_per_grid_ts` from processor output in Qwen2.5-Omni model, causing incorrect multimodal Rotary Embedding calculation when using non-default FPS values for video inputs. ## Description In the Qwen2.5-Omni model (and possibly Qwen-VL), vLLM does not correctly retrieve the variable `second_per_grid_ts` from the processor's return value, which is used to calculate the multimodal Rotary Embedding for inputs. Since `second_per_grid_ts` is not properly set, it always uses the default value, which works fine in typical cases. However, when we specify a different fps for input videos, such as 1 (default is 2), `second_per_grid_ts` needs to be adjusted according to the processor's results to correctly calculate the rotary embedding for video tokens. Due to this bug, we get incorrect rotary embeddings compared to the standard HuggingFace implementation. ## Reproduction I provide a demonstration code that mainly specifies fps for inference, including both the standard HuggingFace implementation and the vLLM implementation. Please install `qwen_omni_utils` first. ## Impact on Results I checked t...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Incorrect video rotary embedding calculation in Qwen2.5-Omni due to missing `second_per_grid_ts` mapping bug ### Your current environment ### 🐛 Describe the bug ## TL;DR vLLM fails to correctly extract `second_pe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: he default value, which works fine in typical cases. However, when we specify a different fps for input videos, such as 1 (default is 2), `second_per_grid_ts` needs to be adjusted according to the processor's results to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tions (fps=2), vLLM's results match HF's, while modifying fps produces mismatches. I tested the output of Qwen2.5-Omni-7B, and the incorrect positional encoding causes perturbations in the results, but the outputs remai...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: , vLLM's results match HF's, while modifying fps produces mismatches. I tested the output of Qwen2.5-Omni-7B, and the incorrect positional encoding causes perturbations in the results, but the outputs remain reasonable....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: upport;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;triton build_error;mismatch dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
