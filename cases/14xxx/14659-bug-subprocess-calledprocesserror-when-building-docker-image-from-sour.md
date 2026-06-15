# vllm-project/vllm#14659: [Bug]:  `subprocess.CalledProcessError` when building docker image from source on AMD MI210

| 字段 | 值 |
| --- | --- |
| Issue | [#14659](https://github.com/vllm-project/vllm/issues/14659) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  `subprocess.CalledProcessError` when building docker image from source on AMD MI210

### Issue 正文摘录

### Your current environment I have trouble building docker image right now. ### 🐛 Describe the bug The raised error: > 1913.1 File "/usr/local/lib/python3.12/dist-packages/setuptools/_distutils/cmd.py", line 339, in run_command > 1913.1 self.distribution.run_command(command) > 1913.1 File "/usr/local/lib/python3.12/dist-packages/setuptools/dist.py", line 999, in run_command > 1913.1 super().run_command(command) > 1913.1 File "/usr/local/lib/python3.12/dist-packages/setuptools/_distutils/dist.py", line 1002, in run_command > 1913.1 cmd_obj.run() > 1913.1 File "/usr/local/lib/python3.12/dist-packages/setuptools/_distutils/command/build.py", line 136, in run > 1913.1 self.run_command(cmd_name) > 1913.1 File "/usr/local/lib/python3.12/dist-packages/setuptools/_distutils/cmd.py", line 339, in run_command > 1913.1 self.distribution.run_command(command) > 1913.1 File "/usr/local/lib/python3.12/dist-packages/setuptools/dist.py", line 999, in run_command > 1913.1 super().run_command(command) > 1913.1 File "/usr/local/lib/python3.12/dist-packages/setuptools/_distutils/dist.py", line 1002, in run_command > 1913.1 cmd_obj.run() > 1913.1 File "/app/vllm/setup.py", line 267, in run > 1913.1 su...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: `subprocess.CalledProcessError` when building docker image from source on AMD MI210 bug ### Your current environment I have trouble building docker image right now. ### 🐛 Describe the bug The raised error: > 1913...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: mmand '['cmake', '--build', '.', '-j=192', '--target=_moe_C', '--target=_rocm_C', '--target=_C']' returned non-zero exit status 1. > ------ > Dockerfile.rocm:40 > -------------------- > 39 | # Build vLLM > 40 | >>> RUN...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ledProcessError: Command '['cmake', '--build', '.', '-j=192', '--target=_moe_C', '--target=_rocm_C', '--target=_C']' returned non-zero exit status 1. > ------ > Dockerfile.rocm:40 > -------------------- > 39 | # Build v...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
