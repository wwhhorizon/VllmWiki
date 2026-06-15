# vllm-project/vllm#2052: V0.2.4 Docker Image fails to run mixtral

| 字段 | 值 |
| --- | --- |
| Issue | [#2052](https://github.com/vllm-project/vllm/issues/2052) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> V0.2.4 Docker Image fails to run mixtral

### Issue 正文摘录

Using kubernetes, with the abbreviated configuration and version v0.2.4 of the docker image: ``` containers: - name: mixtral-vllm args: - "--model" - "mistralai/Mixtral-8x7B-Instruct-v0.1" - "--tensor-parallel-size" - "2" ... ``` I get a `KeyError: 'mixtral'` error. V0.2.4 should support mixtral, is there additional config required?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: V0.2.4 Docker Image fails to run mixtral Using kubernetes, with the abbreviated configuration and version v0.2.4 of the docker image: ``` containers: - name: mixtral-vllm args: - "--model"
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Docker Image fails to run mixtral Using kubernetes, with the abbreviated configuration and version v0.2.4 of the docker image: ``` containers: - name: mixtral-vllm args: - "--model" - "mistralai/Mixtral-8x7B-Instruct-v0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
