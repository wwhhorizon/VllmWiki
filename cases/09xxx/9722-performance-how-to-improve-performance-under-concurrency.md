# vllm-project/vllm#9722: [Performance]: How to Improve Performance Under Concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#9722](https://github.com/vllm-project/vllm/issues/9722) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: How to Improve Performance Under Concurrency

### Issue 正文摘录

### Proposal to improve performance I am using vllm version 0.6.3.post1 with four 4090 GPUs to infer the qwen2-72B-chat-int4 model. The request speed is very fast for a single request, but the performance is slow under concurrency, especially the latency for the first token. Additionally, the request throughput remains at about 1 to 2 requests per second. The main use case is intent recognition, with a prompt length of approximately 1000 characters and a generated length of about 5 to 9 characters. Besides using vllm alone for inference, I also tried using fastchat with vllm, and the testing results were basically the same. Below, I will provide the testing results for using vllm alone for inference.（zh_cn：我使用vllm，版本为0.6.3.post1，用4张4090推理qwen2-72B-chat-int4，一个请求速度很快，但并发下性能很慢，特别是首字时间，并且Request throughput一直都每秒1-2个，主要使用场景为意图识别，prompt长度大概在1000字符，生成字符大概在5-9个字。同时除了单独使用vllm启动推理，也尝试过使用fastchat+vllm，测试效果基本一致，下面贴出单独使用vllm启动推理的测试情况） The inference command is: `CUDA_VISIBLE_DEVICES=4,5,6,7 vllm serve /data/models/Qwen2-72B-Instruct-GPTQ-Int4 --max-model-len 10000 --tensor-parallel-size 4 --gpu-memory-utilization 0.6 --served-model-name Qwen2-72B-Chat-GPTQ-Int4` ### Report of performance regres...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: y performance;stale ### Proposal to improve performance I am using vllm version 0.6.3.post1 with four 4090 GPUs to infer the qwen2-72B-chat-int4 model. The request speed is very fast for a single request, but the perfor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: astchat+vllm，测试效果基本一致，下面贴出单独使用vllm启动推理的测试情况） The inference command is: `CUDA_VISIBLE_DEVICES=4,5,6,7 vllm serve /data/models/Qwen2-72B-Instruct-GPTQ-Int4 --max-model-len 10000 --tensor-parallel-size 4 --gpu-memory-utili...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: ce I am using vllm version 0.6.3.post1 with four 4090 GPUs to infer the qwen2-72B-chat-int4 model. The request speed is very fast for a single request, but the performance is slow under concurrency, especially the laten...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: e request, but the performance is slow under concurrency, especially the latency for the first token. Additionally, the request throughput remains at about 1 to 2 requests per second. The main use case is intent recogni...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: vllm version 0.6.3.post1 with four 4090 GPUs to infer the qwen2-72B-chat-int4 model. The request speed is very fast for a single request, but the performance is slow under concurrency, especially the latency for the fir...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
