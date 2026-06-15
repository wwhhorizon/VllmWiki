# vllm-project/vllm#21140: [Performance]: Reduce overhead of FreeKVCacheBlockQueue

| 字段 | 值 |
| --- | --- |
| Issue | [#21140](https://github.com/vllm-project/vllm/issues/21140) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Reduce overhead of FreeKVCacheBlockQueue

### Issue 正文摘录

### Proposal to improve performance # Observations The trace under block_pool.get_new_blocks seems quite fragmented. And we do see some optimization chances there. - [ ] WIP: Avoid __eq__ invocation against KVCacheBlock (https://github.com/vllm-project/vllm/pull/21005) - [ ] Avoid incr_ref function invocations - [ ] Avoid self.enable_caching check inside the for loop # Reproduce ``` export VLLM_USE_MODELSCOPE=False; export VLLM_TORCH_PROFILER_DIR=~/vllm_profile; # for profiling vllm serve facebook/opt-125m \ --swap-space 16 \ --disable-log-requests \ --no-enable-prefix-caching \ --host :: \ --dtype float16 export VLLM_TORCH_PROFILER_DIR=~/vllm_profile; # for profiling vllm bench serve \ --dataset-name random \ --model facebook/opt-125m \ --served-model-name facebook/opt-125m \ --random-input-len 700 \ --random-output-len 1 \ --endpoint /v1/completions \ --ignore-eos \ --host localhost \ --port 8000 \ --request-rate 200 \ --num-prompts 100 \ --profile ``` ### Report of performance regression N/A ### Misc discussion on performance N/A ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` N/A ### Before submitting a new issue......

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: # Reproduce ``` export VLLM_USE_MODELSCOPE=False; export VLLM_TORCH_PROFILER_DIR=~/vllm_profile; # for profiling vllm serve facebook/opt-125m \ --swap-space 16 \ --disable-log-requests \ --no-enable-prefix-caching \ --h...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: le-log-requests \ --no-enable-prefix-caching \ --host :: \ --dtype float16 export VLLM_TORCH_PROFILER_DIR=~/vllm_profile; # for profiling vllm bench serve \ --dataset-name random \ --model facebook/opt-125m \ --served-m...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Performance]: Reduce overhead of FreeKVCacheBlockQueue performance ### Proposal to improve performance # Observations The trace under block_pool.get_new_blocks seems quite fragmented. And we do see some optimization ch...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Reduce overhead of FreeKVCacheBlockQueue performance ### Proposal to improve performance # Observations The trace under block_pool.get_new_blocks seems quite fragmented. And we do see some optimization ch...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ocations - [ ] Avoid self.enable_caching check inside the for loop # Reproduce ``` export VLLM_USE_MODELSCOPE=False; export VLLM_TORCH_PROFILER_DIR=~/vllm_profile; # for profiling vllm serve facebook/opt-125m \ --swap-s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
