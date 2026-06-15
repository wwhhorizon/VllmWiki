# vllm-project/vllm#19863: [Bug]: 5090 gemma-3-12b-it using FP8/INT8/FP16 quantization for conncurent requests DOCKER.

| 字段 | 值 |
| --- | --- |
| Issue | [#19863](https://github.com/vllm-project/vllm/issues/19863) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cuda;fp8;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 5090 gemma-3-12b-it using FP8/INT8/FP16 quantization for conncurent requests DOCKER.

### Issue 正文摘录

### Your current environment I use docker only to host open ai server. ### 🐛 Describe the bug I try to use VLLM docker as my backend to run Gemma3 models and use concurrency and dynamic batching. I use 22.04 Ubuntu 570.153.02 Drivers Nvidia CUDA Version: 12.8 I know I should update to 12.9 24.04 ubuntu but so far all worked I used like faster-whisper docker for llama servers etc. I followed these issues: https://github.com/vllm-project/vllm/issues/17587 https://github.com/vllm-project/vllm/pull/14766 https://github.com/vllm-project/vllm/issues/14452 The only thing that seem to work for me was solution from 14452 of [hongbo-miao](https://github.com/hongbo-miao) Server: docker run --gpus=all \ --volume="$HOME/.cache/huggingface:/root/.cache/huggingface" \ --publish=8000:8000 \ nvcr.io/nvidia/tritonserver:25.05-vllm-python-py3 \ python3 -m vllm.entrypoints.openai.api_server \ --model=Qwen/Qwen2.5-0.5B-Instruct \ --port=8000 \ --gpu-memory-utilization=0.75 \ --max_model_len=8192 \ --tensor-parallel-size=1 \ --max_num_seqs=128 \ --enforce-eager Client: curl http://localhost:8000/v1/chat/completions \ --header "Content-Type: application/json" \ --data '{ "model": "Qwen/Qwen2.5-0.5B-Inst...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 10: [Bug]: 5090 gemma-3-12b-it using FP8/INT8/FP16 quantization for conncurent requests DOCKER. bug;stale ### Your current environment I use docker only to host open ai server. ### 🐛 Describe the bug I try to use VLLM docke...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: gemma-3-12b-it using FP8/INT8/FP16 quantization for conncurent requests DOCKER. bug;stale ### Your current environment I use docker only to host open ai server. ### 🐛 Describe the bug I try to use VLLM docker as my back...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: 5090 gemma-3-12b-it using FP8/INT8/FP16 quantization for conncurent requests DOCKER. bug;stale ### Your current environment I use docker only to host open ai server. ### 🐛 Describe the bug I try to use VLLM docke...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: open ai server. ### 🐛 Describe the bug I try to use VLLM docker as my backend to run Gemma3 models and use concurrency and dynamic batching. I use 22.04 Ubuntu 570.153.02 Drivers Nvidia CUDA Version: 12.8 I know I shoul...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ug]: 5090 gemma-3-12b-it using FP8/INT8/FP16 quantization for conncurent requests DOCKER. bug;stale ### Your current environment I use docker only to host open ai server. ### 🐛 Describe the bug I try to use VLLM docker...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
