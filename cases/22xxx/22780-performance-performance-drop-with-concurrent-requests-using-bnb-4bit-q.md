# vllm-project/vllm#22780: [Performance]: Performance Drop with Concurrent Requests Using BnB-4bit Quantized Models in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#22780](https://github.com/vllm-project/vllm/issues/22780) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | kernel;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Performance Drop with Concurrent Requests Using BnB-4bit Quantized Models in vLLM

### Issue 正文摘录

### Proposal to improve performance Hello vLLM Team I am observing significant performance drops when running concurrent requests with BnB-4bit quantized models on vLLM. Below are the detailed findings: ## Environment Details - **vLLM version**: 0.9.01 - **GPU**: Nvidia Ada 6000 (1x configuration) - **DRAM**: 1TB total memory ## Models Used - **BnB**: [gemma-3-27b-it-bnb-4bit](https://huggingface.co/unsloth/gemma-3-27b-it-bnb-4bit) - **AWQ**: [gemma-3-27b-it-int4-awq](https://huggingface.co/gaunernst/gemma-3-27b-it-int4-awq) ## Throughput Observations ### **BnB-4bit** (Gemma 3 27B) - Single request: ~20 tokens/s - Two concurrent requests: ~9.4 tokens/s ### **AWQ** (Gemma 3 27B) - Single request: ~30 tokens/s - Two concurrent requests: ~56.6 tokens/s ``` bash # vllm service sudo docker run --rm --runtime nvidia --gpus='"device=7"' --mount type=bind,source=/usr/local/models/,target=/usr/local/models/ -p 7415:8000 --ipc=host vllm/vllm-openai:v0.9.0.1 --model /usr/local/models/gemma-3-27b-it-bnb-4bit --served-model-name model --max-model-len 32000 --tensor-parallel-size 1 --gpu-memory-utilization 0.95 # send requests curl http://localhost:7416/v1/completions \ -H "Content-Type: applic...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: vLLM. Below are the detailed findings: ## Environment Details - **vLLM version**: 0.9.01 - **GPU**: Nvidia Ada 6000 (1x configuration) - **DRAM**: 1TB total memory ## Models Used - **BnB**: [gemma-3-27b-it-bnb-4bit](htt...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Performance]: Performance Drop with Concurrent Requests Using BnB-4bit Quantized Models in vLLM performance;stale ### Proposal to improve performance Hello vLLM Team I am observing significant performance drops when ru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nce]: Performance Drop with Concurrent Requests Using BnB-4bit Quantized Models in vLLM performance;stale ### Proposal to improve performance Hello vLLM Team I am observing significant performance drops when running con...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: -int4-awq](https://huggingface.co/gaunernst/gemma-3-27b-it-int4-awq) ## Throughput Observations ### **BnB-4bit** (Gemma 3 27B) - Single request: ~20 tokens/s - Two concurrent requests: ~9.4 tokens/s ### **AWQ** (Gemma 3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Performance Drop with Concurrent Requests Using BnB-4bit Quantized Models in vLLM performance;stale ### Proposal to improve performance Hello vLLM Team I am observing significant performance drops when ru...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
