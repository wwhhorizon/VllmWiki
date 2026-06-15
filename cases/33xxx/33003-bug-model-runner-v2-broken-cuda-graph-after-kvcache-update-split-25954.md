# vllm-project/vllm#33003: [Bug]: Model Runner V2 broken CUDA Graph after kvcache update split(#25954)

| 字段 | 值 |
| --- | --- |
| Issue | [#33003](https://github.com/vllm-project/vllm/issues/33003) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention;cache;cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Model Runner V2 broken CUDA Graph after kvcache update split(#25954)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Content **Description** After PR #25954 ([Performance] Split FlashAttn attention and cache update), Model Runner V2 with FLASH_ATTN backend and CUDA graph enabled is broken with two `AttributeError` issues. **Bug 1: Missing `block_tables` attribute during profile run** ``` File "/mnt/debugger/zhr/vllm_official/vllm/v1/engine/core.py", line 112, in __init__ num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/mnt/debugger/zhr/vllm_official/vllm/v1/engine/core.py", line 242, in _initialize_kv_caches available_gpu_memory = self.model_executor.determine_available_memory() ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ... File "/mnt/debugger/zhr/vllm_official/vllm/v1/worker/gpu/model_runner.py", line 336, in profile_run hidden_states, sample_hidden_states = self._dummy_run( File "/mnt/debugger/zhr/vllm_official/vllm/v1/worker/gpu/model_runner.py", line 310, in _dummy_run self.execute_model( File "/mnt/debugger/zhr/vllm_official/vllm/v1/worker/gpu/model_runner.py", line 885, in execute_model slot_mappings = self.block_tables.compute_slot_mappings( ^^^^^^^^^^^^^^^^^ Attri...

## 现有链接修复摘要

#25954 [Performance] Split FlashAttn attention and cache update

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: h enabled is broken with two `AttributeError` issues. **Bug 1: Missing `block_tables` attribute during profile run** ``` File "/mnt/debugger/zhr/vllm_official/vllm/v1/engine/core.py", line 112, in __init__ num_gpu_block...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: re_model() File "/mnt/debugger/zhr/vllm_official/vllm/v1/worker/gpu/spec_decode/eagle.py", line 178, in capture_model self.cudagraph_manager.capture() ··· File "/mnt/debugger/zhr/vllm_official/vllm/v1/worker/gpu/spec_de...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: es` attribute during profile run** ``` File "/mnt/debugger/zhr/vllm_official/vllm/v1/engine/core.py", line 112, in __init__ num_gpu_blocks, num_cpu_blocks, kv_cache_config = self._initialize_kv_caches( ^^^^^^^^^^^^^^^^^...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Model Runner V2 broken CUDA Graph after kvcache update split(#25954) bug ### Your current environment ### 🐛 Describe the bug ## Content **Description** After PR #25954 ([Performance] Split FlashAttn attention and...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Model Runner V2 broken CUDA Graph after kvcache update split(#25954) bug ### Your current environment ### 🐛 Describe the bug ## Content **Description** After PR #25954 ([Performance] Split FlashAttn attention and

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#25954](https://github.com/vllm-project/vllm/pull/25954) | mentioned | 0.45 | [Performance] Split FlashAttn attention and cache update | ls> ### 🐛 describe the bug ## content **description** after pr #25954 ([performance] split flashattn attention and cache update), model runner v2 with flash_attn backend and cuda |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
