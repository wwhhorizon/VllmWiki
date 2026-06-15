# vllm-project/vllm#16926: [Bug]: vllm  0.8.x unable to load model from S3 using runai_streamer but works in 0.7.3

| 字段 | 值 |
| --- | --- |
| Issue | [#16926](https://github.com/vllm-project/vllm/issues/16926) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm  0.8.x unable to load model from S3 using runai_streamer but works in 0.7.3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In vllm `0.7.3` i am able to load the model from s3 using `runai_streamer` . However it fails in `0.8.x` . Below is the output of run in `0.8.4` The AWS credentials have been checked to be correct and as mentioned above it works if I change the vllm to 0.7.3 version. ```bash !vllm --version ``` ```text 0.8.4 ``` ``` !vllm serve --port 8871 "s3:// /models/hf/meta-llama/Meta-Llama-3-8B-Instruct" --load-format 'runai_streamer' --served-model-name "llama3" ``` **Stack Trace**: ```text DEBUG 04-21 14:30:53 [__init__.py:28] No plugins for group vllm.platform_plugins found. DEBUG 04-21 14:30:53 [__init__.py:34] Checking if TPU platform is available. DEBUG 04-21 14:30:53 [__init__.py:44] TPU platform is not available because: No module named 'libtpu' DEBUG 04-21 14:30:53 [__init__.py:52] Checking if CUDA platform is available. DEBUG 04-21 14:30:53 [__init__.py:72] Confirmed CUDA platform is available. DEBUG 04-21 14:30:53 [__init__.py:100] Checking if ROCm platform is available. DEBUG 04-21 14:30:53 [__init__.py:114] ROCm platform is not available because: No module named 'amdsmi' DEBUG 04-21 14:30:53 [__init__.py:122] Checking if HPU pl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: be correct and as mentioned above it works if I change the vllm to 0.7.3 version. ```bash !vllm --version ``` ```text 0.8.4 ``` ``` !vllm serve --port 8871 "s3:// /models/hf/meta-llama/Meta-Llama-3-8B-Instruct" --load-f...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: vllm 0.8.x unable to load model from S3 using runai_streamer but works in 0.7.3 bug ### Your current environment ### 🐛 Describe the bug In vllm `0.7.3` i am able to load the model from s3 using `runai_streamer` ....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: module named 'libtpu' DEBUG 04-21 14:30:53 [__init__.py:52] Checking if CUDA platform is available. DEBUG 04-21 14:30:53 [__init__.py:72] Confirmed CUDA platform is available. DEBUG 04-21 14:30:53 [__init__.py:100] Chec...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: okens_as_token_ids=False, disable_frontend_multiprocessing=False, enable_request_id_headers=False, enable_auto_tool_choice=False, tool_call_parser=None, tool_parser_plugin='', model='s3:// /models/hf/meta-llama/Meta-Lla...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: dtype='auto', kv_cache_dtype='auto', max_model_len=None, guided_decoding_backend='auto', logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size=1, tensor_parallel_siz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
