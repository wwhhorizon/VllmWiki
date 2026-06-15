# vllm-project/vllm#25818: [Bug]: When using two NUMA nodes for TP, one node has a long AllReduce latency, while the other node has a long gemm latency. 

| 字段 | 值 |
| --- | --- |
| Issue | [#25818](https://github.com/vllm-project/vllm/issues/25818) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When using two NUMA nodes for TP, one node has a long AllReduce latency, while the other node has a long gemm latency. 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When I use two NUMA nodes for TP inference, as shown in the figure below, the AllReduce time of TP0 is very long, but the GEMM calculation time of TP1 is longer than TP0. I have set VLLM_CPU_OMP_THREADS_BIND="0-31|32-63". TP0: TP1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: When using two NUMA nodes for TP, one node has a long AllReduce latency, while the other node has a long gemm latency. bug ### Your current environment ### 🐛 Describe the bug When I use two NUMA nodes for TP infe...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: . correctness ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current env...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
