# vllm-project/vllm#16152: [Bug]: Stuck When Launching Llama-4-Maverick-17B-128E-Instruct-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#16152](https://github.com/vllm-project/vllm/issues/16152) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Stuck When Launching Llama-4-Maverick-17B-128E-Instruct-FP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to launch the vLLM server using the following command from the documentation, and after the model finished loading, it has been stuck there for over ten hours. ```bash vllm serve meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 -tp 8 --max-model-len 128000 --load-format runai_streamer --override-generation-config='{"attn_temperature_tuning": true}' --kv-cache-dtype fp8 ``` Logs: ``` (VllmWorker rank=6 pid=20691) WARNING 04-07 11:11:48 [kv_cache.py:82] Checkpoint does not provide a q scaling factor. Setting it to k_scale. This only matters for the flash-attn backend. (VllmWorker rank=6 pid=20691) WARNING 04-07 11:11:48 [kv_cache.py:95] Using KV cache scaling factor 1.0 for fp8_e4m3. This may cause accuracy issues. Please make sure k/v_scale scaling factors are available in the fp8 checkpoint. (VllmWorker rank=6 pid=20691) INFO 04-07 11:11:48 [gpu_model_runner.py:1273] Model loading took 48.8682 GiB and 117.477290 seconds (VllmWorker rank=7 pid=20772) WARNING 04-07 11:11:49 [kv_cache.py:82] Checkpoint does not provide a q scaling factor. Setting it to k_scale. This only matters for the flash-attn backend. (VllmWork...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Stuck When Launching Llama-4-Maverick-17B-128E-Instruct-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to launch the vLLM server using the following command from the documentati...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Stuck When Launching Llama-4-Maverick-17B-128E-Instruct-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug When attempting to launch the vLLM server using the following command from the documentati...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cache;cuda;fp8;operato...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ling factor. Setting it to k_scale. This only matters for the flash-attn backend. (VllmWorker rank=6 pid=20691) WARNING 04-07 11:11:48 [kv_cache.py:95] Using KV cache scaling factor 1.0 for fp8_e4m3. This may cause accu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
