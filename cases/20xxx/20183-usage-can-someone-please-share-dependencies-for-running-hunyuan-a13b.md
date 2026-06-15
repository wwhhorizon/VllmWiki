# vllm-project/vllm#20183: [Usage]: Can someone please share dependencies for running Hunyuan-A13B?

| 字段 | 值 |
| --- | --- |
| Issue | [#20183](https://github.com/vllm-project/vllm/issues/20183) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Can someone please share dependencies for running Hunyuan-A13B?

### Issue 正文摘录

I've spent hours trying to get the Hunyuan model working with vLLM. Downgrading, upgrading, testing different versions..nothing worked so far. The team shared a Docker image using vLLM 0.8.5, so I’m assuming that’s the best version. What I need to know is: - What version of transformers? - What version of torch? - What version of flash-attn? - Which CUDA version? - If not 0.8.5, then what version of vllm? If you’ve got it running, please share your working setup. Thanks.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Usage]: Can someone please share dependencies for running Hunyuan-A13B? usage;stale I've spent hours trying to get the Hunyuan model working with vLLM. Downgrading, upgrading, testing different versions..nothing worked...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rmers? - What version of torch? - What version of flash-attn? - Which CUDA version? - If not 0.8.5, then what version of vllm? If you’ve got it running, please share your working setup. Thanks.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ing Hunyuan-A13B? usage;stale I've spent hours trying to get the Hunyuan model working with vLLM. Downgrading, upgrading, testing different versions..nothing worked so far. The team shared a Docker image using vLLM 0.8....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ]: Can someone please share dependencies for running Hunyuan-A13B? usage;stale I've spent hours trying to get the Hunyuan model working with vLLM. Downgrading, upgrading, testing different versions..nothing worked so fa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ying to get the Hunyuan model working with vLLM. Downgrading, upgrading, testing different versions..nothing worked so far. The team shared a Docker image using vLLM 0.8.5, so I’m assuming that’s the best version. What...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
