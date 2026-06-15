# vllm-project/vllm#36249: [Bug]: Qwen3.5-27B-GPTQ-Int4 crashes [vllm version v0.16.1rc1]

| 字段 | 值 |
| --- | --- |
| Issue | [#36249](https://github.com/vllm-project/vllm/issues/36249) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-27B-GPTQ-Int4 crashes [vllm version v0.16.1rc1]

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Summary We experience a crash issue with vLLM (v0.16.1rc1) when serving the Qwen3.5-27B-GPTQ-Int4 model on an NVIDIA H200 NVL GPU. The crash consistently occurs after the system reaches a certain throughput threshold. We attempted to mitigate the issue by adjusting GPU memory utilization settings (ranging from 0.6 to 0.9), but the crashes persist. **Note:** We conducted the same tests with Qwen3.5-27B and Qwen3.5-27B-FP8 models under identical conditions, and neither of these models experienced this crash issue. This suggests the problem may be specific to the GPTQ-Int4 quantization. ### Command Used ```bash vllm serve Qwen3.5-27B-GPTQ-Int4 \ --language-model-only \ --reasoning-parser qwen3 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' ``` ### Troubleshooting Attempts - Tested with `--gpu-memory-utilization` values ranging from 0.6 to 0.9 - Issue persists across different memory utilization settings --- **Crash Logs:** https://gist.github.com/berkayersoyy/00196125112ca88ddb5cdb9f5758d70c --- ### Before submitting a new issue... - [x]...

## 现有链接修复摘要

#36462 [Bugfix] Fix GDN in_proj_ba crash with GPTQ/FP8 and TP > 1

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Qwen3.5-27B-GPTQ-Int4 crashes [vllm version v0.16.1rc1] bug ### Your current environment ### 🐛 Describe the bug ## Summary We experience a crash issue with vLLM (v0.16.1rc1) when serving the Qwen3.5-27B-GPTQ-Int4...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Qwen3.5-27B-GPTQ-Int4 crashes [vllm version v0.16.1rc1] bug ### Your current environment ### 🐛 Describe the bug ## Summary We experience a crash issue with vLLM (v0.16.1rc1) when serving the Qwen3.5-27B-GPTQ-Int4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5-27B-GPTQ-Int4 crashes [vllm version v0.16.1rc1] bug ### Your current environment ### 🐛 Describe the bug ## Summary We experience a crash issue with vLLM (v0.16.1rc1) when serving the Qwen3.5-27B-GPTQ-Int4...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: --- ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: VL GPU. The crash consistently occurs after the system reaches a certain throughput threshold. We attempted to mitigate the issue by adjusting GPU memory utilization settings (ranging from 0.6 to 0.9), but the crashes p...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36462](https://github.com/vllm-project/vllm/pull/36462) | closes_keyword | 0.95 | [Bugfix] Fix GDN in_proj_ba crash with GPTQ/FP8 and TP > 1 | Closes #36249 Closes #35502 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
