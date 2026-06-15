# vllm-project/vllm#8735: [Bug]: stuck at  "generating GPU P2P access cache in /home/luban/.cache/vllm/gpu_p2p_access_cache_for_0,1.json"

| 字段 | 值 |
| --- | --- |
| Issue | [#8735](https://github.com/vllm-project/vllm/issues/8735) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: stuck at  "generating GPU P2P access cache in /home/luban/.cache/vllm/gpu_p2p_access_cache_for_0,1.json"

### Issue 正文摘录

### Your current environment ### Model Input Dumps python vllm_test.py 2024-09-23 17:49:44.893334: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`. 2024-09-23 17:49:44.910873: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered 2024-09-23 17:49:44.932328: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered 2024-09-23 17:49:44.938677: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered 2024-09-23 17:49:44.954346: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations. To enable th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: owing instructions: AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags. 2024-09-23 17:49:46.068503: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT W...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: =None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16, max_seq_len=4096, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=2, pipeline_parallel_size=1, disable_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ccess_cache_for_0,1.json" bug;stale ### Your current environment ### Model Input Dumps python vllm_test.py 2024-09-23 17:49:44.893334: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see sli...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: cache in /home/luban/.cache/vllm/gpu_p2p_access_cache_for_0,1.json" bug;stale ### Your current environment ### Model Input Dumps python vllm_test.py 2024-09-23 17:49:44.893334: I tensorflow/core/util/port.cc:153] oneDNN...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collect_model_forward_time=False, collect_model_execute_t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
