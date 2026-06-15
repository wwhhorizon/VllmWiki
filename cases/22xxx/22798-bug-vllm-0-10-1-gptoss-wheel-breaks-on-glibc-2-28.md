# vllm-project/vllm#22798: [Bug]: vllm 0.10.1+gptoss wheel breaks on glibc 2.28

| 字段 | 值 |
| --- | --- |
| Issue | [#22798](https://github.com/vllm-project/vllm/issues/22798) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.10.1+gptoss wheel breaks on glibc 2.28

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Issue description** The `vllm-0.10.1+gptoss‑cp38‑abi3‑linux_x86_64.whl` fails to import on a system that only provides **glibc 2.28**. The import error ends with: ``` ImportError: /lib64/libc.so.6: version `GLIBC_2.32' not found (required by .../_C.abi3.so) ``` **Why this happens** The wheel is built for **many‑linux 2020** (or later) and therefore links against **glibc ≥ 2.32**. Our compute nodes run **glibc 2.28** (e.g. CentOS 7). When Python tries to load `_C.abi3.so`, the dynamic linker cannot locate `GLIBC_2.32`, so an ImportError is raised. **Reproduction steps** 1. Install the wheel in a Python 3.12 environment. 2. Execute on a machine with glibc 2.28 (CentOS 7, RHEL 7, etc.). 3. Run `python -c "import vllm"` and observe the ImportError. **Expected behavior** The wheel should load successfully on **many‑linux_2_28** (glibc 2.28) platforms, or the documentation should clearly state that a newer glibc version is required. **Actual behavior** ImportError is raised, stopping any downstream workflow. **Environment** - OS: CentOS 7 (glibc 2.28) - Python: 3.12 - vllm: 0.10.1+gptoss - CUDA: 12.x (if GPU is used) - Traceback show...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Bug]: vllm 0.10.1+gptoss wheel breaks on glibc 2.28 bug;unstale ### Your current environment ### 🐛 Describe the bug **Issue description** The `vllm-0.10.1+gptoss‑cp38‑abi3‑linux_x86_64.whl` fails to import on a system...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: - OS: CentOS 7 (glibc 2.28) - Python: 3.12 - vllm: 0.10.1+gptoss - CUDA: 12.x (if GPU is used) - Traceback shown above. **Historical context** - PyTorch official wheels have long supported **many‑linux 2.28** (and even...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: links against glibc 2.17 and works on older systems. 2. Update the CI configuration (e.g., `cibuildwheel --manylinux 2_28`) to generate the compatible wheel. 3. Document the minimal glibc version in the README and relea...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: arallel;frontend_api;hardware_porting;model_support cuda;kernel;operator;triton build_error;crash;import_error env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vllm 0.10.1+gptoss wheel breaks on glibc 2.28 bug;unstale ### Your current environment ### 🐛 Describe the bug **Issue description** The `vllm-0.10.1+gptoss‑cp38‑abi3‑linux_x86_64.whl` fails to import on a system...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
