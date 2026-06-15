# vllm-project/vllm#9990: [Bug]: I cannot able to load the model on TESLA T4 GPU in Full precision 

| 字段 | 值 |
| --- | --- |
| Issue | [#9990](https://github.com/vllm-project/vllm/issues/9990) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: I cannot able to load the model on TESLA T4 GPU in Full precision 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug In Tesla T4 GPU i cannot able to load the model for serving using ```python !vllm serve Qwen/Qwen2.5-0.5B ``` Attached the [google colab notebook](https://colab.research.google.com/drive/1sPAP4XRT8xzvw1bvsudWJFPAxzUm2Nvu?usp=sharing) for reference ```python 2024-11-04 10:12:11.903616: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2024-11-04 10:12:12.186153: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered 2024-11-04 10:12:12.258842: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered 2024-11-04 10:12:12.704425: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations. To enable the following instruc...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: : I cannot able to load the model on TESLA T4 GPU in Full precision bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug In Tesla T4 GPU i cannot able to load the model for s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: I cannot able to load the model on TESLA T4 GPU in Full precision bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug In Tesla T4 GPU i cannot able to load the model...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: ='', host=None, port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: I cannot able to load the model on TESLA T4 GPU in Full precision bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug In Tesla T4 GPU i cannot able to load the model...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: auto', quantization_param_path=None, max_model_len=None, guided_decoding_backend='outlines', distributed_executor_backend=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=1, max_parallel_loadin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
