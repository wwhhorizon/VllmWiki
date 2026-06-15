# vllm-project/vllm#20252: [Bug]: [xPyD][main_br] [1p1d with vllm qwen2.5vl_7b]: dst_kv_cache_layer[:, slot_mapping, ...] = src_kv_cache ; RuntimeError: CUDA error: device-side assert triggered

| 字段 | 值 |
| --- | --- |
| Issue | [#20252](https://github.com/vllm-project/vllm/issues/20252) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [xPyD][main_br] [1p1d with vllm qwen2.5vl_7b]: dst_kv_cache_layer[:, slot_mapping, ...] = src_kv_cache ; RuntimeError: CUDA error: device-side assert triggered

### Issue 正文摘录

### Your current environment main branch build from src codes ## main error log ```text PrefixCacheStats(reset=False, requests=1, queries=1977, hits=1968), spec_decoding_stats=None, num_corrupted_reqs=0) ERROR 06-30 04:45:12 [core.py:521] EngineCore encountered a fatal error. ERROR 06-30 04:45:12 [core.py:521] Traceback (most recent call last): ERROR 06-30 04:45:12 [core.py:521] File "/juicefs-algorithm/workspace/vision/yongshuai_wang/codes/gitlab/vllm_debug/package/vllm-main_0526/vllm/v1/engine/core.py", line 512, in run_engine_core ERROR 06-30 04:45:12 [core.py:521] engine_core.run_busy_loop() ERROR 06-30 04:45:12 [core.py:521] File "/juicefs-algorithm/workspace/vision/yongshuai_wang/codes/gitlab/vllm_debug/package/vllm-main_0526/vllm/v1/engine/core.py", line 539, in run_busy_loop ERROR 06-30 04:45:12 [core.py:521] self._process_engine_step() ERROR 06-30 04:45:12 [core.py:521] File "/juicefs-algorithm/workspace/vision/yongshuai_wang/codes/gitlab/vllm_debug/package/vllm-main_0526/vllm/v1/engine/core.py", line 564, in _process_engine_step ERROR 06-30 04:45:12 [core.py:521] outputs, model_executed = self.step_fn() ERROR 06-30 04:45:12 [core.py:521] ^^^^^^^^^^^^^^ ERROR 06-30 04:45:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: side assert triggered bug;stale ### Your current environment main branch build from src codes ## main error log ```text PrefixCacheStats(reset=False, requests=1, queries=1977, hits=1968), spec_decoding_stats=None, num_c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: g]: [xPyD][main_br] [1p1d with vllm qwen2.5vl_7b]: dst_kv_cache_layer[:, slot_mapping, ...] = src_kv_cache ; RuntimeError: CUDA error: device-side assert triggered bug;stale ### Your current environment main branch buil...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: rc_kv_cache ; RuntimeError: CUDA error: device-side assert triggered bug;stale ### Your current environment main branch build from src codes ## main error log ```text PrefixCacheStats(reset=False, requests=1, queries=19...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: dst_kv_cache_layer[:, slot_mapping, ...] = src_kv_cache ; RuntimeError: CUDA error: device-side assert triggered bug;stale ### Your current environment main branch build from src codes ## main error log ```text PrefixCa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: [xPyD][main_br] [1p1d with vllm qwen2.5vl_7b]: dst_kv_cache_layer[:, slot_mapping, ...] = src_kv_cache ; RuntimeError: CUDA error: device-side assert triggered bug;stale ### Your current environment main branch b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
