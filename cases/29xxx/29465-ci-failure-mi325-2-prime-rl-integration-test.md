# vllm-project/vllm#29465: [CI Failure]: mi325_2: Prime-RL Integration Test

| 字段 | 值 |
| --- | --- |
| Issue | [#29465](https://github.com/vllm-project/vllm/issues/29465) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: mi325_2: Prime-RL Integration Test

### Issue 正文摘录

### Name of failing test `bash .buildkite/scripts/run-prime-rl-test.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **3 Prime-RL integration tests** - vLLM server health check timeout during test setup #### Failed Tests: 1. `test_no_error` in `tests/integration/test_rl.py` 2. `test_no_error_resume` in `tests/integration/test_rl.py` 3. `test_check_reward` in `tests/integration/test_rl.py` **Failure:** RuntimeError at `tests/conftest.py:198` - "vLLM server did not become healthy within timeout" **Configuration:** - Integration tests with Prime-RL framework - Test timeout: ~180 seconds (3 minutes) - Server health check failure during pytest fixture setup - Tests show ERROR status (setup failure) not FAILED (test failure) - 1 test skipped, 3 errored during setup **Likely cause:** vLLM server fails to start or reach healthy state on ROCm within the 3-minute timeout during Prime-RL integration test setup. The server health check waits for the `/health` endpoint to respond but times out, preventing any tests from running. This is likely caused due to incompatibility betw...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: mi325_2: Prime-RL Integration Test ci-failure ### Name of failing test `bash .buildkite/scripts/run-prime-rl-test.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by ext
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ailing test `bash .buildkite/scripts/run-prime-rl-test.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: run-prime-rl-test.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test **3 Prime-RL integration tests** -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: **Likely cause:** vLLM server fails to start or reach healthy state on ROCm within the 3-minute timeout during Prime-RL integration test setup. The server health check waits for the `/health` endpoint to respond but tim...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [CI Failure]: mi325_2: Prime-RL Integration Test ci-failure ### Name of failing test `bash .buildkite/scripts/run-prime-rl-test.sh` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by exte...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
