# vllm-project/vllm#13482: [Bug]: when nsight cature nvtx with PP>1, vllmWorkerProcess will unexpectedly terminate 

| 字段 | 值 |
| --- | --- |
| Issue | [#13482](https://github.com/vllm-project/vllm/issues/13482) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | attention;cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: when nsight cature nvtx with PP>1, vllmWorkerProcess will unexpectedly terminate 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When utilizing nsight to capture nvtx, the VllmWorkerProcess will unexpectedly terminate. However, capturing CUDA proceeds and PP=1 without issues. Reproduce: ``` bash nsys profile -t nvtx -o /tmp/vllm_output -f true python3 -m vllm.entrypoints.openai.api_server --model /models/Meta-Llama-3.1-8B-Instruct-FP8 --tensor-parallel-size=1 --pipeline-parallel-size=2 --gpu-memory-utilization=0.95 --trust-remote-code --port 8000 --max-model-len 8000 --block-size 16 ``` nsight version is latest ``` NVIDIA Nsight Systems version 2025.1.1.103-251135427971v0 ``` Error message ``` text INFO 02-18 05:04:58 config.py:1401] Defaulting to use mp for distributed inference WARNING 02-18 05:04:58 config.py:669] Async output processing can not be enabled with pipeline parallel INFO 02-18 05:04:58 llm_engine.py:234] Initializing a V0 LLM engine (v0.7.2) with config: model='/data00/zeh/models/Meta-Llama-3.1-8B-Instruct-FP8', speculative_config=None, tokenizer='/data00/zeh/models/Meta-Llama-3.1-8B-Instruct-FP8', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None, tokenizer_revision=None, trust_remote_code=True, dty...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: remote-code --port 8000 --max-model-len 8000 --block-size 16 ``` nsight version is latest ``` NVIDIA Nsight Systems version 2025.1.1.103-251135427971v0 ``` Error message ``` text INFO 02-18 05:04:58 config.py:1401] Defa...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: entrypoints.openai.api_server --model /models/Meta-Llama-3.1-8B-Instruct-FP8 --tensor-parallel-size=1 --pipeline-parallel-size=2 --gpu-memory-utilization=0.95 --trust-remote-code --port 8000 --max-model-len 8000 --block...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ature nvtx with PP>1, vllmWorkerProcess will unexpectedly terminate bug;stale ### Your current environment ### 🐛 Describe the bug When utilizing nsight to capture nvtx, the VllmWorkerProcess will unexpectedly terminate....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: uto, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='xgrammar'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_ti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: /tmp/vllm_output -f true python3 -m vllm.entrypoints.openai.api_server --model /models/Meta-Llama-3.1-8B-Instruct-FP8 --tensor-parallel-size=1 --pipeline-parallel-size=2 --gpu-memory-utilization=0.95 --trust-remote-code...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
