# vllm-project/vllm#12614: [Bug]: VLLM (0.7.0) will report gpu missing on the hosting node in Ray

| 字段 | 值 |
| --- | --- |
| Issue | [#12614](https://github.com/vllm-project/vllm/issues/12614) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM (0.7.0) will report gpu missing on the hosting node in Ray

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ## Context I'm using Ray Serve to deploy a vLLM App. It was working well til recently we upgrade version of vLLM to 0.7.0 and adapted to the API change. ## Hardware Env We have a instance with six 4090 GPUs. We deployed a Ray cluster on it with one head node and 5 worker nodes. All are docker containers. Each container is attached to a gpu. ## Issue The core issue is that whenever the vLLM app tries to load the model from the disk, it fails to find GPU to the container where the APP is hosted. - All containers have exactly the same ENV - We can use vllm cli to run the model directly without any issue. - **We tried to re-deploy many times. Each time the APP could be hosted on an arbitrary node. Whenever a node becomes the hosting node, it will throw error of that it does not have GPU. But in the cases when that node is not the hosted node, it can work well and load model weights smoothly.** - We are now trying to downgrade the vllm version but want to get an idea if this is a bug or our usage issue. Thanks! ## Ray Error log The error line seems ``` ValueError: Current node has no GPU available....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Serve to deploy a vLLM App. It was working well til recently we upgrade version of vLLM to 0.7.0 and adapted to the API change. ## Hardware Env We have a instance with six 4090 GPUs. We deployed a Ray cluster on it with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: hat node is not the hosted node, it can work well and load model weights smoothly.** - We are now trying to downgrade the vllm version but want to get an idea if this is a bug or our usage issue. Thanks! ## Ray Error lo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: on the hosting node in Ray bug;ray ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ## Context I'm using Ray Serve to deploy a vLLM App. It was working well til recently we upgrade...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ted_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
