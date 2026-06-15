# vllm-project/vllm#1369: ImportError: libcudart.so.11.0: cannot open shared object file: No such file or directory

| 字段 | 值 |
| --- | --- |
| Issue | [#1369](https://github.com/vllm-project/vllm/issues/1369) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 22; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | model_support |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 | crash;import_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> ImportError: libcudart.so.11.0: cannot open shared object file: No such file or directory

### Issue 正文摘录

When I used vllm to serve my local model, the terminal displayed the following message: ImportError: libcudart.so.11.0: cannot open shared object file: No such file or directory The traceback pointed to the following code in site-packages/vllm/utils.py and the execution of the single line could also trigger the same error: "from vllm import cuda_utils" I suppose it may be caused by the mismatch between vllm and my CUDA version or Pytorch version. The CUDA version is 12.2 (only this version installed) on my machine and installing a new version 11 is not so convenient, the Pytorch version is 2.1.0, vllm version is 0.2.0 How could I solve the problem without re-install CUDA 11? Many thanks!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ImportError: libcudart.so.11.0: cannot open shared object file: No such file or directory installation When I used vllm to serve my local model, the terminal displayed the following message: ImportError: libcudart.so.11.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ImportError: libcudart.so.11.0: cannot open shared object file: No such file or directory installation When I used vllm to serve my local model, the terminal displayed the following message: ImportError: libcudart.so.11...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: error: "from vllm import cuda_utils" I suppose it may be caused by the mismatch between vllm and my CUDA version or Pytorch version. The CUDA version is 12.2 (only this version installed) on my machine and installing a...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: o such file or directory installation When I used vllm to serve my local model, the terminal displayed the following message: ImportError: libcudart.so.11.0: cannot open shared object file: No such file or directory The...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
