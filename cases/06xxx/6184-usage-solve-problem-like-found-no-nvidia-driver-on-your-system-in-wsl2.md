# vllm-project/vllm#6184: [Usage]: solve problem like "Found no NVIDIA driver on your system." in WSL2

| 字段 | 值 |
| --- | --- |
| Issue | [#6184](https://github.com/vllm-project/vllm/issues/6184) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: solve problem like "Found no NVIDIA driver on your system." in WSL2

### Issue 正文摘录

### Your current environment In WSL2, after I update vllm from v0.5.0.post1 to v0.5.1, all model unable to load immediately. After extensive troubleshooting, I discovered the cause. In here: https://learn.microsoft.com/en-us/windows/ai/directml/gpu-cuda-in-wsl [you need a kernel version of 5.10.43.3 or higher. You can check the version number by running the following command in PowerShell: wsl cat /proc/version] and I get "Linux version 5.10.16.3-microsoft-standard-WSL2 (oe-user@oe-host)" So I look here and use update command: https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl-2 Then I get: "Linux version 5.15.153.1-microsoft-standard-WSL2 (root@941d701f84f1)" Everything is fine now, except for my 2080ti graphics card which does not support FP8 quantization. ### How would you like to use vllm _No response_

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: g is fine now, except for my 2080ti graphics card which does not support FP8 quantization. ### How would you like to use vllm _No response_
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: crosoft.com/en-us/windows/ai/directml/gpu-cuda-in-wsl [you need a kernel version of 5.10.43.3 or higher. You can check the version number by running the following command in PowerShell: wsl cat /proc/version] and I get...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ause. In here: https://learn.microsoft.com/en-us/windows/ai/directml/gpu-cuda-in-wsl [you need a kernel version of 5.10.43.3 or higher. You can check the version number by running the following command in PowerShell: ws...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vironment In WSL2, after I update vllm from v0.5.0.post1 to v0.5.1, all model unable to load immediately. After extensive troubleshooting, I discovered the cause. In here: https://learn.microsoft.com/en-us/windows/ai/di...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
