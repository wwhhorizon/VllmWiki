# vllm-project/vllm#4136: [Bug]: benchmark trtllm failed

| 字段 | 值 |
| --- | --- |
| Issue | [#4136](https://github.com/vllm-project/vllm/issues/4136) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | triton |
| 症状 | crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: benchmark trtllm failed

### Issue 正文摘录

### Your current environment ```text trtllm: 0.8.0 triton server version: 2.43.0 triton_backend version: a4c7ac7e4036a2c7e41ee663697859cc8575367d tritonserver docker: nvcr.io/nvidia/tritonserver:24.02-trtllm-python-py3 ``` ### 🐛 Describe the bug benchmark trtllm using the trt_llm backend with the following command: ```bash python3 benchmark_serving.py \ --endpoint /v2/models/ensemble/generate_stream \ --port 19000 \ --backend tensorrt-llm \ --model llama2-7b \ --tokenizer $HF_MODEL_DIR \ --dataset-name sharegpt \ --dataset-path ./ShareGPT_V3_unfiltered_cleaned_split.json \ --request-rate 128 \ --num-prompts 1000 ``` I get the error: ```text prompt_len=29, error='Traceback (most recent call last):\n File "/tensorrtllm_backend/dataset-benchmark/backend_request_func.py", line 154, in async_request_trt_llm\n output.generated_text = json.loads(data)["text_output"]\n File "/usr/lib/python3.10/json/__init__.py", line 339, in loads\n raise TypeError(f\'the JSON object must be str, bytes or bytearray, \'\nTypeError: the JSON object must be str, bytes or bytearray, not dict\n'), ``` which I think's it's due to the duplicated `json.load` of `data` returned by trtllm https://github.com/vllm-p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ed bug ### Your current environment ```text trtllm: 0.8.0 triton server version: 2.43.0 triton_backend version: a4c7ac7e4036a2c7e41ee663697859cc8575367d tritonserver docker: nvcr.io/nvidia/tritonserver:24.02-trtllm-pyth...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nd: ```bash python3 benchmark_serving.py \ --endpoint /v2/models/ensemble/generate_stream \ --port 19000 \ --backend tensorrt-llm \ --model llama2-7b \ --tokenizer $HF_MODEL_DIR \ --dataset-name sharegpt
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: rk trtllm failed bug ### Your current environment ```text trtllm: 0.8.0 triton server version: 2.43.0 triton_backend version: a4c7ac7e4036a2c7e41ee663697859cc8575367d tritonserver docker: nvcr.io/nvidia/tritonserver:24....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: aset-path ./ShareGPT_V3_unfiltered_cleaned_split.json \ --request-rate 128 \ --num-prompts 1000 ``` I get the error: ```text prompt_len=29, error='Traceback (most recent call last):\n File "/tensorrtllm_backend/dataset-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: benchmark trtllm failed bug ### Your current environment ```text trtllm: 0.8.0 triton server version: 2.43.0 triton_backend version: a4c7ac7e4036a2c7e41ee663697859cc8575367d tritonserver docker: nvcr.io/nvidia/tr...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
