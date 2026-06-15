# vllm-project/vllm#28661: [Bug]: NIXL `run_accuracy_test.sh` is broken for `block_size=128`

| 字段 | 值 |
| --- | --- |
| Issue | [#28661](https://github.com/vllm-project/vllm/issues/28661) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: NIXL `run_accuracy_test.sh` is broken for `block_size=128`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug NIXL lm-eval run test (`run_accuracy_test.sh`) is broken on main and likely has been for some commits. To repro, apply block_size=128 "patch" to run_accuracy_test.sh and limit lm-eval to 10 example for speed ``` diff --git a/tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh b/tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh index a9817313c..571eb4966 100755 --- a/tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh +++ b/tests/v1/kv_connector/nixl_integration/run_accuracy_test.sh @@ -132,10 +132,12 @@ run_tests_for_model() { BASE_CMD="CUDA_VISIBLE_DEVICES=$GPU_ID \ VLLM_KV_CACHE_LAYOUT='HND' \ UCX_NET_DEVICES=all \ + VLLM_LOGGING_LEVEL="DEBUG" \ VLLM_NIXL_SIDE_CHANNEL_PORT=$SIDE_CHANNEL_PORT \ vllm serve $model_name \ --port $PORT \ --enforce-eager \ + --block-size 128 \ --gpu-memory-utilization $GPU_MEMORY_UTILIZATION \ --tensor-parallel-size $PREFILLER_TP_SIZE \ --kv-transfer-config '$KV_CONFIG'" @@ -173,10 +175,12 @@ run_tests_for_model() { BASE_CMD="CUDA_VISIBLE_DEVICES=$GPU_ID \ VLLM_KV_CACHE_LAYOUT=$DECODER_KV_LAYOUT \ UCX_NET_DEVICES=all \ + VLLM_LOGGING_LEVEL="DEBUG" \ VLLM_NIXL_SIDE_CHANNEL_PO...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: NIXL `run_accuracy_test.sh` is broken for `block_size=128` bug ### Your current environment ### 🐛 Describe the bug NIXL lm-eval run test (`run_accuracy_test.sh`) is broken on main and likely has been for some com...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: NIXL `run_accuracy_test.sh` is broken for `block_size=128` bug ### Your current environment ### 🐛 Describe the bug NIXL lm-eval run test (`run_accuracy_test.sh`) is broken on main and likely has been for some com...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ixl_integration/run_accuracy_test.sh @@ -132,10 +132,12 @@ run_tests_for_model() { BASE_CMD="CUDA_VISIBLE_DEVICES=$GPU_ID \ VLLM_KV_CACHE_LAYOUT='HND' \ UCX_NET_DEVICES=all \ + VLLM_LOGGING_LEVEL="DEBUG" \ VLLM_NIXL_SID...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: emory-utilization $GPU_MEMORY_UTILIZATION \ --tensor-parallel-size $PREFILLER_TP_SIZE \ --kv-transfer-config '$KV_CONFIG'" @@ -173,10 +175,12 @@ run_tests_for_model() { BASE_CMD="CUDA_VISIBLE_DEVICES=$GPU_ID \ VLLM_KV_C...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: NIXL `run_accuracy_test.sh` is broken for `block_size=128` bug ### Your current environment ### 🐛 Describe the bug NIXL lm-eval run test (`run_accuracy_test.sh`) is broken on main and likely has been for some com...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
