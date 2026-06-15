# vllm-project/vllm#2352: Why vLLM - GPTQ deployment consumes high memory?

| 字段 | 值 |
| --- | --- |
| Issue | [#2352](https://github.com/vllm-project/vllm/issues/2352) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why vLLM - GPTQ deployment consumes high memory?

### Issue 正文摘录

Hi, We are working on creating a benchmark with Inferless/SOLAR-10.7B-Instruct-v1.0-GPTQ model, we found that when deploying the GPTQ version of the model with vLLM it consumes around 69GB of GPU, whereas AutoGPTQ consumes around 5.67GB. Deploying with vLLM does improve the token/sec a lot, but the concern is that it consumes very high GPU memory. Here's a link to our tutorial: https://tutorials.inferless.com/deploy-quantized-version-of-solar-10.7b-instruct-using-inferless

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: AR-10.7B-Instruct-v1.0-GPTQ model, we found that when deploying the GPTQ version of the model with vLLM it consumes around 69GB of GPU, whereas AutoGPTQ consumes around 5.67GB. Deploying with vLLM does improve the token...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: . Here's a link to our tutorial: https://tutorials.inferless.com/deploy-quantized-version-of-solar-10.7b-instruct-using-inferless
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: prove the token/sec a lot, but the concern is that it consumes very high GPU memory. Here's a link to our tutorial: https://tutorials.inferless.com/deploy-quantized-version-of-solar-10.7b-instruct-using-inferless
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ng on creating a benchmark with Inferless/SOLAR-10.7B-Instruct-v1.0-GPTQ model, we found that when deploying the GPTQ version of the model with vLLM it consumes around 69GB of GPU, whereas AutoGPTQ consumes around 5.67G...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: GPTQ deployment consumes high memory? Hi, We are working on creating a benchmark with Inferless/SOLAR-10.7B-Instruct-v1.0-GPTQ model, we found that when deploying the GPTQ version of the model with vLLM it consumes arou...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
