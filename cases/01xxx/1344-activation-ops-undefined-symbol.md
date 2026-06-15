# vllm-project/vllm#1344: activation_ops undefined symbol

| 字段 | 值 |
| --- | --- |
| Issue | [#1344](https://github.com/vllm-project/vllm/issues/1344) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;import_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> activation_ops undefined symbol

### Issue 正文摘录

I build vllm-0.2.0 in ngc23.08 (cuda12). The building process was successful. However when running, an error occurred: ``` File "/workspace/vllm-0.2.0/vllm/model_executor/layers/activation.py", line 5, in from vllm import activation_ops ImportError: /workspace/vllm-0.2.0/vllm/activation_ops.cpython-310-x86_64-linux-gnu.so: undefined symbol: _ZN3c106detail14torchCheckFailEPKcS2_jRKSs ``` Is this a cuda related error or pytorch version related error?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: activation_ops undefined symbol I build vllm-0.2.0 in ngc23.08 (cuda12). The building process was successful. However when running, an error occurred: ``` File "/workspace/vllm-0.2.0/vllm/model_executor/layers/activatio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: activation_ops undefined symbol I build vllm-0.2.0 in ngc23.08 (cuda12). The building process was successful. However when running, an error occurred: ``` File "/workspace/vllm-0.2.0/vllm/model_executor/layers/activatio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: er when running, an error occurred: ``` File "/workspace/vllm-0.2.0/vllm/model_executor/layers/activation.py", line 5, in from vllm import activation_ops ImportError: /workspace/vllm-0.2.0/vllm/activation_ops.cpython-31...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
