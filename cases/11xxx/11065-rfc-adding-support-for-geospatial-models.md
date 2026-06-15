# vllm-project/vllm#11065: [RFC]: Adding support for Geospatial models

| 字段 | 值 |
| --- | --- |
| Issue | [#11065](https://github.com/vllm-project/vllm/issues/11065) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Adding support for Geospatial models

### Issue 正文摘录

### Motivation. Modern models are now not only targeting the generation of text but also the generation of images from text or image input as well. This RFC wants to open the stage towards supporting models that do not only generate text but also images either as a single modality or even supporting multi-modal output. One example of great interest to us is a set of models developed in co-operation with NASA for earth observation (https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M) working on satellite images can be fine-tuned for several tasks including floods forecast, crop classification etc. This example model, works on images of a fixed size in input and generates an image of the same size in output. In the specific, input images in the geotiff format are split in patches of dimensions 224×224, each patch is passed through the model for inference that generates a tensor of the same size as the input. This is similar in a way got an autoregressive process, with the difference that at every iteration the data passed to the model is different and there is no relationship when inferencing subsequent patches. All the output patches are then “re-assembled” into a geotiff image...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [RFC]: Adding support for Geospatial models RFC;stale ### Motivation. Modern models are now not only targeting the generation of text but also the generation of images from text or image input as well. This RFC wants to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ze in input and generates an image of the same size in output. In the specific, input images in the geotiff format are split in patches of dimensions 224×224, each patch is passed through the model for inference that ge...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ation the data passed to the model is different and there is no relationship when inferencing subsequent patches. All the output patches are then “re-assembled” into a geotiff image. The goal of this RFC is that of crea...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [RFC]: Adding support for Geospatial models RFC;stale ### Motivation. Modern models are now not only targeting the generation of text but also the generation of images from text or image input as well. This RFC wants to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
