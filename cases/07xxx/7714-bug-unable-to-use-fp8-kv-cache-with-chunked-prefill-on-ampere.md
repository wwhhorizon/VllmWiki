# vllm-project/vllm#7714: [Bug]: Unable to use fp8 kv cache with chunked prefill on ampere

| 字段 | 值 |
| --- | --- |
| Issue | [#7714](https://github.com/vllm-project/vllm/issues/7714) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to use fp8 kv cache with chunked prefill on ampere

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running the nightly pip, pulled 9:00 PM EST 8/20/24. Running under docker image 0.5.4. I also tested the same commands under normal 0.5.4. ``` python3 -m vllm.entrypoints.openai.api_server --model /home/ndurkee/Meta-Llama-3.1-70B-Instruct-quantized.w8a16 -tp 8 --gpu-memory-utilization 0.995 --dtype auto --distributed-executor-backend mp --max-model-len 40000 --kv-cache-dtype fp8 ``` This is the model I am using https://huggingface.co/neuralmagic/Meta-Llama-3-70B-Instruct-quantized.w8a16 It also fails with https://huggingface.co/neuralmagic/Meta-Llama-3.1-70B-Instruct-FP8 ``` (VllmWorkerProcess pid=4055) ERROR 08-21 01:06:31 multiproc_worker_utils.py:226] Exception in worker VllmWorkerProcess while processing method start_worker_execution_loop: at 110:17: (VllmWorkerProcess pid=4055) ERROR 08-21 01:06:31 multiproc_worker_utils.py:226] cur_kv_head * stride_k_cache_h + (VllmWorkerProcess pid=4055) ERROR 08-21 01:06:31 multiproc_worker_utils.py:226] (offs_d[:, None] // x) * stride_k_cache_d + (VllmWorkerProcess pid=4055) ERROR 08-21 01:06:31 multiproc_worker_utils.py:226] ((start_n + offs_n[None, :]) % block_size) * (VllmWorkerP...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: I am running the nightly pip, pulled 9:00 PM EST 8/20/24. Running under docker image 0.5.4. I also tested the same commands under normal 0.5.4. ``` python3 -m vllm.entrypoints.openai.api_server --model /home/ndurkee/Met...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Unable to use fp8 kv cache with chunked prefill on ampere bug;stale ### Your current environment ### 🐛 Describe the bug I am running the nightly pip, pulled 9:00 PM EST 8/20/24. Running under docker image 0.5.4....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Unable to use fp8 kv cache with chunked prefill on ampere bug;stale ### Your current environment ### 🐛 Describe the bug I am running the nightly pip, pulled 9:00 PM EST 8/20/24. Running under docker image 0.5.4....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: under normal 0.5.4. ``` python3 -m vllm.entrypoints.openai.api_server --model /home/ndurkee/Meta-Llama-3.1-70B-Instruct-quantized.w8a16 -tp 8 --gpu-memory-utilization 0.995 --dtype auto --distributed-executor-backend mp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Unable to use fp8 kv cache with chunked prefill on ampere bug;stale ### Your current environment ### 🐛 Describe the bug I am running the nightly pip, pulled 9:00 PM EST 8/20/24. Running under docker image 0.5.4....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
