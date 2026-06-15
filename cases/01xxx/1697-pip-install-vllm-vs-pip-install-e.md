# vllm-project/vllm#1697: pip install vllm vs pip install -e .

| 字段 | 值 |
| --- | --- |
| Issue | [#1697](https://github.com/vllm-project/vllm/issues/1697) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> pip install vllm vs pip install -e .

### Issue 正文摘录

I've noticed that the way of installing vllm will lead to different codes. With "pip install vllm", the vllm version will be vllm-0.2.1.post1 and there is no parameter named "repetition_penalty" in sampling_params.py; while actually there is "repetition _penalty" parameter in the lateset repo.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: pip install vllm vs pip install -e . I've noticed that the way of installing vllm will lead to different codes. With "pip install vllm", the vllm version will be vllm-0.2.1.post1 and there is no parameter named "repetit...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
