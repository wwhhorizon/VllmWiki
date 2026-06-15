# vllm-project/vllm#21637: [Bug]: Scout with DP=4,TP=2,EP with full cuda graph would stuck in decode

| 字段 | 值 |
| --- | --- |
| Issue | [#21637](https://github.com/vllm-project/vllm/issues/21637) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8;moe;operator;quantization;sampling;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Scout with DP=4,TP=2,EP with full cuda graph would stuck in decode

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It can be reproduced with the following serving command and a curl prompt request. In comparison, DP=8+EP works fine in the same machine. ```bash VLLM_LOGGING_LEVEL=DEBUG VLLM_ALL2ALL_BACKEND=pplx VLLM_USE_DEEP_GEMM=1 \ vllm serve meta-llama/Llama-4-Scout-17B-16E --max_model_len 8192 --kv_cache_dtype fp8 \ --enable-expert-parallel --tensor-parallel-size 2 --data-parallel-size 4 --trust-remote-code \ --gpu-memory-utilization 0.9 --disable-log-requests \ --compilation-config '{"full_cuda_graph":true}' 2>&1 \ | tee ~/log/ep_`date +%Y%m%d_%H%M%S`.log ``` ```bash curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{ "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Who won the world series in 2020?"} ] }' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Scout with DP=4,TP=2,EP with full cuda graph would stuck in decode bug;stale ### Your current environment ### 🐛 Describe the bug It can be reproduced with the following serving command and a curl prompt request....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;fp8;moe;opera...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: serve meta-llama/Llama-4-Scout-17B-16E --max_model_len 8192 --kv_cache_dtype fp8 \ --enable-expert-parallel --tensor-parallel-size 2 --data-parallel-size 4 --trust-remote-code \ --gpu-memory-utilization 0.9 --disable-lo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: =DEBUG VLLM_ALL2ALL_BACKEND=pplx VLLM_USE_DEEP_GEMM=1 \ vllm serve meta-llama/Llama-4-Scout-17B-16E --max_model_len 8192 --kv_cache_dtype fp8 \ --enable-expert-parallel --tensor-parallel-size 2 --data-parallel-size 4 --...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ```bash VLLM_LOGGING_LEVEL=DEBUG VLLM_ALL2ALL_BACKEND=pplx VLLM_USE_DEEP_GEMM=1 \ vllm serve meta-llama/Llama-4-Scout-17B-16E --max_model_len 8192 --kv_cache_dtype fp8 \ --enable-expert-parallel --tensor-parallel-size 2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
