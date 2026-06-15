# vllm-project/vllm#37302: [Bug]: R1 NVFP4 gsm8k drop in lm_eval

| 字段 | 值 |
| --- | --- |
| Issue | [#37302](https://github.com/vllm-project/vllm/issues/37302) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;moe;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;kernel;moe |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: R1 NVFP4 gsm8k drop in lm_eval

### Issue 正文摘录

### Your current environment Prefill yaml: Decode yaml: ### 🐛 Describe the bug On NVL72, vllm hash `106ff69c4eb` and prior, `DeepSeek-R1-0528-FP4-v2`produces the following gsm8k lm_eval: ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 10|exact_match|↑ |0.9545|± |0.0057| | | |strict-match | 10|exact_match|↑ |0.9515|± |0.0059| ``` with FI `0.6.4` and the new FI a2a `--all2all-backend "flashinfer_nvlink_one_sided" ` and deepep LL with this DeepEP fork (https://github.com/elvircrn/DeepEP/commits/gb200_blog/). On `9c7cab5ebb0f8a15e632e7ea2cfeebcca1d3628f` I noticed a degradation in lm_eval gsm8k: ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-extract| 10|exact_match|↑ |0.9409|± |0.0065| | | |strict-match | 10|exact_match|↑ |0.9393|± |0.0066| ``` I ruled out FI 0.6.4 -> 0.6.6 upgrade on decode and prefill paths, so this does not explain this. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living...

## 现有链接修复摘要

#37217 [MoE/EPLB] Fix FlashInfer nvfp4 experts + EPLB correctness

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: eepSeek-R1-0528-FP4-v2`produces the following gsm8k lm_eval: ``` |Tasks|Version| Filter |n-shot| Metric | |Value | |Stderr| |-----|------:|----------------|-----:|-----------|---|-----:|---|-----:| |gsm8k| 3|flexible-ex...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: R1 NVFP4 gsm8k drop in lm_eval bug ### Your current environment Prefill yaml: Decode yaml: ### 🐛 Describe the bug On NVL72, vllm hash `106ff69c4eb` and prior, `DeepSeek-R1-0528-FP4-v2`produces the following gsm8k
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: R1 NVFP4 gsm8k drop in lm_eval bug ### Your current environment Prefill yaml: Decode yaml: ### 🐛 Describe the bug On NVL72, vllm hash `106ff69c4eb` and prior, `DeepSeek-R1-0528-FP4-v2`produces the following gsm8k...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: questions. performance attention_kv_cache;ci_build;distributed_parallel;model_support;moe;multimodal_vlm;quantization;scheduler_memory cuda;fp8;kernel;moe build_error;crash dtype;env_dependency;shape #37217 [MoE/EPLB] F...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: R1 NVFP4 gsm8k drop in lm_eval bug ### Your current environment Prefill yaml: Decode yaml: ### 🐛 Describe the bug On NVL72, vllm hash `106ff69c4eb` and prior, `DeepSeek-R1-0528-FP4-v2`produces the following gsm8k...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37217](https://github.com/vllm-project/vllm/pull/37217) | mentioned | 0.45 | [MoE/EPLB] Fix FlashInfer nvfp4 experts + EPLB correctness | cd /opt/vllm-source # revert eplb nvfp4 pr #37217 to test without it # image has a shallow clone with wrong remote; fetch full history from ups |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
