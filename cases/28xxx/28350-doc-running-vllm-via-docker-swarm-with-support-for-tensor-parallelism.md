# vllm-project/vllm#28350: [Doc]: Running VLLM via Docker Swarm With Support for Tensor Parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#28350](https://github.com/vllm-project/vllm/issues/28350) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Running VLLM via Docker Swarm With Support for Tensor Parallelism

### Issue 正文摘录

### 📚 Running VLLM via Docker Swarm With Support for Tensor Parallelism There's no documentation that I have found outlining how to run VLLM in a docker swarm when utilizing tensor parallelism. The issue is that ```ipc=host``` is not an available option within docker swarm. Consulting the AI feature on the VLLM website suggests to use the ```shm``` option which is available to swarm, but this produces continued failures on startup. Please advise how to run VLLM via docker swarm utilizing tensor parallelism. thx

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Doc]: Running VLLM via Docker Swarm With Support for Tensor Parallelism documentation ### 📚 Running VLLM via Docker Swarm With Support for Tensor Parallelism There's no documentation that I have found outlining how to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Doc]: Running VLLM via Docker Swarm With Support for Tensor Parallelism documentation ### 📚 Running VLLM via Docker Swarm With Support for Tensor Parallelism There's no documentation that I have found outlining how to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
