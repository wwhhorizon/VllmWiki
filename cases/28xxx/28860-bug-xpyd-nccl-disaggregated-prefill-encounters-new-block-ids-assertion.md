# vllm-project/vllm#28860: [Bug]: xPyD NCCL disaggregated prefill encounters new_block_ids AssertionError under high benchmark concurrency

| 字段 | 值 |
| --- | --- |
| Issue | [#28860](https://github.com/vllm-project/vllm/issues/28860) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: xPyD NCCL disaggregated prefill encounters new_block_ids AssertionError under high benchmark concurrency

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am using the nightly version of vLLM 0.11.1rc7. For the [exemplar xPyD usage script](https://github.com/vllm-project/vllm/blob/577bb34fffc83598d3e4940f8492c122d9e3318d/examples/online_serving/disaggregated_serving_p2p_nccl_xpyd/disagg_example_p2p_nccl_xpyd.sh), if we (1) set to 2P2D & reduce the gpu-mem-utilization (2) increase the benchmark workload, AssertionError occurs in one of the prefill instance. partial error logs in `prefill1.log`: ``` [1;36m(EngineCore_DP0 pid=1722095)[0;0m Traceback (most recent call last): [1;36m(EngineCore_DP0 pid=1722095)[0;0m File "/hpc2ssd/JH_DATA/spooler/xzhanggb/miniconda3/envs/vllm_nightly/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap [1;36m(EngineCore_DP0 pid=1722095)[0;0m self.run() [1;36m(EngineCore_DP0 pid=1722095)[0;0m File "/hpc2ssd/JH_DATA/spooler/xzhanggb/miniconda3/envs/vllm_nightly/lib/python3.11/multiprocessing/process.py", line 108, in run [1;36m(EngineCore_DP0 pid=1722095)[0;0m self._target(*self._args, **self._kwargs) [1;36m(EngineCore_DP0 pid=1722095)[0;0m File "/hpc2ssd/JH_DATA/spooler/xzhanggb/miniconda3/envs/vllm_nightly/lib/python3.11/site-...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r current environment ### 🐛 Describe the bug I am using the nightly version of vLLM 0.11.1rc7. For the [exemplar xPyD usage script](https://github.com/vllm-project/vllm/blob/577bb34fffc83598d3e4940f8492c122d9e3318d/exam...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: xPyD NCCL disaggregated prefill encounters new_block_ids AssertionError under high benchmark concurrency bug ### Your current environment ### 🐛 Describe the bug I am using the nightly version of vLLM 0.11.1rc7. F...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: sh) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: xPyD NCCL disaggregated prefill encounters new_block_ids AssertionError under high benchmark concurrency bug ### Your current environment ### 🐛 Describe the bug I am using the nightly version of vLLM 0.11.1rc7. F...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: disaggregated prefill encounters new_block_ids AssertionError under high benchmark concurrency bug ### Your current environment ### 🐛 Describe the bug I am using the nightly version of vLLM 0.11.1rc7. For the [exemplar...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
