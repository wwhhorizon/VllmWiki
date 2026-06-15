# vllm-project/vllm#11134: [Feature]: Allow Ray placement group more time to wait for resources to be ready

| 字段 | 值 |
| --- | --- |
| Issue | [#11134](https://github.com/vllm-project/vllm/issues/11134) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Allow Ray placement group more time to wait for resources to be ready

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ``` ray start --head --dashboard-host 0.0.0.0 --disable-usage-stats --block --num-gpus 1 python -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-1.5B-Instruct --trust-remote-code --distributed-executor-backend ray --tensor-parallel-size 2 ``` I am using a ray cluster as the distributed executor backend. However, my cluster sometimes takes time to be ready. there are multiple reasons - image downloading speed is different, some node has image cache and some does not. - node short of resources, node level autoscaler will make decision to bring up more nodes but it takes time for new ray node to join and form a cluster I do not want the engine to early exit. ![image](https://github.com/user-attachments/assets/7a621963-21fb-4f16-9573-71299e951bad) ![image](https://github.com/user-attachments/assets/5b06c173-1465-4675-a5a0-2627a3b8b18d) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: -block --num-gpus 1 python -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-1.5B-Instruct --trust-remote-code --distributed-executor-backend ray --tensor-parallel-size 2 ``` I am using a ray cluster as the dis...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: Qwen2.5-1.5B-Instruct --trust-remote-code --distributed-executor-backend ray --tensor-parallel-size 2 ``` I am using a ray cluster as the distributed executor backend. However, my cluster sometimes takes time to be read...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e does not. - node short of resources, node level autoscaler will make decision to bring up more nodes but it takes time for new ray node to join and form a cluster I do not want the engine to early exit. ![image](https...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: image cache and some does not. - node short of resources, node level autoscaler will make decision to bring up more nodes but it takes time for new ray node to join and form a cluster I do not want the engine to early e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
