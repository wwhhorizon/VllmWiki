# vllm-project/vllm#34939: [CI Failure]: V1 e2e + engine : Cannot re-initialize CUDA in forked subprocess

| 字段 | 值 |
| --- | --- |
| Issue | [#34939](https://github.com/vllm-project/vllm/issues/34939) |
| 状态 | open |
| 标签 | stale;ci-failure |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI Failure]: V1 e2e + engine : Cannot re-initialize CUDA in forked subprocess

### Issue 正文摘录

### Name of failing test v1/e2e/test_kv_sharing_fast_prefill.py::test_kv_sharing_fast_prefill[*, *], v1/e2e/test_mamba_prefix_cache.py::test_mamba_prefix_cache ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test v1/e2e/test_kv_sharing_fast_prefill.py::test_kv_sharing_fast_prefill[True-False] v1/e2e/test_kv_sharing_fast_prefill.py::test_kv_sharing_fast_prefill[True-True] v1/e2e/test_kv_sharing_fast_prefill.py::test_kv_sharing_fast_prefill[False-False] v1/e2e/test_kv_sharing_fast_prefill.py::test_kv_sharing_fast_prefill[False-True] v1/e2e/test_mamba_prefix_cache.py::test_mamba_prefix_cache - all tests fail with the same `RuntimeError: Cannot re-initialize CUDA in forked subprocess.` error. ### 📝 History of failing test Started Feb 19th - https://buildkite.com/vllm/ci/builds/52218#019c74b4-5f0a-4a6c-b0e9-2b835f8f6963 ### CC List. cc @divakar-amd @sarckk most certainly not related to your changes but can you help take a look. Thanks 🙌

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: V1 e2e + engine : Cannot re-initialize CUDA in forked subprocess stale;ci-failure ### Name of failing test v1/e2e/test_kv_sharing_fast_prefill.py::test_kv_sharing_fast_prefill[*, *], v1/e2e/test_mamba_prefi
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ilure]: V1 e2e + engine : Cannot re-initialize CUDA in forked subprocess stale;ci-failure ### Name of failing test v1/e2e/test_kv_sharing_fast_prefill.py::test_kv_sharing_fast_prefill[*, *], v1/e2e/test_mamba_prefix_cac...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: t_mamba_prefix_cache ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test v1/e2e/test_kv_sharing_fast_prefill...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CI Failure]: V1 e2e + engine : Cannot re-initialize CUDA in forked subprocess stale;ci-failure ### Name of failing test v1/e2e/test_kv_sharing_fast_prefill.py::test_kv_sharing_fast_prefill[*, *], v1/e2e/test_mamba_pref...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e2e/test_kv_sharing_fast_prefill.py::test_kv_sharing_fast_prefill[True-False] v1/e2e/test_kv_sharing_fast_prefill.py::test_kv_sharing_fast_prefill[True-True] v1/e2e/test_kv_sharing_fast_prefill.py::test_kv_sharing_fast_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
