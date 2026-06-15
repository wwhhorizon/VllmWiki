# vllm-project/vllm#27021: [Usage]: Need guidance reproducing benchmark results from PR #25337 — results differ significantly from reported data

| 字段 | 值 |
| --- | --- |
| Issue | [#27021](https://github.com/vllm-project/vllm/issues/27021) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | fp8 |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Usage]: Need guidance reproducing benchmark results from PR #25337 — results differ significantly from reported data

### Issue 正文摘录

## Background Recently, we have been working on optimizing the position computation for multimodal models in vLLM. During benchmarking, we noticed that our results were not as expected. To investigate, we decided to reproduce the benchmark results from [PR #25337](https://github.com/vllm-project/vllm/pull/25337), comparing the performance before and after that PR was merged into the main branch. - Before PR commit: cf56cf78b47e5f9b6a81ce0d50a94f9291922315 - After PR commit: 30d08911f7cf78287f8da003ddcc99f6ef196f9f However, our reproduced results differ **significantly** from the performance data reported in the PR. We’d like to understand whether this discrepancy may be caused by hardware differences, model choice, or benchmark setup. **Who can help guide me?** ## Model and Environment - Model used: Qwen/Qwen3-VL-30B-A3B-Instruct-FP8(The modelQwen3-VL-4B used in the PR could not be found on Hugging Face.) - GPU: NVIDIA A100 PCIe - vLLM startup command: ```bash vllm serve "Qwen/Qwen3-VL-30B-A3B-Instruct-FP8" \ --trust-remote-code \ --gpu-memory-utilization 0.9 \ --max-model-len 16384 ``` ## Benchmark Command ```bash vllm bench serve \ --backend openai-chat \ --model "Qwen/Qwen3-VL-...

## 现有链接修复摘要

#25337 [MM][Perf] Minor Optimization on Qwen3-VL `fast_pos_embed_interpolate`

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ecently, we have been working on optimizing the position computation for multimodal models in vLLM. During benchmarking, we noticed that our results were not as expected. To investigate, we decided to reproduce the benc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Usage]: Need guidance reproducing benchmark results from PR #25337 — results differ significantly from reported data usage;stale ## Background Recently, we have been working on optimizing the position computation for m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: * ## Model and Environment - Model used: Qwen/Qwen3-VL-30B-A3B-Instruct-FP8(The modelQwen3-VL-4B used in the PR could not be found on Hugging Face.) - GPU: NVIDIA A100 PCIe - vLLM startup command: ```bash vllm serve "Qw...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: s from PR #25337 — results differ significantly from reported data usage;stale ## Background Recently, we have been working on optimizing the position computation for multimodal models in vLLM. During benchmarking, we n...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: model-len 16384 ``` ## Benchmark Command ```bash vllm bench serve \ --backend openai-chat \ --model "Qwen/Qwen3-VL-30B-A3B-Instruct-FP8" \ --base-url "http://localhost:8000" \ --endpoint "/v1/chat/completions" \ --datas...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25337](https://github.com/vllm-project/vllm/pull/25337) | mentioned | 0.45 | [MM][Perf] Minor Optimization on Qwen3-VL `fast_pos_embed_interpolate` | ained are noticeably different from the benchmark numbers shown in pr #25337. could this gap be explained by differences such as: - model: qwen3-vl-4b vs. qwen3-vl-30b-a3b-instruc… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
