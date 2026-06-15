# vllm-project/vllm#502: Importation Issue 

| 字段 | 值 |
| --- | --- |
| Issue | [#502](https://github.com/vllm-project/vllm/issues/502) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | import_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Importation Issue 

### Issue 正文摘录

I am using a 13.2 ML Runtime Cluster w/ 28GB of RAM via databricks. Have no problem installing vllm, but import statement is showing the following error. Have pytorch installed as well. ImportError: /local_disk0/.ephemeral_nfs/envs/pythonEnv-b7b6859e-7f75-46c9-a4c3-4fd3a56fdb84/lib/python3.10/site-packages/vllm/activation_ops.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN3c106detail19maybe_wrap_dim_slowEllb For a side-note: I am not capable of using vllm on my local machine, so I'm not sure what kind of testing I can do outside of databricks. I am on a linux based system, the cluster I'm on uses CUDA 11.7, and I'm on a T4 GPU (documentation says that is valid for computer capability). Any tips?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Importation Issue installation I am using a 13.2 ML Runtime Cluster w/ 28GB of RAM via databricks. Have no problem installing vllm, but import statement is showing the following error. Have pytorch installed as well.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e of databricks. I am on a linux based system, the cluster I'm on uses CUDA 11.7, and I'm on a T4 GPU (documentation says that is valid for computer capability). Any tips? development cuda import_error I am using a 13.2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: capable of using vllm on my local machine, so I'm not sure what kind of testing I can do outside of databricks. I am on a linux based system, the cluster I'm on uses CUDA 11.7, and I'm on a T4 GPU (documentation says th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
