# vllm-project/vllm#9678: [Bug]: An EXTREMELY WEIRD bug when I import evaluate before vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#9678](https://github.com/vllm-project/vllm/issues/9678) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: An EXTREMELY WEIRD bug when I import evaluate before vllm

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` evaluate == 0.4.3 vllm == 0.6.3.post1 ``` If I import `evaluate` before `vllm`: ``` import evaluate import vllm vllm.LLM('my_local_path_of_mistral_7b_base') ``` A bug will be raised: ``` 2024-10-25 10:55:49.480431: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`. 2024-10-25 10:55:49.497640: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2024-10-25 10:55:49.518802: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered 2024-10-25 10:55:49.525222: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been re...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 10: port evaluate before vllm bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` evaluate == 0.4.3 vllm == 0.6.3.post1 ``` If I import `evaluate` before `vllm`: ``` import...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: An EXTREMELY WEIRD bug when I import evaluate before vllm bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` evaluate == 0.4.3 vllm == 0.6.3.post1 ``` If I impor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: An EXTREMELY WEIRD bug when I import evaluate before vllm bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` evaluate == 0.4.3 vllm == 0.6.3.post1 ``` If I impor...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: salLM', 'MambaForCausalLM', 'MistralForCausalLM', 'MixtralForCausalLM', 'QuantMixtralForCausalLM', 'MptForCausalLM', 'MPTForCausalLM', 'MiniCPMForCausalLM', 'MiniCPM3ForCausalLM', 'NemotronForCausalLM', 'OlmoForCausalLM...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
