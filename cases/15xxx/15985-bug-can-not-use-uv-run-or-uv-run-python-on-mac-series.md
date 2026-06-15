# vllm-project/vllm#15985: [Bug]: can not use uv run or uv run python on mac series

| 字段 | 值 |
| --- | --- |
| Issue | [#15985](https://github.com/vllm-project/vllm/issues/15985) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: can not use uv run or uv run python on mac series

### Issue 正文摘录

### Your current environment I also raise an issue on uv side https://github.com/astral-sh/uv/issues/12578 and I think its the same issue as #15953 ### 🐛 Describe the bug error: ``` ⠴ Resolving dependencies... × No solution found when resolving dependencies for split (python_full_version >= '3.12' and platform_machine == 'x86_64' and sys_platform == 'darwin'): ╰─▶ Because there is no version of torch{platform_machine == 'x86_64'}==2.6.0+cpu and your project depends on torch{platform_machine == 'x86_64'}==2.6.0+cpu, we can conclude that your project's requirements are unsatisfiable. And because your project requires vllm[audio], we can conclude that your project's requirements are unsatisfiable. ``` OS macOS m3 uv and vllm both latest reproduce: 1. clone vllm && cd vllm 2. uv python pin 3.12 3. uv pip install -r requirements/cpu.txt 4. uv pip install -e . then `uv run python failed` with the error message debug: cat requirements/cpu.txt ``` -r common.txt # Dependencies for CPUs torch==2.6.0+cpu; platform_machine == "x86_64" torch==2.6.0; platform_system == "Darwin" torch==2.6.0; platform_machine == "ppc64le" or platform_machine == "aarch64" torch==2.7.0.dev20250304; platform_machin...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ue as #15953 ### 🐛 Describe the bug error: ``` ⠴ Resolving dependencies... × No solution found when resolving dependencies for split (python_full_vers
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ct's requirements are unsatisfiable. ``` OS macOS m3 uv and vllm both latest reproduce: 1. clone vllm && cd vllm 2. uv python pin 3.12 3. uv pip install -r requirements/cpu.txt 4. uv pip install -e . then `uv run python...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: equirements are unsatisfiable. ``` OS macOS m3 uv and vllm both latest reproduce: 1. clone vllm && cd vllm 2. uv python pin 3.12 3. uv pip install -r requirements/cpu.txt 4. uv pip install -e . then `uv run python faile...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: in" torch==2.6.0; platform_machine == "ppc64le" or platform_machine == "aarch64" torch==2.7.0.dev20250304; platform_machine == "s390x" # required for the image processor of minicpm-o-2_6, this must be updated alongside...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: can not use uv run or uv run python on mac series bug;stale ### Your current environment I also raise an issue on uv side https://github.com/astral-sh/uv/issues/12578 and I think its the same issue as #15953 ###...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
