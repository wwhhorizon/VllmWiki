# vllm-project/vllm#38097: [ROCm][CI]:  `create_new_process_for_each_test("spawn")` may silently skip tests without `__main__` entrypoint

| 字段 | 值 |
| --- | --- |
| Issue | [#38097](https://github.com/vllm-project/vllm/issues/38097) |
| 状态 | closed |
| 标签 | rocm;ci-failure |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [ROCm][CI]:  `create_new_process_for_each_test("spawn")` may silently skip tests without `__main__` entrypoint

### Issue 正文摘录

### Summary `create_new_process_for_each_test("spawn")` runs tests by invoking `python -m ` in a subprocess. If the test file has no `if __name__ == "__main__":` block, the subprocess exits successfully without running any tests, and the decorator interprets this as a pass. So, tests silently appear to pass when they are not actually executed. This affects ROCm since the default method is `"spawn"` when no argument is provided - Related issue: #34323 cc @DarkLight1337 ### Root cause In [`tests/utils.py:1405`](https://github.com/vllm-project/vllm/blob/main/tests/utils.py#L1405), the spawn path runs: ```python cmd = [sys.executable, "-m", f"{module_name}"] returned = subprocess.run(cmd, input=input_bytes, capture_output=True, env=env) returned.check_returncode() # exit code 0 (means "passed") ``` When a test file has no `__main__` block, `python -m tests.some.test_file` imports the module, does nothing, and exits with code 0. The decorator sees a successful return code and considers the test passed. The `"fork"` path does not have this problem because it calls the test function directly in the forked process. ### Possible fixes 1. Fix the spawn implementation and instead of running...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [ROCm][CI]: `create_new_process_for_each_test("spawn")` may silently skip tests without `__main__` entrypoint rocm;ci-failure ### Summary `create_new_process_for_each_test("spawn")` runs tests by invoking `python -m ` i...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [ROCm][CI]: `create_new_process_for_each_test("spawn")` may silently skip tests without `__main__` entrypoint rocm;ci-failure ### Summary `create_new_process_for_each_test("spawn")` runs tests by invoking `python -m ` i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [ROCm][CI]: `create_new_process_for_each_test("spawn")` may silently skip tests without `__main__` entrypoint rocm;ci-failure ### Summary `create_new_process_for_each_test("spawn")` runs tests by invoking `python -m `
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ` in a subprocess. If the test file has no `if __name__ == "__main__":` block, the subprocess exits successfully without running any tests, and the decorator interprets this as a pass. So, tests silently appear to pass...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
