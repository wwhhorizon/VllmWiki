# vllm-project/vllm#11562: [Bug]: assert total_num_scheduled_tokens > 0

| 字段 | 值 |
| --- | --- |
| Issue | [#11562](https://github.com/vllm-project/vllm/issues/11562) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: assert total_num_scheduled_tokens > 0

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ![image](https://github.com/user-attachments/assets/a9a50164-579c-4bc9-9a1b-6b5cca5f055e) When V1 and prefix_caching are enabled, when allocating slots for requests in the waiting queue, the function immediately _touch(computed_blocks) at the beginning, incrementing their ref_cnt by 1. If free_block_queue.num_free_blocks is insufficient to allocate new blocks, the function returns None, causing the scheduling loop to break directly. At this point, the request remains in the waiting queue, but the ref_cnt of all blocks in computed_blocks has been incremented. This situation recurs, eventually leading to some blocks having a ref_cnt greater than 0 even though no request is using them. ```python # ===============scheduler request = self.waiting[0] computed_blocks = self.kv_cache_manager.get_computed_blocks( request) ...... new_blocks = self.kv_cache_manager.allocate_slots( request, num_new_tokens, computed_blocks) if new_blocks is None: break self.waiting.popleft() #================kv_cache_manager def allocate_slots( self, request: Request, num_tokens: int, computed_blocks: List[KVCacheBlock], )...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: 055e) When V1 and prefix_caching are enabled, when allocating slots for requests in the waiting queue, the function immediately _touch(computed_blocks) at the beginning, incrementing their ref_cnt by 1. If free_block_qu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: b-6b5cca5f055e) When V1 and prefix_caching are enabled, when allocating slots for requests in the waiting queue, the function immediately _touch(computed_blocks) at the beginning, incrementing their ref_cnt by 1. If fre...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: enting their ref_cnt by 1. If free_block_queue.num_free_blocks is insufficient to allocate new blocks, the function returns None, causing the scheduling loop to break directly. At this point, the request remains in the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;scheduler_memory;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency;memory_layout Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
