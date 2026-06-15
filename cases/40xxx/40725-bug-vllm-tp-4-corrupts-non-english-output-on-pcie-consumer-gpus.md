# vllm-project/vllm#40725: [Bug]: vLLM TP=4 corrupts non-English output on PCIe consumer GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#40725](https://github.com/vllm-project/vllm/issues/40725) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;moe;sampling |
| 症状 | crash;nondeterministic;slowdown |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM TP=4 corrupts non-English output on PCIe consumer GPUs

### Issue 正文摘录

### Your current environment ## Environment - vLLM 0.19.0, also reproduced on 0.19.1 - torch 2.10.0+cu129, CUDA 12.9 - 4× RTX 3090 (SM 8.6), PCIe-only, no NVLink - Linux 6.17, Python 3.12 - NCCL 2.27.5 (bundled with torch), driver 590.48.01 ### 🐛 Describe the bug ## Summary Running vLLM with `--tensor-parallel-size 4` on 4× RTX 3090 (PCIe, no NVLink) produces deterministic text corruption in non-English languages: glued, truncated or duplicated words, sometimes a non-Latin character in the middle of a Spanish sentence. **English output from the same run is clean.** Switch back to TP=4 with a Spanish/Italian/Portuguese/French prompt and the corruption comes back. The thing I can't explain is how stable the symptom is across models and variants. I first hit it on `Qwen/Qwen3.6-35B-A3B`. Then I reproduced it on `Qwen/Qwen3.5-35B-A3B-FP8` (different version, different dtype), on `google/gemma-4-26B-A4B-it` (MoE), on `google/gemma-4-31B-it` (**dense**, not MoE at all), and on `Qwen/Qwen3.6-35B-A3B-FP8`. Different model families, different dtypes, MoE and dense — as long as it's TP=4 on this hardware, non-English output corrupts and English does not. The same hardware works correctly un...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 5: PUs bug ### Your current environment ## Environment - vLLM 0.19.0, also reproduced on 0.19.1 - torch 2.10.0+cu129, CUDA 12.9 - 4× RTX 3090 (SM 8.6), PCIe-only, no NVLink - Linux 6.17, Python 3.12 - NCCL 2.27.5 (bundled...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: vLLM TP=4 corrupts non-English output on PCIe consumer GPUs bug ### Your current environment ## Environment - vLLM 0.19.0, also reproduced on 0.19.1 - torch 2.10.0+cu129, CUDA 12.9 - 4× RTX 3090 (SM 8.6), PCIe-on...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: on `Qwen/Qwen3.6-35B-A3B`. Then I reproduced it on `Qwen/Qwen3.5-35B-A3B-FP8` (different version, different dtype), on `google/gemma-4-26B-A4B-it` (MoE), on `google/gemma-4-31B-it` (**dense**, not MoE at all), and on `Q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: mes back. The thing I can't explain is how stable the symptom is across models and variants. I first hit it on `Qwen/Qwen3.6-35B-A3B`. Then I reproduced it on `Qwen/Qwen3.5-35B-A3B-FP8` (different version, different dty...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: vironment - vLLM 0.19.0, also reproduced on 0.19.1 - torch 2.10.0+cu129, CUDA 12.9 - 4× RTX 3090 (SM 8.6), PCIe-only, no NVLink - Linux 6.17, Python 3.12 - NCCL 2.27.5 (bundled with torch), driver 590.48.01 ### 🐛 Descri...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
