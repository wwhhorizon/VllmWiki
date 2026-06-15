# vllm-project/vllm#28726: [Bug]: Unbounded CPU Memory Growth When Using Prefix Caching

| 字段 | 值 |
| --- | --- |
| Issue | [#28726](https://github.com/vllm-project/vllm/issues/28726) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unbounded CPU Memory Growth When Using Prefix Caching

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello! First of all, thank you for the awesome work you’ve done 🙏 While using online serving with the qwen2-VL-2b model, I noticed that CPU memory usage kept increasing over time. Even when no new requests were coming in, the memory was not released, eventually causing the server to restart. After some investigation, I found the previous memory-leak issues related to multimodal input processor caching. I tried disabling that cache, but the issue persisted. Only after disabling `prefix caching` did CPU memory remain stable. Is there a way to limit the amount of memory allocated to these caches (similar to `VLLM_MM_INPUT_CACHE_GIB`)? Or perhaps configure a maximum lifetime for cached entries? Thanks again for all your great work! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#34183 [Bugfix][Core] Fix CPU memory leak from Request reference cycle in prefix caching

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: for the awesome work you’ve done 🙏 While using online serving with the qwen2-VL-2b model, I noticed that CPU memory usage kept increasing over time. Even when no new requests were coming in, the memory was not released,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampli...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rk! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: oticed that CPU memory usage kept increasing over time. Even when no new requests were coming in, the memory was not released, eventually causing the server to restart. After some investigation, I found the previous mem...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ltimodal_vlm;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency #34183 [Bugfix][Core] Fix CPU memory leak from Request reference cycle in prefix caching Your current en...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34183](https://github.com/vllm-project/vllm/pull/34183) | closes_keyword | 0.95 | [Bugfix][Core] Fix CPU memory leak from Request reference cycle in prefix caching | FIXES #28726 #24964 #27896 Introduced a change so that each request cycle creates fewer GC-tracked objects and overall there are less frequent gen-2 collections. While this is |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
