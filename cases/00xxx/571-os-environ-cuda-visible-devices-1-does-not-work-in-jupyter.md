# vllm-project/vllm#571: os.environ['CUDA_VISIBLE_DEVICES'] = '1' does not work in jupyter

| 字段 | 值 |
| --- | --- |
| Issue | [#571](https://github.com/vllm-project/vllm/issues/571) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> os.environ['CUDA_VISIBLE_DEVICES'] = '1' does not work in jupyter

### Issue 正文摘录

As the title says, it is invalid to specify the GPU through `CUDA_VISIBLE_DEVICES` in jupyter, and only 'GPU:0' will still be used; but it is effective when using `CUDA_VISIBLE_DEVICES=1 python *.py`

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: '] = '1' does not work in jupyter As the title says, it is invalid to specify the GPU through `CUDA_VISIBLE_DEVICES` in jupyter, and only 'GPU:0' will still be used; but it is effective when using `CUDA_VISIBLE_DEVICES=...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: os.environ['CUDA_VISIBLE_DEVICES'] = '1' does not work in jupyter As the title says, it is invalid to specify the GPU through `CUDA_VISIBLE_DEVICES` in jupyter, and only 'GPU:0' will still be used; but it is effective w...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
