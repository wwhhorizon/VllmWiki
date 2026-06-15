# vllm-project/vllm#22082: [RFC]: Clear and stable interface for platform in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#22082](https://github.com/vllm-project/vllm/issues/22082) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Clear and stable interface for platform in vLLM

### Issue 正文摘录

### Motivation. vLLM support platform plugin feature for a long time. More and more hardware now uses this mechanism to work with vLLM. While there is a problem that the interface between vLLM and platform plugin is not completed designed. The compatibility is not well considered as well. This often causes the platform plugin to be broken, especially for real-time main-to-main projects like `vllm-ascend`, where CI breaks once a week on average. For the long-term evolution of the community, we should make the interface clear and stable enough. ### Proposed Change. In this section. I'll mainly describe what interface should be considered and how should they work. Before we go into the details, I think we can leave some high level principle first. IMO, the interface should be: 1. Detailed: All module should be considered. I'll list them one by one. 2. Stable: Once the interface is determined, it cannot be changed frequently. 3. Compatible: The new version of interface should be compatible with old version, at least N and N+1 version should be compatible. #### Detailed Let's visit the interface one by one. I collected all the interface that vllm-ascend using now. If I missed something...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: sidered as well. This often causes the platform plugin to be broken, especially for real-time main-to-main projects like `vllm-ascend`, where CI breaks once a week on average. For the long-term evolution of the communit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: in feature for a long time. More and more hardware now uses this mechanism to work with vLLM. While there is a problem that the interface between vLLM and platform plugin is not completed designed. The compatibility is...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: one by one. More detail will coming soon. - [ ] platform - [ ] config - [ ] distributed - [ ] forward_context - [ ] lora - [ ] CustomOp - [ ] quantization - [ ] attention - [ ] compilation - [ ] model_executor - [ ] sam...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Clear and stable interface for platform in vLLM RFC;stale ### Motivation. vLLM support platform plugin feature for a long time. More and more hardware now uses this mechanism to work with vLLM. While there is a p...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ed - [ ] forward_context - [ ] lora - [ ] CustomOp - [ ] quantization - [ ] attention - [ ] compilation - [ ] model_executor - [ ] sample - [ ] scheduler - [ ] kv cache ### Before submitting a new issue... - [x] Make su...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
