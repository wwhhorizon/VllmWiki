# vllm-project/vllm#7207: [Installation]: run vllm in the rocm docker raied: RuntimeError: No HIP GPUs are available

| 字段 | 值 |
| --- | --- |
| Issue | [#7207](https://github.com/vllm-project/vllm/issues/7207) |
| 状态 | closed |
| 标签 | installation;rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: run vllm in the rocm docker raied: RuntimeError: No HIP GPUs are available

### Issue 正文摘录

### Your current environment The host can see the GPUs, but processes inside Docker cannot. Any idea? ### How you are installing vllm Build the vllm-rocm docker

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: run vllm in the rocm docker raied: RuntimeError: No HIP GPUs are available installation;rocm ### Your current environment The host can see the GPUs, but processes inside Docker cannot. Any idea? ### How
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Installation]: run vllm in the rocm docker raied: RuntimeError: No HIP GPUs are available installation;rocm ### Your current environment The host can see the GPUs, but processes inside Docker cannot. Any idea? ### How...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
