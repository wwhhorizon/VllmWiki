# vllm-project/vllm#36167: [Bug]: Engine initialization failure with Qwen3 Omni on Strix Halo/ROCM

| 字段 | 值 |
| --- | --- |
| Issue | [#36167](https://github.com/vllm-project/vllm/issues/36167) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Engine initialization failure with Qwen3 Omni on Strix Halo/ROCM

### Issue 正文摘录

### Your current environment I couldnt get the collect_env.py working on NixOS vllm: 0.16.0 rocm: 7.1.1/7.1.52802-9999 python 3.13.12 hardware: AMD RYZEN AI MAX+ 395 w/ Radeon 8060S ### 🐛 Describe the bug When I run the following command, i hit a "Engine core initialization failed" ```sh $ vllm serve Qwen/Qwen3-Omni-30B-A3B-Instruct ``` Crash Log: [https://gist.github.com/Eoghanmc22/91da3def96afe0c87f2e3d1b7f5df0b7](https://gist.github.com/Eoghanmc22/91da3def96afe0c87f2e3d1b7f5df0b7) The relevant part of the log appears to be ```text (EngineCore_DP0 pid=160843) ERROR 03-05 12:36:31 [core.py:1006] hip runtime failed to load. (EngineCore_DP0 pid=160843) ERROR 03-05 12:36:31 [core.py:1006] Error: Please provide architecture for which code is to be generated. ``` Note: I tested the gpt-oss-20b model which works without issue, the problem appears to be specific to qwen3 omni. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Engine initialization failure with Qwen3 Omni on Strix Halo/ROCM bug;rocm ### Your current environment I couldnt get the collect_env.py working on NixOS vllm: 0.16.0 rocm: 7.1.1/7.1.52802-9999 python 3.13.12 hard...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Engine initialization failure with Qwen3 Omni on Strix Halo/ROCM bug;rocm ### Your current environment I couldnt get the collect_env.py working on NixOS vllm: 0.16.0 rocm: 7.1.1/7.1.52802-9999 python 3.13.12 hard...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: pt-oss-20b model which works without issue, the problem appears to be specific to qwen3 omni. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ase provide architecture for which code is to be generated. ``` Note: I tested the gpt-oss-20b model which works without issue, the problem appears to be specific to qwen3 omni. ### Before submitting a new issue... - [x...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
