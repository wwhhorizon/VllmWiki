# vllm-project/vllm#7791: [Bug]: Critical distributed executor bug

| 字段 | 值 |
| --- | --- |
| Issue | [#7791](https://github.com/vllm-project/vllm/issues/7791) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Critical distributed executor bug

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM crashes when using multiprocessing distributed executor but works fine when ray is specified instead. By default vLLM is using mp for distributed workloads so even if distributed_executor_backend isn't specified it still crashes. ```python from vllm import LLM llm = LLM("facebook/opt-13b", tensor_parallel_size=4, distributed_executor_backend="mp") output = llm.generate("San Franciso is a") ``` Error output is below: ``` (VllmWorkerProcess pid=17500) WARNING 08-22 18:13:07 logger.py:147] VLLM_TRACE_FUNCTION is enabled. It will record every function executed by Python. This will slow down the code. It is suggested to be used for debugging hang or crashes only. (VllmWorkerProcess pid=17500) INFO 08-22 18:13:07 logger.py:151] Trace frame log is saved to /tmp/vllm/vllm-instance-23db0e96103a493c8d8ca99a7a192568/VLLM_TRACE_FUNCTION_for_process_17500_thread_139868197311680_at_2024-08-22_18:13:07.936704.log (VllmWorkerProcess pid=17498) Process VllmWorkerProcess: (VllmWorkerProcess pid=17498) Traceback (most recent call last): (VllmWorkerProcess pid=17498) File "/opt/conda/envs/py_3.9/lib/python3.9/multiprocessing/process.py", line 3...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: using multiprocessing distributed executor but works fine when ray is specified instead. By default vLLM is using mp for distributed workloads so even if distributed_executor_backend isn't specified it still crashes. ``...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: /vllm/executor/multiproc_worker_utils.py:169, in ProcessWorkerWrapper._enqueue_task(self, future, method, args, kwargs) 168 try: --> 169 self._task_queue.put((task_id, method, args, kwargs)) 170 except BaseException as...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: LM is using mp for distributed workloads so even if distributed_executor_backend isn't specified it still crashes. ```python from vllm import LLM llm = LLM("facebook/opt-13b", tensor_parallel_size=4, distributed_executo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Critical distributed executor bug bug;rocm ### Your current environment ### 🐛 Describe the bug vLLM crashes when using multiprocessing distributed executor but works fine when ray is specified instead. By default...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: izer_mode, skip_tokenizer_init, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, cpu_offload_gb, enforce_eager, max_context_len_to_cap...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
