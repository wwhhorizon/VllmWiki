# vllm-project/vllm#21141: [Performance]: Opportunities to speed up BlockPool processing

| 字段 | 值 |
| --- | --- |
| Issue | [#21141](https://github.com/vllm-project/vllm/issues/21141) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Opportunities to speed up BlockPool processing

### Issue 正文摘录

### Proposal to improve performance # Observations The trace under block_pool.get_new_blocks seems quite fragmented. And we do see some optimization chances there. - https://github.com/vllm-project/vllm/pull/21005 - [x] Avoid __eq__ invocation against KVCacheBlock dataclass - [WIP] https://github.com/vllm-project/vllm/pull/21222 - [ ] Introduce buck append and buck popleft to avoid unnecessary linked list operations - [ ] Avoid incr_ref function invocations - [ ] Avoid self.enable_caching check in the inner for loop # Reproduce ``` export VLLM_USE_MODELSCOPE=False; export VLLM_TORCH_PROFILER_DIR=~/vllm_profile; # for profiling vllm serve facebook/opt-125m \ --swap-space 16 \ --disable-log-requests \ --no-enable-prefix-caching \ --host :: \ --dtype float16 export VLLM_TORCH_PROFILER_DIR=~/vllm_profile; # for profiling vllm bench serve \ --dataset-name random \ --model facebook/opt-125m \ --served-model-name facebook/opt-125m \ --random-input-len 700 \ --random-output-len 1 \ --endpoint /v1/completions \ --ignore-eos \ --host localhost \ --port 8000 \ --request-rate 200 \ --num-prompts 100 \ --profile ``` ### Report of performance regression N/A ### Misc discussion on performance N/...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: # Reproduce ``` export VLLM_USE_MODELSCOPE=False; export VLLM_TORCH_PROFILER_DIR=~/vllm_profile; # for profiling vllm serve facebook/opt-125m \ --swap-space 16 \ --disable-log-requests \ --no-enable-prefix-caching \ --h...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: le-log-requests \ --no-enable-prefix-caching \ --host :: \ --dtype float16 export VLLM_TORCH_PROFILER_DIR=~/vllm_profile; # for profiling vllm bench serve \ --dataset-name random \ --model facebook/opt-125m \ --served-m...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Performance]: Opportunities to speed up BlockPool processing performance;stale ### Proposal to improve performance # Observations The trace under block_pool.get_new_blocks seems quite fragmented. And we do see some opt...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Performance]: Opportunities to speed up BlockPool processing performance;stale ### Proposal to improve performance # Observations The trace under block_pool.get_new_blocks seems quite fragmented. And we do see some opti...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ions - [ ] Avoid self.enable_caching check in the inner for loop # Reproduce ``` export VLLM_USE_MODELSCOPE=False; export VLLM_TORCH_PROFILER_DIR=~/vllm_profile; # for profiling vllm serve facebook/opt-125m \ --swap-spa...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
