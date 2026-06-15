# vllm-project/vllm#2019: why online seving slower than offline serving??

| 字段 | 值 |
| --- | --- |
| Issue | [#2019](https://github.com/vllm-project/vllm/issues/2019) |
| 状态 | closed |
| 标签 |  |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support |
| 子分类 | throughput |
| Operator 关键词 | cache |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> why online seving slower than offline serving??

### Issue 正文摘录

1. offline serving ![image](https://github.com/vllm-project/vllm/assets/43260218/87e216b5-9064-4c2a-a021-cac08e22795d) 2. online serving(fastapi) ![image](https://github.com/vllm-project/vllm/assets/43260218/322cc4a4-a78f-4212-a266-d586e8e2969d) ![image](https://github.com/vllm-project/vllm/assets/43260218/49c9cf76-ca3f-4362-95d8-191cbbdd3543) log: INFO 12-11 21:50:36 llm_engine.py:649] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.4%, CPU KV cache usage: 0.0% INFO 12-11 21:50:41 async_llm_engine.py:111] Finished request 261ddff3312f44cd8ee1c52a6acd10e6. Why is the speed 2 seconds slower when displayed as fastapi?? parameters is same, prompt is same "Open-Orca/Mistral-7B-OpenOrca" this model same issue and any llama2 model same issue python : 3.10.12 [my library list.txt](https://github.com/vllm-project/vllm/files/13641002/my.library.list.txt) cuda_version : 12.0 gpu: a100 40g my library list attached

## 现有链接修复摘要

#41606 Bump the minor-update group across 1 directory with 140 updates | #41766 Bump the minor-update group across 1 directory with 141 updates | #41859 Bump the minor-update group across 1 directory with 141 updates | #42056 Bump the minor-update group across 1 directory with 142 updates | #42717 Bump the minor-update group across 1 directory with 143 updates | #43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: //github.com/vllm-project/vllm/files/13641002/my.library.list.txt) cuda_version : 12.0 gpu: a100 40g my library list attached performance attention_kv_cache;frontend_api;model_support cache slowdown env_dependency #4160...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ttps://github.com/vllm-project/vllm/files/13641002/my.library.list.txt) cuda_version : 12.0 gpu: a100 40g my library list attached performance attention_kv_cache;frontend_api;model_support cache slowdown env_dependency...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: parameters is same, prompt is same "Open-Orca/Mistral-7B-OpenOrca" this model same issue and any llama2 model same issue python : 3.10.12 [my library list.txt](https://github.com/vllm-project/vllm/files/13641002/my.libr...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ut: 0.0 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.4%, CPU KV cache usage: 0.0% INFO 12-11 21:50:41 async_llm_engine.py:111] Finished request 261ddff3312f44cd8ee1c52a6acd10e6. Why...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: cache usage: 0.0% INFO 12-11 21:50:41 async_llm_engine.py:111] Finished request 261ddff3312f44cd8ee1c52a6acd10e6. Why is the speed 2 seconds slower when displayed as fastapi?? parameters is same, prompt is same "Open-Or...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41606](https://github.com/vllm-project/vllm/pull/41606) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 140 updates | href="https://redirect.github.com/huggingface/tokenizers/issues/2019">#2019</a>)</li> <li>Additional commits viewable in <a href="https://github.com/huggingface/tokenizers/compare… |
| [#41766](https://github.com/vllm-project/vllm/pull/41766) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | href="https://redirect.github.com/huggingface/tokenizers/issues/2019">#2019</a>)</li> <li>Additional commits viewable in <a href="https://github.com/huggingface/tokenizers/compare… |
| [#41859](https://github.com/vllm-project/vllm/pull/41859) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 141 updates | href="https://redirect.github.com/huggingface/tokenizers/issues/2019">#2019</a>)</li> <li>Additional commits viewable in <a href="https://github.com/huggingface/tokenizers/compare… |
| [#42056](https://github.com/vllm-project/vllm/pull/42056) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 142 updates | href="https://redirect.github.com/huggingface/tokenizers/issues/2019">#2019</a>)</li> <li>Additional commits viewable in <a href="https://github.com/huggingface/tokenizers/compare… |
| [#42717](https://github.com/vllm-project/vllm/pull/42717) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 143 updates | href="https://redirect.github.com/huggingface/tokenizers/issues/2019">#2019</a>)</li> <li>Additional commits viewable in <a href="https://github.com/huggingface/tokenizers/compare… |
| [#43505](https://github.com/vllm-project/vllm/pull/43505) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 145 updates | href="https://redirect.github.com/huggingface/tokenizers/issues/2019">#2019</a>)</li> <li>Additional commits viewable in <a href="https://github.com/huggingface/tokenizers/compare… |
| [#43993](https://github.com/vllm-project/vllm/pull/43993) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 147 updates | href="https://redirect.github.com/huggingface/tokenizers/issues/2019">#2019</a>)</li> <li>Additional commits viewable in <a href="https://github.com/huggingface/tokenizers/compare… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
