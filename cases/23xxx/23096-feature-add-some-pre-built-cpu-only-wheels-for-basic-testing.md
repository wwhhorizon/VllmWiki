# vllm-project/vllm#23096: [Feature]: add some pre-built CPU-only wheels for basic testing

| 字段 | 值 |
| --- | --- |
| Issue | [#23096](https://github.com/vllm-project/vllm/issues/23096) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: add some pre-built CPU-only wheels for basic testing

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This is important for educational purposes: being able to install vllm with cpu-only PyTorch and test some vllm features (e.g. `min_tokens` or `truncate_prompt_tokens`) - for this, maybe even being able to run 0.6B models or similar is sufficient. Even some basic, not performant binaries (like those which can be built on GitHub Actions runners) would be helpful https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html#pre-built-wheels --- - Currently, using vllm on a CPU-only machine leads to following when creating an instance of `vllm.LLM(...)`: `RuntimeError: Device string must not be empty` - is rather strange error for this - And also it prints for some reason `No platform detected, vLLM is running on UnspecifiedPlatform`, should it not auto-detect CPU as a platform and not even try to dlopen `libcuda.so` (could it not check that `torch.cuda.get_device_count()` returns 0?) and not try loading any other CUDA libs or import GPU-only packages? Might be a good idea of allowing an explicit `device` / `device_type` argument in `vllm.LLM(...)` https://docs.vllm.ai/en/latest/api/vllm/index.html#vllm.LLM ? ``` INFO 08-18 12:41:19 [__i...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Feature]: add some pre-built CPU-only wheels for basic testing feature request;unstale ### 🚀 The feature, motivation and pitch This is important for educational purposes: being able to install vllm with cpu-only PyTorc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: `truncate_prompt_tokens`) - for this, maybe even being able to run 0.6B models or similar is sufficient. Even some basic, not performant binaries (like those which can be built on GitHub Actions runners) would be helpfu...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: add some pre-built CPU-only wheels for basic testing feature request;unstale ### 🚀 The feature, motivation and pitch This is important for educational purposes: being able to install vllm with cpu-only PyTorc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ould it not auto-detect CPU as a platform and not even try to dlopen `libcuda.so` (could it not check that `torch.cuda.get_device_count()` returns 0?) and not try loading any other CUDA libs or import GPU-only packages?...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: add some pre-built CPU-only wheels for basic testing feature request;unstale ### 🚀 The feature, motivation and pitch This is important for educational purposes: being able to install vllm with cpu-only PyTorc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
