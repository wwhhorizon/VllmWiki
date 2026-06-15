# vllm-project/vllm#24246: [Installation]: Warning on char conversion on aarch64

| 字段 | 值 |
| --- | --- |
| Issue | [#24246](https://github.com/vllm-project/vllm/issues/24246) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Warning on char conversion on aarch64

### Issue 正文摘录

### Your current environment ```text ``` I wanted to just report that I see the following when building from source which seems to assume `char` is `signed` which on aarch64 the default `char` is `unsigned`. I couldn't see any specific issue covering this. To remove the following warnings the fork vllm-flash-attn (where I could not raise an issue) may require a fix to cast using `(signed char)` instead. Example warning I see: ``` /vllm/container/vllm/.deps/vllm-flash-attn-src/csrc/flash_attn/flash_api_sparse.cpp: In function ‘std::vector flash::mha_fwd_sparse(at: :Tensor&, const at::Tensor&, const at::Tensor&, const at::Tensor&, const at::Tensor&, const at::Tensor&, const at::Tensor&, const std::optional &, const std::optional &, double, double, bool, double, bool, std::optional )’: /vllm/container/vllm/.deps/vllm-flash-attn-src/csrc/flash_attn/flash_api_sparse.cpp:234:38: warning: narrowing conversion of ‘(char)(& q)->at::Tens or:: .at::TensorBase::get_device()’ from ‘char’ to ‘c10::DeviceIndex’ {aka ‘signed char’} [-Wnarrowing] 234 | at::cuda::CUDAGuard device_guard{(char)q.get_device()}; | ^~~~~~~~~~~~~~~~~~~~ ``` ### How you are installing vllm Following guide on building from...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Warning on char conversion on aarch64 installation;stale ### Your current environment ```text ``` I wanted to just report that I see the following when building from source which seems to assume `char`
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: Warning on char conversion on aarch64 installation;stale ### Your current environment ```text ``` I wanted to just report that I see the following when building from source which seems to assume `char` i...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: Warning on char conversion on aarch64 installation;stale ### Your current environment ```text ``` I wanted to just report that I see the following when building from source which seems to assume `char` i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development attention_kv_cache;ci_build cuda build_error Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
