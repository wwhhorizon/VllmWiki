# vllm-project/vllm#8042: [Installation]: Issues with installing vLLM on ROCM without sudo access

| 字段 | 值 |
| --- | --- |
| Issue | [#8042](https://github.com/vllm-project/vllm/issues/8042) |
| 状态 | closed |
| 标签 | installation;rocm |
| 评论 | 35; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Issues with installing vLLM on ROCM without sudo access

### Issue 正文摘录

### Your current environment Hi! I have been trying to install vLLM on a cluster that has AMD MI250X GPUs using the documentation provided and running into the following issue: `ninja: error: '/opt/rocm/lib/libamdhip64.so', needed by '/full_path_here/vllm/_core_C.abi3.so', missing and no known rule to make it` Now, there are 3 issues: 1) I do not have sudo access on the cluster so I cannot copy libamdhip64.so. Is there a way to download the patch in some other path and have the installation use it? 2) The cluster I am on has ROCM 6.2 but going by this issue: https://github.com/vllm-project/vllm/issues/8004, it still requires this file 3) The rocm path on the cluster is not /opt/rocm but opt/rocm-6.2. I don't see a way to specify explicitly the ROCM Path to be used during the installation. Let me know if there is a way to bypass these issues. ### How you are installing vllm ``` pip install --upgrade pip # Install PyTorch pip uninstall torch -y pip install --no-cache-dir --pre torch==2.5.0.dev20240726 --index-url https://download.pytorch.org/whl/nightly/rocm6.1 # Build & install AMD SMI pip install /opt/rocm/share/amd_smi # Install dependencies pip install --upgrade numba scipy hugg...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Installation]: Issues with installing vLLM on ROCM without sudo access installation;rocm ### Your current environment Hi! I have been trying to install vLLM on a cluster that has AMD MI250X GPUs using the documentation...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Installation]: Issues with installing vLLM on ROCM without sudo access installation;rocm ### Your current environment Hi! I have been trying to install vLLM on a cluster that has AMD MI250X GPUs using the documentation
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /share/amd_smi # Install dependencies pip install --upgrade numba scipy huggingface-hub[cli] pip install "numpy<2" pip install -r requirements-rocm.txt # Apply the patch to ROCM 6.1 (requires root permission) wget -N ht...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
