# vllm-project/vllm#10685: [Bug]: AssertError when testing VLLM performance with preempt mode set to "swap" and VLLM_TEST_ENABLE_ARTIFICIAL_PREEMPT=1

| 字段 | 值 |
| --- | --- |
| Issue | [#10685](https://github.com/vllm-project/vllm/issues/10685) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AssertError when testing VLLM performance with preempt mode set to "swap" and VLLM_TEST_ENABLE_ARTIFICIAL_PREEMPT=1

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When setting the environment variable `VLLM_TEST_ENABLE_ARTIFICIAL_PREEMPT` on the server and enabling the swap preemption mode, running the `benchmarks/benchmark_serving.py` script to test the performance of VLLM triggers an AssertionError. Steps to Reproduce: Client-side: ``` python benchmark_serving.py --model Qwen2.5-7B-Instruct --request-rate 2 --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json --disable-tqdm ``` Server-side: ``` export VLLM_TEST_ENABLE_ARTIFICIAL_PREEMPT=1 vllm serve Qwen2.5-7B-Instruct \ --block-size 32 \ --dtype float16 \ --preemption-mode swap \ --disable-log-requests \ --max-model-len 1024 \ --max_num_batched_tokens 10000 \ --gpu-memory-utilization 0.9 ``` Server-side error: ``` WARNING 11-27 02:04:48 scheduler.py:1481] Sequence group cmpl-f5a99b8801444ad19f63a764ebb493b7-0 is preempted by PreemptionMode.SWAP mode because there is not enough KV cache space. This can affect the end-to-end performance. Increase gpu_memory_utilization or tensor_parallel_size to provide more KV cache memory. total_num_cumulative_preemption=1 ERROR 11-27 02:04:48 engine.py:135] Asser...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: preempt mode set to "swap" and VLLM_TEST_ENABLE_ARTIFICIAL_PREEMPT=1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When setting the environment variable `VLLM_TEST_ENA...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: inamoto/miniconda3/envs/vllm_main/lib/python3.10/site-packages/starlette/routing.py", line 715, in __call__ await self.middleware_stack(scope, receive, send) File "/home/minamoto/miniconda3/envs/vllm_main/lib/python3.10...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: M performance with preempt mode set to "swap" and VLLM_TEST_ENABLE_ARTIFICIAL_PREEMPT=1 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When setting the environment vari...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: _TEST_ENABLE_ARTIFICIAL_PREEMPT=1 vllm serve Qwen2.5-7B-Instruct \ --block-size 32 \ --dtype float16 \ --preemption-mode swap \ --disable-log-requests \ --max-model-len 1024 \ --max_num_batched_tokens 10000 \ --gpu-memo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: L_PREEMPT=1 vllm serve Qwen2.5-7B-Instruct \ --block-size 32 \ --dtype float16 \ --preemption-mode swap \ --disable-log-requests \ --max-model-len 1024 \ --max_num_batched_tokens 10000 \ --gpu-memory-utilization 0.9 ```...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
