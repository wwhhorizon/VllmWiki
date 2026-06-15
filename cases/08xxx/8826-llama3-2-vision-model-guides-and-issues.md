# vllm-project/vllm#8826: Llama3.2 Vision Model: Guides and Issues

| 字段 | 值 |
| --- | --- |
| Issue | [#8826](https://github.com/vllm-project/vllm/issues/8826) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 55; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Llama3.2 Vision Model: Guides and Issues

### Issue 正文摘录

Running the server (using the vLLM CLI or our [docker image](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html)): * `vllm serve meta-llama/Llama-3.2-11B-Vision-Instruct --enforce-eager --max-num-seqs 16` * `vllm serve meta-llama/Llama-3.2-90B-Vision-Instruct --enforce-eager --max-num-seqs 32 --tensor-parallel-size 8` Currently: * Only one leading image is supported. Support for multiple images and interleaving images are work in progress. * Text only inference is supported. * Only NVIDIA GPUs are supported. * *Performance is acceptable but to be optimized!* We aim at first release to be functionality correct. We will work on making it fast 🏎️ **Please see the [next steps](https://github.com/vllm-project/vllm/issues/8826#issuecomment-2379960574) for better supporting this model on vLLM.** cc @heheda12345 @ywang96

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Llama3.2 Vision Model: Guides and Issues stale Running the server (using the vLLM CLI or our [docker image](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html)): * `vllm serve meta-llama/Llama-3.2-11B-Visi
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: : Guides and Issues stale Running the server (using the vLLM CLI or our [docker image](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html)): * `vllm serve meta-llama/Llama-3.2-11B-Vision-Instruct --enforc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Llama3.2 Vision Model: Guides and Issues stale Running the server (using the vLLM CLI or our [docker image](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html)): * `vllm serve meta-llama/Llama-3.2-11B-Vis...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rver (using the vLLM CLI or our [docker image](https://docs.vllm.ai/en/latest/serving/deploying_with_docker.html)): * `vllm serve meta-llama/Llama-3.2-11B-Vision-Instruct --enforce-eager --max-num-seqs 16` * `vllm serve...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
