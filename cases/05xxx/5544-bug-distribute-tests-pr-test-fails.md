# vllm-project/vllm#5544: [Bug]: Distribute Tests PR test fails

| 字段 | 值 |
| --- | --- |
| Issue | [#5544](https://github.com/vllm-project/vllm/issues/5544) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Distribute Tests PR test fails

### Issue 正文摘录

### Your current environment ``` vLLM version 0.5.0.post1 ``` ### 🐛 Describe the bug Hello! I would like to know if the `tests/distributed/test_utils.py` file (Merged at #5473) might be causing errors during the **Distribute Tests** process on BuildKite. When I checked #5422 and #5412, I found that both PRs failed during the Distribute Tests process. The reason for the failure is as follows: ``` [2024-06-14T00:24:15Z] Running 1 items in this shard: tests/distributed/test_utils.py::test_cuda_device_count_stateless [2024-06-14T00:24:15Z] [2024-06-14T00:24:30Z] distributed/test_utils.py::test_cuda_device_count_stateless 2024-06-14 00:24:30,636 INFO worker.py:1753 -- Started a local Ray instance. [2024-06-14T00:24:33Z] FAILED [2024-06-14T00:24:33Z] [2024-06-14T00:24:33Z] =================================== FAILURES =================================== [2024-06-14T00:24:33Z] _______________________ test_cuda_device_count_stateless _______________________ [2024-06-14T00:24:33Z] [2024-06-14T00:24:33Z] def test_cuda_device_count_stateless(): [2024-06-14T00:24:33Z] """Test that cuda_device_count_stateless changes return value if [2024-06-14T00:24:33Z] CUDA_VISIBLE_DEVICES is changed.""" [20...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: istribute Tests PR test fails bug ### Your current environment ``` vLLM version 0.5.0.post1 ``` ### 🐛 Describe the bug Hello! I would like to know if the `tests/distributed/test_utils.py` file (Merged at #5473) might be...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 5Z] Running 1 items in this shard: tests/distributed/test_utils.py::test_cuda_device_count_stateless [2024-06-14T00:24:15Z] [2024-06-14T00:24:30Z] distributed/test_utils.py::test_cuda_device_count_stateless 2024-06-14 0...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: he plugin docker command hook exited with status 1 ``` Since I am not an expert in the Ray framework, so I am not sure how critical the difference between `0, 1` and `1, 0`. **I think the fact that "1,0" was output in a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: Distribute Tests PR test fails bug ### Your current environment ``` vLLM version 0.5.0.post1 ``` ### 🐛 Describe the bug Hello! I would like to know if the `tests/distributed/test_utils.py` file (Merged at #5473)...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
