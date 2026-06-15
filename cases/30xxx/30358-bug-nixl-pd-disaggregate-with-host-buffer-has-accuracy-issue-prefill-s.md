# vllm-project/vllm#30358: [Bug]: NIXL PD disaggregate with host_buffer has accuracy issue - Prefill scheduled num_block mismatch at update_state_after_alloc and request_finished

| 字段 | 值 |
| --- | --- |
| Issue | [#30358](https://github.com/vllm-project/vllm/issues/30358) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: NIXL PD disaggregate with host_buffer has accuracy issue - Prefill scheduled num_block mismatch at update_state_after_alloc and request_finished

### Issue 正文摘录

### Your current environment vllm-commit-id: 73a484caa1ad320d6e695f098c25c479a71e6774 Tested with A100 ### 🐛 Describe the bug How to reproduce ``` PREFILL_BLOCK_SIZE=16 DECODE_BLOCK_SIZE=16 bash tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh --kv_buffer_device cpu ``` accuracy is ~0.3 much lower than expected 0.4 with Qwen0.6 --- What is the issue I found that the num_blocks sent to `update_state_after_alloc` and `request_finished` sometimes is not match. `update_state_after_alloc` => this function is scheduled by `scheduler.schedule` to update req_to_save and req_to_receive list, and block_ids passed by the method will indicate which blocks belong to one request. `request_finished` => this function is called also in `scheduler._connector_finished` to send completed request block_ids list to create a new metadata for decoder. However, based print logs, sometimes, block_ids in `scheduler.schedule` `update_state_after_alloc` is shorter than `scheduler._connector_finished` `request_finished` sometimes. Example as below ``` 📊 Found 1320 unique Request IDs. FINAL SUMMARY ✅ Consistent Requests : 1085 => num_blocks are same at `update_state_after_alloc` and `request_finished...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: NIXL PD disaggregate with host_buffer has accuracy issue - Prefill scheduled num_block mismatch at update_state_after_alloc and request_finished bug;stale ### Your current environment vllm-commit-id: 73a484caa1ad...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: [Bug]: NIXL PD disaggregate with host_buffer has accuracy issue - Prefill scheduled num_block mismatch at update_state_after_alloc and request_finished bug;stale ### Your current environment vllm-commit-id: 73a484caa1ad...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: gate with host_buffer has accuracy issue - Prefill scheduled num_block mismatch at update_state_after_alloc and request_finished bug;stale ### Your current environment vllm-commit-id: 73a484caa1ad320d6e695f098c25c479a71...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: disaggregate with host_buffer has accuracy issue - Prefill scheduled num_block mismatch at update_state_after_alloc and request_finished bug;stale ### Your current environment vllm-commit-id: 73a484caa1ad320d6e695f098c2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: NIXL PD disaggregate with host_buffer has accuracy issue - Prefill scheduled num_block mismatch at update_state_after_alloc and request_finished bug;stale ### Your current environment vllm-commit-id: 73a484caa1ad...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
