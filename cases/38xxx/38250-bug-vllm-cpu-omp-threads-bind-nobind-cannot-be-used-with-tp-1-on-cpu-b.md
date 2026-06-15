# vllm-project/vllm#38250: [Bug]: VLLM_CPU_OMP_THREADS_BIND=nobind cannot be used with tp>1 on CPU backends

| 字段 | 值 |
| --- | --- |
| Issue | [#38250](https://github.com/vllm-project/vllm/issues/38250) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM_CPU_OMP_THREADS_BIND=nobind cannot be used with tp>1 on CPU backends

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug VLLM when using the multiproc executor for tp>1 initializes OMP more than once. As a result, it is impossible to define more than one "PLACE" (as per OMP spec) to run each of the TP workers and it is not possible to define correct thread bindings. Example: Let's try to run an 8 core system at tp=2. We set the OMP environment as follows: OMP_PLACES="{0,1,2,3},{4,5,6,7}" OMP_PROC_BIND=True OMP_NUM_THREADS=8 VLLM initializes OMP once. That initialization reduces the CPU affinity mask which permits which cores can be used to "{0, 1, 2, 3}". Then out of this environment it invokes the initialization again, but now it has 4 cores available and as a result it does not have enough cores to allocate 8 threads. Various other approaches result in anything from 1 core/thread to 4 cores/threads available and contention between the workers for the same OMP_PLACE. How to reproduce - try any of the exact binding examples in the OMP spec: https://www.openmp.org/spec-html/5.0/openmpch6.html https://www.openmp.org/spec-html/5.0/openmpse53.html#x292-20600006.5 They all fail. How to debug: enable OMP_DISPLAY_ENV (and optionally OMP_DISPLAY_AFFINITY)...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: VLLM_CPU_OMP_THREADS_BIND=nobind cannot be used with tp>1 on CPU backends bug ### Your current environment ### 🐛 Describe the bug VLLM when using the multiproc executor for tp>1 initializes OMP more than once. As...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ut. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: able and contention between the workers for the same OMP_PLACE. How to reproduce - try any of the exact binding examples in the OMP spec: https://www.openmp.org/spec-html/5.0/openmpch6.html https://www.openmp.org/spec-h...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ed questions. correctness ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
