# vllm-project/vllm#26711: [Bug]: DeepSeek V3.2 running with MTP will cause DeepseekV32IndexerMetadata parsing error

| 字段 | 值 |
| --- | --- |
| Issue | [#26711](https://github.com/vllm-project/vllm/issues/26711) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek V3.2 running with MTP will cause DeepseekV32IndexerMetadata parsing error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug start the service with command ```shell vllm serve ${MODEL_PATH} \ --trust-remote-code \ --served-model-name deepseek_v32 \ --max-model-len 32000 \ --max-num-seqs 32 \ --gpu-memory-utilization 0.9 \ -tp 8 \ --max-num-batched-tokens 8000 \ --kv-cache-dtype bfloat16 \ --speculative_config '{"num_speculative_tokens":1,"method":"deepseek_mtp"}' \ --no-enable-prefix-caching ``` Firstly, I come across the error ``` ^[[1;36m(Worker_TP0 pid=131406)^[[0;0m ERROR 10-13 19:43:47 [v1/executor/multiproc_executor.py:694] WorkerProc hit an exception.^M ^[[1;36m(Worker_TP0 pid=131406)^[[0;0m ERROR 10-13 19:43:47 [v1/executor/multiproc_executor.py:694] Traceback (most recent call last):^M ^[[1;36m(Worker_TP0 pid=131406)^[[0;0m ERROR 10-13 19:43:47 [v1/executor/multiproc_executor.py:694] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 689, in worker_busy_loop^M ^[[1;36m(Worker_TP0 pid=131406)^[[0;0m ERROR 10-13 19:43:47 [v1/executor/multiproc_executor.py:694] output = func(*args, **kwargs)^M ^[[1;36m(Worker_TP0 pid=131406)^[[0;0m ERROR 10-13 19:43:47 [v1/executor/multiproc_executor.py:694] ^^^^^^^^^^^^^^...

## 现有链接修复摘要

#26779 [Bugfix] DeepSeek V3.2 MTP metadata & CUDA graph issues

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lib/python3.12/dist-packages/vllm/v1/worker/gpu_worker.py", line 361, in compile_or_warm_up_model^M ^[[1;36m(Worker_TP0 pid=131406)^[[0;0m ERROR 10-13 19:43:47 [v1/executor/multiproc_executor.py:694] cuda_graph_memory_b...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ion 0.9 \ -tp 8 \ --max-num-batched-tokens 8000 \ --kv-cache-dtype bfloat16 \ --speculative_config '{"num_speculative_tokens":1,"method":"deepseek_mtp"}' \ --no-enable-prefix-caching ``` Firstly, I come across the error...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: --max-num-batched-tokens 8000 \ --kv-cache-dtype bfloat16 \ --speculative_config '{"num_speculative_tokens":1,"method":"deepseek_mtp"}' \ --no-enable-prefix-caching ``` Firstly, I come across the error ``` ^[[1;36m(Work...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: y:694] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/attention/backends/mla/flashmla_sparse.py", line 509, in forward^M ^[[1;36m(Worker_TP6 pid=100106)^[[0;0m ERROR 10-13 17:28:00 [v1/executor/multiproc_executor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ^[[0;0m ERROR 10-13 19:43:47 [v1/executor/multiproc_executor.py:694] cuda_graph_memory_bytes = self.model_runner.capture_model()^M ^[[1;36m(Worker_TP0 pid=131406)^[[0;0m ERROR 10-13 19:43:47 [v1/executor/multiproc_execu...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#26779](https://github.com/vllm-project/vllm/pull/26779) | closes_keyword | 0.95 | [Bugfix] DeepSeek V3.2 MTP metadata & CUDA graph issues | fix applied to verify if the issues recur. ## Test Result Verification for Issue #26711 has been completed. After the fix: DeepSeek V3.2 MTP metadata mapping works normally, and t |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
