# vllm-project/vllm#7469: [Feature]: ROCm 6.2 support & FP8 Support

| 字段 | 值 |
| --- | --- |
| Issue | [#7469](https://github.com/vllm-project/vllm/issues/7469) |
| 状态 | closed |
| 标签 | feature request;rocm |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | fp8;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: ROCm 6.2 support & FP8 Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Last week AMD announced rocm 6.2 (https://rocm.docs.amd.com/en/latest/about/release-notes.html) also announcing expanded support for VLLM & FP8. Actually I was able to run it following the guides ( Rocm branch ) and executing it like this: python -m vllm.entrypoints.openai.api_server --model /work/work2/Meta-Llama-3.1-70B-Instruct --tensor-parallel-size 1 --port 8010 --host 0.0.0.0 --quantization fp8 --quantized-weights-path /work/work2/Meta-Llama-3.1-70B-Instruct-fp8/llama.safetensors --kv-cache-dtype fp8_e4m3 --quantization-param-path /work/work2/Meta-Llama-3.1-70B-Instruct-fp8-scales/kv_cache_scales.json But the performance is like 3/4 times slower than using the model withouth quantitization. I don't know if ROCm 6.2 can solve thsi issues ... actually the performance we got with mi300x(half) is similar than running the a A100(FP8) on our tests. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Feature]: ROCm 6.2 support & FP8 Support feature request;rocm ### 🚀 The feature, motivation and pitch Last week AMD announced rocm 6.2 (https://rocm.docs.amd.com/en/latest/about/release-notes.html) also announcing expa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Feature]: ROCm 6.2 support & FP8 Support feature request;rocm ### 🚀 The feature, motivation and pitch Last week AMD announced rocm 6.2 (https://rocm.docs.amd.com/en/latest/about/release-notes.html) also announcing expa...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: https://rocm.docs.amd.com/en/latest/about/release-notes.html) also announcing expanded support for VLLM & FP8. Actually I was able to run it following the guides ( Rocm branch ) and executing it like this: python -m vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: executing it like this: python -m vllm.entrypoints.openai.api_server --model /work/work2/Meta-Llama-3.1-70B-Instruct --tensor-parallel-size 1 --port 8010 --host 0.0.0.0 --quantization fp8 --quantized-weights-path /work/...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: hts-path /work/work2/Meta-Llama-3.1-70B-Instruct-fp8/llama.safetensors --kv-cache-dtype fp8_e4m3 --quantization-param-path /work/work2/Meta-Llama-3.1-70B-Instruct-fp8-scales/kv_cache_scales.json But the performance is l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
