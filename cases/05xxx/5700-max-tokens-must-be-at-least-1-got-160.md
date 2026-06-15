# vllm-project/vllm#5700: max_tokens must be at least 1, got -160 

| 字段 | 值 |
| --- | --- |
| Issue | [#5700](https://github.com/vllm-project/vllm/issues/5700) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> max_tokens must be at least 1, got -160 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh pip install -vvv vllm ```

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: max_tokens must be at least 1, got -160 installation ### Your current environment ```text The output of `python collect_env.py` ``` ### How you are installing vllm ```sh pip install -vvv vllm ```

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
