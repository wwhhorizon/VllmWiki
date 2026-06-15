# vllm-project/vllm#19579: [Bug]: V1 piecewise cudagraph capture size on ROCm is much higher than on cuda

| 字段 | 值 |
| --- | --- |
| Issue | [#19579](https://github.com/vllm-project/vllm/issues/19579) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: V1 piecewise cudagraph capture size on ROCm is much higher than on cuda

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The size of piecewise cudagraph is much higher on rocm (mi300) than on cuda (h100). See table below. Also, this issue seems to be specific to piecewise capture; when doing a fullgraph capture on rocm, the graph size is fine. **Note**: The issue is Not related to rccl/all_reduce etc. because the captured sizes below use TP=1 #### Instructions to reproduce the issue: Engine init logs contain the graph captured size. e.g: `VLLM_USE_V1=1 python examples/offline_inference/basic/generate.py` ``` INFO 06-12 19:49:27 [gpu_model_runner.py:2051] Graph capturing finished in 38 secs, took 6.32 GiB ``` | Model (V1 engine) | rocm | cuda | |---------------------|-----------|----------| | Llama-2-7b-hf | 2.97 GiB | 0.61 GiB | | Llama-2-70b-hf | 6.32 GiB | 1.35 GiB | ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: V1 piecewise cudagraph capture size on ROCm is much higher than on cuda bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug The size of piecewise cudagraph is much higher on rocm (mi300) t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ise cudagraph capture size on ROCm is much higher than on cuda bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug The size of piecewise cudagraph is much higher on rocm (mi300) than on cuda (h10...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: amples/offline_inference/basic/generate.py` ``` INFO 06-12 19:49:27 [gpu_model_runner.py:2051] Graph capturing finished in 38 secs, took 6.32 GiB ``` | Model (V1 engine) | rocm | cuda | |---------------------|----------...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: uce etc. because the captured sizes below use TP=1 #### Instructions to reproduce the issue: Engine init logs contain the graph captured size. e.g: `VLLM_USE_V1=1 python examples/offline_inference/basic/generate.py` ```...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: graph capture size on ROCm is much higher than on cuda bug;torch.compile;stale ### Your current environment ### 🐛 Describe the bug The size of piecewise cudagraph is much higher on rocm (mi300) than on cuda (h100). See...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
