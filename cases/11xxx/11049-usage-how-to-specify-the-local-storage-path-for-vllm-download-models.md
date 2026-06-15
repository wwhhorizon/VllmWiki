# vllm-project/vllm#11049: [Usage]: How to specify the local storage path for vllm download models？

| 字段 | 值 |
| --- | --- |
| Issue | [#11049](https://github.com/vllm-project/vllm/issues/11049) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to specify the local storage path for vllm download models？

### Issue 正文摘录

### Your current environment How to specify the local storage path for vllm download models? I have made the following attempts but none of them are effective. VLLM always stores the model in the directory “~/. cache/hug”. ﻿ 1. Set the environment variable VLLM_CACHE_ROOT. 2. Set the environment variable HF_HUB_CACHE. 3. When using the function LLM to load models, set its argument "hf_overrides" as {"cache_dir": "xxx"}. ﻿ I would be greatly grateful if someone could help me with this issue. ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to specify the local storage path for vllm download models？ usage ### Your current environment How to specify the local storage path for vllm download models? I have made the following attempts but none of...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: How to specify the local storage path for vllm download models？ usage ### Your current environment How to specify the local storage path for vllm download models? I have made the following attempts but none of...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
