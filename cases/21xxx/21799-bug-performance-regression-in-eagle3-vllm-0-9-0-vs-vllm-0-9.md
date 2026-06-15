# vllm-project/vllm#21799: [Bug]: Performance Regression in Eagle3: vLLM 0.9.0 vs. vLLM 0.9.

| 字段 | 值 |
| --- | --- |
| Issue | [#21799](https://github.com/vllm-project/vllm/issues/21799) |
| 状态 | closed |
| 标签 | bug;performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Performance Regression in Eagle3: vLLM 0.9.0 vs. vLLM 0.9.

### Issue 正文摘录

### Name of failing test vllm\v1\spec_decode\eagle.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Hello, during my testing, I found that the performance of eagle3 in vLLM 0.9.0 is worse compared to vLLM 0.9.2. Is the eagle3 architecture different between the two versions? Are there other changes or modifications? ### 📝 History of failing test Hello, during my testing, I found that the performance of eagle3 in vLLM 0.9.0 is worse compared to vLLM 0.9.2. Is the eagle3 architecture different between the two versions? Are there other changes or modifications? ### CC List. _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rformance Regression in Eagle3: vLLM 0.9.0 vs. vLLM 0.9. bug;performance;stale ### Name of failing test vllm\v1\spec_decode\eagle.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by ext...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Performance Regression in Eagle3: vLLM 0.9.0 vs. vLLM 0.9. bug;performance;stale ### Name of failing test vllm\v1\spec_decode\eagle.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caus...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: \spec_decode\eagle.py ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test Hello, during my testing, I found...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ared to vLLM 0.9.2. Is the eagle3 architecture different between the two versions? Are there other changes or modifications? ### 📝 History of failing test Hello, during my testing, I found that the performance of eagle3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e of eagle3 in vLLM 0.9.0 is worse compared to vLLM 0.9.2. Is the eagle3 architecture different between the two versions? Are there other changes or modifications? ### 📝 History of failing test Hello, during my testing,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
