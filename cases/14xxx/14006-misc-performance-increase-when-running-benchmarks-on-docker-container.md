# vllm-project/vllm#14006: [Misc]: Performance Increase When Running Benchmarks on Docker Container

| 字段 | 值 |
| --- | --- |
| Issue | [#14006](https://github.com/vllm-project/vllm/issues/14006) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support |
| 子分类 | throughput |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: Performance Increase When Running Benchmarks on Docker Container

### Issue 正文摘录

### Anything you want to discuss about vllm. I am currently using an AMD GPU to test vLLM. As recommended on the [official documents](https://docs.vllm.ai/en/v0.6.5/getting_started/amd-installation.html), I used a docker image and container to run vLLM with ROCm. I am running some benchmark tests with the vLLM server using the Llama 3 8B Instruct model with the benchmark_serving.py file provided by vLLM. I noticed that when I deploy a new container and run the benchmark test I get a TPS of around 250. However, even if I stop the vLLM server and start it again, the second time I run the benchmark using the same inputs, I get a TPS of around 1000. On the other hand, if I remove the container and deploy a new one, I get a TPS of around 250 again. Has anybody noticed this same issue before? I think maybe it has something to do with the values used for Paged Attention being cached somewhere in the container? And only when the container is removed it seems like it is properly reset? If anyone can provide some insight, it would be very helpful. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right c...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Misc]: Performance Increase When Running Benchmarks on Docker Container stale ### Anything you want to discuss about vllm. I am currently using an AMD GPU to test vLLM. As recommended on the [official documents](https:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: installation.html), I used a docker image and container to run vLLM with ROCm. I am running some benchmark tests with the vLLM server using the Llama 3 8B Instruct model with the benchmark_serving.py file provided by vL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: h ROCm. I am running some benchmark tests with the vLLM server using the Llama 3 8B Instruct model with the benchmark_serving.py file provided by vLLM. I noticed that when I deploy a new container and run the benchmark...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Misc]: Performance Increase When Running Benchmarks on Docker Container stale ### Anything you want to discuss about vllm. I am currently using an AMD GPU to test vLLM. As recommended on the [official documents](https:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Performance Increase When Running Benchmarks on Docker Container stale ### Anything you want to discuss about vllm. I am currently using an AMD GPU to test vLLM. As recommended on the [official documents](https:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
