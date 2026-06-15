# vllm-project/vllm#7087: [Installation]: Install a shared vllm package compatible with multiple GPU architectures

| 字段 | 值 |
| --- | --- |
| Issue | [#7087](https://github.com/vllm-project/vllm/issues/7087) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Install a shared vllm package compatible with multiple GPU architectures

### Issue 正文摘录

### Your current environment collect_env.py", line 266, in get_vllm_version return vllm.__version__ AttributeError: module 'vllm' has no attribute '__version__' ### How you are installing vllm git clone https://github.com/vllm-project/vllm pip install -e . I want to install a shared vllm 0.5.3 (or newer version) on machines with 3090, A6000, and V100 GPUs, running Python 3.9.9, PyTorch 2.4.0, and CUDA 12.4. However, I've found that if I use pip install -e ., it only works correctly on one device. On the others, I get the error "CUDA error: no kernel image is available for execution on the device". I suspect that the compilation instructions don't support the corresponding architectures. How should I modify the CMakeLists.txt file to make it a universal vllm installation package? If I install them separately on each machine, they all work fine.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: Install a shared vllm package compatible with multiple GPU architectures installation;stale ### Your current environment collect_env.py", line 266, in get_vllm_version return vllm.__version__ Attribut
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nstallation]: Install a shared vllm package compatible with multiple GPU architectures installation;stale ### Your current environment collect_env.py", line 266, in get_vllm_version return vllm.__version__ AttributeErro...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: red vllm package compatible with multiple GPU architectures installation;stale ### Your current environment collect_env.py", line 266, in get_vllm_version return vllm.__version__ AttributeError: module 'vllm' has no att...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
