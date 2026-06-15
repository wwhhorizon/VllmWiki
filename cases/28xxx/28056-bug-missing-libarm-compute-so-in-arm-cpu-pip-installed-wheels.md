# vllm-project/vllm#28056: [Bug]: Missing libarm_compute.so in Arm CPU pip installed wheels

| 字段 | 值 |
| --- | --- |
| Issue | [#28056](https://github.com/vllm-project/vllm/issues/28056) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Missing libarm_compute.so in Arm CPU pip installed wheels

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We now have vllm wheels for Arm CPUs in pypi thanks to https://github.com/vllm-project/vllm/pull/26931 and https://github.com/vllm-project/vllm/pull/27331 You can install Arm CPU wheels with: ``` pip install --pre vllm==0.11.1rc3+cpu --extra-index-url https://wheels.vllm.ai/0.11.1rc3%2Bcpu/ ``` However it will currently fail, unless you ldpreload ACL: ``` WARNING 10-29 12:33:18 [interface.py:171] Failed to import from vllm._C: ImportError('libarm_compute.so: cannot open shared object file: No such file or directory') We need to figure out how to package libarm_compute.so in the wheel ``` Best way to reproduce this locally is: - build vllm from main locally with `VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel` - remove `vllm/deps` which contains the libarm_compute.so - pip install the wheel you built then you will run into the issue (because it will try to load libarm_compute.so under vllm/.deps/arm_compute-src/build/) Note: ACL/oneDNN are built in vllm here: We need to figure out how to bundle `libarm_compute.so` in the wheel to avoid this. ### Before submitting a new issue... - [x] Make sure you already searched for relevan...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Missing libarm_compute.so in Arm CPU pip installed wheels bug ### Your current environment ### 🐛 Describe the bug We now have vllm wheels for Arm CPUs in pypi thanks to https://github.com/vllm-project/vllm/pull/2...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: gure out how to package libarm_compute.so in the wheel ``` Best way to reproduce this locally is: - build vllm from main locally with `VLLM_TARGET_DEVICE=cpu python3 setup.py bdist_wheel` - remove `vllm/deps` which cont...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
