# vllm-project/vllm#31755: [Feature]: Optimizations for MOE models (GLM4.7, DeepSeek series)

| 字段 | 值 |
| --- | --- |
| Issue | [#31755](https://github.com/vllm-project/vllm/issues/31755) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;gemm_linear;model_support;moe;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;moe;sampling |
| 症状 | nan_inf;slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Feature]: Optimizations for MOE models (GLM4.7, DeepSeek series)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch [h100-tep8-glm4.7fp8.gz](https://github.com/user-attachments/files/24442034/h100-tep8-glm4.7fp8.gz) I am trying to optimize MOE models like GLM4.7 in vLLM, let's have this issue to track. Tasks: - [x] Optimize grouped_topk kernel (For GLM4.6 but works for 4.7 as well) #30159 - [x] Optimize additional fill(0) in cutlass moe #31754 - [x] Optimize cutlass moe problem size calculation #31830 - [x] Optimize group topk kernel further #32058 - [x] Optimize the moe permute/unpermute kernel https://github.com/vllm-project/vllm/pull/32273 ## Command used to check accuracy and benchmark `export MODEL="zai-org/GLM-4.7-FP8"` `vllm serve $MODEL -tp 8 --port 9256 --enable-expert-parallel --max_num_seqs 128` ### Acc `lm_eval --model local-completions --model_args "base_url=http://127.0.0.1:9256/v1/completions,model=$MODEL,num_concurrent=1024" --tasks gsm8k` ```bash |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 5|exact_match|↑ |0.9484|± |0.0061| | | |strict-match | 5|exact_match|↑ |0.9409|± |0.0065| ``` ### Perf `vllm bench serve --model $MODEL...

## 现有链接修复摘要

#30159 [Perf] Optimize `group_topk` kernel, 1.9% Throughput improvement, 2.1% TPOT improvemnt | #31754 [Perf] Optimize additional `fill(0)` in cutlass moe, 2.9% E2E throughput improvement, 10.8% TTFT improvement | #31830 [Perf] Optimize cutlass moe problem size calculation, 5.3% E2E Throughput improvement, 2.2% TTFT improvement | #32058 [Perf] Optimize grouped topk kernel, 1.2%~2% E2E Throughput improvement

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 8: ttps://github.com/vllm-project/vllm/pull/32273 ## Command used to check accuracy and benchmark `export MODEL="zai-org/GLM-4.7-FP8"` `vllm serve $MODEL -tp 8 --port 9256 --enable-expert-parallel --max_num_seqs 128` ### A...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 6: [Feature]: Optimizations for MOE models (GLM4.7, DeepSeek series) feature request ### 🚀 The feature, motivation and pitch [h100-tep8-glm4.7fp8.gz](https://github.com/user-attachments/files/24442034/h100-tep8-glm4.7fp8.g...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ure request ### 🚀 The feature, motivation and pitch [h100-tep8-glm4.7fp8.gz](https://github.com/user-attachments/files/24442034/h100-tep8-glm4.7fp8.gz) I am trying to optimize MOE models like GLM4.7 in vLLM, let's have...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: eek series) feature request ### 🚀 The feature, motivation and pitch [h100-tep8-glm4.7fp8.gz](https://github.com/user-attachments/files/24442034/h100-tep8-glm4.7fp8.gz) I am trying to optimize MOE models like GLM4.7 in v...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 6 but works for 4.7 as well) #30159 - [x] Optimize additional fill(0) in cutlass moe #31754 - [x] Optimize cutlass moe problem size calculation #31830 - [x] Optimize group topk kernel further #32058 - [x] Optimize the m...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#30159](https://github.com/vllm-project/vllm/pull/30159) | mentioned | 0.45 | [Perf] Optimize `group_topk` kernel, 1.9% Throughput improvement, 2.1% TPOT improvemnt | ] optimize grouped_topk kernel (for glm4.6 but works for 4.7 as well) #30159 - [x] optimize additional fill(0) in cutlass moe #31754 - [x] optimize cutlass moe problem size calcul… |
| [#31754](https://github.com/vllm-project/vllm/pull/31754) | mentioned | 0.45 | [Perf] Optimize additional `fill(0)` in cutlass moe, 2.9% E2E throughput improvement, 10.8% TTFT improvement | 4.7 as well) #30159 - [x] optimize additional fill(0) in cutlass moe #31754 - [x] optimize cutlass moe problem size calculation #31830 - [x] optimize group topk kernel further #32… |
| [#31830](https://github.com/vllm-project/vllm/pull/31830) | mentioned | 0.45 | [Perf] Optimize cutlass moe problem size calculation, 5.3% E2E Throughput improvement, 2.2% TTFT improvement | utlass moe #31754 - [x] optimize cutlass moe problem size calculation #31830 - [x] optimize group topk kernel further #32058 - [x] optimize the moe permute/unpermute kernel https:… |
| [#32058](https://github.com/vllm-project/vllm/pull/32058) | mentioned | 0.45 | [Perf] Optimize grouped topk kernel, 1.2%~2% E2E Throughput improvement | blem size calculation #31830 - [x] optimize group topk kernel further #32058 - [x] optimize the moe permute/unpermute kernel https://github.com/vllm-project/vllm/pull/32273 ## com… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
