# vllm-project/vllm#20458: [Installation]: Solved Bug: CMake `execute_process` fails to read `/proc/cpuinfo` without absolute path

| 字段 | 值 |
| --- | --- |
| Issue | [#20458](https://github.com/vllm-project/vllm/issues/20458) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Solved Bug: CMake `execute_process` fails to read `/proc/cpuinfo` without absolute path

### Issue 正文摘录

### Your current environment ```text Ubuntu, the most important is that all is standard here: which cat /bin/cat $ file /bin/cat /bin/cat: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=70bb40952afe7016b06511e5c96e926f1f4774ba, for GNU/Linux 3.2.0, stripped ``` I have quickly searched for `cpuinfo` problem in all issues, including closed ones and it seems to be new one. Gemini CLI solved it and wrote most of below: ### Bug: CMake `execute_process` fails to read `/proc/cpuinfo` without absolute path **Description:** When building vLLM with `VLLM_TARGET_DEVICE=cpu`, the CMake configuration fails because the `execute_process` command in `cmake/cpu_extension.cmake` is unable to read `/proc/cpuinfo`. The error message reported is "Failed to check CPU features via /proc/cpuinfo". **Reproduction Steps:** 1. Clone the vLLM repository. 2. Run `cmake . -DVLLM_TARGET_DEVICE=cpu -D VLLM_PYTHON_EXECUTABLE=/usr/bin/python3` **Expected Behavior:** The CMake configuration should complete successfully, detecting CPU features from `/proc/cpuinfo`. **Observed Behavior:** The CMake configuration fails with the error:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: Solved Bug: CMake `execute_process` fails to read `/proc/cpuinfo` without absolute path installation;stale ### Your current environment ```text Ubuntu, the most important is that all is standard here:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e5c96e926f1f4774ba, for GNU/Linux 3.2.0, stripped ``` I have quickly searched for `cpuinfo` problem in all issues, including closed ones and it seems to be new one. Gemini CLI solved it and wrote most of below: ### Bug:...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: scription:** When building vLLM with `VLLM_TARGET_DEVICE=cpu`, the CMake configuration fails because the `execute_process` command in `cmake/cpu_extension.cmake` is unable to read `/proc/cpuinfo`. The error message repo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: rocess` fails to read `/proc/cpuinfo` without absolute path installation;stale ### Your current environment ```text Ubuntu, the most important is that all is standard here: which cat /bin/cat $ file /bin/cat /bin/cat: E...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
