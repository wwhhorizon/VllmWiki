# vllm-project/vllm#3811: [Installation]: Tesla V100 cuda11.4, I have no permission to install a upper-version cuda driver, how can I install vllm? I have tried to build from source and use pip, both failed.

| 字段 | 值 |
| --- | --- |
| Issue | [#3811](https://github.com/vllm-project/vllm/issues/3811) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Tesla V100 cuda11.4, I have no permission to install a upper-version cuda driver, how can I install vllm? I have tried to build from source and use pip, both failed.

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh pip install -vvv vllm ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: Tesla V100 cuda11.4, I have no permission to install a upper-version cuda driver, how can I install vllm? I have tried to build from source and use pip, both failed. installation ### Your current environ...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Installation]: Tesla V100 cuda11.4, I have no permission to install a upper-version cuda driver, how can I install vllm? I have tried to build from source and use pip, both failed. installation ### Your current environ...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
