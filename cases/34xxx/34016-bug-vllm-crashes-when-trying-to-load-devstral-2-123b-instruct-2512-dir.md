# vllm-project/vllm#34016: [Bug]: vLLM crashes when trying to load Devstral-2-123B-Instruct-2512 directly from S3

| 字段 | 值 |
| --- | --- |
| Issue | [#34016](https://github.com/vllm-project/vllm/issues/34016) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM crashes when trying to load Devstral-2-123B-Instruct-2512 directly from S3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I try to load Devstral-2-123B-Instruct-2512 directly from S3 using the Run:ai streamer in distributed mode, vLLM crashes when initializing workers. I deploy vLLM with vLLM Production Stack on a Kubernetes cluster. Relevant `vllm serve` parameters: ```text --load-format "runai_streamer" \ --model-loader-extra-config "{\"distributed\":true,\"memory_limit\":3758096384,\"chunk_bytesize\":16777216}" ``` The error I see in the log: ```text [multiproc_executor.py:772] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/llama.py", line 487, in load_weights [multiproc_executor.py:772] param = params_dict[name] [multiproc_executor.py:772] ~~~~~~~~~~~^^^^^^ [multiproc_executor.py:772] KeyError: 'layers.0.mlp.gate_up_proj.activation_scale' [multiproc_executor.py:772] WorkerProc failed to start. ``` I'm not 100% sure it's not some misconfiguration on my part, but the problem is only with the Run:ai streamer in distributed mode, I can load the model from local filesystem without problems. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ltiproc_executor.py:772] KeyError: 'layers.0.mlp.gate_up_proj.activation_scale' [multiproc_executor.py:772] WorkerProc failed to start. ``` I'm not 100% sure it's not some misconfiguration on my part, but the problem is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: a Kubernetes cluster. Relevant `vllm serve` parameters: ```text --load-format "runai_streamer" \ --model-loader-extra-config "{\"distributed\":true,\"memory_limit\":3758096384,\"chunk_bytesize\":16777216}" ``` The error...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculativ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ms. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: orrectness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding attention;cuda;fp8;operator;quan...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
