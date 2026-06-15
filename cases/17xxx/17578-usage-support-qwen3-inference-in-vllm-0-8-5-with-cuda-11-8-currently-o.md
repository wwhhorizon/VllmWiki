# vllm-project/vllm#17578: [Usage]: Support Qwen3 inference in vLLM==0.8.5 with CUDA 11.8 (currently only vLLM==0.6.1.post1 works)

| 字段 | 值 |
| --- | --- |
| Issue | [#17578](https://github.com/vllm-project/vllm/issues/17578) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Support Qwen3 inference in vLLM==0.8.5 with CUDA 11.8 (currently only vLLM==0.6.1.post1 works)

### Issue 正文摘录

I’m currently using a machine with CUDA 11.6 and Python 3.10, and vllm==0.6.1.post1 works fine in this setup, as instructed in the [official documentation](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html). However, it appears that the newly released Qwen3 models are only supported in vLLM >= 0.8.4, which is currently incompatible with my CUDA 11.6/11.8 setup. While attempting to install newer versions like vllm==0.8.5, I encountered multiple issues — particularly when building the wheel for xformers, which fails under my environment. I cannot upgrade my CUDA version on this machine due to environment constraints. This makes it difficult to use Qwen3 on many machines that haven’t upgraded to newer CUDA versions. I’d like to request: • Support for Qwen3 models on vLLM versions compatible with CUDA 11.8 • Or at least clearer documentation on version compatibility (vLLM ↔ CUDA ↔ model support) • Any guidance or workaround for building xformers under this setup would also be appreciated Thanks for your attention to this matter. I hope support can be added, and the documentation updated accordingly.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nd vllm==0.6.1.post1 works fine in this setup, as instructed in the [official documentation](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html). However, it appears that the newly released Qwen3 model...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Support Qwen3 inference in vLLM==0.8.5 with CUDA 11.8 (currently only vLLM==0.6.1.post1 works) usage I’m currently using a machine with CUDA 11.6 and Python 3.10, and vllm==0.6.1.post1 works fine in this setup,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage]: Support Qwen3 inference in vLLM==0.8.5 with CUDA 11.8 (currently only vLLM==0.6.1.post1 works) usage I’m currently using a machine with CUDA 11.6 and Python 3.10, and vllm==0.6.1.post1 works fine in this setup,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: many machines that haven’t upgraded to newer CUDA versions. I’d like to request: • Support for Qwen3 models on vLLM versions compatible with CUDA 11.8 • Or at least clearer documentation on version compatibility (vLLM ↔...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: as instructed in the [official documentation](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html). However, it appears that the newly released Qwen3 models are only supported in vLLM >= 0.8.4, which is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
