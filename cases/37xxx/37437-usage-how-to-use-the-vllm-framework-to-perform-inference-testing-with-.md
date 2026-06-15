# vllm-project/vllm#37437: [Usage]: How to use the vLLM framework to perform inference testing with Prefill-Decode (PD) Separation for the DeepSeek-R1 NVFP4 model across multiple GB300 server nodes (N Prefill nodes + M Decode nodes)?

| 字段 | 值 |
| --- | --- |
| Issue | [#37437](https://github.com/vllm-project/vllm/issues/37437) |
| 状态 | open |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use the vLLM framework to perform inference testing with Prefill-Decode (PD) Separation for the DeepSeek-R1 NVFP4 model across multiple GB300 server nodes (N Prefill nodes + M Decode nodes)?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Dear vLLM Team, Pardon me for troubling you, and thank you so much for your great work on the vLLM engine. I am currently trying to run inference with Prefill-Decode Disaggregation for the DeepSeek-R1 NVFP4 model across a cluster of GB300 servers. My goal is to deploy a fully disaggregated setup: N dedicated Prefill nodes + M dedicated Decode nodes across multiple physical machines. However, I am facing the following challenges: I am using a GB300-optimized vLLM 0.11.0+custom build, which does not support high-level PD disaggregation CLI arguments such as --separate-prefill-decode, --prefill-node-ips, --decode-node-ips, --role, etc. These flags return "unrecognized arguments". I have tried using basic distributed arguments (--node-rank, --master-addr, --nnodes) to simulate Prefill/Decode splitting, but I cannot achieve real, strict Prefill-Decode Disaggregation where the two stages are fully isolated on separate nodes. My environment: multiple GB300 nodes with InfiniBand, Docker with --network=host, and the same DeepSeek-R1 NVFP4 model accessible across all nodes. I wo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: edicated Decode nodes across multiple physical machines. However, I am facing the following challenges: I am using a GB300-optimized vLLM 0.11.0+custom build, which does not support high-level PD disaggregation CLI argu...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: nference testing with Prefill-Decode (PD) Separation for the DeepSeek-R1 NVFP4 model across multiple GB300 server nodes (N Prefill nodes + M Decode nodes)? usage ### Your current environment ```text The output of `pytho...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ce testing with Prefill-Decode (PD) Separation for the DeepSeek-R1 NVFP4 model across multiple GB300 server nodes (N Prefill nodes + M Decode nodes)? usage ### Your current environment ```text The output of `python coll...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: How to use the vLLM framework to perform inference testing with Prefill-Decode (PD) Separation for the DeepSeek-R1 NVFP4 model across multiple GB300 server nodes (N Prefill nodes + M Decode nodes)? usage ### Yo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ds, ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
