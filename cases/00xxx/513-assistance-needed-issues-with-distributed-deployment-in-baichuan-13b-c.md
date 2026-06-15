# vllm-project/vllm#513: Assistance Needed: Issues with Distributed Deployment in Baichuan-13b-Chat Server Implementation

| 字段 | 值 |
| --- | --- |
| Issue | [#513](https://github.com/vllm-project/vllm/issues/513) |
| 状态 | closed |
| 标签 | bug;help wanted |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Assistance Needed: Issues with Distributed Deployment in Baichuan-13b-Chat Server Implementation

### Issue 正文摘录

Dear Community, We've recently submitted a pull request for a server setup that facilitates baichuan-13b-chat inference. This implementation, as detailed in [Pull Request #512](https://github.com/vllm-project/vllm/pull/512), works successfully in a non-distributed environment with a single GPU. However, we are experiencing inconsistencies when employing tensor parallelism in a distributed setup. The command we use for initiating the server in this setup is: ``` python -m vllm.entrypoints.openai.api_server --host [0.0.0.0](http://0.0.0.0/) --port 8000 --model /path/to/baichuan-13b-chat --pipeline-parallel-size 1 --tensor-parallel-size 2 --gpu-memory-utilization 0.8 --dtype half ``` While the server operates and delivers outputs under these conditions, the results are neither consistent nor correct. We are reaching out to the community, seeking your expertise and assistance in resolving this issue. We believe your insights could significantly enhance our current implementation. For a complete understanding of the context, please review the pull request linked above. We value and appreciate any contributions made towards improving this implementation. Thank you in advance for your su...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nity, We've recently submitted a pull request for a server setup that facilitates baichuan-13b-chat inference. This implementation, as detailed in [Pull Request #512](https://github.com/vllm-project/vllm/pull/512), work...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: -parallel-size 1 --tensor-parallel-size 2 --gpu-memory-utilization 0.8 --dtype half ``` While the server operates and delivers outputs under these conditions, the results are neither consistent nor correct. We are reach...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ever, we are experiencing inconsistencies when employing tensor parallelism in a distributed setup. The command we use for initiating the server in this setup is: ``` python -m vllm.entrypoints.openai.api_server --host...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: points.openai.api_server --host [0.0.0.0](http://0.0.0.0/) --port 8000 --model /path/to/baichuan-13b-chat --pipeline-parallel-size 1 --tensor-parallel-size 2 --gpu-memory-utilization 0.8 --dtype half ``` While the serve...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: sistent nor correct. We are reaching out to the community, seeking your expertise and assistance in resolving this issue. We believe your insights could significantly enhance our current implementation. For a complete u...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
