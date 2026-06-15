# vllm-project/vllm#18433: [Feature]: Create KVCacheManagerConfig

| 字段 | 值 |
| --- | --- |
| Issue | [#18433](https://github.com/vllm-project/vllm/issues/18433) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Create KVCacheManagerConfig

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm working on solving #14729 and am facing a problem. The way my solution works is I design a trie. When inserting a request into the trie, we get the request's KVCacheBlocks and go down the trie. We add new nodes to the trie if a request's current KVCacheBlock we are traversing is not in the trie. In this way, we can distinguish common prefixes between two requests. The problem I am facing is I need to pass a config related to this optimization (Forested Cascade Attention) into allocate_slots in class KVCacheManager. I want the config to be easily recoverable from the kv_cache_config attribute of KVCacheManager. However, this ForestedCascadeConfig is not at all related to KVCacheConfig. I propose creating a KVCacheConfigManager class as so: ``` class KVCacheManagerConfig: kv_cache_config: KVCacheConfig strategy_configs: dict[str, Any] = field(default_factory=dict) ``` This way, we can pass strategies like forested cascade attention to functions like allocate_slots without putting these unrelated configs in KVCacheConfig. ### Alternatives The alternative is to place ForestedCascadeConfig in KVCacheConfig. The problem with this is ForestedCa...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: rie. When inserting a request into the trie, we get the request's KVCacheBlocks and go down the trie. We add new nodes to the trie if a request's current KVCacheBlock we are traversing is not in the trie. In this way, w...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Create KVCacheManagerConfig feature request;stale ### 🚀 The feature, motivation and pitch I'm working on solving #14729 and am facing a problem. The way my solution works is I design a trie. When inserting a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he feature, motivation and pitch I'm working on solving #14729 and am facing a problem. The way my solution works is I design a trie. When inserting a request into the trie, we get the request's KVCacheBlocks and go dow...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Create KVCacheManagerConfig feature request;stale ### 🚀 The feature, motivation and pitch I'm working on solving #14729 and am facing a problem. The way my solution works is I design a trie. When inserting a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
