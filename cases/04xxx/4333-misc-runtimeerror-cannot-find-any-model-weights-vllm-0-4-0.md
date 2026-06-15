# vllm-project/vllm#4333: [Misc]: RuntimeError: Cannot find any model weights [vllm=0.4.0]

| 字段 | 值 |
| --- | --- |
| Issue | [#4333](https://github.com/vllm-project/vllm/issues/4333) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: RuntimeError: Cannot find any model weights [vllm=0.4.0]

### Issue 正文摘录

### Anything you want to discuss about vllm. I run into the below error when using meta-llama/CodeLlama-7b-Instruct-hf with `vllm==0.4.0, torch==2.1.2`, the code works perfectly with` vllm==0.2.1`, but I want to use the most updated version of vllm for some more functionalities. It seems to be a trivial error and I tried several things, reinstall pytorch, transformer, verifying cuda versions etc. Would be great to get any help! Error msg: `(RayWorkerVllm pid=1842765) ERROR 04-24 09:33:04 ray_utils.py:44] RuntimeError: Cannot find any model weights with 'meta-llama/CodeLlama-7b-Instruct-hf'`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e works perfectly with` vllm==0.2.1`, but I want to use the most updated version of vllm for some more functionalities. It seems to be a trivial error and I tried several things, reinstall pytorch, transformer, verifyin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Misc]: RuntimeError: Cannot find any model weights [vllm=0.4.0] usage;stale ### Anything you want to discuss about vllm. I run into the below error when using meta-llama/CodeLlama-7b-Instruct-hf with `vllm==0.4.0, torc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: or and I tried several things, reinstall pytorch, transformer, verifying cuda versions etc. Would be great to get any help! Error msg: `(RayWorkerVllm pid=1842765) ERROR 04-24 09:33:04 ray_utils.py:44] RuntimeError: Can...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: RuntimeError: Cannot find any model weights [vllm=0.4.0] usage;stale ### Anything you want to discuss about vllm. I run into the below error when using meta-llama/CodeLlama-7b-Instruct-hf with `vllm==0.4.0, torc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
