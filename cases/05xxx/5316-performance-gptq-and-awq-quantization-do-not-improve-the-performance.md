# vllm-project/vllm#5316: [Performance]: gptq and awq quantization do not improve the performance

| 字段 | 值 |
| --- | --- |
| Issue | [#5316](https://github.com/vllm-project/vllm/issues/5316) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: gptq and awq quantization do not improve the performance

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression vllm version: 0.4.3, gpu A40, 46Gi, single gpu ### phi3 fp16 $python -m vllm.entrypoints.openai.api_server --model /t9k/mnt/workspace/llm_models/phi3 --dtype bfloat16 --trust-remote-code --max-model-len 4096 python test_serving.py --backend 'vllm' --model /t9k/mnt/workspace/llm_models/phi3 --dataset-name summarize --num-prompts 1000 --request-rate 60 ============ Serving Benchmark Result ============ Successful requests: 1000 **Benchmark duration (s): 118.85** Total input tokens: 686000 Total generated tokens: 56000 **Request throughput (req/s): 8.41** Input token throughput (tok/s): 5772.20 Output token throughput (tok/s): 471.20 ---------------Time to First Token---------------- Mean TTFT (ms): 47476.00 Median TTFT (ms): 50637.58 P99 TTFT (ms): 98138.44 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 190.66 Median TPOT (ms): 189.92 P99 TPOT (ms): 338.66 ### awq performance: python -m vllm.entrypoints.openai.api_server --model phi3-4k-awq --quantization 'awq' --dtype auto --trust-remote-code $python test_serving.py --backend 'vllm' --model phi3-4k-awq --dataset-name summarize...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: roposal to improve performance _No response_ ### Report of performance regression vllm version: 0.4.3, gpu A40, 46Gi, single gpu ### phi3 fp16 $python -m vllm.entrypoints.openai.api_server --model /t9k/mnt/workspace/llm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Performance]: gptq and awq quantization do not improve the performance performance ### Proposal to improve performance _No response_ ### Report of performance regression vllm version: 0.4.3, gpu A40, 46Gi, single gpu #...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: oat16 --trust-remote-code --max-model-len 4096 python test_serving.py --backend 'vllm' --model /t9k/mnt/workspace/llm_models/phi3 --dataset-name summarize --num-prompts 1000 --request-rate 60 ============ Serving Benchm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e performance _No response_ ### Report of performance regression vllm version: 0.4.3, gpu A40, 46Gi, single gpu ### phi3 fp16 $python -m vllm.entrypoints.openai.api_server --model /t9k/mnt/workspace/llm_models/phi3 --dt...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ingle gpu ### phi3 fp16 $python -m vllm.entrypoints.openai.api_server --model /t9k/mnt/workspace/llm_models/phi3 --dtype bfloat16 --trust-remote-code --max-model-len 4096 python test_serving.py --backend 'vllm' --model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
