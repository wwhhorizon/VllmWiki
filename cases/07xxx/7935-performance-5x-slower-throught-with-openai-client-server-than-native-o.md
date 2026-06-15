# vllm-project/vllm#7935: [Performance]: 5x slower throught with openAI client/server than native one

| 字段 | 值 |
| --- | --- |
| Issue | [#7935](https://github.com/vllm-project/vllm/issues/7935) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: 5x slower throught with openAI client/server than native one

### Issue 正文摘录

### Proposal to improve performance I've been trying to write a reliable benchmark to be used with vllm, and I discovered that when I use the openAI client it can't scale. If I try to use 50 concurrent clients the gpu load goes down to 5% and the throughput is extremely slow. The more clients I add the worst things get. With a single client there is no problem. I then used the same benchmark switching to the [vllm native client/server](https://docs.vllm.ai/en/latest/getting_started/examples/api_client.html) and I'm getting a 60-70% gpu util and 5x higher throughput. I checked that I had the same `SamplingParams` reported by the server in both cases. In parallel with those I was using https://github.com/grafana/k6 against both uses cases - with openAI entrypoints and with the native entrypoint - I can confirm that the server isn't the problem - in both cases I get high gpu util with k6 client and high throughput. I thought that perhaps streaming was the cause but disabling it made a very small difference. So everything points to the openAI client - I know that it's not your product but you recommend using it with [the openAI entrypoint](https://docs.vllm.ai/en/latest/getting_starte...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Your current environment (if you think it is necessary) ```text PyTorch version: 2.4.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 20.04.6 LTS (x86_64) GCC ver...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: hought that perhaps streaming was the cause but disabling it made a very small difference. So everything points to the openAI client - I know that it's not your product but you recommend using it with [the openAI entryp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: True CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: GPU 0: NVIDIA H100 80GB HBM3 GPU 1: NVIDIA H100 80GB HBM3 Nvidia driver version: 550.90.07 cuDNN version: Probably one o...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ## Proposal to improve performance I've been trying to write a reliable benchmark to be used with vllm, and I discovered that when I use the openAI client it can't scale. If I try to use 50 concurrent clients the gpu lo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: d with vllm, and I discovered that when I use the openAI client it can't scale. If I try to use 50 concurrent clients the gpu load goes down to 5% and the throughput is extremely slow. The more clients I add the worst t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
