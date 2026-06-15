# vllm-project/vllm#13640: [Bug]: Errors Encountered While Running Qwen2.5-VL-72B-AWQ Inference on 2xA800 GPUs (Works Fine with Qwen2-VL-72B-AWQ)

| 字段 | 值 |
| --- | --- |
| Issue | [#13640](https://github.com/vllm-project/vllm/issues/13640) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Errors Encountered While Running Qwen2.5-VL-72B-AWQ Inference on 2xA800 GPUs (Works Fine with Qwen2-VL-72B-AWQ)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## error Configure the Qwen/Qwen2.5-VL-72B-Instruct-AWQ model to run using the following parameters: ```shell python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-VL-72B-Instruct-AWQ --host 0.0.0.0 --port 8000 --tensor-parallel-size 2 ``` An error occurred, the main error is: ```shell ValueError: Weight input_size_per_partition = 14784 is not divisible by min_thread_k = 128. Consider reducing tensor_parallel_size or running with --quantization gptq. ``` ## check * [x] The latest transformers repository has been installed, and a single A800 GPU can successfully run Qwen/Qwen2.5-VL-3B-Instruct * [x] Running with the configuration `--tensor-parallel-size 2` can successfully run Qwen/Qwen2-VL-72B-Instruct-AWQ ## detail ```shell python3 -m vllm.entrypoints.openai.api_server --model /root/.cache/modelscope/hub/Qwen/Qwen2.5-VL-72B-Instruct-AWQ --host 0.0.0.0 --port 8000 --tensor-parallel-size 2 INFO 02-13 14:17:57 __init__.py:190] Automatically detected platform cuda. INFO 02-13 14:17:58 api_server.py:840] vLLM API server version 0.7.2 INFO 02-13 14:17:58 api_server.py:841] args: Namespace(host='0.0.0.0', port=8000, uvicor...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 9: -72B-AWQ Inference on 2xA800 GPUs (Works Fine with Qwen2-VL-72B-AWQ) bug;stale ### Your current environment ### 🐛 Describe the bug ## error Configure the Qwen/Qwen2.5-VL-72B-Instruct-AWQ model to run using the following...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: r_partition = 14784 is not divisible by min_thread_k = 128. Consider reducing tensor_parallel_size or running with --quantization gptq. ``` ## check * [x] The latest transformers repository has been installed, and a sin...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: thread_k = 128. Consider reducing tensor_parallel_size or running with --quantization gptq. ``` ## check * [x] The latest transformers repository has been installed, and a single A800 GPU can successfully run Qwen/Qwen2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Errors Encountered While Running Qwen2.5-VL-72B-AWQ Inference on 2xA800 GPUs (Works Fine with Qwen2-VL-72B-AWQ) bug;stale ### Your current environment ### 🐛 Describe the bug ## error Configure the Qwen/Qwen2.5-VL...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: host='0.0.0.0', port=8000, uvicorn_log_level='info', allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], api_key=None, lora_modules=None, prompt_adapters=None, chat_template=Non...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
