# vllm-project/vllm#35980: [Bug]: Why does deploying Qwen3-32B-AWQ via vllm:v0.10.1.1 result in different outputs for the same input?

| 字段 | 值 |
| --- | --- |
| Issue | [#35980](https://github.com/vllm-project/vllm/issues/35980) |
| 状态 | open |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | moe;operator;quantization;sampling |
| 症状 |  |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Why does deploying Qwen3-32B-AWQ via vllm:v0.10.1.1 result in different outputs for the same input?

### Issue 正文摘录

### I sincerely invite all experts to answer this question. ### Your current environment GPU: NVIDIA L40 * 4 vllm: v0.10.1.1 LLM: Qwen3-32B-AWQ ### 🐛 Describe the bug Why does deploying Qwen3-32B-AWQ via vllm:v0.10.1.1 result in different outputs for the same input? **If I reuse the same request body with the same content, I might get the same result; however, if I call request bodies with different content simultaneously—that is, during batch complex inference—the result becomes unstable. The result I'm referring to is mainly related to _True/False_ judgments.** **I searched the issue and found it might be due to inaccurate numerical values ​​or batch processing problems, but there wasn't a detailed explanation. I'm hoping to get _a more detailed answer_.** I deployed Qwen3-32B-AWQ using vllm:v0.10.1.1 via Kubernetes containerization. The Deployment is as follows: ```yml kind: Pod apiVersion: v1 metadata: name: llm-7df94bdccf-s6fwr generateName: llm-7df94bdccf- namespace: dev-fc2-qm-yfzx-aiznfwpt-ai-system labels: app: llm hami.io/vgpu-node: prod-ai-fusioncloud-fc-k8s-worker03 pod-template-hash: 7df94bdccf annotations: cni.projectcalico.org/containerID: 51c80d3a71af5418e441d44713...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: [Bug]: Why does deploying Qwen3-32B-AWQ via vllm:v0.10.1.1 result in different outputs for the same input? bug ### I sincerely invite all experts to answer this question. ### Your current environment GPU: NVIDIA L40 * 4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: tes containerization. The Deployment is as follows: ```yml kind: Pod apiVersion: v1 metadata: name: llm-7df94bdccf-s6fwr generateName: llm-7df94bdccf- namespace: dev-fc2-qm-yfzx-aiznfwpt-ai-system labels: app: llm hami....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Why does deploying Qwen3-32B-AWQ via vllm:v0.10.1.1 result in different outputs for the same input? bug ### I sincerely invite all experts to answer this question. ### Your current environment GPU: NVIDIA L40 * 4...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: comes unstable. The result I'm referring to is mainly related to _True/False_ judgments.** **I searched the issue and found it might be due to inaccurate numerical values ​​or batch processing problems, but there wasn't...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: in different outputs for the same input? bug ### I sincerely invite all experts to answer this question. ### Your current environment GPU: NVIDIA L40 * 4 vllm: v0.10.1.1 LLM: Qwen3-32B-AWQ ### 🐛 Describe the bug Why doe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
