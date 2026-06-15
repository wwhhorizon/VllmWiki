# vllm-project/vllm#41614: [Windows] RTX 5070 Ti (Blackwell sm_120) - setup and deployment notes

| 字段 | 值 |
| --- | --- |
| Issue | [#41614](https://github.com/vllm-project/vllm/issues/41614) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Windows] RTX 5070 Ti (Blackwell sm_120) - setup and deployment notes

### Issue 正文摘录

### Environment - **GPU**: NVIDIA GeForce RTX 5070 Ti Laptop GPU (Blackwell, compute capability 12.0) - **Driver**: 595.79 - **OS**: Windows 11 (via WSL2 and native) - **Python**: 3.14 ### Problem Deploying vLLM on RTX 5070 Ti requires several workarounds: 1. **Blackwell architecture** (sm_120) is not in vLLM's default arch list. Must set `TORCH_CUDA_ARCH_LIST=12.0`. 2. **Windows hybrid graphics** routes Python to Intel iGPU by default. Registry fix required. 3. **CUDA DLL conflict**: CUDA Toolkit vs PyTorch cu130 PATH priority issue. ### Solution ```bash export TORCH_CUDA_ARCH_LIST=12.0 export CUDA_VISIBLE_DEVICES=0 export CUDA_MODULE_LOADING=LAZY ``` For Windows laptops, also set GPU Preference in registry: ```python import winreg key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\DirectX\UserGpuPreferences', 0, winreg.KEY_SET_VALUE) winreg.SetValueEx(key, r'C:\path\to\python.exe', 0, winreg.REG_SZ, 'GpuPreference=2;') ``` ### Question Is there a plan to add Blackwell (sm_120) to vLLM's supported architectures list? RTX 5070 Ti/5080/5090 laptops are becoming common and users will need first-class support. Happy to contribute a PR with updated docs or arch detect...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Windows] RTX 5070 Ti (Blackwell sm_120) - setup and deployment notes ### Environment - **GPU**: NVIDIA GeForce RTX 5070 Ti Laptop GPU (Blackwell, compute capability 12.0) - **Driver**: 595.79 - **OS**: Windows 11 (via...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ``` For Windows laptops, also set GPU Preference in registry: ```python import winreg key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\DirectX\UserGpuPreferences', 0, winreg.KEY_SET_VALUE) winreg.SetV...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
