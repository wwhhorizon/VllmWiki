# vllm-project/vllm#11968: [New Model]: Cosmos-1.0-Autoregressive (World Foundation Models)

| 字段 | 值 |
| --- | --- |
| Issue | [#11968](https://github.com/vllm-project/vllm/issues/11968) |
| 状态 | closed |
| 标签 | new-model;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Cosmos-1.0-Autoregressive (World Foundation Models)

### Issue 正文摘录

### The model to consider. **Cosmos World Foundation Models**: A family of highly performant pre-trained world foundation models purpose-built for generating physics-aware videos and world states for physical AI development. The Cosmos autoregressive models are a collection of pre-trained world foundation models that are ideal for predicting and rapidly generating video sequences from video or image inputs for physical AI. They can serve as the building block for various applications or research that are related to world generation. [**Hugging Face**](https://huggingface.co/collections/nvidia/cosmos-6751e884dc10e013a0a0d8e6) | [**Code**](https://github.com/NVIDIA/Cosmos) | [**Paper**](https://arxiv.org/abs/2501.03575) In Cosmos 1.0 release, the Cosmos Autoregressive WFM family includes the following models: - [Cosmos-1.0-Autoregressive-4B](https://huggingface.co/nvidia/Cosmos-1.0-Autoregressive-4B) - Given a 9-frame input video, predicts the future 24 frames. - Given an image as the first frame, predicts the future 32 frames. - [Cosmos-1.0-Autoregressive-5B-Video2World](https://huggingface.co/nvidia/Cosmos-1.0-Autoregressive-5B-Video2World) - Given text description and a 9-frame i...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [New Model]: Cosmos-1.0-Autoregressive (World Foundation Models) new-model;stale ### The model to consider. **Cosmos World Foundation Models**: A family of highly performant pre-trained world foundation models purpose-b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: uences from video or image inputs for physical AI. They can serve as the building block for various applications or research that are related to world generation. [**Hugging Face**](https://huggingface.co/collections/nv...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [New Model]: Cosmos-1.0-Autoregressive (World Foundation Models) new-model;stale ### The model to consider. **Cosmos World Foundation Models**: A family of highly performant pre-trained world foundation models purpose-b...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: om video or image inputs for physical AI. They can serve as the building block for various applications or research that are related to world generation. [**Hugging Face**](https://huggingface.co/collections/nvidia/cosm...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ew Model]: Cosmos-1.0-Autoregressive (World Foundation Models) new-model;stale ### The model to consider. **Cosmos World Foundation Models**: A family of highly performant pre-trained world foundation models purpose-bui...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
