# vllm-project/vllm#22862: [Bug]: Numerics of Embedding Models

| 字段 | 值 |
| --- | --- |
| Issue | [#22862](https://github.com/vllm-project/vllm/issues/22862) |
| 状态 | closed |
| 标签 | bug;help wanted;torch.compile |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 | precision |
| Operator 关键词 | attention |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Numerics of Embedding Models

### Issue 正文摘录

### Your current environment vLLM CI (L4) ### 🐛 Describe the bug We have been seeing some numerical differences in embedding models and have had to increase the tolerance in the CI recently (though locally on H100 machines we have not seen any issues) e.g. https://github.com/vllm-project/vllm/pull/22844 It would be great if someone could look into the source of these numerics and see if there is a recommended attention backend that can resolve the problem or if there is some other fundamental problem that we have with embedding models. Thanks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#26408 [CI] Pooling models mteb test disable enforce_eager

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Numerics of Embedding Models bug;help wanted;torch.compile ### Your current environment vLLM CI (L4) ### 🐛 Describe the bug We have been seeing some numerical differences in embedding models and have had to incre...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: Numerics of Embedding Models bug;help wanted;torch.compile ### Your current environment vLLM CI (L4) ### 🐛 Describe the bug We have been seeing some numerical differences in embedding models and have had to incre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: have had to increase the tolerance in the CI recently (though locally on H100 machines we have not seen any issues) e.g. https://github.com/vllm-project/vllm/pull/22844 It would be great if someone could look into the s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: the source of these numerics and see if there is a recommended attention backend that can resolve the problem or if there is some other fundamental problem that we have with embedding models. Thanks! ### Before submitti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Numerics of Embedding Models bug;help wanted;torch.compile ### Your current environment vLLM CI (L4) ### 🐛 Describe the bug We have been seeing some numerical differences in embedding models and have had to incre...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26408](https://github.com/vllm-project/vllm/pull/26408) | mentioned | 0.6 | [CI] Pooling models mteb test disable enforce_eager  | rpose Related to https://github.com/vllm-project/vllm/issues/22862 - #22862 (flaky test finded) - #22878 (uses enforce_eager) - #24088 (Since https://github.com/vllm-project/vllm/… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
