# vllm-project/vllm#31145: [Bug]: [P/D] multi-connector cannot be used together with P2pNcclConnector that uses a put mode(push kv cache from P node to D node)

| 字段 | 值 |
| --- | --- |
| Issue | [#31145](https://github.com/vllm-project/vllm/issues/31145) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [P/D] multi-connector cannot be used together with P2pNcclConnector that uses a put mode(push kv cache from P node to D node)

### Issue 正文摘录

### fixpr https://github.com/vllm-project/vllm/pull/31144 ### Your current environment ### 🐛 Describe the bug ```python def get_num_new_matched_tokens( self, request: "Request", num_computed_tokens: int, ) -> tuple[int | None, bool]: to_return = (0, False) for i, c in enumerate(self._connectors): toks, load_async = c.get_num_new_matched_tokens( request, num_computed_tokens ) # If there is a connector still looking up the matches, # we return None to indicate that we are not done yet. if toks is None: return (None, False) # The first connector that has new matched tokens will be assigned # to this request. if to_return[0] == 0 and toks > 0: self._requests_to_connector[request.request_id] = i to_return = (toks, load_async) return to_return def update_state_after_alloc( self, request: "Request", blocks: "KVCacheBlocks", num_external_tokens: int ): chosen_connector = self._requests_to_connector.get(request.request_id, -1) empty_blocks = blocks.new_empty() for i, c in enumerate(self._connectors): if i == chosen_connector: # Forward call to the chosen connector (if any). c.update_state_after_alloc(request, blocks, num_external_tokens) else: # Call with empty blocks for other connectors....

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: tokens: int, ) -> tuple[int | None, bool]: to_return = (0, False) for i, c in enumerate(self._connectors): toks, load_async = c.get_num_new_matched_tokens( request, num_computed_tokens ) # If there is a connector still...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: lConnector that uses a put mode(push kv cache from P node to D node) bug;stale ### fixpr https://github.com/vllm-project/vllm/pull/31144 ### Your current environment ### 🐛 Describe the bug ```python def get_num_new_matc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: cannot be used together with P2pNcclConnector that uses a put mode(push kv cache from P node to D node) bug;stale ### fixpr https://github.com/vllm-project/vllm/pull/31144 ### Your current environment ### 🐛 Describe the...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Ds and causing the push KV cache operation to fail.** ``` --kv-transfer-config '{"kv_connector":"MultiConnector","kv_role":"kv_both","kv_connector_extra_config":{"connectors":[{"kv_connector":"P2pNcclConnector","kv_role...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
