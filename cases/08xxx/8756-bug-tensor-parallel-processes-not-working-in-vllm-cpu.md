# vllm-project/vllm#8756: [Bug]: tensor parallel processes not working in vllm_cpu

| 字段 | 值 |
| --- | --- |
| Issue | [#8756](https://github.com/vllm-project/vllm/issues/8756) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: tensor parallel processes not working in vllm_cpu

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug According to the link below, it says that the sensor parallel is supported in cpu, but it does not work. https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html#related-runtime-environment-variables ex) export VLLM_CPU_OMP_THREADS_BIND="0-17|18-35" but ``` INFO 09-24 10:50:13 selector.py:183] Cannot use _Backend.FLASH_ATTN backend on CPU. INFO 09-24 10:50:13 selector.py:128] Using Torch SDPA backend. INFO 09-24 10:50:13 cpu_worker.py:211] OMP threads binding of Process 1563: INFO 09-24 10:50:13 cpu_worker.py:211] OMP tid: 1563, core 0 INFO 09-24 10:50:13 cpu_worker.py:211] OMP tid: 1754, core 1 INFO 09-24 10:50:13 cpu_worker.py:211] OMP tid: 1755, core 2 INFO 09-24 10:50:13 cpu_worker.py:211] OMP tid: 1756, core 3 INFO 09-24 10:50:13 cpu_worker.py:211] OMP tid: 1757, core 4 INFO 09-24 10:50:13 cpu_worker.py:211] OMP tid: 1758, core 5 INFO 09-24 10:50:13 cpu_worker.py:211] OMP tid: 1759, core 6 INFO 09-24 10:50:13 cpu_worker.py:211] OMP tid: 1760, core 7 INFO 09-24 10:50:13 cpu_worker.py:211] OMP tid: 1761, core 8 INFO 09-24 10:50:13 cpu_worker.py:211] OMP tid: 1762, core 9 INFO 09-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: del Input Dumps _No response_ ### 🐛 Describe the bug According to the link below, it says that the sensor parallel is supported in cpu, but it does not work. https://docs.vllm.ai/en/latest/getting_started/cpu-installati...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ="0-17|18-35" but ``` INFO 09-24 10:50:13 selector.py:183] Cannot use _Backend.FLASH_ATTN backend on CPU. INFO 09-24 10:50:13 selector.py:128] Using Torch SDPA backend. INFO 09-24 10:50:13 cpu_worker.py:211] OMP threads...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 1a) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ocesses not working in vllm_cpu bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug According to the link below, it says that the sensor parallel is supported in cpu, but it does...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: lel is supported in cpu, but it does not work. https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html#related-runtime-environment-variables ex) export VLLM_CPU_OMP_THREADS_BIND="0-17|18-35" but ``` INFO 09...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
