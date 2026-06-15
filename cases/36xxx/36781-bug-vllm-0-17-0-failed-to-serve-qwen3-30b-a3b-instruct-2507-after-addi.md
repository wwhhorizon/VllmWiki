# vllm-project/vllm#36781: [Bug]: vLLM 0.17.0 failed to serve Qwen3-30B-A3B-Instruct-2507 after adding `--enable_lora`

| 字段 | 值 |
| --- | --- |
| Issue | [#36781](https://github.com/vllm-project/vllm/issues/36781) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.17.0 failed to serve Qwen3-30B-A3B-Instruct-2507 after adding `--enable_lora`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug This serving command ```bash vllm serve ./Qwen3-30B-A3B-Instruct-2507/ \ --dtype bfloat16 \ --load_format safetensors \ --distributed_executor_backend mp \ --worker_extension_cls 'verl.workers.rollout.vllm_rollout.utils.vLLMColocateWorkerExtension' \ --max-model-len 262144 \ --max_num_seqs 1024 \ --enable_chunked_prefill \ --max_num_batched_tokens 32768 \ --enable_prefix_caching \ --enable_sleep_mode \ --logprobs_mode processed_logprobs \ --gpu-memory-utilization 0.6 \ --tensor-parallel-size 4 \ --seed 0 \ --override_generation_config '{"temperature": 1.0, "top_k": -1, "top_p": 1, "repetition_penalty": 1.0, "max_new_tokens": 2048}' \ --hf_overrides '{}' \ --scheduling_policy fcfs \ --compilation_config '{"cudagraph_mode": "FULL_AND_PIECEWISE"}' \ --enable_lora \ --max_loras 1 \ --max_lora_rank 64 ``` raises the the following error: ```bash (Worker pid=263605) (Worker_TP0 pid=263605) ERROR 03-11 19:12:05 [multiproc_executor.py:880] WorkerProc hit an exception. (Worker pid=263605) (Worker_TP0 pid=263605) ERROR 03-11 19:12:05 [multiproc_executor.py:880] Traceback (most recent call last): (Worker pid=263605) (Worker_TP0 pid=263605) E...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vLLM 0.17.0 failed to serve Qwen3-30B-A3B-Instruct-2507 after adding `--enable_lora` bug ### Your current environment ### 🐛 Describe the bug This serving command ```bash vllm serve ./Qwen3-30B-A3B-Instruct-2507/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ) ERROR 03-11 19:12:05 [multiproc_executor.py:880] output = self.aot_compiled_fn(self, *args, **kwargs) (Worker pid=263605) (Worker_TP0 pid=263605) ERROR 03-11 19:12:05 [multiproc_executor.py:880] ^^^^^^^^^^^^^^^^^^^^^^...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: erving command ```bash vllm serve ./Qwen3-30B-A3B-Instruct-2507/ \ --dtype bfloat16 \ --load_format safetensors \ --distributed_executor_backend mp \ --worker_extension_cls 'verl.workers.rollout.vllm_rollout.utils.vLLMC...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: /usr/local/lib/python3.11/dist-packages/vllm/model_executor/models/qwen3_moe.py", line 783, in forward (Worker pid=263605) (Worker_TP0 pid=263605) ERROR 03-11 19:12:05 [multiproc_executor.py:880] hidden_states = self.mo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ) ERROR 03-11 19:12:05 [multiproc_executor.py:880] self.model_runner.profile_run() (Worker pid=263605) (Worker_TP0 pid=263605) ERROR 03-11 19:12:05 [multiproc_executor.py:880] File "/usr/local/lib/python3.11/dist-packag...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
