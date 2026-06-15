# vllm-project/vllm#33916: [Bug] IndexError: list index out of range in chat_completion_stream_generator with --tool-call-parser=mistral during streaming tool calls

| 字段 | 值 |
| --- | --- |
| Issue | [#33916](https://github.com/vllm-project/vllm/issues/33916) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] IndexError: list index out of range in chat_completion_stream_generator with --tool-call-parser=mistral during streaming tool calls

### Issue 正文摘录

````md ### Your current environment ## Description This is what happens: **IndexError** occurs in `vllm/entrypoints/openai/chat_completion/serving.py:1259` when using `--tool-call-parser=mistral` + `--enable-auto-tool-choice` during **streaming** (`stream=True`) chat completions that contain tool calls. ```python actual_call = tool_parser.streamed_args_for_tool[index] IndexError: list index out of range ``` This happens inside `chat_completion_stream_generator` when the tool parser's `streamed_args_for_tool` list is empty or shorter than the expected index. Our deployment looks like: ```yaml - name: "devstral-small-2-24b-fp8-256k" modelURL: "mistralai/Devstral-Small-2-24B-Instruct-2512" vllmConfig: gpuMemoryUtilization: 0.95 maxModelLen: 262144 dtype: "auto" enableChunkedPrefill: true enablePrefixCaching: true maxNumSeqs: 128 extraArgs: [ "--served-model-name=Devstral-Small-2-24B-Instruct-2512", "--trust-remote-code", "--tensor-parallel-size=1", "--max-num-batched-tokens=32768", "--load-format=mistral", "--tokenizer-mode=mistral", "--config-format=mistral", "--tool-call-parser=mistral", "--enable-auto-tool-choice", "--disable-log-requests", '--limit_mm_per_prompt={"image":4, "vide...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: e expected index. Our deployment looks like: ```yaml - name: "devstral-small-2-24b-fp8-256k" modelURL: "mistralai/Devstral-Small-2-24B-Instruct-2512" vllmConfig: gpuMemoryUtilization: 0.95 maxModelLen: 262144 dtype: "au...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ization: 0.95 maxModelLen: 262144 dtype: "auto" enableChunkedPrefill: true enablePrefixCaching: true maxNumSeqs: 128 extraArgs: [ "--served-model-name=Devstral-Small-2-24B-Instruct-2512", "--trust-remote-code", "--tenso...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: eployment looks like: ```yaml - name: "devstral-small-2-24b-fp8-256k" modelURL: "mistralai/Devstral-Small-2-24B-Instruct-2512" vllmConfig: gpuMemoryUtilization: 0.95 maxModelLen: 262144 dtype: "auto" enableChunkedPrefil...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: al=5", # adding stream-interval for more throughput "--attention-backend=flashinfer", "--kv-cache-dtype=fp8", ] # KAI Scheduler settings schedulerName: kai-scheduler runtimeClassName: nvidia labels: kai.scheduler/queue:...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: s of frequently asked questions. ``` ``` correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_dec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
