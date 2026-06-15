# vllm-project/vllm#37890: [Bug]: NaNs in vLLM using DeepSeek-R1-0528-NVFP4-v2

| 字段 | 值 |
| --- | --- |
| Issue | [#37890](https://github.com/vllm-project/vllm/issues/37890) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;operator |
| 症状 | nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NaNs in vLLM using DeepSeek-R1-0528-NVFP4-v2

### Issue 正文摘录

### Your current environment Manifests: * Prefill: https://github.com/tlrmchlsmth/j-llm-d/blob/dc5db36f591f1112f874b5e1f34846ca947affee/gb200/base/prefill.yaml * Decode: https://github.com/tlrmchlsmth/j-llm-d/blob/dc5db36f591f1112f874b5e1f34846ca947affee/gb200/base/decode.yaml Image: https://github.com/llm-d/llm-d/blob/bc2e40d5a806672b4744879ca48a42eaa047f1ba/docker/Dockerfile.cuda ### 🐛 Describe the bug We are seeing NaNs when using the `FLASHINFER_MLA` attention backend in vLLM. * We're using sing `DeepSeek-R1-0528-NVFP4-v2` * Attention inputs are clean but outputs contain NaNs -- Not sure about the KV cache yet. * Once we start seeing NaNs, gsm8k eval scores start slowly dropping over time * Hard to repro - we're seeing this in WideEP GB200 settings, and it can take up to 1 hour before seeing poor evals. Affects: * FP4 models (BF16/FP8 models are ok), namely: nvidia/DeepSeek-R1-0528-NVFP4-v2 * wide-EP (standard single node DP not reproduced as far as im aware?) * with and without EPLB (although EPLB can accelerate reproduction) * all kv-cache dtypes (both FP8 and BF16) Known 1 . Attention can introduce NaN in the padded token regions a. from torch.empty for max_model_len = 4096...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: NaNs in vLLM using DeepSeek-R1-0528-NVFP4-v2 bug ### Your current environment Manifests: * Prefill: https://github.com/tlrmchlsmth/j-llm-d/blob/dc5db36f591f1112f874b5e1f34846ca947affee/gb200/base/prefill.yaml * D...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s://github.com/llm-d/llm-d/blob/bc2e40d5a806672b4744879ca48a42eaa047f1ba/docker/Dockerfile.cuda ### 🐛 Describe the bug We are seeing NaNs when using the `FLASHINFER_MLA` attention backend in vLLM. * We're using sing `De...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: current environment Manifests: * Prefill: https://github.com/tlrmchlsmth/j-llm-d/blob/dc5db36f591f1112f874b5e1f34846ca947affee/gb200/base/prefill.yaml * Decode: https://github.com/tlrmchlsmth/j-llm-d/blob/dc5db36f591f11...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: ttention inputs are clean but outputs contain NaNs -- Not sure about the KV cache yet. * Once we start seeing NaNs, gsm8k eval scores start slowly dropping over time * Hard to repro - we're seeing this in WideEP GB200 s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: , and it can take up to 1 hour before seeing poor evals. Affects: * FP4 models (BF16/FP8 models are ok), namely: nvidia/DeepSeek-R1-0528-NVFP4-v2 * wide-EP (standard single node DP not reproduced as far as im aware?) *...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
