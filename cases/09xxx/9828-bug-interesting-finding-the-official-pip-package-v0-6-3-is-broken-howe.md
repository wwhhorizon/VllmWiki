# vllm-project/vllm#9828: > **Bug**:Interesting finding: The official pip package v0.6.3 is broken. However, installing `https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl` fixes this issue. (`vLLM API server version 0.6.3.post2.dev139+g622b7ab9`)

| 字段 | 值 |
| --- | --- |
| Issue | [#9828](https://github.com/vllm-project/vllm/issues/9828) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> > **Bug**:Interesting finding: The official pip package v0.6.3 is broken. However, installing `https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl` fixes this issue. (`vLLM API server version 0.6.3.post2.dev139+g622b7ab9`)

### Issue 正文摘录

> Interesting finding: The official pip package v0.6.3 is broken. However, installing `https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl` fixes this issue. (`vLLM API server version 0.6.3.post2.dev139+g622b7ab9`) @SinanAkkoyun What does python 3.10.15 should install, seemly I meet the same issue, thanks a lot!! _Originally posted by @Wiselnn570 in https://github.com/vllm-project/vllm/issues/9732#issuecomment-2445843188_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: > **Bug**:Interesting finding: The official pip package v0.6.3 is broken. However, installing `https://vllm-wheels.s3.us-west-2.amazonaws.com/nightly/vllm-1.0.0.dev-cp38-abi3-manylinux1_x86_64.whl` fixes this issue. (`v...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
