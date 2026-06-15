# vllm-project/vllm#28982: [Bug]: CPU Backend: vllm / torch.compile issue with torch > 2.8

| 字段 | 值 |
| --- | --- |
| Issue | [#28982](https://github.com/vllm-project/vllm/issues/28982) |
| 状态 | closed |
| 标签 | bug;torch.compile;cpu |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CPU Backend: vllm / torch.compile issue with torch > 2.8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Steps to reproduce: - Build vllm on CPU with `torch==2.9.1` by running: `VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel` - Then run ` vllm bench throughput --input_len 32 --max_model_len 1024` We hit this inductor error: ``` (EngineCore_DP0 pid=73386) File "/Users/mgoin/code/venvs/vllm/lib/python3.12/site-packages/torch/_inductor/scheduler.py", line 5345, in _codegen_partitions (EngineCore_DP0 pid=73386) self._codegen(partition) (EngineCore_DP0 pid=73386) File "/Users/mgoin/code/venvs/vllm/lib/python3.12/site-packages/torch/_inductor/scheduler.py", line 5440, in _codegen (EngineCore_DP0 pid=73386) raise AssertionError(f"{type(self)=}") (EngineCore_DP0 pid=73386) torch._inductor.exc.InductorError: AssertionError: type(self)= ``` This is not the case with `torch==2.8` which is the current version used in `vllm/requirements/cpu.txt` However it's problem for Darwin which uses `torch==2.9` and a blocker for updating to `torch==2.9` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/e...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: CPU Backend: vllm / torch.compile issue with torch > 2.8 bug;torch.compile;cpu ### Your current environment ### 🐛 Describe the bug Steps to reproduce: - Build vllm on CPU with `torch==2.9.1` by running: `VLLM_TAR...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: _TARGET_DEVICE=cpu python3 setup.py bdist_wheel` - Then run ` vllm bench throughput --input_len 32 --max_model_len 1024` We hit this inductor error: ``` (EngineCore_DP0 pid=73386) File "/Users/mgoin/code/venvs/vllm/lib/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: CPU Backend: vllm / torch.compile issue with torch > 2.8 bug;torch.compile;cpu ### Your current environment ### 🐛 Describe the bug Steps to reproduce: - Build vllm on CPU with `torch==2.9.1` by running: `VLLM_TAR...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: le;cpu ### Your current environment ### 🐛 Describe the bug Steps to reproduce: - Build vllm on CPU with `torch==2.9.1` by running: `VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel` - Then run ` vllm bench throughput...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .9` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
