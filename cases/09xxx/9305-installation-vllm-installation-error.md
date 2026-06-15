# vllm-project/vllm#9305: [Installation]: vllm installation error

| 字段 | 值 |
| --- | --- |
| Issue | [#9305](https://github.com/vllm-project/vllm/issues/9305) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: vllm installation error

### Issue 正文摘录

### Your current environment **env** llamafactory version: 0.9.1.dev0 Platform: Linux-5.15.0-25-generic-aarch64-with-glibc2.35 Python version: 3.10.15 PyTorch version: 2.1.0 (NPU) Transformers version: 4.45.0 Datasets version: 2.21.0 Accelerate version: 0.34.2 PEFT version: 0.12.0 TRL version: 0.9.6 NPU type: Ascend910B3 CANN version: 7.0.1 DeepSpeed version: 0.13.2 **error** Collecting vllm =0.4.3 (from llamafactory==0.9.1.dev0) Using cached vllm-0.6.2.tar.gz (2.6 MB) Installing build dependencies ... error error: subprocess-exited-with-error × pip subprocess to install build dependencies did not run successfully. │ exit code: 2 ╰─> [86 lines of output] Collecting cmake>=3.26 Using cached cmake-3.30.4-py3-none-manylinux_2_17_aarch64.manylinux2014_aarch64.whl.metadata (6.4 kB) Collecting ninja Using cached ninja-1.11.1.1-py2.py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl.metadata (5.3 kB) Collecting packaging Using cached packaging-24.1-py3-none-any.whl.metadata (3.2 kB) Collecting setuptools>=61 Using cached setuptools-75.1.0-py3-none-any.whl.metadata (6.9 kB) Collecting setuptools-scm>=8.0 Using cached setuptools_scm-8.1.0-py3-none-any.whl.metadata (6.6 kB) Collecting...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: vllm installation error installation;stale ### Your current environment **env** llamafactory version: 0.9.1.dev0 Platform: Linux-5.15.0-25-generic-aarch64-with-glibc2.35 Python version: 3.10.15 PyTorch ve
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: d cmake-3.30.4-py3-none-manylinux_2_17_aarch64.manylinux2014_aarch64.whl.metadata (6.4 kB) Collecting ninja Using cached ninja-1.11.1.1-py2.py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl.metadata (5.3 kB) Col...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Installation]: vllm installation error installation;stale ### Your current environment **env** llamafactory version: 0.9.1.dev0 Platform: Linux-5.15.0-25-generic-aarch64-with-glibc2.35 Python version: 3.10.15 PyTorch v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nv** llamafactory version: 0.9.1.dev0 Platform: Linux-5.15.0-25-generic-aarch64-with-glibc2.35 Python version: 3.10.15 PyTorch version: 2.1.0 (NPU) Transformers version: 4.45.0 Datasets version: 2.21.0 Accelerate versio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tallation error installation;stale ### Your current environment **env** llamafactory version: 0.9.1.dev0 Platform: Linux-5.15.0-25-generic-aarch64-with-glibc2.35 Python version: 3.10.15 PyTorch version: 2.1.0 (NPU) Tran...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
