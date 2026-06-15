# vllm-project/vllm#20587: [Installation]: Deploy vLLM for CPU server using GGUF model on Kubernetes

| 字段 | 值 |
| --- | --- |
| Issue | [#20587](https://github.com/vllm-project/vllm/issues/20587) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Deploy vLLM for CPU server using GGUF model on Kubernetes

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm I am trying to deploy vLLM in Kubernetes cluster where we don't have GPUs. I have ready that GGUF models are supported in vLLM (https://docs.vllm.ai/en/v0.9.0/features/quantization/gguf.html) Thus, I considered deploying the pod with a CPU VLLM image public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:v0.9.1 and not the vllm/vllm-openai:latest which is GPU oriented It seems it can start with "vllm serve /model/gemma-3-1b-it-q4_0.gguf" I have uploaded the file using hostpath INFO 07-07 18:10:24 [cpu_worker.py:52] OMP tid: 1318, core 52 INFO 07-07 18:10:24 [cpu_worker.py:52] OMP tid: 1319, core 54 INFO 07-07 18:10:24 [cpu_worker.py:52] OMP tid: 1320, core 56 INFO 07-07 18:10:24 [cpu_worker.py:52] OMP tid: 1321, core 58 INFO 07-07 18:10:24 [cpu_worker.py:52] OMP tid: 1322, core 60 INFO 07-07 18:10:24 [cpu_worker.py:52] OMP tid: 1323, core 62 INFO 07-07 18:10:24 [cpu_worker.py:52] INFO 07-07 18:10:24 [parallel_state.py:1065] rank 0 in world size 1 is assigned as DP rank 0, PP rank 0, TP rank 0, EP rank 0 WARNING 07-07 18:10:24 [_logger.py:72] Pin memory is not supported on CPU. INF...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Installation]: Deploy vLLM for CPU server using GGUF model on Kubernetes installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm I am trying to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Installation]: Deploy vLLM for CPU server using GGUF model on Kubernetes installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm I am trying to
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: UF models are supported in vLLM (https://docs.vllm.ai/en/v0.9.0/features/quantization/gguf.html) Thus, I considered deploying the pod with a CPU VLLM image public.ecr.aws/q9t5s3a7/vllm-cpu-release-repo:v0.9.1 and not th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: _0: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: est which is GPU oriented It seems it can start with "vllm serve /model/gemma-3-1b-it-q4_0.gguf" I have uploaded the file using hostpath INFO 07-07 18:10:24 [cpu_worker.py:52] OMP tid: 1318, core 52 INFO 07-07 18:10:24...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
