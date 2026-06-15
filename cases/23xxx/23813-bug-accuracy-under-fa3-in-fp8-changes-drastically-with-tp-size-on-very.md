# vllm-project/vllm#23813: [Bug]: Accuracy under FA3 in FP8 changes drastically with TP size on very long context length

| 字段 | 值 |
| --- | --- |
| Issue | [#23813](https://github.com/vllm-project/vllm/issues/23813) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Accuracy under FA3 in FP8 changes drastically with TP size on very long context length

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Model = Llama-3.1-8B-Instruct (in BF16) Setup = FP8 KV-cache quantization with FA3 Evaluation = long context RULER at 128k length, and NIAH task Problem = accuracy changes drastically (by ~40 points) by just changing TP size 1st row = baseline model without KV-cache quantization 2nd row = with FP8 KV-cache (scales calc disabled) 3rd row = with FP8 KV-cache (scales calc enabled) 1st column = eval accuracy on NIAH task under TP=1 2nd column = eval accuracy on NIAH task under TP=8 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: Accuracy under FA3 in FP8 changes drastically with TP size on very long context length bug ### Your current environment ### 🐛 Describe the bug Model = Llama-3.1-8B-Instruct (in BF16) Setup = FP8 KV-cache quantiza...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Accuracy under FA3 in FP8 changes drastically with TP size on very long context length bug ### Your current environment ### 🐛 Describe the bug Model = Llama-3.1-8B-Instruct (in BF16) Setup = FP8 KV-cache quantiza...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;quantization;samp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Accuracy under FA3 in FP8 changes drastically with TP size on very long context length bug ### Your current environment ### 🐛 Describe the bug Model = Llama-3.1-8B-Instruct (in BF16) Setup = FP8 KV-cache quantiza...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | el: NO (0 matches) #23814: Should have ROCm label: NO (0 matches) #23813: Should have ROCm label: NO (0 matches) #23805: Should have ROCm label: NO (0 matches) #23804: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
