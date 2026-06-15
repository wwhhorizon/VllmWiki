# vllm-project/vllm#14110: [Bug]:  [vllm + Qwen2.5 VL72B] Model Continuously Outputs “!” for Certain Images

| 字段 | 值 |
| --- | --- |
| Issue | [#14110](https://github.com/vllm-project/vllm/issues/14110) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  [vllm + Qwen2.5 VL72B] Model Continuously Outputs “!” for Certain Images

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I’m currently using the open-source Qwen2.5 VL72B model and deploying it locally on a V100 32GB GPU, running the service with the vllm framework. During testing with a few images, I noticed an issue: for some images, the model keeps generating “!!!!!!!” until it reaches the max-model-len of 32768. This seems to happen randomly, and when I run Qwen2.5 VL72B without vllm, the problem doesn’t occur. I’m wondering if anyone else has encountered this same problem. Is this a known issue with the vllm framework, or could it be related to the V100 GPU? Any insights or suggestions would be greatly appreciated. ![Image](https://github.com/user-attachments/assets/4e0e3ef7-01c1-40f7-b3bc-c28e6cdad004) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: [vllm + Qwen2.5 VL72B] Model Continuously Outputs “!” for Certain Images bug;stale ### Your current environment ### 🐛 Describe the bug I’m currently using the open-source Qwen2.5 VL72B model and deploying it loca...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lated to the V100 GPU? Any insights or suggestions would be greatly appreciated. ![Image](https://github.com/user-attachments/assets/4e0e3ef7-01c1-40f7-b3bc-c28e6cdad004) ### Before submitting a new issue... - [x] Make...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 04) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: VL72B without vllm, the problem doesn’t occur. I’m wondering if anyone else has encountered this same problem. Is this a known issue with the vllm framework, or could it be related to the V100 GPU? Any insights or sugge...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: m + Qwen2.5 VL72B] Model Continuously Outputs “!” for Certain Images bug;stale ### Your current environment ### 🐛 Describe the bug I’m currently using the open-source Qwen2.5 VL72B model and deploying it locally on a V1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
