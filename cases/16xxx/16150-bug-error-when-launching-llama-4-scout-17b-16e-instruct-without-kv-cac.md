# vllm-project/vllm#16150: [Bug]: Error When Launching Llama-4-Scout-17B-16E-Instruct Without `--kv-cache-dtype fp8`

| 字段 | 值 |
| --- | --- |
| Issue | [#16150](https://github.com/vllm-project/vllm/issues/16150) |
| 状态 | closed |
| 标签 | bug;torch.compile |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error When Launching Llama-4-Scout-17B-16E-Instruct Without `--kv-cache-dtype fp8`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When attempting to launch the vLLM server using the following command from the documentation, I encountered an error: ```bash vllm serve meta-llama/Llama-4-Scout-17B-16E-Instruct -tp 8 --max-model-len 128000 --override-generation-config='{"attn_temperature_tuning": true}' --load-format runai_streamer ``` Error Logs: ``` ERROR 04-07 10:56:15 [core.py:390] EngineCore hit an exception: Traceback (most recent call last): ERROR 04-07 10:56:15 [core.py:390] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 378, in run_engine_core ERROR 04-07 10:56:15 [core.py:390] engine_core = EngineCoreProc(*args, **kwargs) ERROR 04-07 10:56:15 [core.py:390] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 319, in __init__ ERROR 04-07 10:56:15 [core.py:390] super().__init__(vllm_config, executor_class, log_stats) ERROR 04-07 10:56:15 [core.py:390] File "/usr/local/lib/python3.10/dist-packages/vllm/v1/engine/core.py", line 71, in __init__ ERROR 04-07 10:56:15 [core.py:390] self._initialize_kv_caches(vllm_config) ERROR 04-07 10:56:15 [core.py:390] File "/usr/local/lib/python3.10/dist-packages/vllm/v1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Llama-4-Scout-17B-16E-Instruct Without `--kv-cache-dtype fp8` bug;torch.compile ### Your current environment ### 🐛 Describe the bug When attempting to launch the vLLM server using the following command from the document...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Error When Launching Llama-4-Scout-17B-16E-Instruct Without `--kv-cache-dtype fp8` bug;torch.compile ### Your current environment ### 🐛 Describe the bug When attempting to launch the vLLM server using the followi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Error When Launching Llama-4-Scout-17B-16E-Instruct Without `--kv-cache-dtype fp8` bug;torch.compile ### Your current environment ### 🐛 Describe the bug When attempting to launch the vLLM server using the following comm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: py:383] File "/usr/local/lib/python3.10/dist-packages/vllm/compilation/backends.py", line 608, in __call__ (VllmWorker rank=5 pid=9469) ERROR 04-07 10:56:15 [multiproc_executor.py:383] return self.compiled_graph_for_gen...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
